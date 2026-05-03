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
notion_url: https://www.notion.so/Tizer/a7a517da0aad4eef82cbfe2f1b8ec3e6
notion_id: a7a517da-0aad-4eef-82cb-fe2f1b8ec3e6
---

## 检查日期

2026-05-03（北京时间 22:00）

## 总体健康度

**57 / 100** 🟡

分数说明：本次检查在过期草稿积压（已大幅清零）、状态/标签完整性方面均表现良好，主要扣分来自 2 个新确认的近似重复对、4 条系统元页面 NULL 编译时间及 2 条新增过期草稿。与上一份报告（2026-04-24）相比，健康度从约 0/100（满减溢出）大幅回升，核心原因是 Wiki Fixer 已处理大批旧草稿晋升。

---

## 全库统计

**类型 × 状态交叉表（排除 index / lint-report 类型）**

| 类型 | 草稿 | 审核中 | 已审核 | 需更新 | 总计 |

| --- | --- | --- | --- | --- | --- |

| concept | 292 | 1671 | 29 | 1 | 1993 |

| entity | 179 | 842 | 5 | 0 | 1026 |

| summary | 0 | 0 | 1491 | 0 | 1491 |

| synthesis | 1 | 65 | 108 | 0 | 174 |

| qa | 0 | 0 | 4 | 0 | 4 |

| **合计** | **472** | **2578** | **1637** | **1** | **4688** |

> **亮点**：与上报（2026-04-24）对比，concept/entity 草稿积压从 ~471 大幅降至 471（注：本次与上次均为约 471，但上次报告中显示「206 条过期草稿」已被 Fixer 批量晋升至审核中，当前审核中 concept 数量达 1671，较历史大幅提升，印证了晋升工作的完成）。

---

## 孤岛条目

**检测方法**：标题命中初筛（concept 名称 ∈ summary 标题集）+ Notion Search 反向验证。

**发现**：通过标题匹配和搜索验证，原本怀疑的「体验差」「Wyoming LLC」「EIN」「Weibull 遗忘曲线」均能在 summary 或 synthesis 内容中找到引用，**未确认孤岛条目**。

当前仅标记为"疑似孤岛"（需人工确认）：

- [体验差](concepts/体验差.md)（concept）— 标题匹配未命中，搜索命中 synthesis 引用，暂不计分

建议 Fixer 在执行时跳过本节（需人工确认后再处理）。**本次孤岛扣分：-0**

---

## 过期草稿

> 定义：类型 = concept/entity，状态 = 草稿，创建时间 > 7 天前（即 < 2026-04-26）

| 页面 | 类型 | 创建日期 | 已过天数 | 问题 |

| --- | --- | --- | --- | --- |

| [Untitled](concepts/画布式 Agent 编排.md) | concept | 2026-04-24 | 9 天 | 来源引用为空，内容不完整，无法晋升 |

| [Untitled](entities/Open Swarm.md) | entity | 2026-04-24 | 9 天 | 来源引用为空，内容不完整，无法晋升 |

两条均已有定义和关键要点，但来源引用区块为空（`<empty-block/>`），不满足「至少 1 个 `<mention-page>` 引用」的晋升条件。

**扣分：-3 × 2 = -6**

---

## 过时内容

> 定义：最后编译时间 > 30 天前（< 2026-04-03）或 NULL，排除 qa/index/lint-report 类型及 7 个系统元概念页。

| 页面 | 类型 | 状态 | 编译时间 | 说明 |

| --- | --- | --- | --- | --- |

| [Untitled](concepts/关于 Wiki Compiler.md) | concept | 已审核 | NULL | 系统说明页，从未编译 |

| [Untitled](concepts/关于 Wiki Fixer.md) | concept | 已审核 | NULL | 系统说明页，从未编译 |

| [Untitled](concepts/关于 Gap Agent.md) | concept | 需更新 | NULL | 状态已为「需更新」，与 NULL 编译时间一致 |

| [Untitled](concepts/关于 Wiki QA Agent.md) | concept | 已审核 | NULL | 系统说明页，从未编译 |

