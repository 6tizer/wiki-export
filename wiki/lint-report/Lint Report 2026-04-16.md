---
title: Lint Report 2026-04-16
type: lint-report
tags:
- Agent 编排
- Coding Agent
- 商业/生态
- Agent 技能
- OpenClaw
- LLM
- 记忆系统
- 开发工具
- Crypto/DeFi
- Agent 框架
- 工作流
- 知识管理
- 安全/隐私
- 内容创作
status: 草稿
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/5ed0bd6457ee417b95a7b4fb2c64b13d
notion_id: 5ed0bd64-57ee-417b-95a7-b4fb2c64b13d
---

## 检查日期

2026-04-16

## 总体健康度

🟡 **67 / 100**

> 知识库整体质量良好，无过期草稿和过时内容。主要扣分项为 concept/entity 近似重复对（3 对）与 summary 近似重复组（~7 组）。引用结构化率约 43%，纯文本引用存量较多，需批量修复。

---

## 全库统计

| 类型 | 草稿 | 审核中 | 已审核 | 需更新 | 合计 |

| --- | --- | --- | --- | --- | --- |

| concept | 824 | 107 | 12 | 1 | 944 |

| entity | 389 | 50 | 1 | 0 | 440 |

| summary | 0 | 0 | 863 | 0 | 863 |

| synthesis | 47 | 0 | 0 | 0 | 47 |

| qa | 1 | 0 | 4 | 0 | 5 |

| **合计** | **1261** | **157** | **880** | **1** | **2299** |

**备注：** 草稿积压量大（1261 条），其中 concept 草稿 824 条、entity 草稿 389 条，synthesis 草稿 47 条。synthesis 全部处于草稿状态，需关注。

---

## 孤岛条目

✅ **本次未发现确认的孤岛条目。**

检测方法：对前 300 个 concept/entity 条目进行标题匹配初筛，所有抽查条目均可在 summary 标题中找到关联词汇。由于 summary 无 relation 字段指向 concept，无法全量 SQL 精确检测，建议后续引入 relation 字段以提升检测精度。

---

## 过期草稿

✅ **无过期草稿（>7 天）。**

全库 concept/entity 草稿均创建于 2026-04-10 之后，距今不足 7 天，暂无需晋升。随着时间推移，下次检查将产生大量可晋升草稿，建议届时重点关注。

---

## 过时内容

✅ **无过时内容（最后编译时间 >30 天）。**

所有条目最后编译时间均在 2026-03-17 之后。知识库仍处于快速增长阶段，时效性良好。

---

## 重复疑似

### A. Concept/Entity 完全同名重复

✅ 无完全同名重复对。

### B. Concept/Entity 规范化后近似重复

发现 **3 个疑似重复对**（差异原因见备注）：

| # | 条目 A | 条目 B | 差异原因 |

| --- | --- | --- | --- |

| 1 | [Untitled](concepts/Agent Team.md)（concept） | Untitled（concept） | 单复数差异，归一化后同名 |

| 2 | [Untitled](concepts/Agent Team.md) / Untitled | Untitled（concept） | 英文/中文版本，语义完全相同 |

| 3 | [Untitled](entities/AI Scientist.md)（entity） | Untitled（entity） | 驼峰/空格格式差异，同一产品 |

| 4 | Untitled（concept） | [Untitled](concepts/x402 协议.md)（concept） | 同一协议，名称含/不含后缀词 |

**注：** 第 1/2 行实为同一组三元重复（Agent Team / Agent Teams / Agent团队），计为 2 对。

### C. Summary 完全同名重复

✅ 无完全同名重复。

### D. Summary 近似同名重复

在前 100 条 summary 中发现 **~7 组**近似重复（由 Compiler 对相同源文章重复触发导致）：

| # | 组描述 | 代表条目 | 差异原因 |

| --- | --- | --- | --- |

| 1 | 2025元旦 AI Agent 全景（市値/市值） | [Untitled](summaries/摘要：2025 元旦 AI Agent 全景：Mindshare vs 市值，谁在领跑加密智能体赛道？.md) vs Untitled | 繁简体字差异（値→值） |

| 2 | Andrej Karpathy LLM+MD+Wiki 知识库 | [Untitled](summaries/摘要：Andrej Karpathy 现在成了一个超级 AI 明星。他最近主推的一个 LLM+ MD + Wiki 的个人知识库特别火.md) / Untitled / Untitled | 标题格式微差（空格/括号） |

| 3 | ai-hedge-fund 巴菲特/芒格（错字） | [Untitled](summaries/摘要：ai-hedge-fund：让 AI 扮演巴菲特和芒格，帮你做投资决策.md) vs Untitled | 人名错字（应为「巴菲特」） |

