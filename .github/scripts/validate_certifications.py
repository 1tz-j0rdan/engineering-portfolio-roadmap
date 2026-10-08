"""Validate the certification tracker. Does not check external provider catalogs."""
from pathlib import Path
import csv,datetime,sys
root=Path(__file__).resolve().parents[1]
def read(name):
    with (root/'data'/name).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
certs=read('certifications.csv');phases=read('certification_phases.csv')
errors=[];seen=set();orders=set()
statuses={'Not Started','Planned','Studying','Exam Scheduled','Passed - Pending Credential','Earned','On Hold','Expired','Retired'}
for c in certs:
    if c['id'] in seen:errors.append('Duplicate ID '+c['id'])
    seen.add(c['id'])
    if c['order'] in orders:errors.append('Duplicate order '+c['order'])
    orders.add(c['order'])
    if c['status'] not in statuses:errors.append('Invalid status '+c['id'])
    if not c['provider'] or not c['certification']:errors.append('Missing name '+c['id'])
    if not any(p['phase']==c['phase'] for p in phases):errors.append('Unknown phase '+c['id'])
    if c['status']=='Earned' and not c['earned_on']:errors.append('Missing earned_on '+c['id'])
    for field in ('study_started_on','exam_scheduled_on','earned_on','expires_on'):
        if c[field]:
            try:datetime.date.fromisoformat(c[field])
            except ValueError:errors.append('Invalid date '+c['id']+' '+field)
    for field in ('credential_url',):
        if c[field] and not c[field].startswith('https://'):errors.append('Invalid URL '+c['id']+' '+field)
    for field in ('exam_cost','amount_paid'):
        if c[field]:
            try:
                if float(c[field])<0:raise ValueError()
            except ValueError:errors.append('Invalid amount '+c['id']+' '+field)
if len(certs)!=125:errors.append(f'Expected 125 certifications; got {len(certs)}')
if len(phases)!=22:errors.append(f'Expected 22 phases; got {len(phases)}')
if errors:print('CERTIFICATION VALIDATION FAILED\n'+'\n'.join(errors));sys.exit(1)
print(f'Certification validation passed: {len(certs)} certifications, {len(phases)} phases')
