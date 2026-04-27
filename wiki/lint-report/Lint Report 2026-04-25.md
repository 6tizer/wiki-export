---
title: Lint Report 2026-04-25
type: lint-report
tags:
- 知识管理
- OpenClaw
- 商业/生态
status: 草稿
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/f635e4d3f73047ac8c58d4d825bbe3c7
notion_id: f635e4d3-f730-47ac-8c58-d4d825bbe3c7
---

## 检查日期

2026-04-25（定时触发，每日 14:00 北京时间）

## 总体健康度

🔴 **0/100**

> 主要扣分项：386 个过期草稿（-1,158 分）已超出基准分，另有系统性纯文本引用问题（额外 -10 分）。分数下限为 0。

---

## 全库统计（类型 × 状态）

| 类型 | 草稿 | 审核中 | 已审核 | 需更新 | 总计 |

| --- | --- | --- | --- | --- | --- |

| concept | 827 | 843 | 24 | 1 | 1,695 |

| entity | 340 | 474 | 4 | 0 | 818 |

| summary | 0 | 0 | 1,242 | 0 | 1,242 |

| synthesis | 0 | 2 | 84 | 0 | 86 |

| qa | 0 | 0 | 4 | 0 | 4 |

| **总计** | **1,167** | **1,319** | **1,358** | **1** | **3,845** |

---

## 孤岛条目

**检测方法**：Phase 1 使用标题命中初筛（concept/entity 名称 vs summary 标题 LIKE 匹配），大多数近期条目在摘要标题中有所体现。由于 summary 无 relation 字段，精确孤岛检测需逐条搜索，本次抽样验证了 5 个草稿条目，均有来源引用（但多为纯文本形式，非结构化 mention-page）。

**结论**：当前无法通过 SQL 精确枚举孤岛列表（需要 self-join）。由于大量条目存在纯文本引用（见「引用结构化检查」），实际孤岛数量可能被低估——纯文本引用不会被知识图谱识别为连接。

**建议**：修复纯文本引用后（见改进建议），再执行孤岛检测可获得更准确结果。

---

## 过期草稿

**共 386 条**：类型为 concept 或 entity、状态为「草稿」、创建时间早于 2026-04-18（即超过 7 天）。

典型样本：

- [SuperHQ](entities/SuperHQ.md)（entity，创建于 2026-04-11，已编译，有1个 mention-page 引用 + 纯文本）

- [find-skills](concepts/find-skills.md)（concept，创建于 2026-04-11，纯文本引用）

- [Skill-Based Agent 架构](concepts/Skill-Based Agent 架构.md)（concept，创建于 2026-04-11，纯文本引用）

- [CrewClaw](entities/CrewClaw.md)（entity，创建于 2026-04-11，纯文本引用）

- [投委会模拟](concepts/投委会模拟.md)（concept，创建于 2026-04-12，纯文本引用）

**注**：大量草稿的「来源引用」使用纯文本格式，无 `<mention-page>` 标签，导致无法进行状态晋升自动判断。需先修复引用结构后再批量晋升。

---

## 过时内容（最后编译时间 > 30 天）

**共 0 条**（豁免系统元页面后）。

所有非豁免条目的最后编译时间均在 2026-04-10 以后，未超过 30 天阈值。

**豁免条目**（last_compile 为 null，属正常）：

- [关于 Wiki Compiler](concepts/关于 Wiki Compiler.md)

- [关于 Wiki Lint Agent](concepts/关于 Wiki Lint Agent.md)

- [关于 Wiki Fixer](concepts/关于 Wiki Fixer.md)

- [关于 Gap Agent](concepts/关于 Gap Agent.md)（当前状态：需更新，建议人工核查）

- [关于 Wiki QA Agent](concepts/关于 Wiki QA Agent.md)

- [关于 Notion AI（Wiki 协调者）](concepts/关于 Notion AI（Wiki 协调者）.md)

- [关于 Wiki Synthesizer](concepts/关于 Wiki Synthesizer.md)

---

## 重复疑似

### A. Concept/Entity 完全同名重复

- **Wish Coding**（concept）：发现 2 个同名页面 — Wish Coding 及另一同名页

- **时序知识图谱**（concept）：发现 2 个同名页面 — 时序知识图谱 及另一同名页

### B. Concept/Entity 归一化近似重复

从已检索的约 1,500 条名称中，未发现归一化后严格相同的对（除完全同名外）。已检查以下候选：