| 4 | agency-agents AI 虚拟团队 | [Untitled](summaries/摘要：Agency Agents：用 147 个 AI 专家角色，把 Claude Code 变成一整家公司.md) / [Untitled](summaries/摘要：agency-agents：一个开源的 AI 虚拟团队，144 个专业 Agent 覆盖 12 个职能部门.md) / [Untitled](summaries/摘要：agency-agents：用 147 个 Markdown 文件，搭建你的零成本 AI 专业团队.md) | 同源文章，标题改写差异 |

| 5 | Anthropic 封杀 OpenClaw 48小时 | [Untitled](summaries/摘要：Anthropic 封杀 48 小时，逼出 OpenClaw 最强反击！龙虾首次会生视频了.md) / Untitled / Untitled | 标题有无句号/空格差异 |

| 6 | Andrej Karpathy LLM+MD+Wiki（Notion+1） | Untitled vs [Untitled](summaries/摘要：Andrej Karpathy 现在成了一个超级 AI 明星。他最近主推的一个 LLM+ MD + Wiki 的个人知识库特别火.md) | 标题描述详略差异 |

| 7 | AutoResearch Karpathy相关 | [Untitled](summaries/摘要：AutoResearchClaw + MetaClaw：让 AI 自主写论文，还能从失败中越跑越强.md) vs [Untitled](summaries/摘要：AutoResearch：Karpathy 让 AI 自主跑实验的方法论，以及它如何改变你的工作方式.md) | 侧重点不同但主题高度重叠 |

> 全库共 863 条 summary，本次仅抽查前 100 条即发现 7 组，按比例估计全库可能有 **50–60 组**近似重复。建议 Fixer 做全量归并。

---

## 状态异常

✅ **无状态为空的条目。**

全库 2,299 条目（不含 index/lint-report）均有状态值。

---

## 标签异常

### 缺失标签

✅ **无 concept/entity 缺失标签。**

### 废弃标签使用

✅ **无废弃标签（AI Agent / MCP / Notion）使用。**

全库已完成标签体系迁移，当前 14 个合法标签使用正常。

---

## 标签分布统计

> 注：基于前 300 个 concept/entity 样本统计，供趋势参考（非全量精确计数）。

| 标签 | 样本计数 | 趋势 |

| --- | --- | --- |

| Agent 编排 | 65+ | 🔴 最高频，主要领域 |

| Coding Agent | 55+ | 🔴 高频，增长快 |

| 商业/生态 | 50+ | 🔴 高频 |

| Agent 技能 | 45+ | 🟡 中等 |

| OpenClaw | 40+ | 🟡 中等 |

| LLM | 38+ | 🟡 中等 |

| 记忆系统 | 25+ | 🟡 中等 |

| 开发工具 | 30+ | 🟡 中等 |

| Crypto/DeFi | 28+ | 🟡 中等 |

| Agent 框架 | 22+ | 🟢 正常 |

| 工作流 | 20+ | 🟢 正常 |

| 知识管理 | 18+ | 🟢 正常 |

| 安全/隐私 | 15+ | 🟢 正常 |

| 内容创作 | 15+ | 🟢 正常 |

---

## 类型启发式筛查结果

以下 concept 条目疑似应重新分类为 entity（建议人工确认，不自动判定）：

| 条目 | 命中规则 | 依据 |

| --- | --- | --- |

| [Untitled](concepts/Agent Reach.md)（concept） | Rule C | 特定开源工具项目（GitHub: Panniantong/agent-reach），有具体仓库地址，非通用术语 |

| [Untitled](entities/Agent Service Toolkit.md)（concept） | Rule B | 名称含 Toolkit 产品后缀，是具体 GitHub 项目（LangGraph + FastAPI + Streamlit 框架） |

| [Untitled](concepts/Antigravity MCP.md)（concept） | Rule B | 名称含 MCP 产品后缀，是特定 MCP 服务实现 |

| [Untitled](entities/AEO Engine.md)（concept） | Rule B | 名称含 Engine 产品后缀，疑似具体产品/工具 |

| [Untitled](entities/andrej-karpathy-skills.md)（concept） | Rule C | 特定 GitHub 仓库名称（小写+连字符命名），是具体开源项目 |

| [Untitled](concepts/AutoSkill.md)（concept） | Rule C | 疑似特定产品名，非通用方法论术语 |

> 计分：本次启发式结果为候选列表，待人工确认后才影响扣分。**0 分扣减**（确认前不计分）。

---

## 标签分类合理性检查

通过 Phase 2 抽样加载，发现以下潜在误分类：

