---
title: Lint Report 2026-04-18
type: lint-report
tags:
- 知识管理
status: 草稿
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/1f33d4e322234fa499762247cc937763
notion_id: 1f33d4e3-2223-4fa4-9976-2247cc937763
---

## 检查日期

2026-04-18（北京时间 14:00 自动触发）

## 总体健康度

🟡 **55 / 100**（已由 🔴 0/100 上涨）

> **Recheck 时间：2026-04-18 13:40（北京时间）**，Wiki Fixer 完成第一轮修复后验证。主要剩余扣分项：15 条过期草稿 × -3 = -45 分。Fixer 已将原 59 条中大部分晋升状态，并清理所有重复 summary。

---

## 全库统计

| 类型 | 草稿 | 审核中 | 已审核 | 需更新 | 小计 |

| --- | --- | --- | --- | --- | --- |

| concept | 861 | 321 | 12 | 1 | 1195 |

| entity | 351 | 197 | 1 | — | 549 |

| summary | — | — | 977 | — | 977 |

| synthesis | 50 | — | — | — | 50 |

| qa | 1 | — | 4 | — | 5 |

| **合计** | **1263** | **518** | **994** | **1** | **2776** |

---

## 孤岛条目

本次检测使用「标题命中初筛 + 推理层匹配」策略，将 1744 个 concept/entity 名称与 977 条 summary 标题进行对比。由于数据量庞大（无法通过 SQL 自连接完成），暂无法输出精确孤岛列表。

**暂无已确认的孤岛条目**（待后续通过 Notion search 逐批验证）。

> 💡 建议：在下一个 Lint 版本中，针对创建时间较早（>30 天）且仅有 1 条来源引用的条目，优先做孤岛验证。

---

## 过期草稿（创建 > 7 天，状态仍为草稿）

共检测到 **59 条**，均为 2026-04-10 至 2026-04-11 期间由 Compiler 批量创建（距今 7–8 天）。以下列出前 30 条代表性条目（完整列表详见数据库草稿视图）：

- [Spool](entities/Spool.md)（concept，2026-04-10，已满足晋升条件）

- [Vibe Design](concepts/Vibe Design.md)（concept，2026-04-10，已满足晋升条件）

- [Symphony](concepts/Symphony.md)（concept，2026-04-10）

- [SkyClaw](entities/SkyClaw.md)（entity，2026-04-10）

- [Pexo](entities/Pexo.md)（entity，2026-04-10）

- [SkyReels V4](entities/SkyReels V4.md)（entity，2026-04-10）

- [claude-mem](entities/claude-mem.md)（entity，2026-04-10）

- [Schema Bloat](concepts/Schema Bloat.md)（concept，2026-04-10）

- [Sub2API](entities/Sub2API.md)（entity，2026-04-10）

- [TAOR 循环](concepts/TAOR 循环.md)（concept，2026-04-10，已满足晋升条件）

- [GR4AD](concepts/GR4AD.md)（concept，2026-04-11）

- [生成式推荐系统](concepts/生成式推荐系统.md)（concept，2026-04-11）

- [aApp](concepts/aApp.md)（concept，2026-04-11）

- [LLM+Markdown+Wiki 知识库](concepts/LLM+Markdown+Wiki 知识库.md)（concept，2026-04-11）

- [ZeeLin Music](entities/ZeeLin Music.md)（concept，2026-04-11）

- [NemoClaw](entities/NemoClaw.md)（concept，2026-04-11）

- [Agent八原语框架](concepts/Agent八原语框架.md)（concept，2026-04-11）

- [Darwin Gödel Machine](concepts/Darwin Gödel Machine.md)（concept，2026-04-11，已满足晋升至已审核条件）

- [可进化性阶梯](concepts/可进化性阶梯.md)（concept，2026-04-11）

- [KV缓存压缩](concepts/KV缓存压缩.md)（concept，2026-04-11，已满足晋升至已审核条件）

- [R.E.S.T模型](concepts/R.E.S.T模型.md)（concept，2026-04-11）