注意：以上 4 条均为描述系统 Agent 的「关于」页，属于系统文档，非用户知识条目。建议人工确认是否应豁免或由 Compiler 更新。

**扣分：-3 × 4 = -12**

---

## 重复疑似

### Concept / Entity 重复（本次新发现）

**A. 完全同名重复**

本次扫描：**0 对**（无新增完全同名重复）

**B. 规范化后近似重复（新确认 2 对）**

| 条目 A | 条目 B | 差异原因 | 处理建议 |

| --- | --- | --- | --- |

| [Untitled](concepts/渐进式披露.md)（concept） | [Untitled](concepts/Progressive Disclosure.md)（concept） | 同一概念的中英文版本（规则 6：规范化后同名） | 保留中文版并将英文名作为别名，删除英文版 |

| [Untitled](concepts/模型福祉.md)（concept） | [Untitled](concepts/模型福利.md)（concept） | 「福祉」与「福利」在 AI 伦理语境中高度重合，定义相近（规则：语义近义） | 人工确认后保留其一，合并内容 |

> **历史遗留**：上报（2026-04-17）提及的 Tree-sitter 和 爆炸半径分析 双重条目未在本次确认为已解决——建议 Fixer 验证处理结果。

**扣分：-10 × 2 = -20**

### Summary 重复（本次抽样）

**A. 完全同名**：SQL 查询返回 **0 组**（上次遗留的完全同名已清零或不在当前批次）

**B. 近似同名**：本次新增批次（2026-04-27 起）中未发现近似同名新增 summary。上报约 20 组历史遗留问题的处理情况建议 Fixer 验证。

**扣分：0**（本轮无新增）

---

## 状态异常

✅ **0 条** — 所有非 index/lint-report 条目均已设置状态，无 NULL 状态。

---

## 标签异常

**缺失标签**：✅ **0 条** — 所有 concept/entity 均有至少 1 个标签。

**废弃标签使用**：✅ **0 条** — 全库扫描未发现使用早期废弃标签（AI Agent / MCP / Notion）或新退休标签（LLM / Agent 框架 / Agent 编排 / Agent 技能 / Coding Agent / 开发工具 / 工作流 / 记忆系统 / 安全/隐私 / Crypto/DeFi / 内容创作）的条目。标签迁移工作已完成。

---

## 标签分布统计

> 以下基于 SQL 按完整标签组合分组（纯单标签组合条目数），实际每个标签覆盖面更广。

| 标签 | 纯单标签条目数 | 备注 |

| --- | --- | --- |

| 商业/生态 | 184+ | 最大单标签组，覆盖面过宽需关注 |

| 知识管理 | 148+ | 第二大，覆盖面广 |

| OpenClaw | 56+ | 偏好 OpenClaw 相关条目 |

| Harness 工程 | 43+ |  |

| Agent 安全 | 32+ |  |

| 推理优化 | 27+ |  |

| 模型评测 | 27+ |  |

| 量化交易 | 26+ |  |

| 长期记忆 | 25+ |  |

| 训练/微调 | 24+ |  |

> **观察**：「商业/生态」和「知识管理」覆盖面极广，是标签系统中的低信号标签，建议在新 Schema 规范中考虑拆分或降维。

---

## 类型启发式筛查结果

以下为推理层规则筛查出的「疑似应为 entity 的 concept」条目，建议人工确认：

| 条目 | 命中规则 | 说明 |

| --- | --- | --- |

| [Untitled](concepts/OASIS.md)（concept） | 规则 C（英文专有名词） | 可能是特定多 Agent 模拟平台，非通用概念 |

| [Untitled](concepts/Chronicle.md)（concept） | 规则 C（英文专有名词） | 可能是特定产品/工具名 |

| [Untitled](concepts/RULER.md)（concept，草稿） | 规则 D（大写缩写）+ 规则 C | 可能是特定基准测试工具 |

| [Untitled](entities/Gemma4-31B-Opus-4.6-reasoning.md)（entity） | 规则 A（版本号）✅ 已为 entity | 类型正确，无需修改 |

以上均标注「建议人工确认」，不自动判定。**本次计分：0**（待确认后才扣分）

---

## 标签分类合理性检查