- "Dreaming 记忆机制" vs "Dreaming 记忆整合"：归一化后不同（不同概念）

- "agency-agents" vs "agency-agents-zh"：归一化后不同（中文版 vs 原版）

> ⚠️ 注：总共 2,513 条 concept/entity，本次仅检索了约 1,500 条名称列表，另约 1,000 条未经归一化检查。建议 Fixer 执行全量近似重复扫描。

### A. Summary 完全同名重复

**SQL 查询结果**：未发现完全同名（GROUP BY 名称 HAVING COUNT > 1 = 0）。

### B. Summary 近似同名重复（推理层匹配）

从已检索的约 2,000 条摘要名称中，发现以下疑似组：

**组 1**（差异：末尾标点）：

- [摘要：湾大北交大开源 CutClaw，自动踩点音乐的 AI 智能视频剪辑师](summaries/摘要：湾大北交大开源 CutClaw，自动踩点音乐的 AI 智能视频剪辑师.md)

- 摘要：湾大北交大开源 CutClaw，自动踩点音乐的 AI 智能视频剪辑师！

**组 2**（差异：语序/措辞，同一开源事件）：

- 摘要：最强大脑组合！CodeBrain-1 & MemBrain1.5同时开源

- 摘要：最强大脑组合！MemBrain1.5 与 CodeBrain-1 同时开源

- [摘要：最强大脑组合！全球SOTA的逻辑和记忆CodeBrain-1&MemBrain1.5同时开源](summaries/摘要：最强大脑组合！全球SOTA的逻辑和记忆CodeBrain-1&MemBrain1.5同时开源.md)

**组 3**（差异：缺少"后"字，同一事件）：

- 摘要：开源模型首超Opus4.6！智谱GLM-5.1登场，14小时CUDA专家被冲了

- [摘要：开源模型首超Opus4.6！智谱GLM-5.1登场，14小时后CUDA专家被冲了](summaries/摘要：开源模型首超Opus4.6！智谱GLM-5.1登场，14小时后CUDA专家被冲了.md)

**组 4**（agency-agents 同一项目不同角度的摘要）：

- [摘要：Agency Agents：用 147 个 AI 专家角色，把 Claude Code 变成一整家公司](summaries/摘要：Agency Agents：用 147 个 AI 专家角色，把 Claude Code 变成一整家公司.md)

- [摘要：agency-agents：一个开源的 AI 虚拟团队，144 个专业 Agent 覆盖 12 个职能部门](summaries/摘要：agency-agents：一个开源的 AI 虚拟团队，144 个专业 Agent 覆盖 12 个职能部门.md)

- [摘要：agency-agents：用 147 个 Markdown 文件，搭建你的零成本 AI 专业团队](summaries/摘要：agency-agents：用 147 个 Markdown 文件，搭建你的零成本 AI 专业团队.md)

> 以上共 4 组，按计分规则扣 0 分（每10组 summary 重复扣1分）。

---

## 状态异常

**共 0 条**：SQL 查询未发现状态为 NULL 的条目。所有条目均已设置状态。✅

---

## 标签异常

### 缺失标签

**共 0 条**：所有 concept/entity 均有至少 1 个标签。✅

### 废弃标签使用

**共 0 条**：未发现使用废弃标签（AI Agent、MCP、Notion）的条目。✅

---

## 标签分布统计

以下为部分高频标签（基于已检索的约 1,500 条 concept/entity 名称，完整统计需全量查询）：

| 标签 | 估算条目数 | 备注 |

| --- | --- | --- |

| Agent 框架 | 高频 | 核心标签，分布广泛 |

| Agent 编排 | 高频 | 与 Agent 框架存在重叠风险 |

| OpenClaw | 高频 | OpenClaw 生态相关条目量大 |

| 记忆系统 | 中频 | 含长期记忆、上下文管理子标签 |

| Coding Agent | 中频 | 新标签，替代原 AI Agent 废弃标签 |

| Crypto/DeFi | 中频 | 加密相关条目独立聚集 |

| 知识管理 | 中频 | Wiki 系统自身的元标签 |

| 商业/生态 | 低频 | 覆盖面较窄 |

> ⚠️ 注意：发现多个扩展子标签（如「推理优化」「多模态」「IDE 集成」「MCP 协议」「多Agent协作」等）未在标准 14 个有效标签之列。这些标签被大量使用，建议人工确认是否为合法扩展或需归并。

---

## 类型启发式筛查结果（疑似 concept → entity）

