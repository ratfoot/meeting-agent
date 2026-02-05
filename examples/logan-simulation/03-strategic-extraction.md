# Phase 2: Strategic Extraction

---

## Section A: Strategic Context (The "Why")

| Element | Extracted Value |
|---------|-----------------|
| **Primary Objective** | Build ML models for treatment response prediction in depression; move from research to clinical validation |
| **The "Why Now"** | Grant renewal deadline in 90 days; competitors at Stanford just published similar work; promising GNN architecture sitting idle for 4 months |
| **Cost of Inaction** | |
| - Labor Loss | 8 months of postdoc time on DUA paperwork; 60% of bioinformatician (Marcus) time on "digital janitorial work" instead of model training |
| - Resource Loss | $47,000/quarter in cloud egress fees ("almost a postdoc salary"); redundant storage across walled gardens (UK Biobank, Snellius) |
| - Opportunity Loss | GNN lithium response paper delayed 4+ months; Stanford competitors published first despite Logan having the idea first |
| **Scientific Alpha at Risk** | "We had the idea first. My competitors at Stanford published something similar last month." - Direct publication and priority loss; risk of being scooped again on future work |

### The "Data Harmonization Tax" (Customer's Own Framing)
Logan describes four compounding barriers:
1. **Access Barrier** - 8-month DUA approval cycles
2. **Aggregation Barrier** - $47K/quarter egress fees
3. **Normalization Barrier** - 60% FTE on coordinate liftover, column munging
4. **Custodial Barrier** - No unified warehouse; rebuilds pipeline every 6 months on methodology pivots

---

## Section B: Practical Logistics & Personas (The "How")

| Element | Extracted Value |
|---------|-----------------|
| **Persona** | Principal Investigator (Logan) - Computational Psychiatry; Secondary: Bioinformatician (Marcus) |
| **Needs & Goals** | Logan: "My job is to make discoveries. Instead I'm a data janitor with a PhD." Wants to redirect budget from data wrangling to science. Marcus: Wants to train models, not clean CSVs. |
| **Key JTBD** | "I need to **reduce ingestion-to-analysis time from 2 weeks to 4 hours** so that I can **train ML models and publish before competitors**" |
| **Data Ecosystem** | |
| - External Sources | UK Biobank, NCBI GEO, Dutch Snellius supercomputer (collaborator data) |
| - Internal Modalities | Genomic (hg19, hg38), Clinical phenotypes, potentially EEG (future) |
| - Scale | ~15,000 subjects in pilot cohort |
| **Current Workflow Friction** | |
| 1. | DUA approval process (8 months for UK Biobank) |
| 2. | Data stuck in walled gardens (cannot move, must pay egress) |
| 3. | Coordinate liftover (hg19 → hg38) |
| 4. | Column name harmonization across sources |
| 5. | Timestamp format normalization |
| 6. | No central warehouse - rebuild pipeline on every pivot |
| 7. | No cross-modality versioning system |
| **Feature Alignment** | |
| - Data Management | Eliminate manual DUA overhead with pre-harmonized biobank data |
| - Warehouse API | Unified schema eliminates coordinate liftover and column munging |
| - Compute | Avoid egress by keeping data and compute co-located |
| - Versioning | Metadata-driven core handles modality pivots without rebuild |

---

## Section C: Power Dynamics & Success Roadmap (The "Win")

| Element | Extracted Value |
|---------|-----------------|
| **Champion** | Dr. Logan Martinez (PI) - feels the pain directly, has discretionary grant funds for pilot |
| **Technical Evaluator** | Marcus (Bioinformatician) - will evaluate API, daily user |
| **Economic Buyer (Scale)** | Dr. Patel (Department Chair) - needed for departmental adoption |
| **Influencers/Blockers** | IT Security - must sign off on PHI/protected health data |
| **Success Definition** | "Ingestion-to-analysis goes from two weeks to four hours" on UK Biobank psychiatric cohort |
| **Pilot Requirements** | |
| - First Dataset | UK Biobank psychiatric cohort (~15,000 subjects, genomic + phenotypic) |
| - Security/Compliance | PHI handling, likely needs HIPAA alignment, IT Security review |
| - Timeline | 90-day grant renewal deadline creates urgency |
| **Expansion Question** | "If we prove automation, who else needs to see that to greenlight full adoption?" → **Dr. Patel** (confirmed) |

### Stakeholder Map

```
                    ┌─────────────────┐
                    │   Dr. Patel     │
                    │ (Dept Chair)    │
                    │ ECONOMIC BUYER  │
                    └────────┬────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
     ┌────────▼────────┐          ┌────────▼────────┐
     │   Dr. Logan     │          │   IT Security   │
     │  (PI, Champion) │          │   (Blocker)     │
     │ PILOT AUTHORITY │          │   PHI Sign-off  │
     └────────┬────────┘          └─────────────────┘
              │
     ┌────────▼────────┐
     │     Marcus      │
     │(Bioinformatician)│
     │ TECHNICAL EVAL  │
     └─────────────────┘
```

---

## Quantified Value Summary

| Metric | Current State | Target State | Value |
|--------|---------------|--------------|-------|
| DUA Approval Time | 8 months | 0 (pre-harmonized) | 8 months recovered |
| Egress Costs | $47K/quarter | $0 (co-located) | ~$188K/year savings |
| Bioinformatician Utilization | 40% on science | 100% on science | 60% FTE recovered |
| Ingestion-to-Analysis | 2 weeks | 4 hours | 97% reduction |
| Time-to-Publication | Delayed (4+ months) | Competitive | First-mover advantage |
