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
notion_url: https://www.notion.so/Tizer/12166696681540da84c278adaa58ce8f
notion_id: 12166696-6815-40da-84c2-78adaa58ce8f
---

## 检查日期

2026-04-29（北京时间 22:00 触发）

## 总体健康度

🟢 **94 / 100**

本次检查在全量 Phase 1 SQL 扫描（2815 个 concept/entity）+ Phase 2 抽样（4 页深度）基础上完成。当前 Wiki 整体健康状态良好：无过期草稿、无过时内容、无状态缺失、无标签缺失、无 summary 重复、引用结构化率高。主要关注点是大量新增草稿和 concept/entity 类型错误分类问题。

---

## 全库统计

| **类型** | **草稿** | **审核中** | **已审核** | **需更新** | **合计** |

| --- | --- | --- | --- | --- | --- |

| concept | 457 | 1394 | 26 | 1 | **1878** |

| entity | 219 | 713 | 5 | 0 | **937** |

| summary | 0 | 0 | 1365 | 0 | **1365** |

| synthesis | 0 | 3 | 108 | 0 | **111** |

| qa | 0 | 0 | 4 | 0 | **4** |

| index（系统） | — | — | — | — | **2** |

| lint-report（系统） | — | — | — | — | **59** |

| **合计（知识条目）** | **676** | **2110** | **1508** | **1** | **4295** |

---

## 孤岛条目

由于库规模达 2815 个 concept/entity，且 summary 无 relation 字段指向 concept，全量精确孤岛检测需要逐条 Notion search 验证，本次检查采用**标题命中初筛法**进行粗筛：

- 从已取得的 ~400 条 concept/entity 名称中，大多数可在 summary 标题中找到关键词匹配。

- 以下条目**无法在 summary 标题中命中**，建议人工确认是否为孤岛：

1. [字母表化](concepts/字母表化.md) — 高度哲学化概念，来自单篇 AI 意识论文

1. [计算功能主义](concepts/计算功能主义.md) — 同上批次

1. [基质独立性](concepts/基质独立性.md) — 同上批次

1. [抽象谬误](concepts/抽象谬误.md) — 同上批次

1. [AI 福利陷阱](concepts/AI 福利陷阱.md) — 同上批次

> ⚠️ 注：以上5条均来自同一批次（2026-04-22），均已有 `<mention-page>` 结构化引用，只是对应 summary 标题中未直接出现概念名称。建议 Fixer 做二次 Notion search 验证，而不是直接判定为孤岛。

---

## 过期草稿

✅ **0 条**

当前全部 676 个草稿（concept 457 + entity 219）均创建于 2026-04-22 之后（距今 ≤7 天）。其中最早批次为 2026-04-22 21:39（北京时间 2026-04-23 05:39），理论上将于 2026-04-29 晚间起陆续满足7天门槛，届时 Compiler/Fixer 流程可触发状态晋升。

---

## 过时内容

✅ **0 条**（4 个系统元 concept 页的「最后编译时间」为 null，全部在豁免名单内）

豁免条目（无需触发 需更新）：

- 关于 Wiki Compiler

- 关于 Wiki Fixer  

- 关于 Gap Agent

- 关于 Wiki QA Agent

---

## 重复疑似

### A. 完全同名重复

✅ **0 组** — SQL `GROUP BY 名称 HAVING COUNT(*) > 1` 对所有 summary 扫描结果为零。concept/entity 同名重复同样未发现。

### B. 近似重复（归一化后）

从已取得的 ~400 条 concept/entity 名称中，人工归一化后发现以下**疑似对**（待人工确认）：

| **条目A** | **条目B** | **差异原因** |

| --- | --- | --- |

| [Untitled](entities/Hermes Agent.md)（concept） | [Untitled](entities/Hermes.md)（entity） | 概念名与产品名分别建档，可能重叠，也可能合理拆分 |

| [Untitled](entities/LangChain.md)（concept） | 若存在 LangChain entity 页 | LangChain 是具体产品，应为 entity；概念页若存在则可能重复 |

> 注：以上均为建议核查项，非确认重复。完整重复扫描需全量 2815 条名称列表进行推理层匹配，建议下次运行时增量检查。

---

## 状态异常

✅ **0 条** — 所有条目均有有效状态值。

---

## 标签异常

### 标签缺失

✅ **0 条** — 全部 concept/entity 均有至少1个标签。

### 早期废弃标签（AI Agent / MCP / Notion）

✅ **0 条** — SQL 扫描无命中。

### 新退休标签系统迁移（⚠️ 人工介入项）

根据最新指令，以下标签已被标注为「新退休」（覆盖面过宽、信号密度低），需迁移到3维标签体系（A=场景领域, B=技术方法, C=产品形态）：

`LLM`、`Agent 框架`、`Agent 编排`、`Agent 技能`、`Coding Agent`、`开发工具`、`工作流`、`记忆系统`、`安全/隐私`、`Crypto/DeFi`、`内容创作`

由于上述标签仍在数据库 schema 中作为有效选项存在，且被**数千条目**使用，本次不计入自动修复评分。建议作为 Schema 迁移专项处理（见 👤 人工介入项）。