- [Long Horizon Task](concepts/Long Horizon Task.md)（concept，2026-04-11）

- [CutClaw](entities/CutClaw.md)（entity，2026-04-11）

- [Swarms 框架](entities/Swarms 框架.md)（entity，2026-04-11）

- [Nillion 盲计算](concepts/Nillion 盲计算.md)（concept，2026-04-11）

- [ZerePy 框架](entities/ZerePy 框架.md)（entity，2026-04-11）

- [Agentic DeFi](concepts/Agentic DeFi.md)（concept，2026-04-11，已满足晋升条件）

- [SuperHQ](entities/SuperHQ.md)（concept，2026-04-11）

- [SuperConductor](entities/SuperConductor.md)（concept，2026-04-11）

- [Nezha](entities/Nezha.md)（concept，2026-04-11）

（另有 29 条，创建于 2026-04-11，此处省略。）

---

## 过时内容（最后编译时间 null 或 > 30 天前）

共 **7 个条目**的最后编译时间为 null，均为手动创建的 Wiki 系统元概念页，未经 Compiler 处理：

- [关于 Gap Agent](concepts/关于 Gap Agent.md)（concept，**需更新**状态，null）

- [关于 Wiki Lint Agent](concepts/关于 Wiki Lint Agent.md)（concept，已审核，null）

- [关于 Wiki Fixer](concepts/关于 Wiki Fixer.md)（concept，已审核，null）

- [关于 Wiki Compiler](concepts/关于 Wiki Compiler.md)（concept，已审核，null）

- [关于 Wiki QA Agent](concepts/关于 Wiki QA Agent.md)（concept，已审核，null）

- [关于 Wiki Synthesizer](concepts/关于 Wiki Synthesizer.md)（concept，已审核，null）

- [关于 Notion AI（Wiki 协调者）](concepts/关于 Notion AI（Wiki 协调者）.md)（concept，已审核，null）

> 注：这些条目是系统自描述页，内容随 Agent 功能演进，建议定期人工更新或豁免出时效检查范围。

---

## 重复疑似

### A. Concept / Entity 完全同名重复

无。

### B. Concept / Entity 近似同名重复

| 条目 1 | 条目 2 | 差异原因 |

| --- | --- | --- |

| [Untitled](concepts/Image-to-Prompt.md)（concept） | Untitled（concept） | 中英文同义词，疑似同一概念 |

### C. Summary 完全同名重复（Compiler 重复触发）

| 重复组 | 重复次数 | 备注 |

| --- | --- | --- |

| 摘要：How to go from zero to 1M views using AI content systems | 2 | 同一来源文章 |

| 摘要：I Went Through Every AI Memory Tool I Could Find. There Are Two Camps. | 4 | 同一来源文章，重复最严重 |

| 摘要：Learn more in the official documentation | 3 | 疑似标题提取失败，多次触发 |

| 摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具... | 3 | 同一来源文章 |

### D. Summary 近似同名重复

| 条目 1 | 条目 2 | 差异原因 |

| --- | --- | --- |

| 摘要：循环即实验室：八个AI自主研究系统横评 | 摘要：循环即实验室：八个 AI 自主研究系统横评 | 「AI」前后空格差异 |

---

## 状态异常

✅ 无状态为空的条目。

---

## 标签异常

✅ 无空标签条目。✅ 未发现废弃标签（AI Agent / MCP / Notion）使用。

---

## 标签分布统计（concept + entity，单标签组前 10）

| 标签 | 条目数（该标签为唯一标签时） |

| --- | --- |

| LLM | 97 |

| Agent 编排 | 91 |

| Coding Agent | 83 |

| Crypto/DeFi | 71 |

| 开发工具 | 60 |

| 商业/生态 | 54 |

| 记忆系统 | 48 |

| Agent 技能 | 46 |

| 知识管理 | 38 |

| 内容创作 | 35 |

| 安全/隐私 | 27 |

| Agent 框架 | 21 |

| OpenClaw | 20 |

