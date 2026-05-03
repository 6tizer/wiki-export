---
title: Lint Report 2026-05-03
type: lint-report
tags:
- 知识管理
status: 草稿
confidence: high
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a7300ac8bba748dc92bc4aee509d6398
notion_id: a7300ac8-bba7-48dc-92bc-4aee509d6398
---

## 检查日期

2026-05-03（北京时间 10:00 定时触发）

## 总体健康度

**86 / 100** 🟢

健康状况良好。主要扣分来自 3 条过期草稿 + 1 条 synthesis 未编译 + 1 处标签误分类。废弃标签已全面清零，引用结构化质量优良，无系统性问题。

---

## 全库统计（类型 × 状态）

| **类型** | **草稿** | **审核中** | **已审核** | **需更新** | **小计** |

| --- | --- | --- | --- | --- | --- |

| concept | 279 | 1670 | 29 | 1 | **1979** |

| entity | 173 | 836 | 5 | 0 | **1014** |

| summary | 0 | 0 | 1474 | 0 | **1474** |

| synthesis | 1 | 58 | 108 | 0 | **167** |

| qa | 0 | 0 | 4 | 0 | **4** |

| **合计** | **453** | **2564** | **1620** | **1** | **4638** |

> 注：index 和 lint-report 类型已从所有检查中排除。

---

## 孤岛条目

> ⚠️ **检测限制**：summary 无 relation 字段直接指向 concept/entity，孤岛检测须依赖标题初筛 + Notion 搜索验证。当前仅完成了基于摘要标题词库的初步匹配，无法对全部 2993 条 concept/entity 做精确判定。以下为 **疑似孤岛候选**，建议 Fixer 进行 Notion search 二次验证。

以下条目名称在已获取的摘要标题样本中未命中，且在 Wiki 核心主题中显得较为孤立：

- [ΛCDM 模型](concepts/ΛCDM 模型.md)（concept，天体物理）——宇宙学标准模型，与 AI/Agent 主题关联不明显

- [L-GALAXIES 半解析模型](concepts/L-GALAXIES 半解析模型.md)（concept，天体物理）——天文半解析模拟框架

- [冯·曼戈尔特函数](concepts/冯·曼戈尔特函数.md)（concept，知识管理）——数学函数，归类为知识管理存疑

- [普罗克鲁斯特斯分析法](concepts/普罗克鲁斯特斯分析法.md)（concept，模型评测）——统计分析方法，孤立性较高

- [TuriX Parallelum](concepts/TuriX Parallelum.md)（concept，Agent 协作模式）——名称罕见，来源不明

以上条目均来自同一批次（2026-04-26 草稿），疑似由含杂项内容的单篇文章编译产生。

---

## 过期草稿（草稿状态 >7 天）

共发现 **3 条**（创建于 2026-04-24 / 2026-04-25）：

| **页面** | **类型** | **创建日期** | **距今** | **内容完整性** |

| --- | --- | --- | --- | --- |

| [Untitled](concepts/画布式 Agent 编排.md) | concept | 2026-04-24 | 9 天 | ❌ 来源引用为空 |

| [Untitled](entities/Open Swarm.md) | entity | 2026-04-24 | 9 天 | ❌ 来源引用为空 |

| [Untitled](entities/Path2AGI.md) | entity | 2026-04-25 | 8 天 | ✅ 完整（定义+关键信息+mention-page 引用） |

> 注：2026-04-26 创建的 ~50 条草稿条目恰好处于 7 天边界（草稿状态晋升资格线），未纳入过期草稿扣分，但已在「状态晋升建议」中列出。

---

## 过时内容（最后编译时间 >30 天或 null）

豁免后共 **1 条**：

- [研究计划：Cross-Layer Failure Propagation in AI Safety](syntheses/研究计划：Cross-Layer Failure Propagation in AI Safety.md)（synthesis，草稿，最后编译时间：null）

  - 创建于 2026-05-02，昨天新建，内容为人工撰写的 AI 安全研究计划，从未经过 Compiler 编译流程，属于「永久 null compile_time」类型，并非真正过时，但技术上触发了 null 检测条件。

  - 👤 建议人工确认：此类人工撰写的 synthesis 是否需要填写一个占位编译时间。

> 豁免条目（null compile_time 系统元页）：关于 Wiki Compiler、关于 Wiki Fixer、关于 Gap Agent、关于 Wiki QA Agent（均为系统概念页，豁免）。