以下条目疑似应分类为 entity（建议人工确认，不自动判定）：

| 条目名称 | 当前类型 | 命中规则 | 说明 |

| --- | --- | --- | --- |

| [Untitled](entities/OKX OnchainOS.md) | concept | 规则 B（Platform/OS）+ 规则 C | OKX 的具体产品，有版本号和团队背景 |

| [Untitled](concepts/obsidian-cli.md) | concept | 规则 B（CLI） | 具体工具/开源项目 |

| [Untitled](concepts/NanoClaw.md) | concept | 规则 C（英文专有名词） | OpenClaw 生态中的具体实现项目 |

| [Untitled](concepts/OASIS.md) | concept | 规则 D（大写缩写） | 可能是具体项目名称 |

> 以上为部分样本，完整扫描建议对全量 1,695 条 concept 执行推理层规则匹配。

---

## 标签分类合理性检查（Phase 2 抽样）

基于已检索的 concept/entity 数据，发现以下潜在标签误分类：

**非标准标签（扩展标签大量使用）**：

- `推理优化`、`多模态`、`IDE 集成`、`代码生成`、`多Agent协作`、`MCP 协议`、`上下文管理`、`长期记忆`、`RAG/检索`、`笔记工具`、`AI 产品`、`模型部署`、`CLI 工具`、`前端开发`、`浏览器自动化`、`社交媒体`、`图像生成`、`视频/3D`、`AI 交易`、`AI 对齐` 等均被使用，但不在标准 14 标签之列。

**建议确认的误分类**：

- [Qwen3.5](entities/Qwen3.5.md)（entity）标签含 `LLM`：entity 类型正确，但 LLM 标签是否应改为更精确的扩展标签？

- 多个 `开发工具` 标签的 entity 中存在 AI Coding Agent（如 Cursor、Devin 等）：按规则这些应归入 `Coding Agent` 标签。

---

## 引用结构化检查

### 🚨 系统性问题

**抽样规模**：5 个草稿 concept/entity 页面（创建日期跨度：2026-04-11 至 2026-04-12）

| 指标 | 数值 | 阈值 | 状态 |

| --- | --- | --- | --- |

| Affected page rate（含纯文本引用的页面比例） | 80%（5/5 中 4 个） | ≥30% | 🚨 超出 |

| Plain-text rate（纯文本引用占总引用比例） | ~80% | ≥20% | 🚨 超出 |

**抽样页面详情**：

- [SuperHQ](entities/SuperHQ.md)：1 个 `<mention-page>` ✅ + 纯文本"未匹配：GitHub README" ⚠️

- [find-skills](concepts/find-skills.md)：纯文本引用 2 条 ❌

- [Skill-Based Agent 架构](concepts/Skill-Based Agent 架构.md)：纯文本引用 1 条 ❌

- [CrewClaw](entities/CrewClaw.md)：纯文本+原文链接 ❌

- [投委会模拟](concepts/投委会模拟.md)：纯文本引用 1 条 ❌

**系统性影响估算**：

- 草稿 concept/entity 共 1,167 条

- 按 80% 受影响率推算：约 **934 条**页面存在纯文本引用问题

- 这些页面的「来源引用」不会被知识图谱识别，孤岛检测将失准，状态晋升无法自动执行

**根因分析**：早期 Compiler 批次（2026-04-10 至 2026-04-12）产出的草稿使用纯文本引用格式（`《标题》｜X书签文章｜原文链接：https://...`），未生成 `<mention-page>` 结构化标签。

---

## 计分明细

| 检查项 | 发现 | 扣分规则 | 扣分 |

| --- | --- | --- | --- |

| 孤岛条目 | 无法精确计数（纯文本引用导致图谱断链） | -5/个 | 0（待修复引用后重测） |

| 过期草稿（>7天） | 386 条 | -3/个 | -1,158 |

| 过时内容（>30天） | 0 条 | -3/个 | 0 |

| concept/entity 重复对 | 2 个完全同名对 | -10/对 | -20 |

| summary 重复组 | 4 组 | -1/10组 | 0 |

| 状态异常 | 0 条 | -2/个 | 0 |

| 缺失/空标签 | 0 条 | -2/个 | 0 |

| 废弃标签使用 | 0 条 | -5/个 | 0 |

| 纯文本引用（抽样5个） | 4 个页面有纯文本引用（共约5条） | -1/5个 | -1 |

| 系统性问题额外扣分 | Affected rate=80% ≥ 30% 阈值 | -10（一次性） | -10 |

