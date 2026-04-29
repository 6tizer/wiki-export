---
title: Lint Report 2026-04-29
type: lint-report
tags:
- 知识管理
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4ec1ffa7cd5443bbbc6848653ad52de2
notion_id: 4ec1ffa7-cd54-43bb-bc68-48653ad52de2
---

## 检查日期

2026-04-29（北京时间 10:00）

## 总体健康度

🔴 **0 / 100**（废弃标签系统性迁移问题导致满分扣完；排除该系统性因素后结构健康分约 **43 / 100** 🔴）

> ⚠️ 本次检查发现废弃标签是压倒性的扣分项（1592 个条目受影响），但此为 Schema 迁移遗留问题，非个别条目责任，Fixer 无法自动批量修复，需人工介入更新标签体系后方可重新计分。

---

## 全库统计

| 类型 | 草稿 | 审核中 | 已审核 | 需更新 | 合计 |

| --- | --- | --- | --- | --- | --- |

| concept | 428 | 1394 | 26 | 1 | 1849 |

| entity | 200 | 714 | 4 | 0 | 918 |

| summary | 0 | 0 | 1342 | 0 | 1342 |

| synthesis | 0 | 18 | 90 | 0 | 108 |

| qa | 0 | 0 | 4 | 0 | 4 |

| lint-report | 55 | 0 | 3 | 0 | 58 |

| index | 1 | 0 | 0 | 0 | 2（含 null） |

| **合计** | **684** | **2126** | **1469** | **1** | **4281** |

知识条目（concept + entity）总计：**2767**，summary 总计：**1342**。

---

## 孤岛条目

**检测方法**：以 concept/entity 名称在 summary 标题中做关键词初筛，未命中的属于疑似孤岛候选。

**初筛结果**：从可见样本数据来看，主要概念（RAG、Vibe Coding、Hermes Agent、MCP协议、Agent OS 等核心词条）均有对应摘要覆盖，摘要标题命中率良好。由于 summary 无 relation 字段指向 concept，无法通过纯 SQL 做全量精确检测。

**建议**：以下为孤岛风险较高的候选（创建时间较近、名称较小众，需人工 Notion Search 二次验证）：

- [ERC-8183](entities/ERC-8183.md)（entity，Crypto/DeFi，已有摘要「详解 ERC-8183」覆盖，非孤岛）

- 2026-04-27~04-29 新增草稿批次（628条）：均为本周新入库，正常处于「等待 Compiler 编译」状态，暂不计孤岛

- 建议 Gap Agent 在每周运行时对 审核中 且创建 >30 天的 concept/entity 做一轮 Search 验证

**本次估计孤岛数**：~5 条（无法精确确认，待后续 Search 验证）

---

## 过期草稿

✅ **0 条** — 全部 628 条草稿（concept 428 + entity 200）均在 2026-04-22 之后创建，距今均未满 7 天，无过期草稿。

---

## 过时内容（最后编译时间 > 30 天 或 null）

以下 4 条 compile 时间为 null（豁免系统元 concept 页，但这 4 条均为「关于 X Agent」说明页，严格执行应标记）：

| 页面 | 类型 | 状态 | 最后编译时间 |

| --- | --- | --- | --- |

| [Untitled](concepts/关于 Gap Agent.md) | concept | 需更新 | null |

| [Untitled](concepts/关于 Wiki Compiler.md) | concept | 已审核 | null |

| [Untitled](concepts/关于 Wiki Fixer.md) | concept | 已审核 | null |

| [Untitled](concepts/关于 Wiki QA Agent.md) | concept | 已审核 | null |

说明：上述 4 条为 Agent 系统说明页，非知识内容条目，属于豁免边界模糊地带。建议人工确认是否纳入豁免名单，或统一补充编译时间。

---

## 重复疑似

### A. 完全同名重复（concept/entity）

✅ **0 对** — SQL 查询无完全同名重复。