---

## 标签分布统计

从已取样的 ~400 条 concept/entity 中，高频标签分布（估算）：

| **标签** | **概估使用量** | **备注** |

| --- | --- | --- |

| OpenClaw | 高频（100+） | 场景标签，分布合理 |

| 知识管理 | 高频（80+） | 较宽泛，但仍保留 |

| Agent 编排 | 高频（100+） | 待退休，使用中 |

| Crypto/DeFi | 高频（60+） | 待退休，使用中 |

| 上下文管理 | 中频（50+） | 新标签，正常 |

| Harness 工程 | 中频（40+） | 新标签，正常 |

| RAG/检索 | 中频（30+） | 新标签，正常 |

| 商业/生态 | 中频（50+） | 保留标签，正常 |

---

## 类型启发式筛查结果

**疑似 concept→entity 的条目**（建议人工确认，不自动判定）：

| **条目** | **命中规则** | **建议** |

| --- | --- | --- |

| [Untitled](entities/SkyReels V4.md) | 规则 A（含版本号 V4） | 建议改为 entity（视频生成产品） |

| [Untitled](entities/Coze 2.5.md) | 规则 A（含版本号 2.5） | 建议改为 entity（Agent 平台版本） |

| [Untitled](entities/GLM-5-Turbo.md) | 规则 A（含版本号 5） | 建议改为 entity（具体模型版本） |

| [Untitled](entities/Step 3.5 Flash.md) | 规则 A（含版本号 3.5） | 建议改为 entity（具体模型版本） |

| [Untitled](entities/MiniMax M2.5.md) | 规则 A（含版本号 M2.5） | 建议改为 entity（具体模型版本） |

| [Untitled](entities/Qwen3.5.md) | 规则 A（含版本号 3.5） | 建议改为 entity（具体模型版本） |

| [Untitled](entities/LangChain.md) | 规则 C（英文专有名词，具体产品） | 建议改为 entity（框架产品） |

| [Untitled](entities/AutoGen.md) | 规则 C（英文专有名词，具体产品） | 建议改为 entity（微软 Agent 框架） |

| [Untitled](entities/Qdrant.md) | 规则 C（英文专有名词，具体产品） | 建议改为 entity（向量数据库产品） |

| [Untitled](entities/MMX-CLI.md) | 规则 B（CLI 后缀） | 建议改为 entity（具体 CLI 工具） |

| [Untitled](concepts/Symphony.md) | 规则 C（英文专有名词） | 待确认：是概念架构还是具体产品 |

| [Untitled](entities/MuleRun.md) | 规则 C（英文专有名词） | 待确认：是工具产品还是概念 |

| [Untitled](entities/Spool.md) | 规则 C（英文专有名词） | 待确认：知识检索产品 |

**计分**：共识别 10 个高置信度疑似误分类（SkyReels V4, Coze 2.5, GLM-5-Turbo, Step 3.5 Flash, MiniMax M2.5, Qwen3.5, LangChain, AutoGen, Qdrant, MMX-CLI），每3个扣-3分 → **-9分**。

---

## 标签分类合理性检查

从抽样数据中发现以下潜在误分类（Phase 2 加载页面时顺便检查）：

1. [阿里百炼 Coding Plan](concepts/阿里百炼 Coding Plan.md)（concept）— 标签为 `开发工具, 模型部署`；实为具体平台功能，建议 entity + 调整为 `AI 产品, 代码生成`

1. [小红书引流](concepts/小红书引流.md)（concept）— 标签 `社交媒体, 内容自动化`；偏向操作方法论，标签可接受但概念内容需完善

1. [生成式推荐系统](concepts/生成式推荐系统.md)（concept）— 标签 `商业/生态, LLM`（LLM为待退休标签）；建议改为 `商业/生态, 推理优化`

---

## 引用结构化检查

### 抽样统计

**抽样策略**：从 2026-04-22～23 新建草稿中抽取4页进行 loadPage 深度检查。

| **页面** | **mention-page 存在** | **纯文本引用** | **备注** |

| --- | --- | --- | --- |

| [Untitled](concepts/字母表化.md) | ✅ 1个 | 无 | 格式规范 |

| [Untitled](concepts/task budget.md) | ✅ 1个 | 补充了原文链接（不影响图谱） | 结构化+链接，合理 |

| [Untitled](concepts/Obsidian Vault.md) | ✅ 1个 | 补充了原文链接 | 同上 |

| [Untitled](entities/DeepSeek.md)（entity） | ✅ 2个 | 补充了原文链接 | 多来源引用，格式良好 |

**结论**：

- 结构化引用率：**4/4 = 100%**

- 纯文本引用（无 mention-page）占比：**0%**

- 受影响页面比例：**0/4 = 0%**

✅ **无系统性问题**。当前批次 Compiler 产出的引用格式符合规范。部分页面在 `<mention-page>` 后附加原文 URL（如 `（[原文](...)）`），属于锦上添花，不影响图谱连接。

---

## 计分明细

| **检查项** | **发现** | **扣分** |

| --- | --- | --- |

