---
title: Lint Report 2026-04-12
type: lint-report
tags:
- 知识管理
- 商业/生态
- 内容自动化
status: 草稿
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f596971a17ea4212b37738375f8407dc
notion_id: f596971a-17ea-4212-b377-38375f8407dc
---

## 检查日期

- 2026-04-12

## 总体健康度

- **0/100 🔴**

- 扣分构成：重复疑似 18 组 × 10 分 = 180 分

- 本轮未发现以下硬性问题：过期草稿、过时内容、缺失状态、缺失标签、废弃标签

- 说明：当前健康度被**重复条目**集中拉低，说明 Wiki 的主要风险已从“字段缺失”转向“概念分叉与重复沉淀”

## 孤岛条目

- 本轮**未确认**孤岛 concept 条目

- 说明：现有 summary 页面里，部分“提取的概念”仍以普通文本呈现，而非统一的页面 mention 或反向关系，因此 concept / entity 的孤岛检测仍有漏判风险

- 当前结论：**暂无已确认孤岛条目**

## 过期草稿

- 无

## 过时内容

- 无

## 重复疑似

- [6551-twitter-to-binance-square](entities/6551-twitter-to-binance-square.md) ↔ 6551-twitter-to-binance-square：名称完全一致

- ClawHub ↔ [ClawHub](entities/ClawHub.md)：名称完全一致

- [Coinglass](entities/Coinglass.md) ↔ Coinglass：名称完全一致

- [CryptoQuant](entities/CryptoQuant.md) ↔ CryptoQuant：名称完全一致

- [DeFiLlama](entities/DeFiLlama.md) ↔ DeFiLlama：名称完全一致

- [FRED](entities/FRED.md) ↔ FRED：名称完全一致

- [Gate MCP Skills](entities/Gate MCP Skills.md) ↔ Gate MCP Skills：名称完全一致

- [IDENTITY.md](concepts/IDENTITY.md.md) ↔ IDENTITY.md：名称完全一致

- [memory-lancedb-pro](entities/memory-lancedb-pro.md) ↔ memory-lancedb-pro：名称完全一致

- OnchainOS Signal ↔ [OnchainOS Signal](concepts/OnchainOS Signal.md)：名称完全一致

- OpenClaw ↔ [OpenClaw](entities/OpenClaw.md)：同名且出现 **concept / entity** 双轨分裂

- [System Prompt 泄露](concepts/System Prompt 泄露.md) ↔ System Prompt 泄露：名称完全一致

- [total-recall](entities/total-recall.md) ↔ total-recall：名称完全一致

- wshobson/agents ↔ [wshobson/agents](entities/wshobson-agents.md)：名称完全一致

- [指纹浏览器](concepts/指纹浏览器.md) ↔ 指纹浏览器：名称完全一致

- [提示注入](concepts/提示注入.md) ↔ 提示注入：名称完全一致

- [跨交易所套利](concepts/跨交易所套利.md) ↔ 跨交易所套利：名称完全一致

- [静态住宅 IP](concepts/静态住宅 IP.md) ↔ 静态住宅 IP：名称完全一致

## 状态异常

- 无

## 标签异常

- 缺失标签：无

- 使用废弃标签（AI Agent / MCP / Notion）：无

- 备注：本轮未发现 concept / entity 的标签空值问题，标签体系完整度良好

## 标签分布统计

| 标签 | concept 数量 |  |  |

| --- | --- | --- | --- |

| Agent 编排 | 86 | LLM | 65 |

| Crypto/DeFi | 60 | OpenClaw | 60 |

| Agent 技能 | 55 | 工作流 | 53 |

| 记忆系统 | 47 | 开发工具 | 43 |

| 安全/隐私 | 37 | Coding Agent | 33 |

| 知识管理 | 28 | 商业/生态 | 24 |

| 内容创作 | 20 | Agent 框架 | 13 |

## 标签分类合理性检查

- **开发工具 → Coding Agent**

  - [Gemini CLI](entities/Gemini CLI.md)：更像 AI 编程代理产品，应优先归入 **Coding Agent**，且类型更适合 **entity**

  - wshobson/agents：本质是 Claude Code / Coding Agent 插件集合，更适合 **Coding Agent**