| **合计** |  |  | **最低 0/100** |

---

## 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 |

| --- | --- | --- | --- |

| [Untitled](entities/SuperHQ.md) | 草稿 | 审核中 | 创建 >7 天，定义+要点完整，有1个 mention-page 引用 |

| synthesis 审核中（2条） | 审核中 | 已审核 | synthesis 类型不需要人工审核，应自动晋升至已审核 |

| 386 条过期草稿 | 草稿 | 审核中（条件满足后） | 需先修复来源引用为 mention-page 格式，再由 Fixer 批量评估晋升资格 |

> **注**：由于 80% 草稿存在纯文本引用，无法自动批量晋升至审核中。修复引用结构是前提。

---

## 改进建议

### 🤖 自动修复项（Fixer 可直接执行）

1. **[重复合并] concept/entity 完全同名重复**

  - 目标：Wish Coding（2个同名页面） → 合并保留较完整的一个，删除重复页

  - 目标：时序知识图谱（2个同名页面） → 同上

  - 操作：loadPage 比较两页内容 → 保留内容更完整的 → deletePages 删除另一个

1. **[重复合并] summary 近似重复**

  - 组1：[摘要：湾大北交大开源 CutClaw，自动踩点音乐的 AI 智能视频剪辑师](summaries/摘要：湾大北交大开源 CutClaw，自动踩点音乐的 AI 智能视频剪辑师.md) vs 摘要：湾大北交大开源 CutClaw，自动踩点音乐的 AI 智能视频剪辑师！ → 保留一个，deletePages 删除另一个

  - 组2：CodeBrain+MemBrain 3个重复摘要 → 保留最完整的一个，deletePages 其余两个

  - 组3：GLM-5.1 摘要2个重复 → 保留一个，deletePages 另一个

  - 组4：agency-agents 3个重复摘要 → 需人工确认是否为真重复（不同角度可保留），条件成立则合并

1. **[状态更新] synthesis 晋升**

  - 将 2 条「审核中」synthesis 更新状态为「已审核」

  - 操作：querySql 查出这2个页面 URL → updatePage 设置状态=已审核

1. **[状态更新] SuperHQ 草稿晋升**

  - [SuperHQ](entities/SuperHQ.md)：状态草稿→审核中

  - 操作：updatePage 设置状态=审核中

### 👤 人工介入项

1. **🚨 【最高优先级】建立 Autofill Agent（引用升级员）批量修复纯文本引用**

  - 问题规模：约 934 条 concept/entity 草稿存在纯文本引用，无法通过 Wiki Fixer 逐条修复（Fixer 每次处理时间约 30-60 秒，934 条需 8-16 小时）

  - 推荐方案：创建独立的「引用升级员」Autofill Agent，专门负责：

    1. 读取草稿页面的「来源引用」区块

    1. 将纯文本引用（`《标题》｜...`格式）匹配到对应 summary 页面

    1. 替换为 `<mention-page url="...">标题</mention-page>` 结构化格式

  - Fixer 手动批处理等效指令：`对以下页面执行 E2 引用修复：[URL列表]。对每个页面：loadPage → 解析来源引用区块中的文章标题 → searchNotion 找到对应 summary → updatePage 将纯文本替换为 mention-page 格式`

1. **[Schema 确认] 非标准标签大量使用**

  - 约 20 个扩展标签（推理优化、多模态、IDE 集成等）未在标准 14 标签之列，但已被广泛使用

  - 需要人工决定：是否官方纳入标准标签列表？还是迁移归并至标准标签？

  - 建议：扩展标准标签列表至覆盖实际使用的高频标签

1. **[类型确认] 疑似 concept→entity 的条目**

  - 见「类型启发式筛查结果」章节列举的 4 个候选条目

  - 需人工确认后，由 Fixer 执行类型更新

1. **[Compiler 调整] 修复引用生成格式**

  - 根本原因：Compiler 在生成 concept/entity 页面时，「来源引用」区块使用了纯文本格式而非 mention-page

  - 需要更新 Wiki Compiler 的 System Prompt，要求「来源引用」区块必须使用 `<mention-page url="...">` 格式引用对应 summary 页面

1. **[豁免规则审查] 关于 Gap Agent（需更新状态）**

  - [关于 Gap Agent](concepts/关于 Gap Agent.md) 当前状态为「需更新」但 last_compile 为 null

  - 需人工确认该页面是否需要更新内容，或改为豁免

---

 请根据以上报告执行自动修复。