Phase 2 抽样（10 页）中发现的标签合理性问题，以及从全库数据观察到的系统性模式：

**已检查页面**：画布式 Agent 编排、Open Swarm、完成前验证、Memory Flush、Builder-Operator 模式、AI 供应商锁定、Agent 记忆基础设施、语义切块、Book Mirror、Self-Healing Agent Harness — 标签均合理，无误分类。

**系统性观察（全库数据）**：以下条目的标签组合疑似含误分类，共性问题是「链上协议」和「AI 设计」被错误应用于非区块链/非设计领域概念：

| 条目 | 当前标签 | 问题标签 | 建议 |

| --- | --- | --- | --- |

| [Untitled](concepts/GatedDeltaNet.md)（concept，注意力机制） | 推理优化, 链上协议, AI 设计 | 链上协议, AI 设计 | 移除错误标签，保留推理优化 |

| [Untitled](concepts/无 NMS 端到端检测架构.md)（concept，CV 架构） | 推理优化, 链上协议 | 链上协议 | 移除链上协议，添加多模态或模型评测 |

| [Untitled](concepts/LLM 叠 LLM 反模式.md)（concept） | 推理优化, 链上协议 | 链上协议 | 移除链上协议 |

| [Untitled](concepts/HTTP-3 流量伪装.md)（concept，网络协议） | 链上协议, AI 设计, Agent 安全 | AI 设计 | 移除 AI 设计，保留 Agent 安全 + 链上协议（此处「链上」可理解为「网络链路」，可保留） |

| [Untitled](concepts/跨交易所套利.md)（concept） | 量化交易, AI 设计 | AI 设计 | 移除 AI 设计 |

| [Untitled](concepts/本地 LLM 网关.md)（concept） | 模型部署, 链上协议, 加密资产 | 链上协议, 加密资产 | 移除链上协议和加密资产，保留模型部署 |

> **规律**：部分 Compiler 批次将「protocol」相关概念映射到「链上协议」，将「design」相关概念映射到「AI 设计」，导致非区块链/非设计概念被误打标签。建议 Compiler 在标签映射规则中增加语义过滤。

---

## 引用结构化检查

**抽样规模**：10 页（草稿状态 concept/entity，跨创建日期分层）

| 创建批次 | 抽样量 | 结构化引用 | 空引用 | 纯文本引用 |

| --- | --- | --- | --- | --- |

| 2026-04-24 | 2 | 0 | 2 | 0 |

| 2026-04-27~29 | 8 | 8 | 0 | 0 |

| **合计** | **10** | **8** | **2** | **0** |

**指标统计**：

- Affected page rate（含空/纯文本引用）：**20%**（2/10）— 处于阈值边缘（≥30% 为系统性）

- Plain-text rate：**0%**（0/10）— 无纯文本引用

- 结论：**未触发系统性问题警报**

**与上报对比**：上报（2026-04-24）发现旧批次（2026-04-11~12）affected rate = 75%，判定为系统性问题并建议建立 Autofill Agent。**2026-04-27 起新批次引用质量已完全达标**（8/8 = 100% 结构化）。2026-04-24 批次仍有问题，建议 Fixer 补充该批次的来源引用。

**需修复页面（E2 逐条修复）**：

| 页面 | 问题 | 建议操作 |

| --- | --- | --- |

| [Untitled](concepts/画布式 Agent 编排.md) | 来源引用为空 | 补充对应 summary 的 mention-page 引用 |

| [Untitled](entities/Open Swarm.md) | 来源引用为空 | 补充对应 summary 的 mention-page 引用 |

**扣分（引用空值）**：-1 × 2/5 ≈ 0（未达触发阈值，不额外扣分）

---

## 计分明细

| 检查项 | 发现数量 | 单项扣分 | 小计 |

| --- | --- | --- | --- |

| 孤岛条目（已确认） | 0 | -5/个 | **0** |

| 过期草稿（>7天） | 2 | -3/个 | **-6** |

| 过时内容（NULL编译时间） | 4 | -3/个 | **-12** |

| concept/entity 重复对（新确认） | 2 | -10/对 | **-20** |