- **LLM → 记忆系统 / entity**

  - [AI-Native Memory](concepts/AI-Native Memory.md)：主题更接近记忆架构，应优先归入 **记忆系统**

  - MemBrain1.5：是具体开源系统，不应长期停留在 concept

- **开发工具 / OpenClaw → Agent 技能**

  - [Gate MCP Skills](entities/Gate MCP Skills.md)、[6551-twitter-to-binance-square](entities/6551-twitter-to-binance-square.md)、OpenClaw-Medical-Skills：都更像明确的 Skill/技能包，应优先放在 **Agent 技能** 主标签

## 类型分类检查

- **建议 concept → entity**

  - [OpenFang](entities/OpenFang.md)：明确的具体产品/框架，不应保留为 concept

  - [Second Me](entities/Second Me.md)：具体产品名，建议改为 entity

  - [Whisper.cpp](entities/Whisper.cpp.md)：具体开源项目，建议改为 entity

  - [public-apis](entities/public-apis.md)：具体仓库/项目，建议改为 entity

  - [CoPaw](entities/CoPaw.md)：具体产品，建议改为 entity

  - [Cherry Studio](entities/Cherry Studio.md)：具体产品，建议改为 entity

  - [DataClaw](entities/DataClaw.md)：具体项目，建议改为 entity

  - [CLI-Anything](entities/CLI-Anything.md)：具体项目，建议改为 entity

  - [MemOS](entities/MemOS.md)：具体记忆系统，建议改为 entity

  - [TurboQuant](entities/TurboQuant.md)：具体模型/产品名，建议改为 entity

  - [OpenHarness](entities/OpenHarness.md)：具体开源项目，建议改为 entity

  - [EdgeClaw](entities/EdgeClaw.md)：具体产品化实现，建议改为 entity

  - [CutClaw](entities/CutClaw.md)：具体项目，建议改为 entity

  - [Gemini CLI](entities/Gemini CLI.md)：具体产品，建议改为 entity

- **建议 entity → concept**

  - 本轮未发现特别明确的 entity→concept 错分案例

- **需要二选一去重并统一类型**

  - OpenClaw 与 [OpenClaw](entities/OpenClaw.md)：建议保留 **entity** 页，合并 concept 页内容

  - [MemBrain](entities/MemBrain.md) 与 MemBrain1.5：建议按“产品主词条 + 版本信息”统一建模，避免版本号直接分裂成新概念页

## 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 |

| --- | --- | --- | --- |

| [Untitled](concepts/三层知识架构.md) | 草稿 | 审核中 | 已在至少 2 篇 summary 中稳定出现，分别来自 Karpathy LLM Wiki 相关摘要链路 |

| [Untitled](concepts/Karpathy LLM Wiki 方法论.md) | 草稿 | 审核中 | 已被多篇 Karpathy / LLM Wiki 主题摘要反复覆盖，概念边界较稳定 |

## 改进建议

1. **先做去重，不要继续扩量**：优先处理上方 18 组同名重复条目，建议一组只保留 1 个 canonical page，另一页转为内容并入或删除。

1. **统一“产品 = entity，方法/机制 = concept”的判定规则**：尤其是 OpenFang、Second Me、Whisper.cpp、Gemini CLI、MemOS、EdgeClaw 这类条目，已经明显偏向实体页。

1. **把 summary 中的“提取的概念”统一改成页面 mention 或结构化关系**：否则未来孤岛检测、引用计数、状态晋升都会持续失真。

1. **为版本化产品建立主词条机制**：例如 MemBrain / MemBrain1.5、Qwen3.5 / Qwen 3.5，避免“版本号 = 新页面”导致重复膨胀。

1. **对 Skill 类条目单独收口**：Gate MCP Skills、OpenClaw-Medical-Skills、6551-twitter-to-binance-square 等应统一进入 Agent 技能体系，减少标签漂移。

1. **将 OpenClaw 从 concept/entity 双轨合并为单一实体主词条**：当前这是最典型的结构性重复，且会持续污染后续统计。