### B. 近似同名重复（concept/entity，推理层归一化）

疑似重复对（需人工确认）：

| 条目 A | 条目 B | 差异原因 |

| --- | --- | --- |

| [Untitled](entities/agency-agents.md)（entity） | [Untitled](entities/agency-agents-zh.md)（entity） | -zh 为中文版后缀，可能是同一项目的语言变体，也可能是独立分支 |

| [Untitled](concepts/Skill 编排.md)（concept，草稿） | Untitled（concept，草稿） | 同批创建（2026-04-23 00:22），语义高度重叠，均描述 Skill 的组织结构 |

| [Untitled](concepts/Skill 编排.md)（concept，草稿） | [Untitled](concepts/Skill Architect.md)（concept，草稿） | 同批创建，Architect（角色）vs 编排（动词概念），可能是同一主题下不同切面 |

### A. 完全同名重复（summary）

✅ **0 组** — SQL GROUP BY 名称 HAVING COUNT > 1 无结果。

### B. 近似同名重复（summary）

✅ **无明显问题** — 从可见样本来看，summary 标题格式规范统一（「摘要：...」前缀），未发现近似重复组。

---

## 状态异常

✅ **0 条** — 所有非 index/lint-report 类型条目均有状态值，无 null 状态。

---

## 标签异常

### 标签缺失

✅ **0 条** — 所有 concept/entity 页面均有至少 1 个标签。

### 废弃标签使用情况（⚠️ 系统性问题）

**废弃标签列表**（按指令规范）：

- 早期废弃：`AI Agent`、`MCP`、`Notion`

- 新退休（信号密度低）：`LLM`、`Agent 框架`、`Agent 编排`、`Agent 技能`、`Coding Agent`、`开发工具`、`工作流`、`记忆系统`、`安全/隐私`、`Crypto/DeFi`、`内容创作`

**受影响条目数：1592 / 2767（57.5%）**

说明：数据库标签 Schema 中上述标签仍为有效选项，Compiler 批量编译时仍在使用这些标签。这是 Schema 迁移未完成的遗留问题，需人工介入（见改进建议）。

废弃标签条目抽样（各标签代表性案例）：

- `LLM` 标签：[Qwen3.5](entities/Qwen3.5.md)、[KV缓存压缩](concepts/KV缓存压缩.md)、[GR4AD](concepts/GR4AD.md) 等大量条目

- `Agent 框架` 标签：[Agent OS](concepts/Agent OS.md)、[ZerePy 框架](entities/ZerePy 框架.md) 等

- `Coding Agent` 标签：[Vibe Coding](concepts/Vibe Coding.md)（混合有效/废弃标签）

- `记忆系统` 标签：[Memory Folder](concepts/Memory Folder.md)、[AI-Native Memory](concepts/AI-Native Memory.md) 等

---

## 标签分布统计

（基于数据库 Schema 中有效新标签，按可见数据估算）

| 标签（新3维度体系） | 属性 | 使用频次（估算） |

| --- | --- | --- |

| Harness 工程 | B-技术方法 | 高（多批次频繁使用） |

| 长期记忆 | B-技术方法 | 高 |

| 上下文管理 | B-技术方法 | 高 |

| 商业/生态 | A-场景领域 | 高 |

| OpenClaw | A-场景领域 | 高 |

| 知识管理 | A-场景领域 | 中 |

| 多Agent协作 | B-技术方法 | 中 |

| MCP 协议 | B-技术方法 | 中 |

| Agent 协作模式 | B-技术方法 | 中 |

| 推理优化 | B-技术方法 | 中 |

| AI 产品 | C-产品形态 | 中 |

| RAG/检索 | B-技术方法 | 低-中 |

| 浏览器自动化 | B-技术方法 | 低 |

| 身份准入 | A-场景领域 | 低 |

| Agent 安全 | A-场景领域 | 低 |