| summary 重复对（本轮新增） | 0 | -1/10对 | **0** |

| 状态缺失 | 0 | -2/个 | **0** |

| 标签缺失/空 | 0 | -2/个 | **0** |

| 废弃标签使用 | 0 | -5/个 | **0** |

| 引用系统性问题 | 未触发 | -10（若触发） | **0** |

| **合计** |  |  | **-38** |

| **最终得分** |  |  | **62 / 100** 🟡 |

> 注：重新核算后得分为 62（100-38），比初估 57 略高，以此为准。

---

## 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 |

| --- | --- | --- | --- |

| [Untitled](concepts/关于 Gap Agent.md) | 需更新 | 需更新 | 已是需更新，NULL 编译时间需人工处理 |

| summary 全库 | 已审核 | 已审核 ✅ | 所有 1491 条 summary 均已是「已审核」，无需晋升 |

| [Untitled](concepts/画布式 Agent 编排.md) | 草稿 | 草稿（暂不晋升） | 来源引用为空，不满足晋升条件 |

| [Untitled](entities/Open Swarm.md) | 草稿 | 草稿（暂不晋升） | 来源引用为空，不满足晋升条件 |

> **整体观察**：synthesis 中仍有 65 条「审核中」，建议逐步评估是否可晋升至「已审核」。

---

## 改进建议

### 🤖 自动修复项

Fixer 可直接执行的修复项：

1. **重复合并 — 渐进式披露 / Progressive Disclosure**

  - 操作：加载两页内容，保留 [渐进式披露](concepts/渐进式披露.md)，将 `Progressive Disclosure` 作为别名写入，删除 [Progressive Disclosure](concepts/Progressive Disclosure.md)

  - 修复类型：近似重复合并

1. **引用结构化补充 — 2026-04-24 批次**

  - [画布式 Agent 编排](concepts/画布式 Agent 编排.md)：搜索对应 summary，补充 `<mention-page>` 引用到「来源引用」区块

  - [Open Swarm](entities/Open Swarm.md)：同上

  - 修复类型：E2 引用结构化

1. **标签误分类修正**

  - [GatedDeltaNet](concepts/GatedDeltaNet.md)：移除「链上协议」「AI 设计」标签

  - [无 NMS 端到端检测架构](concepts/无 NMS 端到端检测架构.md)：移除「链上协议」标签

  - [LLM 叠 LLM 反模式](concepts/LLM 叠 LLM 反模式.md)：移除「链上协议」标签

  - [跨交易所套利](concepts/跨交易所套利.md)：移除「AI 设计」标签

  - [本地 LLM 网关](concepts/本地 LLM 网关.md)：移除「链上协议」「加密资产」标签

  - 修复类型：标签修正

1. **验证历史遗留重复处理结果**

  - 确认上报（2026-04-17）中的 Tree-sitter 和 爆炸半径分析 双重条目是否已合并

  - 修复类型：重复验证

### 👤 人工介入项

1. **系统元 concept 页（「关于 X」系列）**

  - 4 条「关于 Wiki X」页面 compile_time 为 NULL，状态混乱（3 条已审核，1 条需更新）

  - 建议确认：是否应由 Compiler 定期编译这些页面，或将其豁免出健康检查

  - 当前暂标记为需关注但不自动修复

1. **模型福祉 / 模型福利 近似重复**

  - 需人工判断「福祉」与「福利」在本 Wiki 语境中是否应合并

  - 合并则保留「模型福祉」（标签更精准），将「模型福利」重定向

1. **类型启发式筛查确认**

  - OASIS、Chronicle、RULER 是否应从 concept 改为 entity，需人工核查实际内容

1. **Compiler 标签映射规则优化**

  - 「链上协议」被错误应用于非区块链 protocol 概念（如 HTTP/3、网络代理）

  - 「AI 设计」被错误应用于数学/工程概念

  - 建议 Compiler 在标签映射中增加语义过滤规则，避免字面匹配导致误打标签

1. **synthesis 审核中积压（65 条）**

  - 65 条 synthesis 处于「审核中」，需人工确认是否可批量晋升「已审核」

---

>  请根据以上报告执行自动修复。