| 条目 | 当前标签 | 问题描述 | 建议标签 |

| --- | --- | --- | --- |

| [Untitled](concepts/Agent Reach.md) | Agent 框架 | 该工具是网络内容访问脚手架，提供联网能力，非框架 | **开发工具** 或 **Agent 技能** |

其他 5 个抽样页面标签合理（Auto Memory → 记忆系统 ✓，A2A 协议 → Agent 编排 ✓，[AGENTS.md](http://agents.md/) → Coding Agent ✓，AiPy/Python-Use → 工作流 ✓，Antigravity MCP → Agent 技能 ✓）。

---

## 引用结构化检查

本次从草稿状态 concept/entity 中抽取 **6 个**页面进行引用结构化检查：

| 条目 | 来源引用总数 | 结构化（mention-page） | 纯文本 | 结构化率 |

| --- | --- | --- | --- | --- |

| [Untitled](concepts/Agent Reach.md) | 4 | 0 | **4** | 0% |

| [Untitled](concepts/AGENTS.md.md) | 7 | 4 | **3** | 57% |

| [Untitled](concepts/Auto Memory.md) | 4 | 1 | **3** | 25% |

| [Untitled](concepts/A2A 协议.md) | 4 | 3 | **1** | 75% |

| [Untitled](concepts/AiPy - Python-Use.md) | 1 | 1 | 0 | 100% |

| [Untitled](concepts/Antigravity MCP.md) | 1 | 1 | 0 | 100% |

| **汇总** | **21** | **10** | **11** | **~48%** |

**待修复页面（含纯文本引用）：**

- [Agent Reach](concepts/Agent Reach.md)（4 条纯文本引用）

- [AGENTS.md](concepts/AGENTS.md.md)（3 条纯文本引用）

- [Auto Memory](concepts/Auto Memory.md)（3 条纯文本引用）

- [A2A 协议](concepts/A2A 协议.md)（1 条纯文本引用）

> 抽样扣分：11 条纯文本引用 / 5 = **-2 分**（每 5 个扣 1 分，向上取整）。

> 

> 全库估算：按 48% 结构化率推算，存量纯文本引用可能数千条，建议 Fixer 批量处理。

---

## 计分明细

| 检查项 | 发现 | 扣分 |

| --- | --- | --- |

| 孤岛条目 | 0 条确认 | 0 |

| 过期草稿（>7天） | 0 条 | 0 |

| 过时内容（>30天） | 0 条 | 0 |

| concept/entity 近似重复对 | 3 对（Agent Team系、AI Scientist/AiScientist、x402/x402协议） | -30 |

| 缺失状态 | 0 条 | 0 |

| 缺失/空标签 | 0 条 | 0 |

| 废弃标签 | 0 条 | 0 |

| summary 近似重复（~7组/100条抽样） | 7 组 → 0.7，取整 1 | -1 |

| 引用结构化（11条纯文本/6页抽样） | 11 条 ÷ 5 = 2.2，取整 2 | -2 |

| 类型误分类（启发式，待确认） | 6 个候选，待人工确认 | 0（待确认） |

| **合计** |  | **-33 → 67/100** |

---

## 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 |

| --- | --- | --- | --- |

| — | — | — | 全库 concept/entity 均创建于 2026-04-10 之后，距今 ≤6 天，尚不满足「草稿→审核中（≥7天）」条件。下次检查（2026-04-17+）将产生大量可晋升草稿。 |

> **summary 状态**：全部 863 条 summary 已为「已审核」，无需操作。

> 

> **synthesis 状态**：47 条 synthesis 均为「草稿」，建议人工确认内容后晋升。

---

## 改进建议

### 🤖 自动修复项

Fixer 可直接执行以下操作：

1. **【重复合并】Agent Team 系三元重复**

  - 修复类型：近似重复合并

  - 目标页面：[Agent Team](concepts/Agent Team.md)、Agent Teams、Agent团队

  - 具体操作：以「Agent Team」（审核中）为主词条保留，合并另两页独有内容，修复断链，删除冗余页

1. **【重复合并】AI Scientist / AiScientist**

  - 修复类型：近似重复合并

  - 目标页面：[AI Scientist](entities/AI Scientist.md)（entity）、AiScientist（entity）

  - 具体操作：保留「AI Scientist」（官方命名规范），合并内容，删除冗余页

1. **【重复合并】x402 / x402 协议**

  - 修复类型：近似重复合并

  - 目标页面：x402（concept）、[x402 协议](concepts/x402 协议.md)（concept）

  - 具体操作：以「x402 协议」为主词条（更规范），合并内容，删除冗余页

1. **【标签修正】Agent Reach 标签**

  - 修复类型：标签重分类

  - 目标页面：[Agent Reach](concepts/Agent Reach.md)

  - 具体操作：将标签从「Agent 框架」改为「开发工具」（该工具是联网脚手架，非框架）

1. **【引用结构化升级】纯文本引用批量修复**

  - 修复类型：引用结构化升级

  - 目标页面：[Agent Reach](concepts/Agent Reach.md)（4条）、[AGENTS.md](concepts/AGENTS.md.md)（3条）、[Auto Memory](concepts/Auto Memory.md)（3条）、[A2A 协议](concepts/A2A 协议.md)（1条）

  - 具体操作：将「来源引用」区块中的纯文本引用替换为 `<mention-page>` 结构化链接，并反向检查对应 summary 是否已有该 concept 的结构化引用

1. **【Summary 近似重复合并】7 组 summary 归并**

  - 修复类型：summary 重复合并

  - 目标页面：见「summary 近似同名重复」表格中 7 组条目

  - 具体操作：每组保留信息量最多/标签最完整的版本，其余删除

### 👤 人工介入项

1. **类型误分类确认（启发式候选）**

  需人工确认以下 6 个 concept 是否应改为 entity：Agent Reach、Agent Service Toolkit、Antigravity MCP、AEO Engine、andrej-karpathy-skills、AutoSkill

  确认后告知 Fixer 执行类型迁移。

1. **Synthesis 草稿（47条）状态晋升**

  47 条 synthesis 全部为草稿，需人工阅读内容并确认质量后决定是否晋升为「审核中」或「已审核」。

1. **全库 Summary 近似重复全量扫描**

  本次仅扫描前 100 条，估计全库存在 50-60 组 summary 近似重复。建议调整 Compiler Agent 触发逻辑，增加去重校验机制，防止同一源文章生成多个 summary。

1. **引用结构化全量修复策略**

  当前结构化引用率约 48%，存量纯文本引用可能逾千条。建议将「引用结构化升级」纳入 Fixer 的常规循环任务，每次 Lint 后批量处理 20-30 个。

1. **孤岛检测精度提升**

  当前孤岛检测依赖标题匹配，精度不足。建议在 Wiki Schema 中为 concept/entity 增加 relation 字段指向来源 summary，从根本上解决孤岛检测的 SQL 限制。

---

 请根据以上报告执行自动修复。

---

## 修复记录（2026-04-16）

### 已完成

- 近似重复合并：已保留 [Agent Team](concepts/Agent Team.md)，并删除 Agent Teams、Agent团队；已保留 [AI Scientist](entities/AI Scientist.md)，并删除 AiScientist；已保留 [x402 协议](concepts/x402 协议.md)，并删除 x402。

- 标签修正：已将 [Agent Reach](concepts/Agent Reach.md) 标签改为「开发工具」。

- 引用结构化升级：已修复 [Agent Reach](concepts/Agent Reach.md)、[AGENTS.md](concepts/AGENTS.md.md)、[Auto Memory](concepts/Auto Memory.md)、[A2A 协议](concepts/A2A 协议.md) 的来源引用，并补充对应 summary 回链。

- summary 重复清理：已保留 [摘要：2025 元旦 AI Agent 全景：Mindshare vs 市值，谁在领跑加密智能体赛道？](summaries/摘要：2025 元旦 AI Agent 全景：Mindshare vs 市值，谁在领跑加密智能体赛道？.md)、[摘要：Andrej Karpathy 现在成了一个超级 AI 明星。他最近主推的一个 LLM+ MD + Wiki 的个人知识库特别火](summaries/摘要：Andrej Karpathy 现在成了一个超级 AI 明星。他最近主推的一个 LLM+ MD + Wiki 的个人知识库特别火.md)、[摘要：ai-hedge-fund：让 AI 扮演巴菲特和芒格，帮你做投资决策](summaries/摘要：ai-hedge-fund：让 AI 扮演巴菲特和芒格，帮你做投资决策.md)、[摘要：Anthropic 封杀 48 小时，逼出 OpenClaw 最强反击！龙虾首次会生视频了](summaries/摘要：Anthropic 封杀 48 小时，逼出 OpenClaw 最强反击！龙虾首次会生视频了.md)，并删除对应明显冗余版本。

### 仍需人工决策

- summary 近似重复剩余高歧义组：agency-agents 三条、AutoResearch 相关两条。两组主题高度相近，但表述焦点不完全一致，暂不自动删除。

- 类型误分类候选 6 条仍待人工确认后迁移。

### 备注

- 本次收尾已完成：修复记录已同时保留在本页评论与正文中，便于下轮 Recheck 直接读取。