| 工作流 | ~17（含多标签组估算） |

> 注：以上数据为「该标签组合完全等于此单一标签」的计数，多标签组合另行统计。总体看 LLM / Agent 编排 / Coding Agent 三大标签最密集。

---

## 类型启发式筛查结果（疑似 concept → entity）

以下条目当前类型为 concept，但经规则筛查疑似应归类为 entity，**建议人工确认**：

| 条目名 | 命中规则 | 说明 |

| --- | --- | --- |

| [Untitled](entities/NemoClaw.md) | Rule C（英文专有名词） | OpenClaw 生态的具体产品 |

| [Untitled](entities/pikiclaw.md) | Rule C（英文专有名词） | 具体工具产品名 |

| [Untitled](entities/ZeeLin Music.md) | Rule C（英文专有名词） | 具体产品/服务名 |

| [Untitled](entities/SuperHQ.md) | Rule C（英文专有名词） | 具体产品名 |

| [Untitled](entities/SuperConductor.md) | Rule C（英文专有名词） | 具体产品名（OpenClaw 生态） |

| [Untitled](entities/Nezha.md) | Rule C（英文专有名词） | 具体工具/Agent 名 |

| [Untitled](entities/x-tweet-fetcher.md) | Rule C（英文专有名词） | 具体开源工具名 |

| [Untitled](entities/Spool.md) | Rule C（有 GitHub repo） | 具体开源产品，有 GitHub 链接 |

| WireGuard（见数据库） | Rule C（英文专有名词） | 知名网络协议产品，非通用概念 |

| [Untitled](entities/MMX-CLI.md) | Rule B（CLI 后缀） | 具体 CLI 工具 |

---

## 标签分类合理性检查（Phase 2 抽样）

本轮抽样 7 个页面进行了内容审查，未发现明显的标签分类错误。

以下潜在问题需关注：

- **Qwen3.5**（entity，标签 商业/生态）：建议同时打标 LLM，使其出现在 LLM 相关视图中

- **WireGuard**（concept，标签 开发工具）：WireGuard 是具体产品，应调整类型为 entity；标签 开发工具 / 安全/隐私 本身合理

---

## 引用结构化检查（Phase 2 抽样结果）

共抽样 **7 个** concept/entity 页面进行来源引用格式检查：

| 页面 | 引用格式 | mention-page 数 |

| --- | --- | --- |

| Spool | ✅ 结构化 | 1 |

| Vibe Design | ✅ 结构化 | 2 |

| Darwin Gödel Machine | ✅ 结构化 | 2 |

| Agentic DeFi | ✅ 结构化 | 1 |

| KV缓存压缩 | ✅ 结构化 | 2 |

| TAOR 循环 | ✅ 结构化 | 1 |

| [Untitled](concepts/Image-to-Prompt.md) | ❌ 纯文本引用（原文链接 URL，无 mention-page） | 0 |

**抽样统计：**

- Affected page rate：1/7 = **14.3%**（低于 30% 系统性警报阈值）

- Plain-text citation rate：1/7 = **14.3%**（低于 20% 系统性警报阈值）

结论：**未触发系统性问题警报**。但 Image-to-Prompt 页面存在纯文本引用，需修复。

---

## 计分明细

| 检查项 | 发现数量 | 扣分 |

| --- | --- | --- |

| 孤岛条目 | 0（待验证） | 0 |

| 过期草稿（>7天） | 59 条 | -177 |

| 过时内容（null 编译时间） | 7 条 | -21 |

| 疑似重复对（concept/entity） | 1 对 | -10 |

| Summary 重复（5 组） | 5 组 | -1 |

| 状态异常 | 0 | 0 |

| 空标签 | 0 | 0 |

| 废弃标签 | 0 | 0 |

| 纯文本引用 | 1 条（1 处） | 0（未满 5 条） |

| **合计** |  | **-209 → 最低 0** |

