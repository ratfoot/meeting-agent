# HoX Meeting Tools

Process sales calls and prep with AI agents.

## Local

```bash
python3 run.py
```

Uses Claude CLI locally. For deploy, set `GEMINI_API_KEY`.

## Deploy (Railway)

```bash
railway up
```

Set `GEMINI_API_KEY` in Railway variables. Get key at aistudio.google.com.

## Agents

| Agent | Input | Output |
|-------|-------|--------|
| `discovery-demo` | Call transcript | Deal audit, personas, follow-up email |
| `pre-meeting` | LinkedIn + context | Discovery questions |

## Add Agents

Drop a `.md` file in `agents/`. Auto-appears in dropdown.
