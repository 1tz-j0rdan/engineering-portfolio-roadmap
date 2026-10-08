# Serious Repository Standards

Suggested structure (create only relevant directories):

```text
project/
├── .github/workflows/
├── docs/
│   ├── architecture.md
│   ├── threat-model.md
│   ├── design-decisions/
│   └── diagrams/
├── src/
├── tests/
├── benchmarks/
├── scripts/
├── infrastructure/
├── README.md
├── SECURITY.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
├── Dockerfile          # if applicable
└── compose.yaml        # if applicable
```

The README should cover the problem, features, architecture, installation, usage, examples/screenshots, testing, security, benchmarks when relevant, design decisions, limitations and lessons learned.

**Small projects:** README, basic tests, CI, reproducible setup.
**Medium projects:** requirements, architecture, unit/integration tests, relevant threat model and demo.
**Large projects:** ADRs, extensive testing, observability, IaC, reliability and security reviews.