---

## 重复疑似

### A. 完全同名重复

**concept/entity**：0 组

**summary**：0 组（SQL `GROUP BY 名称 HAVING COUNT(*) > 1` 返回空）

### B. 规范化后近似重复

对已抽样的 ~200 个 concept/entity 名称进行归一化匹配，未发现近似重复对。

> 注：完整近似重复检测需覆盖全部 2993 条，当前仅抽样 ~200 条。建议后续批次扩大覆盖。

---

## 状态异常

**0 条**——所有 concept/entity/summary/synthesis 均已设置状态，无 null 状态。✅

---

## 标签异常

### 缺失标签

**0 条**——所有 concept/entity 均有标签。✅

### 废弃标签使用

**0 条**——旧标签体系（AI Agent、MCP、Notion、LLM 等 14 个废弃标签）已全面迁移至新 3 维度标签体系。✅ 这是本次检查的重大利好。

### 标签误分类（发现 2 处）

1. [Long Horizon Task](concepts/Long Horizon Task.md)（concept）

  - 当前标签：`上下文管理, Harness 工程, 加密资产`

  - 问题：**加密资产** 标签与该概念（AI 长时序任务规划）完全无关，疑似 Compiler 从含多主题的文章中误提取

  - 建议：移除 `加密资产`，补充 `Agent 协作模式` 或 `推理优化`

1. [GLM-5-Turbo](entities/GLM-5-Turbo.md)（entity）

  - 当前标签：`OpenClaw, 多Agent协作, Agent 协作模式`

  - 问题：GLM-5-Turbo 是智谱 AI 的大语言模型，主标签应为模型/多模态类，当前标签偏向了 OpenClaw 使用场景而非模型本体属性

  - 建议：改为 `多模态, 推理优化, AI 产品`（或保留 OpenClaw 作为补充标签）

---

## 标签分布统计

> 以下数据基于 SQL 对标签组合字段的统计（非单标签频次），高频单标签条目的实际总使用量会高于下列数字。

| **标签（组合）** | **条目数** | **备注** |

| --- | --- | --- |

| 商业/生态 | 184（纯此标签） | ⚠️ 高度集中，商业/生态作为单一标签可能过于宽泛 |

| 知识管理 | 148（纯此标签） | Wiki 核心主题，占比正常 |

| OpenClaw | 56 | OpenClaw 专项内容 |

| Harness 工程 | 42 | Agent 运行时工程，重点领域 |

| Agent 安全 | 32 |  |

| 推理优化 | 27 |  |

| 量化交易 | 25 | Crypto 子话题，分布合理 |

| 模型评测 | 25 |  |

| 长期记忆 | 24 |  |

| 训练/微调 | 24 |  |

| Agent 协作模式 | 23（纯此标签）+ 更多多标签条目 |  |

| 身份准入 | 15 |  |

| 视频/3D | 15 |  |

| 浏览器自动化 | 14 |  |

| 链上协议 | 13 |  |

| 前端开发 | 13 |  |

| AI 设计 | 12 |  |

| AI 对齐 | 12 |  |

| MCP 协议 | 11 |  |

| 天体物理 | 2 | ⚠️ 孤立领域，见孤岛检测 |

> **观察**：`商业/生态` 单标签使用率极高（184 条）——这个标签承载了大量商业新闻/产品资讯类条目，可能稀释了信号密度。建议关注此标签是否需要进一步拆分（👤 人工判断）。

---

## 类型启发式筛查结果

对抽样的 ~200 个 concept 名称应用规则筛查，发现 **疑似应为 entity** 的条目：

| **条目** | **当前类型** | **命中规则** | **说明** |

| --- | --- | --- | --- |

| [Untitled](entities/obsidian-cli.md) | concept | Rule B（CLI 后缀） | 特定 CLI 工具，应为 entity |

| [Untitled](entities/G.A.M.E 框架.md) | concept | Rule C（英文专有名词） | Virtuals Protocol 旗下的具体产品框架，建议改为 entity |

| [Untitled](concepts/GraphRAG.md) | concept | Rule C | 微软开源项目，也是技术范式——建议人工确认 concept vs entity |

| [Untitled](concepts/Antigravity MCP.md) | concept | Rule B-ish | 疑似特定 MCP 实现产品，建议确认 |