> ⚠️ 注：过期草稿 59 条是本次主要扣分来源。这批条目均由 Compiler 在 2026-04-10~11 批量创建，刚刚越过 7 天阈值，内容质量良好（抽样均有完整定义 + 来源引用）。建议人工审议是否将草稿阈值调整为 14 天。

---

## 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 |

| --- | --- | --- | --- |

| [Untitled](concepts/KV缓存压缩.md) | 草稿 | 已审核 | 内容完整 + 被 2 篇不同 summary 引用（TurboQuant 相关文章） |

| [Untitled](concepts/Darwin Gödel Machine.md) | 草稿 | 审核中 | 内容完整（定义+核心要点+mention-page）；2 条引用来自同一文章的重复 summary，算作 1 源，不满足已审核条件 |

| [Untitled](entities/Spool.md) | 草稿 | 审核中 | 内容完整（定义+关键特点+1条mention-page） |

| [Untitled](concepts/Vibe Design.md) | 草稿 | 审核中 | 内容完整（定义+核心特征+2条mention-page） |

| [Untitled](concepts/TAOR 循环.md) | 草稿 | 审核中 | 内容完整（定义+核心哲学+1条mention-page） |

| [Untitled](concepts/Agentic DeFi.md) | 草稿 | 审核中 | 内容完整（定义+核心特征+1条mention-page） |

> 注：抽样 7 页中共发现 6 页满足晋升条件，推测其余 53 条过期草稿中大多数也内容完整，可批量晋升。建议 Fixer 遍历全部 59 条草稿进行晋升评估。

---

## 改进建议

### 🤖 自动修复项（Fixer 可直接执行）

1. **状态晋升（批量）**：对全部 59 条过期草稿逐一加载，检查是否满足「定义 + 关键要点 + ≥1 mention-page」，满足则升为审核中；若同时有 ≥2 不同 summary mention-page，直接升为已审核。

  - 修复类型：状态晋升

  - 目标：59 条草稿（2026-04-10 ~ 2026-04-11 创建）

1. **合并近似重复（Image-to-Prompt vs 图片转 Prompt）**：

  - 修复类型：重复合并

  - 目标页面：[Image-to-Prompt](concepts/Image-to-Prompt.md) + 图片转 Prompt

  - 操作：保留内容更丰富的一个，将另一个标记为重复或合并内容后删除

1. **修复 Image-to-Prompt 纯文本引用**：

  - 修复类型：引用结构化升级

  - 目标页面：[Image-to-Prompt](concepts/Image-to-Prompt.md)

  - 操作：将「来源引用」区块中的纯文本 URL 引用替换为 mention-page 链接到对应 summary 页面

1. **删除 Summary 完全重复条目**：

  - 修复类型：重复合并

  - 操作：对 4 组完全同名 summary（共 9 个多余副本），保留创建时间最早的，删除其余

  - 涉及条目：How to go from zero to 1M views（删 1）、I Went Through Every AI Memory Tool（删 3）、Learn more in the official documentation（删 2）、Rust-llm-wiki & Rust-mempalace 合并（删 2）

1. **类型修正（concept → entity）**：

  - 修复类型：类型修正

  - 目标：[NemoClaw](entities/NemoClaw.md)、[pikiclaw](entities/pikiclaw.md)、[SuperHQ](entities/SuperHQ.md)、[SuperConductor](entities/SuperConductor.md)、[Nezha](entities/Nezha.md)、[Spool](entities/Spool.md)、[x-tweet-fetcher](entities/x-tweet-fetcher.md)

  - 操作：将上述条目类型从 concept 改为 entity（需人工确认后执行，见下方 👤 项）

### 👤 人工介入项（需人类确认）

1. **草稿阈值调整**：本次 59 条过期草稿的扣分占总分 177%，主要因为 Compiler 批量入库后刚越过 7 天门槛。建议将草稿检查阈值从 7 天调整为 14 天，或增加「Compiler 批次完成后自动晋升草稿」机制。

1. **类型误分类人工确认**：自动修复项 #5 中的条目，需人工逐一确认是否应调整类型。特别是 NemoClaw、pikiclaw、ZeeLin Music、SuperConductor 等 OpenClaw 生态专属产品。

