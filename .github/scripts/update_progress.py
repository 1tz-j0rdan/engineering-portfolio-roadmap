from pathlib import Path
import csv
from collections import Counter
ROOT = Path(__file__).resolve().parents[1]
with (ROOT/'data/projects.csv').open(encoding='utf-8',newline='') as f:
    projects=list(csv.DictReader(f))
with (ROOT/'data/phases.csv').open(encoding='utf-8',newline='') as f:
    phases=list(csv.DictReader(f))
counts=Counter(p['status'] for p in projects)
summary=f"{len(projects)} projects tracked · {counts['Completed']} completed · {counts['In Progress']} in progress"
lines=['# Progress Dashboard','',f'**{summary}**','', '| Status | Count |','|---|---:|']
for status in ['Not Started','Planned','In Progress','Blocked','Completed','Archived']:
    lines.append(f'| {status} | {counts[status]} |')
lines += ['','## Progress by phase','','| Phase | Topic | Completed | Total |','|---:|---|---:|---:|']
for ph in phases:
    group=[p for p in projects if int(p['phase'])==int(ph['phase'])]
    lines.append(f"| {ph['phase']} | {ph['title']} | {sum(p['status']=='Completed' for p in group)} | {len(group)} |")
lines+=['','## Completed projects','','| ID | Project | Repository | Completed |','|---|---|---|---|']
for p in projects:
    if p['status']=='Completed':
        link=f"[GitHub]({p['repository_url']})" if p['repository_url'] else '—'
        lines.append(f"| {p['id']} | {p['project']} | {link} | {p['completed_on'] or '—'} |")
if counts['Completed']==0:lines.append('| — | No projects completed yet | — | — |')
(ROOT/'docs/PROGRESS.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
road=['# Full 68-Phase Roadmap','','Generated from `data/projects.csv`. Statuses and links update when you run `python scripts/update_progress.py`.','']
for ph in phases:
    road += [f"## Phase {ph['phase']} — {ph['title']}",'']
    for p in projects:
        if int(p['phase'])==int(ph['phase']):
            mark='x' if p['status']=='Completed' else ' '
            link=f" — [repository]({p['repository_url']})" if p['repository_url'] else ''
            road.append(f"- [{mark}] **{p['id']}** {p['project']} — {p['status']}{link}")
    road.append('')
(ROOT/'docs/ROADMAP.md').write_text('\n'.join(road)+'\n',encoding='utf-8')
readme=ROOT/'README.md';txt=readme.read_text(encoding='utf-8');a=txt.index('<!-- PROGRESS_START -->')+len('<!-- PROGRESS_START -->');b=txt.index('<!-- PROGRESS_END -->');readme.write_text(txt[:a]+'\n'+summary+'\n'+txt[b:],encoding='utf-8')
print(summary)
