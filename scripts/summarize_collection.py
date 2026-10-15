"""Build a hash-deduplicated collection overview without changing source assets."""
import argparse
import collections
import csv
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

CATEGORIES = {
    'court_general': 'court_general', 'business': 'business', 'real_estate': 'real_estate',
    'insurance': 'insurance', 'employment': 'employment', 'unknown': 'unclassified',
    'Court procedure': 'court_general', 'Estate and personal planning': 'court_general',
    'Family and conservatorship': 'court_general', 'Probate': 'court_general', 'Family': 'court_general',
    'Court and general': 'court_general', 'Civil procedure and judgments': 'court_general',
    'Civil procedure and property': 'court_general', 'Foreign judgments': 'court_general',
    'Small claims': 'court_general', 'small_claims_and_civil_procedure': 'court_general',
    'family_case_procedure': 'court_general', 'custody_child_support_and_parenting': 'court_general',
    'divorce_and_marital_property': 'court_general', 'protective_orders': 'court_general',
    'peace_orders': 'court_general', 'guardianship': 'court_general', 'name_change': 'court_general',
    'Real estate': 'real_estate', 'Real estate regulation': 'real_estate',
    'Housing and landlord-tenant': 'real_estate', 'Housing and eviction': 'real_estate',
    'housing_and_eviction': 'real_estate', 'Employment': 'employment',
    'Business': 'business', 'Business contracts': 'business', 'Technology and data': 'business',
    'Tax supporting forms': 'business', 'Insurance consumer assistance': 'insurance',
    'Flood insurance (NFIP)': 'insurance',
}
LABELS = {'real_estate': '房地产及住房', 'business': '商业合同及配套文件',
          'insurance': '保险及消费者申诉', 'court_general': '法院程序及一般法律文件',
          'employment': '劳动雇佣', 'unclassified': '类别待确认'}
SPECIAL = {'Permission hold', 'Historical review', 'File quality review', 'Research references'}

def load(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def csvfile(path, rows, fields):
    with path.open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k, v in row.items()})

def safe(value):
    return re.sub(r'[^A-Za-z0-9._-]+', '-', value).strip('-')[:90] or 'document'

