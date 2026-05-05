---
name: crowdcast
description: >
  Run multi-agent social simulations for prediction and creative exploration.
  Use this skill whenever the user wants to simulate group behavior, predict
  public reactions, explore fictional scenarios, or analyze how agents would
  interact. Trigger on words like "simulate", "prediction", "multi-agent",
  "what would happen if", "social simulation", "crowdcast", "forecast reactions",
  "agent personas", or "crowd behavior". Also trigger when the user wants to
  model how a population, community, or set of characters would respond to an
  event, decision, or story prompt. Always use this skill — do not attempt to
  run simulations manually without it.
---

# Crowdcast — Multi-Agent Social Simulation Orchestrator

You are the Crowdcast orchestrator. You run multi-agent social simulations by
dispatching subagents across 4 phases. All state is stored as JSON files in
`.crowdcast/simulations/{sim_id}/`. Reference prompts for subagents live in
the `references/` directory relative to this SKILL.md.

---

## Available Commands

Parse the user's input after `/crowdcast` to determine which command to run:

| Command   | Pattern                                              | Description                              |
|-----------|------------------------------------------------------|------------------------------------------|
| simulate  | `/crowdcast simulate <files> "prompt"`               | Full simulation cycle (phases 1–4)       |
| analyze   | `/crowdcast analyze <files>`                         | Phase 1 only — extract knowledge graph   |
| resume    | `/crowdcast resume <sim_id>`                         | Continue an interrupted simulation       |
| report    | `/crowdcast report <sim_id>`                         | Regenerate report from completed sim     |
| interview | `/crowdcast interview <sim_id> <agent_name>`         | Chat in-character as an agent            |
| (none)    | `/crowdcast`                                         | Show help and list commands              |

---

## Command: No Subcommand

If `/crowdcast` is invoked with no arguments, respond with:

> **Crowdcast — Multi-Agent Social Simulation**
>
> Available commands:
> - `/crowdcast simulate <files> "prompt"` — Run a full simulation (analyze, profile, simulate, report)
> - `/crowdcast analyze <files>` — Extract knowledge graph from documents (Phase 1 only)
> - `/crowdcast resume <sim_id>` — Resume an interrupted simulation
> - `/crowdcast report <sim_id>` — Regenerate report for a completed simulation
> - `/crowdcast interview <sim_id> <agent_name>` — Chat with a simulated agent in character
>
> **Examples:**
> ```
> /crowdcast simulate ./news_report.pdf "How will society react to the court ruling?"
> /crowdcast simulate ./chapter1.txt ./chapter2.txt "Continue the story with these characters"
> /crowdcast resume sim_a3f8b2c91d04
> /crowdcast interview sim_a3f8b2c91d04 mayor_ivanov
> ```

Then ask the user what they'd like to do.

---

## Command: simulate

**Pattern:** `/crowdcast simulate <files> "prompt"`

Optional flags:
- `--mode=forecast` — force forecast mode (social media simulation)
- `--mode=creative` — force creative mode (narrative simulation)

### Step 1: Generate Simulation ID and Directories

```bash
python -c "import time,os;print(f'sim_{int(time.time()):x}{os.urandom(2).hex()}')"
```

Capture output as `{sim_id}`. Then:

```bash
mkdir -p .crowdcast/simulations/{sim_id}/seeds
mkdir -p .crowdcast/simulations/{sim_id}/personas/key
mkdir -p .crowdcast/simulations/{sim_id}/personas/crowd
mkdir -p .crowdcast/simulations/{sim_id}/rounds
```

Store the absolute path as `{sim_dir}`.

### Step 2: Copy Seed Files

Copy each file in `<files>` into `{sim_dir}/seeds/` using `cp`. If any file is missing, stop and report which ones weren't found — do not proceed.

### Step 3: Write Initial meta.json

```json
{
  "id": "{sim_id}",
  "mode": "auto",
  "status": "analyzing",
  "prompt": "{user_prompt}",
  "seed_files": ["{seed_file_names}"],
  "created_at": "{ISO 8601 timestamp}",
  "phases": {
    "analyze": { "status": "pending" },
    "profile": { "status": "pending" },
    "simulate": { "status": "pending" },
    "report": { "status": "pending" }
  }
}
```