| [Untitled](concepts/TuriX Parallelum.md) | concept | Rule C | 专有名词，来源不明，建议人工确认是否为产品 |

以上均为「建议人工确认」，不自动判定。

---

## 标签分类合理性检查

基于 Phase 2 loadPage 抽样（共加载 13 页）：

| 条目 | 问题 | 建议 |

| --- | --- | --- |

| [Untitled](concepts/Long Horizon Task.md) | `加密资产` 标签误分类 | 移除 `加密资产`，补 `推理优化` 或 `Agent 协作模式` |

| [Untitled](entities/GLM-5-Turbo.md) | 标签偏向 OpenClaw 使用场景而非模型属性 | 改为 `多模态, 推理优化, AI 产品` |

| [Untitled](concepts/ΛCDM 模型.md)  • [Untitled](concepts/L-GALAXIES 半解析模型.md) | 天体物理条目与 Wiki 主题不符 | 👤 人工确认：是否属于知识库范畴，若否建议删除 |

---

## 引用结构化检查

**抽样范围**：从 Phase 1 发现的问题条目 + 不同日期批次抽样，共加载 12 个 concept/entity 页面。

| **页面** | **状态** | **来源引用结构** |

| --- | --- | --- |

| [Untitled](concepts/画布式 Agent 编排.md) | 草稿 | ❌ 空（无任何引用） |

| [Untitled](entities/Open Swarm.md) | 草稿 | ❌ 空（无任何引用） |

| [Untitled](entities/Path2AGI.md) | 草稿 | ✅ 1 个 mention-page |

| [Untitled](concepts/RAG.md) | 已审核 | ✅ 7 个 mention-page |

| [Untitled](concepts/Memory Folder.md) | 审核中 | ✅ 1 个 mention-page |

| [Untitled](concepts/Vibe Coding.md) | 已审核 | ✅ 18 个 mention-page |

| [Untitled](entities/SWE-Bench Verified.md) | 草稿 | ✅ 2 个 mention-page |

| [Untitled](concepts/AX Tree.md) | 草稿 | ✅ 1 个 mention-page |

| [Untitled](entities/ChatGPT.md) | 草稿 | ✅ 1 个 mention-page |

| [Untitled](entities/USDC.md) | 草稿 | ✅ 1 个 mention-page |

| [Untitled](concepts/外部记忆.md) | 草稿 | ✅ 1 个 mention-page |

| [Untitled](concepts/模型议价能力.md) | 草稿 | ✅ 1 个 mention-page |

**汇总统计：**

- 抽样量：12 个 concept/entity 页面

- 有结构化引用（mention-page）：10 页（83.3%）

- 无引用（空）：2 页（16.7%）

- 纯文本引用：0 页（0%）

- **Affected page rate：16.7%**（< 30% 阈值）

- **Plain-text rate：0%**（< 20% 阈值）

✅ **无系统性问题警报**。2 个空引用页面（画布式 Agent 编排、Open Swarm）均为已识别的过期草稿，属于孤立问题，不代表 Compiler 批次性问题。

---

## 计分明细

| **检查项** | **发现** | **扣分** |

| --- | --- | --- |

| 孤岛条目 | 5 个疑似候选（未经搜索验证） | 0（待验证后计分） |

| 过期草稿（>7天） | 3 条（2026-04-24/25） | -9（3 × -3） |

| 过时内容（>30天或null） | 1 条 synthesis null compile_time | -3 |

| 重复疑似（concept/entity） | 0 对 | 0 |

| 重复疑似（summary） | 0 对 | 0 |

| 状态异常 | 0 条 | 0 |

| 缺失标签 | 0 条 | 0 |

| 废弃标签 | 0 处 | 0 |

| 标签误分类 | 2 处（Long Horizon Task、GLM-5-Turbo） | -2 |

| 引用结构化问题 | 2 空引用（低于系统性阈值） | 0 |

| **合计** |  | **-14** |

**最终得分：100 - 14 = 86 / 100 🟢**

---

## 状态晋升建议

以下为 Phase 2 已验证内容完整（定义 + 关键要点 + ≥1 mention-page 引用）、且满足 ≥7 天的草稿条目，建议晋升：

| **页面** | **当前状态** | **建议状态** | **原因** |

| --- | --- | --- | --- |

| [Untitled](entities/Path2AGI.md) | 草稿 | 审核中 | 内容完整，有 mention-page 引用，创建 8 天 |

