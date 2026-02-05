# HoX Meeting Tools

Local tools for processing sales meetings and prep for HoX.bio.

## What is HoX?

HoX.bio is a biodata platform that eliminates the "Data Harmonization Tax" for research labs.

**Four barriers we solve:**
1. **Access** — Months of DUA/legal delays for raw data
2. **Aggregation** — Egress fees moving terabytes across clouds
3. **Normalization** — 60% of bioinformatician time on munging (hg19→hg38, schema alignment)
4. **Custodial** — Manual versioning, file-tracking, storage rebuilds

**Capabilities:** Genome Viewer, Warehouse API, Data Management, Compute

**Personas:** PIs, Bioinformaticians, Clinical Researchers

## Project Structure

```
run.py            # Run this
agents/           # Agent prompts (add new .md files here)
app/templates/    # Web UI
examples/         # Sample outputs for reference
```

## Running

```bash
python3 run.py
```

Opens browser at localhost:5001. Select agent, paste input, get output.

## Agents

- **discovery-demo** — Post-call analysis: processes transcript into deal audit, persona map, follow-up email
- **pre-meeting** — Pre-call research: takes LinkedIn + context, outputs discovery questions

### Adding Agents

Create `agents/your-agent.md`. It will auto-appear in the dropdown. The agent prompt should:
- Define the input format expected
- Define the output structure
- Be terse — Claude does the heavy lifting

## Guidelines for Claude

When working on this project:
- Keep agents terse. No lecturing. Output templates, not instructions.
- The app is intentionally minimal — resist adding complexity
- Agents should generate all outputs automatically (no confirmation prompts)
- Reference HoX context (four barriers, personas) in agent prompts
- Example outputs in `examples/logan-simulation/` show expected quality