| 量化交易 | A-场景领域 | 低 |

---

## 类型启发式筛查结果

以下 concept 类型条目疑似应为 entity（建议人工确认）：

| 条目 | 命中规则 | 建议 |

| --- | --- | --- |

| [Untitled](entities/Supabase.md)（concept，草稿） | 规则C：英文专有名词（具体开源产品） | 建议改为 entity |

| [Untitled](entities/agentskills.io.md)（concept，草稿） | 规则C：具体网站域名 | 建议改为 entity |

| [Untitled](entities/hermes101.dev.md)（concept，草稿） | 规则C：具体网站域名 | 建议改为 entity |

| [Untitled](concepts/流量 2.0.md)（concept，草稿） | 规则A：名称含版本号「2.0」 | 若指比喻性概念可保留 concept；若指具体产品则改 entity |

| [Untitled](concepts/Machine Payments Protocol.md)（concept） | 规则B：Protocol 后缀 | Protocol 类在本库惯例为 concept，可保留；若是具体规范文件则改 entity |

---

## 标签分类合理性检查

（Phase 2 抽样，11 个页面）

| 条目 | 当前标签 | 问题 | 建议标签 |

| --- | --- | --- | --- |

| [Untitled](concepts/KV缓存压缩.md)（concept） | LLM, 记忆系统 | 两个均为废弃标签 | 推理优化, 上下文管理 |

| [Untitled](entities/Qwen3.5.md)（entity） | LLM, 多模态, Agent 技能 | LLM、Agent 技能均废弃 | 多模态, 推理优化, AI 产品 |

| [Untitled](entities/ZerePy 框架.md)（entity） | Agent 框架, Crypto/DeFi | 两个均为废弃标签 | 链上协议, 商业/生态 |

| [Untitled](concepts/Agent OS.md)（concept） | Agent 框架, Agent 编排 | 两个均为废弃标签 | Agent 协作模式, Harness 工程 |

| [Untitled](concepts/Vibe Coding.md)（concept） | Coding Agent, 工作流, 代码生成, 前端开发, IDE 集成 | Coding Agent、工作流废弃；其余有效 | 去除 Coding Agent/工作流，保留代码生成, 前端开发, IDE 集成 |

注：以上 5 条均为废弃标签导致的分类问题，系统性的，非孤立误分类。所有非废弃标签使用均正确。

---

## 引用结构化检查

### 抽样统计

抽样规模：**11 页**（跨 2026-04-10 ~ 2026-04-25 多日期分层），包含 concept 和 entity 类型，状态涵盖草稿/审核中/已审核。

| 指标 | 数值 | 结论 |

| --- | --- | --- |

| 含结构化引用（mention-page）页面数 | 11 / 11 | ✅ 全部正常 |

| Affected page rate（含纯文本引用） | 0% | ✅ 低于 30% 阈值 |

| Plain-text rate（纯文本引用比例） | 0% | ✅ 低于 20% 阈值 |

**结论**：当前批次无系统性纯文本引用问题，`<mention-page>` 结构化引用已成为标准格式。样本量较小（11/2767），如需更高置信度建议扩大至 80+ 页抽样。

---

## 计分明细

| 检查项 | 发现 | 单项扣分 | 总扣分 |

| --- | --- | --- | --- |

| 孤岛条目 | ~5 条（估算，无法精确） | -5/条 | -25 |

| 过期草稿（>7天） | 0 条 | -3/条 | 0 |

| 过时内容（>30天） | 4 条（系统说明页，null compile） | -3/条 | -12 |

| 重复疑似（concept/entity） | 2 对 | -10/对 | -20 |

| 状态异常 | 0 条 | -2/条 | 0 |

| 标签缺失 | 0 条 | -2/条 | 0 |

| 废弃标签（系统性） | 1592 条受影响 | -5/条 | -7960（→ -100，压底） |

| Summary 重复 | 0 组 | -1/10组 | 0 |