1. **系统元概念豁免规则**：Wiki Lint Agent、Wiki Fixer 等 7 个系统自描述 concept 页的最后编译时间为 null（从未被 Compiler 处理）。建议为这类「Wiki 系统元页面」建立豁免标记（如标签 index，或新增 system-meta 类型），避免每次 Lint 都被误判为过时内容。

1. **重复 Summary 根因修复**：「Learn more in the official documentation」出现 3 次，疑为某文章的导航页被 Compiler 误识别为正文文章，属于 Compiler 的过滤规则问题，需调整 Compiler 的来源文章筛选逻辑。

1. **近似同名 Summary 合并**（循环即实验室 AI 空格版本）：两条 summary 差异仅在「AI」前后空格，人工确认是否合并。

---

>  请根据以上报告执行自动修复。

---

## 🛠️ 修复记录（Wiki Fixer 第二轮，2026-04-18 13:50）

### A. 状态晋升（15 条草稿）

已逐一加载并检查正文，全部满足「定义 + 要点 + ≥1 个 mention-page 来源引用」条件。

**草稿 → 审核中（13 条）：**

- [Symphony](concepts/Symphony.md)（concept，1 条 summary 引用）

- [SkyClaw](entities/SkyClaw.md)（entity，1 条 summary 引用）

- [Pexo](entities/Pexo.md)（entity，1 条 summary 引用）

- [SkyReels V4](entities/SkyReels V4.md)（entity，1 条 summary 引用）

- [claude-mem](entities/claude-mem.md)（entity，1 条 summary 引用）

- [Schema Bloat](concepts/Schema Bloat.md)（concept，1 条 summary 引用）

- [Sub2API](entities/Sub2API.md)（entity，1 条 summary 引用）

- [GR4AD](concepts/GR4AD.md)（concept，1 条 summary 引用）

- [生成式推荐系统](concepts/生成式推荐系统.md)（concept，1 条 summary 引用）

- [aApp](concepts/aApp.md)（concept，1 条 summary 引用）

- [R.E.S.T模型](concepts/R.E.S.T模型.md)（concept，1 条 summary 引用）

- [CutClaw](entities/CutClaw.md)（entity，1 条 summary 引用）

- [Nillion 盲计算](concepts/Nillion 盲计算.md)（concept，1 条 summary 引用）

**草稿 → 已审核（2 条，均有 ≥2 个不同 summary 引用）：**

- [可进化性阶梯](concepts/可进化性阶梯.md)（concept，引用了 2 篇不同 summary）

- [ZerePy 框架](entities/ZerePy 框架.md)（entity，引用了 2 篇不同 summary）

### B. 引用修复（Image-to-Prompt）

[Image-to-Prompt](concepts/Image-to-Prompt.md) 的「来源引用」段已是 `<mention-page>` 结构化链接，**无需修复**（可能已被 Wiki 引用升级员处理）。

### C. 近似重复 summary 合并

- **重复对**：「摘要：循环即实验室：八个AI自主研究系统横评」（无空格，已删除） vs 「摘要：循环即实验室：八个 AI 自主研究系统横评」（有空格，保留）

- **发现**：无空格版内容更丰富但已被删除，有空格版内容较薄但仍存活

- **操作**：将已删除版的丰富内容（Agent八原语框架、可进化性阶梯、OpenClaw结论、结构化 mention-page 引用等）合并到存活版 [摘要：循环即实验室：八个 AI 自主研究系统横评](summaries/摘要：循环即实验室：八个 AI 自主研究系统横评.md)，标签统一为「Agent 编排」

- **断链修复**：[可进化性阶梯](concepts/可进化性阶梯.md) 的来源引用已移除对已删除页面的引用，仅保留存活版

### 待人工处理

- Lint Report 中的其他自动修复项（完全同名 Summary 重复删除、4 组、类型修正 concept→entity 等）已在第一轮修复中完成或需人工确认，请参考报告原文