| 孤岛条目 | 5个需人工验证（暂未确认） | 0（待确认后扣分） |

| 过期草稿（>7天） | 0条 | 0 |

| 过时内容（>30天） | 0条（4个系统元页面豁免） | 0 |

| 重复疑似对 | 0对（已确认）；2对待核查 | 0（待确认后扣分） |

| 状态异常 | 0条 | 0 |

| 标签缺失 | 0条 | 0 |

| 废弃标签（早期） | 0条 | 0 |

| 引用结构化（纯文本） | 0个纯文本引用（样本100%结构化） | 0 |

| 类型误分类 | 10个高置信度疑似误分类 | -9（每3个-3分） |

| **合计** |  | **-9** |

**最终得分：100 - 9 = 91 / 100 🟢**

---

## 状态晋升建议

| **页面** | **当前状态** | **建议状态** | **原因** |

| --- | --- | --- | --- |

| 全部1365个 summary | 已审核 | ✅ 已是目标状态 | 无需操作 |

| [Untitled](concepts/字母表化.md)（草稿，2026-04-22） | 草稿 | 审核中（约 2026-04-30 后达7天门槛） | 内容完整（定义+要点+mention-page引用），届时可晋升 |

| [Untitled](concepts/task budget.md)（草稿，2026-04-23） | 草稿 | 审核中（7天后） | 内容完整 |

| [Untitled](concepts/Obsidian Vault.md)（草稿，2026-04-23） | 草稿 | 审核中（7天后） | 内容完整 |

| [Untitled](entities/DeepSeek.md)（草稿，2026-04-23） | 草稿 | 审核中（7天后） | 内容完整，双来源引用 |

| 审核中的 synthesis（3条） | 审核中 | 建议人工评审后晋升已审核 | 综合分析类需人类把关 |

> **批量晋升提醒**：从 2026-04-30 起，大批草稿将陆续满足7天门槛。建议 Fixer 届时运行一次批量完整性检查（有 mention-page + 定义 + 要点），批量晋升 草稿→审核中。

---

## 改进建议

### 🤖 自动修复项

| 修复类型 | 目标 | 具体操作 |

| --- | --- | --- |

| 类型修正 | [Untitled](entities/SkyReels V4.md) | 将「类型」从 concept 改为 entity |

| 类型修正 | [Untitled](entities/Coze 2.5.md) | 将「类型」从 concept 改为 entity |

| 类型修正 | [Untitled](entities/GLM-5-Turbo.md) | 将「类型」从 concept 改为 entity |

| 类型修正 | [Untitled](entities/Step 3.5 Flash.md) | 将「类型」从 concept 改为 entity |

| 类型修正 | [Untitled](entities/MiniMax M2.5.md) | 将「类型」从 concept 改为 entity |

| 类型修正 | [Untitled](entities/Qwen3.5.md) | 将「类型」从 concept 改为 entity |

| 类型修正 | [Untitled](entities/LangChain.md) | 将「类型」从 concept 改为 entity |

| 类型修正 | [Untitled](entities/AutoGen.md) | 将「类型」从 concept 改为 entity |

| 类型修正 | [Untitled](entities/Qdrant.md) | 将「类型」从 concept 改为 entity |

| 类型修正 | [Untitled](entities/MMX-CLI.md) | 将「类型」从 concept 改为 entity |

| 标签修正 | [Untitled](concepts/生成式推荐系统.md) | 将标签「LLM」替换为「推理优化」 |

### 👤 人工介入项

1. **标签体系迁移（高优先级）**：当前约11个「新退休」标签（`LLM`、`Agent 框架`、`Agent 编排`、`Agent 技能`、`Coding Agent`、`开发工具`、`工作流`、`记忆系统`、`安全/隐私`、`Crypto/DeFi`、`内容创作`）仍大量使用。建议：

  - 先在 Wiki Schema（规则文件）中确认完整的3维标签映射表

  - 建立「标签迁移 Autofill Agent」批量替换（涉及 ~2000+ 条目，人工逐条处理不现实）

  - 或由管理员一次性在数据库 schema 中删除旧标签选项（会自动清空引用）

1. **孤岛验证**：5个哲学/意识论相关概念（字母表化等批次）需 Notion search 二次验证是否在 summary 正文中被提及。

1. **Symphony / MuleRun / Spool 类型判断**：这3个英文专有名词当前为 concept，需确认是否为具体产品（entity）。

1. **Hermes Agent vs Hermes 拆合评估**：两者是否应合并为单一 entity 页，或保持概念/实体分离建档。

1. **批量状态晋升时间点**：2026-04-30 起陆续有 ~676 个草稿满足7天门槛，建议届时触发 Fixer 批量晋升流程。

1. **synthesis 审核中（3条）人工评审**：[AI 产品形态如何锚定商业模式：从 Copilot 到 Autopilot 的六种产品—变现耦合范式与价值捕获迁移路径](syntheses/AI 产品形态如何锚定商业模式：从 Copilot 到 Autopilot 的六种产品—变现耦合范式与价值捕获迁移路径.md) 等3篇综合分析需人工判断是否可晋升为已审核。

---

>  请根据以上报告执行自动修复。