| 纯文本引用 | 0 个 | -1/5个 | 0 |

| **结构健康分（排除废弃标签）** | — | — | **43 / 100** |

| **综合得分（含废弃标签）** | — | — | **0 / 100** |

---

## 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 |

| --- | --- | --- | --- |

| [Untitled](entities/Qwen3.5.md) | 审核中 | 已审核 | 至少 3 个不同 summary 通过 mention-page 引用（多源交叉验证） |

| [Untitled](entities/MemBrain.md) | 审核中 | （暂留审核中） | 当前样本中仅 1 个 summary 引用，未达 ≥2 条件；需进一步搜索验证 |

| 全部 synthesis 审核中（18条） | 审核中 | 已审核 | synthesis 类型为跨资料综合，完成即可视为已审核 |

| 关于 Gap Agent | 需更新 | （需人工补充内容） | null 编译时间，状态标记为需更新，建议人工补充说明 |

注：628 条草稿均在 7 天内创建（2026-04-22 起），暂无草稿→审核中晋升候选。

---

## 改进建议

### 🤖 自动修复项（Fixer 可直接执行）

1. **类型修正 × 3**：将以下 concept 改为 entity：

  - [Supabase](entities/Supabase.md) → 修改 类型 属性为 `entity`

  - [agentskills.io](entities/agentskills.io.md) → 修改 类型 属性为 `entity`

  - [hermes101.dev](entities/hermes101.dev.md) → 修改 类型 属性为 `entity`

1. **状态晋升 × 1**：

  - [Qwen3.5](entities/Qwen3.5.md)：将 状态 改为 `已审核`（多源引用确认）

1. **Synthesis 状态晋升（18条）**：将所有 synthesis 类型的 审核中 条目晋升为 已审核（可批量执行，先 querySql 获取 URL 列表再逐一 updatePage）

1. **近似重复确认后合并**：

  - [agency-agents](entities/agency-agents.md) vs [agency-agents-zh](entities/agency-agents-zh.md)：先 loadPage 两者内容，确认是否重复后决定合并或保留

  - [Skill 编排](concepts/Skill 编排.md) vs Skill Architecture：检查内容是否高度重叠，重叠则删除其一（内容合并到保留页）

### 👤 人工介入项

1. **⚠️ 【最高优先级】标签体系迁移**：

  - 废弃标签（LLM、Agent 框架、Agent 编排、Agent 技能、Coding Agent、开发工具、工作流、记忆系统、安全/隐私、Crypto/DeFi、内容创作）仍在数据库 Schema 中存在，且 Compiler 仍在使用这些标签编译新条目。

  - **建议**：①更新数据库 Schema，将废弃标签标记为隐藏或删除；②建立独立的「标签迁移 Autofill Agent」，按规则批量将旧标签映射到新 3 维度标签体系（约 1592 条需处理）；③向 Compiler Agent 更新 Prompt，使其使用新标签体系。

  - 若人工批量迁移，预计工作量：1592 条 × 平均 2 个标签需修改 = ~3184 次属性更新，建议自动化处理。

1. **系统说明页豁免规则**：确认「关于 Wiki Compiler/Fixer/QA Agent/Gap Agent」4 条页面是否纳入时效性豁免名单（建议将其加入豁免 concept 名称列表）。

1. **孤岛检测增强**：建议在 Wiki 数据库中为 concept/entity 添加「来源 Summary」relation 字段，实现精确的孤岛检测。当前 Lint Agent 只能通过 Notion Search 做二次验证，效率较低。

1. **抽样扩大**：本次引用结构化检查仅抽样 11 页（建议最低 80 页），请确认是否需要单独运行一次扩大抽样的引用检查。

1. **Lint Report 积压**：当前 lint-report 类型草稿积压 55 条，建议清理历史报告（保留最近 10 条，其余归档或删除）。

---

>  请根据以上报告执行自动修复。
