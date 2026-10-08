# Standard Nine-Stage Project Workflow

Use this lifecycle for every project. Scale the artifacts to project complexity.

## 1. Define
- State problem, audience, goals, non-goals and success criteria.
- Define MVP and measurable acceptance criteria.
- Output: project charter and scoped issue backlog.

## 2. Research
- Study fundamentals, official documentation, related solutions and trade-offs.
- Prototype unknown or risky technology.
- Output: research notes and selected stack.

## 3. Design
- Record functional and nonfunctional requirements.
- Diagram components, data flow and interfaces.
- Identify failure modes, security boundaries and tests.
- Break work into milestones and GitHub issues.
- Output: architecture, requirements, ADRs, threat model as relevant.

## 4. Initialize
- Create the implementation repository, .gitignore and license.
- Configure dependencies, formatting, linting, tests and CI.
- Ensure a clean clone builds and passes an initial test.
- Output: reproducible baseline.

## 5. Implement incrementally
Repeat per issue: select → clarify acceptance criteria → design → branch → implement → test → self-review → PR → merge.
- Make focused commits and update docs with the code.
- Output: reviewed, working increments.

## 6. Verify and harden
- Run unit, integration and end-to-end tests as applicable.
- Test edge cases, failure recovery, security and performance as appropriate.
- Compare results with acceptance criteria; record limitations.
- Output: verification evidence.

## 7. Deploy and demonstrate
- Package or deploy as relevant, with repeatable setup.
- Validate from a clean environment and capture demos/screenshots.
- Never publish credentials, sensitive data or harmful artifacts.
- Output: reproducible demo.

## 8. Document and review
- Finalize README, architecture, usage, tests, decisions, limitations and lessons learned.
- Perform a portfolio-quality review.
- Output: readable technical record.

## 9. Release and maintain
- Tag a release, update changelog and verify published artifacts.
- Link implementation repo in projects.csv; mark Completed only after definition of done.
- Generate progress, commit and push.
- Output: completed portfolio entry and maintenance backlog.

## Definition of done
- Acceptance criteria met; appropriate tests pass.
- Clean checkout is reproducible.
- Security and known limitations documented.
- Technical choices explained; demo or evidence provided.
- Completion date and repository URL recorded in the tracker (for separate repos).
