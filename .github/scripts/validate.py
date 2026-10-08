from pathlib import Path
import csv,sys,datetime
ROOT=Path(__file__).resolve().parents[1]
with (ROOT/'data/projects.csv').open(encoding='utf-8',newline='') as f:projects=list(csv.DictReader(f))
with (ROOT/'data/phases.csv').open(encoding='utf-8',newline='') as f:phases=list(csv.DictReader(f))
with (ROOT/'data/capstones.csv').open(encoding='utf-8',newline='') as f:capstones=list(csv.DictReader(f))
errors=[];ids=set();valid={'Not Started','Planned','In Progress','Blocked','Completed','Archived'}
for p in projects:
    if p['id'] in ids:errors.append('Duplicate ID '+p['id'])
    ids.add(p['id'])
    if p['status'] not in valid:errors.append('Invalid status '+p['id'])
    if not p['project'].strip():errors.append('Missing name '+p['id'])
    if p['status']=='Completed' and not p['completed_on']:errors.append('Completed date missing '+p['id'])
    for field in ('started_on','completed_on'):
        if p[field]:
            try:datetime.date.fromisoformat(p[field])
            except ValueError:errors.append('Invalid date '+p['id']+' '+field)
    if p['repository_url'] and not p['repository_url'].startswith(('https://','http://')):errors.append('Invalid repository URL '+p['id'])
if len(phases)!=68:errors.append('Expected 68 phases')
if len(capstones)!=12:errors.append('Expected 12 capstones')
for c in capstones:
    if c['id'] not in ids:errors.append('Missing capstone in projects '+c['id'])
for filename in ['ROADMAP.md','PROGRESS.md']:
    if not (ROOT/'docs'/filename).exists():errors.append('Missing '+filename)
if errors:
    print('VALIDATION FAILED\n'+'\n'.join(errors));sys.exit(1)
print(f'Validation passed: {len(projects)} projects, {len(phases)} phases, {len(capstones)} capstones')
