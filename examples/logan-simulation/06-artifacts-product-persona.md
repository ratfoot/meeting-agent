# [PRODUCT] Persona & Roadmap Mapping

---

## Primary Persona: The Computational PI

### Profile

| Attribute | Value |
|-----------|-------|
| **Archetype** | Principal Investigator running ML/AI-focused research lab |
| **Role** | Dr. Logan Martinez, Computational Psychiatry Lab |
| **Team Size** | Small (PI + bioinformatician + postdocs) |
| **Budget Authority** | Discretionary grant funds for pilot; institutional approval needed for scale |
| **Technical Sophistication** | High—understands ML pipelines, data formats, coordinate systems |

### Psychographic Profile

**Frustration:** "I'm a PI. My job is to make discoveries. Instead I'm a data janitor with a PhD."

**Self-Image:** Sees himself as a scientist and innovator, not an administrator or IT manager

**Fear:** Being scooped by competitors (Stanford already beat him to publication once)

**Aspiration:** Redirect budget from infrastructure to high-impact science; publish first

---

### Needs & Goals

| Category | Need |
|----------|------|
| **Professional** | Publish faster than competitors; win grant renewals; build reputation in computational psychiatry |
| **Operational** | Reduce time from data acquisition to model training; eliminate manual normalization |
| **Personal** | Stop doing "digital janitorial work"; feel like a scientist again |
| **Team** | Free bioinformatician (Marcus) to do actual ML work instead of ETL |

---

### Key Job to be Done (JTBD)

> "When I am **training ML models for treatment response prediction**, I want to **access harmonized multi-modal data without manual normalization** so that I can **publish discoveries before my competitors and justify my grant renewals**."

**Alternative JTBD formulation:**
> "I need to **reduce ingestion-to-analysis time from 2 weeks to 4 hours** so that I can **iterate on models fast enough to maintain competitive advantage**."

---

## Secondary Persona: The Bioinformatician

### Profile

| Attribute | Value |
|-----------|-------|
| **Archetype** | Technical executor responsible for data pipelines and analysis |
| **Role** | Marcus (bioinformatician in Logan's lab) |
| **Daily Work** | Data cleaning, format conversion, coordinate liftover, pipeline maintenance |
| **Pain** | Spends 60% of time on "munging" instead of model training |

### Key JTBD

> "When I am **preparing datasets for ML training**, I want to **access pre-normalized data via API** so that I can **focus on model architecture and feature engineering instead of CSV cleaning**."

---

## Workflow Friction Map

### Current State (Before HoX)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 1: Data Access                                                         │
│ ├── Submit DUA to UK Biobank → 8 MONTHS                                     │
│ ├── Wait for legal review                                                   │
│ └── Postdoc time consumed by paperwork                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ STEP 2: Data Acquisition                                                    │
│ ├── Download from walled garden                                             │
│ ├── Pay egress fees → $47K/QUARTER                                          │
│ └── Store redundantly across environments                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│ STEP 3: Data Normalization                                                  │
│ ├── Coordinate liftover (hg19 → hg38)                                       │
│ ├── Column name harmonization                                               │
│ ├── Timestamp format alignment                                              │
│ └── Marcus time → 60% OF FTE                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│ STEP 4: Pipeline Maintenance                                                │
│ ├── No central warehouse                                                    │
│ ├── No cross-modality versioning                                            │
│ └── Rebuild on methodology pivot → EVERY 6 MONTHS                           │
├─────────────────────────────────────────────────────────────────────────────┤
│ STEP 5: Model Training                                                      │
│ └── Finally can train models (if time remains)                              │
└─────────────────────────────────────────────────────────────────────────────┘

Total Time: 2 WEEKS (ingestion-to-analysis)
Outcome: Stanford publishes first
```

### Target State (With HoX)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 1: Data Access                                                         │
│ └── Pre-harmonized biobank data available → IMMEDIATE                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ STEP 2: Data Query                                                          │
│ └── Warehouse API returns analysis-ready data → NO EGRESS                   │
├─────────────────────────────────────────────────────────────────────────────┤
│ STEP 3: Model Training                                                      │
│ └── Marcus trains models from day 1                                         │
└─────────────────────────────────────────────────────────────────────────────┘

Total Time: 4 HOURS (ingestion-to-analysis)
Outcome: Logan publishes first
```

---

## Feature Alignment

| Friction Point | HoX Capability | Feature/API |
|----------------|----------------|-------------|
| DUA delays (8 months) | Pre-ingested sovereign biobank | Data Management (licensed datasets) |
| Egress fees ($47K/quarter) | Co-located compute | Compute API + Warehouse |
| Coordinate liftover | Standardized schema (hg38) | Warehouse ingestion pipeline |
| Column name variance | Metadata-driven normalization | Warehouse schema enforcement |
| Timestamp alignment | Automated temporal alignment | Ingestion pre-processor |
| No central warehouse | Unified data warehouse | Warehouse Core |
| No versioning | Metadata-driven versioning | Data Management versioning |
| Rebuild on pivot | Modality-agnostic architecture | Extensible warehouse schema |

---

## Product Feedback for Roadmap

### Signals from This Conversation

| Signal | Implication | Priority |
|--------|-------------|----------|
| **UK Biobank integration critical** | Pre-harmonized Biobank data is a key differentiator for this persona | High |
| **EEG mentioned as future modality** | Multi-modal extensibility (beyond genomic) is important | Medium |
| **"Walled garden" frustration** | Messaging around "sovereign" and "escape vendor lock-in" resonates | High |
| **Grant renewal as buying trigger** | Time-based urgency; align sales cycles to grant calendars | Medium |
| **Stanford competitor pressure** | "Time to publication" is an emotional value driver | High |

### Feature Requests (Implicit)

1. **Biobank-specific documentation** - Logan needs to see exactly how HoX handles UK Biobank data
2. **ROI calculator** - Ability to input current costs and show projected savings
3. **Compliance certifications** - HIPAA/PHI documentation for IT Security conversations

---

## Segment Hypothesis

Logan represents a broader segment: **"Computational PIs"** — researchers running ML-focused labs who:
- Have promising methodologies but are bottlenecked by data infrastructure
- Feel they are "doing IT work instead of science"
- Face grant renewal pressure and competitive publication races
- Have discretionary pilot budgets but need institutional buy-in for scale

**Market sizing question:** How many NIH-funded computational biology labs fit this profile?