def catalog(path, rows, prefix):
    h = lambda value: html.escape(str(value or ''), quote=True)
    options = lambda field: ''.join(f'<option value="{h(v)}">{h(v)}</option>' for v in sorted({r[field] for r in rows}))
    cards = []
    for row in rows:
        search = ' '.join([row['title'], row['state'], row['form_code'], *row['source_categories']]).lower()
        cards.append(f'<article data-search="{h(search)}" data-state="{h(row["state"])}" data-category="{h(row["category"])}" data-section="{h(row["section"])}"><h2><a class="original" href="{h(prefix + row["local_path"])}">{h(row["title"])}</a></h2><p>{h(row["state"])} | {h(row["category"])} | {h(row["format"])} | {h(row["section"])}</p><p>{h(row["form_code"])} | {h(row["recorded_validation"])} | Publication: not approved</p><details><summary>Metadata and provenance</summary><p>Source categories: {h(", ".join(row["source_categories"]))}</p><p>Printed edition: {h(row["printed_revision"] or "Unverified")}</p><p>SHA-256: {h(row["sha256"])}</p><p><a href="metadata/{row["sha256"]}.json">Complete source records</a></p></details></article>')
    page = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Complete collection overview</title><style>body{font:16px/1.5 system-ui;max-width:1100px;margin:30px auto;padding:0 18px;background:#f5f7fa;color:#203040}article{background:white;border:1px solid #ccd5df;border-radius:8px;padding:16px;margin:12px 0}h2{font-size:18px}input,select,button{font:inherit;padding:8px;margin:5px;max-width:100%}p{overflow-wrap:anywhere}[hidden]{display:none!important}</style><h1>Complete legal document collection</h1><p>COUNT distinct original files, deduplicated by SHA-256. Original English titles and source metadata are preserved. Broad categories support browsing and do not establish legal equivalence.</p><p>Permission, historical, quality and reference classifications retain precedence. All product publication approvals remain pending. Recorded parser status is historical evidence, not a new legal or visual review.</p><p><a href="REPORT.zh-CN.md">Chinese collection report</a> | <a href="inventory.csv">Inventory CSV</a> | <a href="summary.json">Statistics JSON</a> | <a href="verification.json">Verification</a></p><form id="filters"><label>Search <input id="search" type="search"></label><label>State / scope <select id="state"><option value="">All</option>STATES</select></label><label>Category <select id="category"><option value="">All</option>CATS</select></label><label>Review section <select id="section"><option value="">All</option>SECTIONS</select></label><button type="reset">Clear filters</button></form><p id="count" role="status" aria-live="polite"></p><p id="empty" hidden>No matching documents.</p><main>CARDS</main><script>const form=document.querySelector('#filters'),cards=[...document.querySelectorAll('article')];function update(){const q=document.querySelector('#search').value.trim().toLowerCase(),fields=['state','category','section'];let n=0;for(const c of cards){c.hidden=!!((q&&!c.dataset.search.includes(q))||fields.some(f=>{const v=document.querySelector('#'+f).value;return v&&c.dataset[f]!==v;}));if(!c.hidden)n++;}document.querySelector('#count').textContent=n+' of '+cards.length+' documents';document.querySelector('#empty').hidden=n!==0;}form.addEventListener('input',update);form.addEventListener('change',update);form.addEventListener('submit',e=>e.preventDefault());form.addEventListener('reset',()=>setTimeout(update,0));update();</script></html>'''
    page = page.replace('COUNT',str(len(rows))).replace('STATES',options('state')).replace('CATS',options('category')).replace('SECTIONS',options('section')).replace('CARDS','\n'.join(cards))
    path.write_text(page, encoding='utf-8', newline='\n')

def build(repo, out, export):
    assert not out.exists(), 'Use a new overview directory; existing snapshots are preserved.'
    tracked = subprocess.check_output(['git','-C',str(repo),'ls-files','-z']).decode().split('\0')
    baseline = {p:digest(repo/p) for p in tracked if p}
    head = subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()
    actual = {}
    for rel in baseline:
        if Path(rel).suffix.lower() in {'.pdf','.docx'}:
            actual.setdefault(baseline[rel],[]).append(rel)
    records = {}; link_only = {}; batches = []; anomalies = []; manifest_checks = []
    base = load(repo/'organized-library/00_Index/all-records.json')
    state_names = {r.get('state_name'):r.get('state_code') for r in base if r.get('state_name')}

    def ingest(rows, inventory, batch, base_records=False):
        before = set(records)
        for r in rows:
            sha = r.get('sha256')
            if not r.get('downloaded',True) or not sha:
                key=r.get('original_file_url') or r.get('artifact_url') or r['title']
                link_only.setdefault(key,[]).append({'inventory':inventory,'record':r})
                continue
            assert sha in actual, (inventory,r['title'],'Original absent')
            category = r.get('legal_category') or r.get('category') or 'unknown'
            assert category in CATEGORIES, category
            state = r.get('state_name') or r.get('state')
            state_code = r.get('state_code') or state_names.get(state,'')
            scope = r.get('scope','unknown')
            if state_code:
                state = state or state_code
            else:
                state = {'federal':'Federal','shared-commercial':'Multistate','historical_unreconciled':'Historical / scope unconfirmed'}.get(scope,'Scope unconfirmed')
            if sha not in records:
                section = r.get('bundle_section') if base_records else 'Review required'
                section = section or 'Review required'
                local=actual[sha][0]
                records[sha]={'sha256':sha,'title':r['title'],'state':state,'state_code':state_code,'scope':scope,'category':CATEGORIES[category],'section':section,'format':Path(local).suffix.lstrip('.'),'bytes':(repo/local).stat().st_size,'local_path':local,'repository_paths':actual[sha],'first_batch':batch,'source_categories':[],'inventory_references':[],'source_urls':[],'artifact_urls':[],'form_code':r.get('form_code') or r.get('form_id') or '', 'printed_revision':r.get('printed_revision') or r.get('version') or '', 'recorded_validation':r.get('validation_status') or r.get('local_verification') or 'unrecorded','publication_status':'not-approved','copyright_status':r.get('copyright_status') or 'review_pending','source_records':[]}
            d=records[sha]
            for field,value in [('source_categories',category),('inventory_references',inventory),('source_urls',r.get('source_page_url') or r.get('source_url')),('artifact_urls',r.get('original_file_url') or r.get('artifact_url'))]:
                if value and value not in d[field]:d[field].append(value)
            d['source_records'].append({'inventory':inventory,'batch':batch,'record':r})
        batches.append({'batch':batch,'downloaded_inventory_records':sum(bool(r.get('sha256')) and r.get('downloaded',True) for r in rows),'new_unique_originals':len(set(records)-before),'combined_unique_originals':len(records),'states':dict(collections.Counter(r.get('state') or r.get('state_name') or r.get('scope') for r in rows if r.get('sha256'))),'inventory':inventory})

    ingest(base,'organized-library/00_Index/all-records.json','Original organized snapshot',True)
    ingest(load(repo/'research-collection/organized/2026-10-14-03/inventory.json'),'research-collection/organized/2026-10-14-03/inventory.json','2026-10-14 supplementary collection')
    rounds=sorted((repo/'research-collection/rounds').glob('*/inventory.json'))
    for p in rounds:
        ingest(load(p),p.relative_to(repo).as_posix(),p.parent.name)
        for findings in sorted((p.parent/'reports').glob('*discrepanc*.json')):
            for finding in load(findings):anomalies.append({'report':findings.relative_to(repo).as_posix(),'finding':finding})
    assert set(records)==set(actual) and len(records)==658
    rows=sorted(records.values(),key=lambda r:(r['state'],r['category'],r['title']))
    for r in rows:
        p=repo/r['local_path'];data=p.read_bytes();assert hashlib.sha256(data).hexdigest()==r['sha256']
        assert data.startswith(b'%PDF-') if r['format']=='pdf' else data.startswith(b'PK')
    manifests=[(repo/'organized-library',repo/'organized-library/00_Index/manifest.json')]+[(p.parent,p.parent/'integrity-manifest.json') for p in rounds]
    for directory,p in manifests:
        entries=load(p)['files']
        for rel,info in entries.items():assert digest(directory/rel)==(info if isinstance(info,str) else info['sha256']),str(p)+' '+rel
        manifest_checks.append({'manifest':p.relative_to(repo).as_posix(),'files_verified':len(entries)})
    supplementary_manifest=load(repo/'research-collection/manifest.json')
    for rel,sha in supplementary_manifest['files'].items():assert digest(repo/'research-collection'/rel)==sha,rel
    for rel,sha in supplementary_manifest['referenced_originals'].items():assert digest(repo/rel)==sha,rel
    manifest_checks.append({'manifest':'research-collection/manifest.json','files_verified':len(supplementary_manifest['files']),'referenced_originals_verified':len(supplementary_manifest['referenced_originals'])})
    latest=rounds[-1].parent
    holds=load(latest/'data/acquisition-holds.json');blocks=load(latest/'data/blocked-hosts.json')
    state_rows=[];coverage=[]
    for state in sorted({r['state'] for r in rows if r['state_code']}):
        rr=[r for r in rows if r['state']==state];counts=collections.Counter(r['category'] for r in rr)
        state_rows.append({'state':state,'state_code':rr[0]['state_code'],'originals':len(rr),'pdf':sum(r['format']=='pdf' for r in rr),'docx':sum(r['format']=='docx' for r in rr),'restricted_section_originals':sum(r['section'] in SPECIAL for r in rr),**{k:counts[k] for k in LABELS}})
        for cat in LABELS:
            cr=[r for r in rr if r['category']==cat];eligible=[r for r in cr if r['section'] not in SPECIAL]
            coverage.append({'state':state,'state_code':rr[0]['state_code'],'category':cat,'physical_originals':len(cr),'research_eligible_by_section':len(eligible),'completion_assessment':'not_assessed','publication_approved':0})
    summary={'as_of':datetime.now(timezone.utc).isoformat(),'baseline_commit':head,'repository_unique_originals':len(rows),'physical_original_paths':sum(map(len,actual.values())),'formats':dict(collections.Counter(r['format'] for r in rows)),'original_bytes':sum(r['bytes'] for r in rows),'states_physically_represented':len(state_rows),'broad_categories':dict(collections.Counter(r['category'] for r in rows)),'sections':dict(collections.Counter(r['section'] for r in rows)),'recorded_validation':dict(collections.Counter(r['recorded_validation'] for r in rows)),'copyright_status':dict(collections.Counter(r['copyright_status'] for r in rows)),'source_hosts':len({__import__('urllib.parse',fromlist=['urlsplit']).urlsplit(url).hostname for r in rows for url in r['source_urls']}),'source_page_urls':len({url for r in rows for url in r['source_urls']}),'distinct_link_only_records':len(link_only),'link_only_record_occurrences':sum(map(len,link_only.values())),'permission_hold_entries':len(holds),'blocked_host_entries':len(blocks),'publication_approvals':0,'state_category_cells':sum(r['category']!='unclassified' for r in coverage),'eligible_occupied_state_category_cells':sum(r['category']!='unclassified' and r['research_eligible_by_section']>0 for r in coverage),'batches':batches,'scope_notes':['Counts are original-file SHA-256 counts, not distinct legal instruments or complete filing packets.','Primary metadata and stricter review sections from the organized snapshot take precedence over overlapping supplementary records.','Broad-category mapping supports navigation; original categories and source records remain available.','Review and validation states are inherited records; this aggregation does not repeat visual or legal review.','State/category presence is not a completion assessment. Source websites were not rechecked during aggregation.']}
    out.mkdir(parents=True)
    for r in rows:write(out/'metadata'/f'{r["sha256"]}.json',r['source_records'])
    public=[{k:v for k,v in r.items() if k!='source_records'} for r in rows]
    write(out/'inventory.json',public);csvfile(out/'inventory.csv',public,list(public[0]))
    write(out/'summary.json',summary);write(out/'link-only.json',link_only);write(out/'review-findings.json',anomalies)
    write(out/'acquisition-holds.json',holds);write(out/'blocked-hosts.json',blocks)
    csvfile(out/'state-summary.csv',state_rows,list(state_rows[0]));csvfile(out/'state-category-coverage.csv',coverage,list(coverage[0]));csvfile(out/'batch-summary.csv',batches,list(batches[0]))
    write(out/'category-mapping.json',CATEGORIES)
    catalog(out/'index.html',public,'../../')
    lines=['# 文档与数据汇总：截至 2026 年 10 月 15 日','',f'本次汇总对应已推送提交 `{head}`。共 **{len(rows)} 份按 SHA-256 去重的原始文件**，其中 **{summary["formats"]["pdf"]} PDF、{summary["formats"]["docx"]} DOCX**；50 个州均有实物文件。州别覆盖包含受限审查文件，不代表各州文件齐全或已获发布许可。','','## 已完成的整理','','统一目录整合原始 410 份快照、补充集合新增 83 份，以及 2026-10-15 的七轮新增 165 份。补充集合的 240 份记录中有 157 份与原始快照重合，不重复计数。一个仅有链接、未下载的俄勒冈州指南单列，也不计入 658 份。','','- `index.html`：全部原件的可搜索目录，按州、类别、审查分区筛选。','- `inventory.csv` / `inventory.json`：去重总清单，保留原始路径、哈希、来源、版本和审查信息。','- `metadata/`：每份原件对应的全部来源记录，重叠记录保留，不覆盖较严格审查状态。','- `state-summary.csv` / `state-category-coverage.csv`：50 州统计及类别有无情况。','- `batch-summary.csv`：批次新增与累计统计。','- `review-findings.json`、权限和访问停止清单：保留后续审查线索。','','## 分类统计','','| 汇总类别 | 份数 |','| --- | ---: |']
    lines += [f'| {LABELS[k]} | {summary["broad_categories"].get(k,0)} |' for k in LABELS]
    lines += ['','分类是浏览用的统一映射。原始类别与细分类别仍完整保留；例如住房诉讼归入房地产及住房，监护、遗产规划、家事和小额诉讼归入法院及一般法律文件。','','## 批次与增长','','| 批次 | 新增去重原件 | 累计 |','| --- | ---: | ---: |']
    lines += [f'| {b["batch"]} | {b["new_unique_originals"]} | {b["combined_unique_originals"]} |' for b in batches]
    lines += ['','## 州别数量较多的地区','','| 州 | 原件数 | PDF | DOCX |','| --- | ---: | ---: | ---: |']
    lines += [f'| {r["state"]} | {r["originals"]} | {r["pdf"]} | {r["docx"]} |' for r in sorted(state_rows,key=lambda r:(-r['originals'],r['state']))[:12]]
    lines += ['','## 验证与限制','',f'本次重新计算全部 {len(rows)} 份原件的 SHA-256，核对 PDF/ZIP 文件签名，并验证原始快照及七轮完整性清单。原有 {len(baseline)} 个 Git 跟踪文件在汇总生成后逐一校验，内容保持一致。记录中的解析状态是此前检查结果，本次未重新执行全库解析、视觉渲染或法律审查。', '',f'按现有分区计算，五大类别的 250 个州／类别格子中，{summary["eligible_occupied_state_category_cells"]} 格有研究材料。此处仅统计材料存在情况，不认定文件家族齐全、当前适用或可直接提交。','','旧快照继续保留权限暂缓 3 份、历史审查 5 份、文件质量审查 11 份及研究参考 3 份；这些分区不会因新目录生成而解除。全库发布批准数仍为 0。10 份文件沿用条件许可记录，其余文件的再分发或商业使用权限仍需逐项审查。', '', '已知复核点包括：威斯康星州 SC-5130V 的目录与印刷版次差异；马里兰州 CC-GN-002 的年龄适用描述差异；CC-DR-062 最后一页页脚表单号差异；既有 XFA、EOF、缺少可搜索文本及其他文件质量标记。附件、送达、签名、计算、现行法律及完整提交包仍需审查。','','完整来源网站本次未重新访问；现有采集时间和网络回执按原记录保留。字节去重不等同于法律语义去重，不同格式或版本可能对应同一文书。','']
    (out/'REPORT.zh-CN.md').write_text('\n'.join(lines),encoding='utf-8',newline='\n')
    for rel,sha in baseline.items():assert digest(repo/rel)==sha,rel
    verification={'status':'passed','checked_at':datetime.now(timezone.utc).isoformat(),'baseline_commit':head,'baseline_tracked_files_preserved':len(baseline),'unique_original_hashes_verified':len(rows),'file_signatures_checked':len(rows),'manifest_checks':manifest_checks,'metadata_records':len(rows),'link_only_unique':len(link_only),'catalog_original_links_resolve':all((repo/r['local_path']).is_file() for r in rows),'source_websites_rechecked':False,'fresh_full_library_parser_review':False,'full_library_semantic_deduplication':False}
    write(out/'verification.json',verification)
    if export:
        assert not export.exists(),'Export destination exists; use a new directory.'
        shutil.copytree(out,export)
        exported=[]
        for row in public:
            row=dict(row);rel=f'documents/{safe(row["section"])}/{safe(row["state"])}/{row["category"]}/{safe(row["title"])}--{row["sha256"][:12]}.{row["format"]}'
            dest=export/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(repo/row['local_path'],dest);assert digest(dest)==row['sha256']
            row['repository_local_path']=row['local_path'];row['local_path']=rel;exported.append(row)
        write(export/'inventory.json',exported);csvfile(export/'inventory.csv',exported,list(exported[0]));catalog(export/'index.html',exported,'')
        write(export/'export-verification.json',{'status':'passed','originals_copied':len(exported),'original_hashes_verified':len(exported),'all_local_original_links_resolve':all((export/r['local_path']).is_file() for r in exported),'source_commit':head})
        write(export/'integrity-manifest.json',{'algorithm':'SHA-256','files':{p.relative_to(export).as_posix():digest(p) for p in sorted(export.rglob('*')) if p.is_file() and p.name!='integrity-manifest.json'}})
    write(out/'integrity-manifest.json',{'algorithm':'SHA-256','files':{p.relative_to(out).as_posix():digest(p) for p in sorted(out.rglob('*')) if p.is_file() and p.name!='integrity-manifest.json'}})
    print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[1]);parser.add_argument('--output',default='collection-overview/2026-10-15');parser.add_argument('--export',type=Path)
    args=parser.parse_args();root=args.repo.resolve()
    if os.name == 'nt':
        root=Path('\\\\?\\'+str(root)) if not str(root).startswith('\\\\?\\') else root
    build(root,root/args.output,args.export)