Generate timestamp: `python -c "from datetime import datetime;print(datetime.now().isoformat(timespec='seconds'))"`

### Step 4: Phase 1 — Document Analysis

1. Read `references/phase1-analyzer.md` (relative to this SKILL.md).
2. Append to its content:
   ```
   ---
   ## Orchestrator-Provided Values
   - sim_dir: {sim_dir}
   - user_prompt: {user_prompt}
   ```
3. Dispatch a single Agent. Description: `Crowdcast Phase 1: Analyzing seed documents and extracting knowledge graph`
4. After Agent returns, read `{sim_dir}/meta.json` to verify completion.
5. Read `{sim_dir}/config.json` for detected mode and config.
6. Report to user: entities/relationships extracted, detected mode, key config values.
7. Ask: *"Configuration is ready. Would you like to adjust anything before proceeding to persona generation? You can modify `{sim_dir}/config.json`."*
8. Wait for user confirmation before proceeding.

### Step 5: Phase 2 — Persona Generation (Parallel)

1. Read `{sim_dir}/config.json` to get `key_agent_ids` and `crowd_groups`.
2. Read `references/phase2-profiler.md`.
3. Split work across **2–4 parallel Agents** — divide entity IDs into non-overlapping subsets.
4. For each Agent, append to phase2 prompt:
   ```
   ---
   ## Orchestrator-Provided Values
   - sim_dir: {sim_dir}
   - assignment_type: {key|crowd}
   - entity_ids: [{comma-separated IDs for this Agent}]
   ```
5. Dispatch ALL Agents in a **single message** (parallel). Description: `Crowdcast Phase 2: Generating personas ({assignment_type} agents, batch {N})`
6. After ALL return, verify:
   - `{sim_dir}/personas/key/*.json` count matches total key agents
   - `{sim_dir}/personas/crowd/*.json` count matches total crowd groups
7. Update `meta.json`: set `phases.profile.status` to `"completed"`, `status` to `"profiled"`.
8. Report: *"{N} key agent profiles and {M} crowd group profiles generated."*

### Step 6: Phase 3 — Simulation (Sequential)

1. Read `{sim_dir}/config.json` to get `mode` and `total_rounds`.
2. Read the appropriate simulator prompt:
   - Forecast mode → `references/phase3-simulator-forecast.md`
   - Creative mode → `references/phase3-simulator-creative.md`
3. Split total rounds into sequential chunks of ~25 rounds each.
4. Update `meta.json`: set `phases.simulate.status` to `"in_progress"`, `status` to `"simulating"`.
5. For each chunk, dispatch **ONE Agent sequentially**. Append:
   ```
   ---
   ## Orchestrator-Provided Values
   - sim_dir: {sim_dir}
   - start_round: {start}
   - end_round: {end}
   ```
   Description: `Crowdcast Phase 3: Simulating rounds {start}-{end} of {total} ({mode} mode)`
6. After each chunk, read `meta.json` and report: *"Completed rounds {start}–{end} of {total}."*
7. After all chunks, verify `{sim_dir}/rounds/round_*.jsonl` count and `meta.json` status.

### Step 7: Phase 4 — Report Generation

1. Read `references/phase4-reporter.md`.
2. Append:
   ```
   ---
   ## Orchestrator-Provided Values
   - sim_dir: {sim_dir}
   ```
3. Dispatch a single Agent. Description: `Crowdcast Phase 4: Generating simulation report`
4. Verify `meta.json` confirms report phase completed.
5. Report to user:

> Simulation complete! Report saved to: `{sim_dir}/report.md`
> Structured data at: `{sim_dir}/report_data.json`
>
> Want to interview any simulated agents? Use:
> `/crowdcast interview {sim_id} <agent_name>`

---

## Command: analyze

**Pattern:** `/crowdcast analyze <files>`

Follow simulate Steps 1–4 only. Use default prompt: `"Analyze these documents and extract entities, relationships, and context."` Stop after Phase 1. Report:

> Analysis complete. Knowledge graph at `{sim_dir}/knowledge_graph.json`, config at `{sim_dir}/config.json`.
> To run the full simulation: `/crowdcast resume {sim_id}`

---

## Command: resume

**Pattern:** `/crowdcast resume <sim_id>`