| [Untitled](entities/SWE-Bench Verified.md) | 草稿 | 审核中 | 内容完整，有 2 个 mention-page 引用，创建 7 天 |

| [Untitled](concepts/AX Tree.md) | 草稿 | 审核中 | 内容完整，有 mention-page 引用，创建 7 天 |

| [Untitled](entities/ChatGPT.md) | 草稿 | 审核中 | 内容完整，有 mention-page 引用，创建 7 天 |

| [Untitled](entities/USDC.md) | 草稿 | 审核中 | 内容完整，有 mention-page 引用，创建 7 天 |

| [Untitled](concepts/外部记忆.md) | 草稿 | 审核中 | 内容完整，有 mention-page 引用，创建 7 天 |

| [Untitled](concepts/模型议价能力.md) | 草稿 | 审核中 | 内容完整，有 mention-page 引用，创建 7 天 |

> **重要提示**：2026-04-26 创建的草稿批次中还有大约 43 个未被 Phase 2 单独加载验证的条目。鉴于本批次中 5/5 已验证条目均内容完整，**强烈建议 Fixer 批量对该日期批次的所有草稿条目执行晋升验证**（加载页面确认有 mention-page 引用即可晋升）。

---

## 改进建议

### 🤖 自动修复项（Fixer 可直接执行）

1. **标签修正 — Long Horizon Task**

  - 修复类型：标签更新

  - 目标页面：[Long Horizon Task](concepts/Long Horizon Task.md)

  - 操作：移除标签 `加密资产`，添加 `Agent 协作模式`

1. **标签修正 — GLM-5-Turbo**

  - 修复类型：标签更新

  - 目标页面：[GLM-5-Turbo](entities/GLM-5-Turbo.md)

  - 操作：将标签从 `OpenClaw, 多Agent协作, Agent 协作模式` 改为 `多模态, 推理优化, AI 产品`

1. **状态晋升 — 批量草稿→审核中**

  - 修复类型：状态更新

  - 目标：以下已验证完整的 7 条 + 2026-04-26 批次其余草稿（需逐一验证引用结构）

  - 已验证可直接晋升：[Path2AGI](entities/Path2AGI.md)、[SWE-Bench Verified](entities/SWE-Bench Verified.md)、[AX Tree](concepts/AX Tree.md)、[ChatGPT](entities/ChatGPT.md)、[USDC](entities/USDC.md)、[外部记忆](concepts/外部记忆.md)、[模型议价能力](concepts/模型议价能力.md)

  - 操作：将 `状态` 从 `草稿` 改为 `审核中`

1. **类型修正 — obsidian-cli**

  - 修复类型：类型更新

  - 目标页面：[obsidian-cli](entities/obsidian-cli.md)

  - 操作：将 `类型` 从 `concept` 改为 `entity`

1. **类型修正 — G.A.M.E 框架**

  - 修复类型：类型更新

  - 目标页面：[G.A.M.E 框架](entities/G.A.M.E 框架.md)

  - 操作：将 `类型` 从 `concept` 改为 `entity`（Virtuals Protocol 产品）

### 👤 人工介入项（需人类确认）

1. **天体物理条目去留** — [ΛCDM 模型](concepts/ΛCDM 模型.md)、[L-GALAXIES 半解析模型](concepts/L-GALAXIES 半解析模型.md)、[冯·曼戈尔特函数](concepts/冯·曼戈尔特函数.md)、[普罗克鲁斯特斯分析法](concepts/普罗克鲁斯特斯分析法.md)：这些条目是否属于 Wiki 知识范畴？如不属于，可直接删除。

1. **synthesis 编译时间规范** — 人工撰写的 synthesis 页（如研究计划）是否需要填写最后编译时间占位值？若需要，建议制定规范，避免 null compile_time 持续触发过时检测。

1. **商业/生态标签粒度** — 该标签覆盖 184+ 条目，信号密度可能过低。建议人工评估是否需要拆分（如「AI 产品发布」「商业模式」「融资/生态」等子标签）。

1. **孤岛验证** — 对以上 5 个疑似孤岛候选，建议通过 Notion Search 二次验证，确认有无 summary 在正文中 mention 了这些页面。

1. **TuriX Parallelum 来源确认** — 名称罕见，来源不明，建议人工确认是否为有效条目或噪声数据。

---

>  请根据以上报告执行自动修复。
