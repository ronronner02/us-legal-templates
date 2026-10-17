# Google API 泄露修复记录（2026-10-17）

## 调试总结

- 目标仓库：`ronronner02/us-legal-templates`。
- 本地目录：`E:\learn\us-legal-templates`。
- 修复分支：`fix/google-api-key-redaction`。
- 修复前提交：`65d79ed80e9c014dbb284e0e36bd1ebb89393ca5`；工作区起始状态干净。
- 根因：采集的网页正文包含 Google Maps 脚本的 API key；原始 HTTP 正文未经脱敏进入版本库。共 4 个 `.body` 文件、2 个不同值，对应 GitHub 告警 #1 和 #2。
- 来源记录分别指向宾州法院网站 `www.pacourts.us` 和犹他州法院网站 `www.utcourts.gov`。犹他州页面本次 HTTP 200，当前网页与快照中的值一致；宾州页面本次 HTTP 403，仅有仓库中的采集回执作为来源证据。未调用这些 key 对应的 Google API，未核验其有效性、限制或账户归属。
- 未将命中值认定为本项目的私有 Google 凭据，也未把告警关闭为误报。

## 修复范围

1. 将 4 个网页快照中的 key 替换为 `[REDACTED_GOOGLE_API_KEY]`。
2. 按脱敏后的 SHA-256 更名快照；同步修正 16 处回执、来源账本和观察记录中的路径、SHA-256 与适用的字节数。
3. 每条受影响回执增加 `redaction`，保留原始 SHA-256、原始字节数、原路径和替换次数；明确区分原始采集件与脱敏衍生件。
4. 刷新两轮完整性清单中的 13 个相关条目。不改写后续轮次的历史基线记录，它们描述的是当时状态。
5. 新增 `scripts/check_google_api_keys.py`：默认扫描 Git 管理的当前文件及未忽略的新文件；`--staged` 读取暂存区实际内容。输出仅含路径和行号，路径本身也做脱敏。
6. 新增 CI `.github/workflows/google-api-key-check.yml`；动作使用完整提交 SHA 固定版本，权限为 `contents: read`，不保留 checkout 凭据。
7. 新增回归测试，覆盖网页正文、二进制内容、重复命中、诊断脱敏、暂存区与工作区分离、读取错误、现有完整性清单和脱敏回执。

逐文件映射见 `google-api-redactions.json`。全部 746 个既有 PDF/DOCX 文件逐字节保持不变；基线中 3,400 个文件保持原始 SHA-256，仅 15 个既有路径属于预期的更名或元数据修复范围。

## 检查命令

```powershell
python scripts/check_google_api_keys.py
python scripts/check_google_api_keys.py --staged
python -m unittest discover -s tests -v
python -m compileall -q scripts tests
git -c core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol diff --check
```

`--staged` 适用于完成精确暂存之后的本地检查；它不替代工作区检查。检查器针对当前已确认的明文 Google API key 形态，不是所有凭据、编码或构建资产的通用审计工具。

## 修复后质量

- 简化检查：在本会话中按复用、质量和效率三个维度逐项检查，仅覆盖本次新增代码。未启动独立 reviewer 或子代理。
- 定向人工审查：核查脱敏前后正文只发生目标替换、原件保存、回执语义、清单更新、暂存区读取、诊断不泄露和 CI 权限。运行时构造测试样本，避免 Python 常量折叠将完整样本写入缓存字节码。
- 现有项目没有配置 lint 或静态类型检查；不把语法检查称作类型检查。
- 采集 JSON 保留既有 CRLF。默认 `git diff --check` 将原有行末 CR 识别为尾随空白，exit 2；按仓库换行格式加入 `cr-at-eol`，同时保留标准空白规则后复查通过。未为消除此诊断而改写整份记录的换行。
- `graphify update .` 已执行，为 AST-only 更新；本地生成物通过 `.git/info/exclude` 排除，不混入源文件修复。
- `verification_run_summary_ref`：`.spec-first/workflows/spec-debug/us-legal-templates/2026-10-17-google-api-redaction/verification-run-summary.json`。
- 最终结果另记于同目录的 `honest-closeout.json`；整体事件范围保留远端发布、历史和 CI 的未完成状态。

## GitHub 端已执行的变更

已启用并重新读取确认 `secret_scanning` 与 `secret_scanning_push_protection`。未修改其他功能开关、可见性、分支保护或仓库内容；两条告警保持 `open`。

## 仍待处理的范围

- 代码修复尚未 commit、push 或创建 PR；远端当前分支仍是修复前内容。
- 14 个可达提交的历史扫描仍命中旧 key。未重写历史、未强制推送，也未处理 GitHub 缓存、外部克隆或 fork；当前快照脱敏不等于历史清除。
- 两条告警尚未关闭，key 的 Google 侧撤销状态未验证。来源网站 key 的生命周期需由其所有者处理，仓库侧脱敏不代表 key 已撤销。
- GitHub Actions 工作流尚未发布或运行，本地检查不代表远端 CI 已通过。
- 只处理指定仓库；未将本次结论扩展到其他仓库、全部 GitHub 协作面或所有类型的秘密。
- 仓库当前为公开状态，而既有 README 要求私有保存；本次未改变可见性，该差异需单独决策。

## 最终验证结果

- 原始复现检查：修复前失败（4 个文件），修复后通过。
- 回归测试：15 项通过；14 份既有完整性清单通过。
- 当前快照：自有检查器零命中；独立 Gitleaks 的 Google 规则扫描零命中，开启两层归档与解码检查。
- 语法、工作流 YAML、CRLF 感知空白检查、原件保持、远端防护复查和 AST 图更新均通过。
- 历史：14 个提交仍命中 4 处旧值；按真实 exit 1 保留为 `failed`。
- GitHub CI 与密钥撤销核验：`not-run`。
- `honest_closeout_verdict`：`degraded`。
- `overall_reason_code`：`degraded-claim`。
- 未使用整体通过结论掩盖历史残留和远端未发布状态。