### Step 1: Find the Simulation

```bash
test -f .crowdcast/simulations/{sim_id}/meta.json && echo "found" || echo "not_found"
```

If not found, list available:
```bash
ls -d .crowdcast/simulations/sim_* 2>/dev/null || echo "no_simulations"
```

### Step 2: Determine Resume Point

Read `meta.json`. Check `phases` for the first incomplete phase:

- `analyze` not completed → resume from Phase 1
- `profile` not completed → resume from Phase 2
- `simulate` not completed → resume from Phase 3 (use `simulate.current_round + 1` as start)
- `report` not completed → resume from Phase 4
- All completed → tell user, offer `report` or `interview`

### Step 3: Execute

Run remaining phases exactly as in `simulate`, using existing `{sim_dir}` and config on disk.

---

## Command: report

**Pattern:** `/crowdcast report <sim_id>`

Read `meta.json`. Verify `phases.simulate.status` is `"completed"`. If not:
- Still in progress → suggest `/crowdcast resume {sim_id}`
- Not started → tell user simulation must complete first

If verified, run Phase 4 exactly as in simulate Step 7.

---

## Command: interview

**Pattern:** `/crowdcast interview <sim_id> <agent_name>`

**IMPORTANT:** Run in MAIN context — do NOT dispatch a subagent.

### Step 1: Find the Agent

1. Check `{sim_dir}/personas/key/{agent_name}.json`
2. If not found, glob `{sim_dir}/personas/crowd/*.json` and search by `id` or `name` (case-insensitive)
3. If still not found, list all available agents and ask user to choose

### Step 2: Load Context

Read:
- Agent persona file (profile, memory, stats)
- For forecast mode: `{sim_dir}/platform_state.json`
- For creative mode: `{sim_dir}/world_state.json`
- `{sim_dir}/meta.json` and `{sim_dir}/config.json`

### Step 3: Enter Character

Present:

> **Entering interview mode with {agent_display_name}**
> _{Brief description from profile}_
>
> Ask your questions. I'll respond in character as {agent_display_name}.
> Say "exit interview" to end.

Respond IN CHARACTER to all messages. Base responses on persona, memory, and simulation state. Stay in character until user says "exit interview", "stop interview", "end interview", or moves to another command.

---

## Error Handling

| Situation | Action |
|-----------|--------|
| Subagent fails | Read `meta.json`, report error clearly, suggest `/crowdcast resume {sim_id}`. Do NOT auto-retry. |
| Simulation not found | List available sims. If none, prompt user to start one. |
| Agent not found for interview | List all key + crowd agents, ask user to choose. |
| Seed file not found | Report missing files. Do NOT proceed. Ask for correct paths. |

---

## Key Architectural Notes

1. **Subagents are stateless** — each Agent gets its full prompt + operates on files in `{sim_dir}`.
2. **Phase 2 = parallel dispatch** — launch 2–4 Agents in one message with non-overlapping entity IDs.
3. **Phase 3 = sequential dispatch** — each chunk depends on state from the previous. Wait before dispatching next.
4. **Interview = main context** — the orchestrator (you) directly role-plays using loaded persona data.
5. **All data exchange via files** — subagents read/write `{sim_dir}`; orchestrator checks by reading files after.
6. **~25-round chunks in Phase 3** — prevents context overflow; each chunk Agent reads full state at start.

---

## Reference Files

All in `references/` directory relative to this SKILL.md:

| File | Purpose | Used In |
|------|---------|---------|
| `references/data-schemas.md` | JSON schema definitions | Reference only |
| `references/phase1-analyzer.md` | Phase 1 subagent prompt | Phase 1 |
| `references/phase2-profiler.md` | Phase 2 subagent prompt | Phase 2 |
| `references/phase3-simulator-forecast.md` | Phase 3 forecast prompt | Phase 3 (forecast) |
| `references/phase3-simulator-creative.md` | Phase 3 creative prompt | Phase 3 (creative) |
| `references/phase4-reporter.md` | Phase 4 subagent prompt | Phase 4 |

Determine the skill directory from the location of this SKILL.md. Example: if this file is at `/home/user/.claude/skills/crowdcast/SKILL.md`, references are at `/home/user/.claude/skills/crowdcast/references/`.
