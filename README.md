# Knowledge Wiki

AI-compiled personal knowledge base, automatically exported from [Notion](https://notion.so) and synced to GitHub.

AI-compiled personal knowledge base, automatically exported from [Notion](https://notion.so) and synced to GitHub.

<!-- stats:start -->
**2,743+ entries** across 14 topic areas, covering the AI agent ecosystem and beyond.

## What's Inside

| Type | Count | Description |
|------|-------|-------------|
| Concept | ~1,186 | Core concepts with definitions, key points, and cross-references |
| Entity | ~542 | Product/company/people profiles with key data and version updates |
| Synthesis | ~48 | Cross-source analytical essays on major topics |
| Summary | ~967 | Single-article summaries (linked from concepts, not in index) |
<!-- stats:end -->

### Topic Areas

Agent Frameworks · Agent Orchestration · Agent Skills · Coding Agents · LLM · Memory Systems · OpenClaw · Crypto/DeFi · Knowledge Management · Dev Tools · Workflows · Security/Privacy · Content Creation · Business/Ecosystem

## Repository Structure

```
├── wiki/
│   ├── index.md          # Global index (grouped by 14 tags)
│   ├── concepts/         # ~1,190 concept files
│   ├── entities/         # ~540 entity profiles
│   ├── syntheses/        # ~48 analytical essays
│   └── summaries/        # ~970 article summaries
├── schema/
│   ├── CLAUDE.md         # Entry point for AI agents
│   └── WIKI-SCHEMA.md    # Type definitions and naming conventions
├── .claude/skills/
│   └── wiki/SKILL.md     # Cross-agent query skill
├── sync_state.json       # Incremental sync state
└── README.md
```

## For AI Agents

This repo is designed to be self-documenting for AI agents. Two ways to integrate:

### 1. Automatic (Claude Code / compatible agents)

The `.claude/skills/wiki/SKILL.md` provides a ready-to-use query skill with relevance-driven layered retrieval (L0 index → L1 metadata → L2 content). Clone this repo and work inside it — the skill loads automatically.

### 2. Manual (any LLM)

1. Read `wiki/index.md` to understand the full scope
2. Search for relevant entries by keyword or tag
3. Read the YAML frontmatter (first ~15 lines) to judge relevance
4. Read full content of highly relevant entries
5. Follow `wikilinks` (`[name](path)`) to explore related topics

### File Format

Every `.md` file has YAML frontmatter:

```yaml
---
title: Memory OS
type: entity            # concept | entity | synthesis | summary
tags: [记忆系统, Agent 编排]
status: 已审核           # 已审核 | 草稿 | 需更新
confidence: high        # high | medium | low
notion_id: abc123...
---
```

## Data Pipeline

```
Notion Wiki Database
        │
        ▼
   export.py          # Full export + incremental sync (cron every 2H)
        │
        ▼
  GitHub Repo         # This repo (auto-synced via cron + flock)
        │
        ▼
  AI Agents           # Query via SKILL.md or manual retrieval
```

- **Source**: Notion database (`f98c88d3-d587-494a-98ff-92fbaf9228c4`)
- **Sync**: Incremental sync every 2 hours via cron (`flock -n` prevents overlap)
- **Direction**: One-way (Notion → Markdown). Read-only for agents.

## Sync Tool

The export script (`export.py`) lives in the parent `wiki-export/` directory. Key capabilities:

- Full export with rate limiting and checkpoint resume
- Incremental sync via `sync_state.json`
- Automatic deletion detection
- Git auto-commit (skips when no changes)
- Block → Markdown conversion with wikilink support
- `flock` lock to prevent concurrent runs

## Knowledge Sources

Content is compiled from:
- WeChat Official Accounts (微信公众号)
- X/Twitter bookmarks and threads
- Technical blogs and newsletters
- Conference talks and recordings

## License

Private repository. All rights reserved.
