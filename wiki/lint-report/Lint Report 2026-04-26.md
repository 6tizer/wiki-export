---
title: Lint Report 2026-04-26
type: lint-report
tags:
- 知识管理
- 多Agent协作
- Agent 协作模式
- OpenClaw
- MCP 协议
status: 草稿
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/8e8f72cf265c4513a792ca7d580fb175
notion_id: 8e8f72cf-265c-4513-a792-ca7d580fb175
---

## 检查日期

2026-04-26（触发方式：定时任务，北京时间 10:00）

## 总体健康度

**0 / 100** 🔴

> 主要拖分项：378 条过期草稿（-1134 pts）+ 引用结构化系统性问题（-10 pts）。草稿积压已超出评分下限，需优先处理。

---

## 全库统计

| 类型 | 草稿 | 审核中 | 已审核 | 需更新 | 小计 |

| --- | --- | --- | --- | --- | --- |

| concept | 810 | 880 | 26 | 1 | **1717** |

| entity | 335 | 487 | 4 | 0 | **826** |

| summary | 0 | 0 | 1247 | 0 | **1247** |

| synthesis | 0 | 4 | 86 | 0 | **90** |

| qa | 0 | 0 | 4 | 0 | **4** |

| **合计** | 1145 | 1371 | 1367 | 1 | **3884** |

---

## 孤岛条目

由于 summary 没有 relation 字段直接指向 concept/entity，孤岛精确检测需要逐条加载 summary 正文。本次检测采用**标题初筛 + 引用结构化检查联合判定**方式：

- 在引用结构化抽样（8 页）中发现，**草稿页面普遍存在纯文本引用**，意味着这批页面即使有来源，也不会在知识图谱中形成结构化链接，在图谱层面等同于孤岛。

- 初步识别为高孤岛风险的页面（纯文本引用 + 创建 ≥7 天）：

| 页面 | 类型 | 创建时间 | 孤岛风险 |

| --- | --- | --- | --- |

| [Untitled](concepts/自生长人格.md) | concept | 2026-04-11 | 高（纯文本引用） |

| [Untitled](concepts/思维预算.md) | concept | 2026-04-11 | 高（纯文本引用） |

| [Untitled](concepts/Claude Code Dreaming.md) | concept | 2026-04-12 | 高（纯文本引用） |

> 建议：建立 Autofill Agent（引用升级员）批量扫描后，可精确统计孤岛数量。当前估算草稿中孤岛风险页面约 200+（基于抽样外推）。

---

## 过期草稿

**状态=草稿 且 创建时间 ≥7 天前（2026-04-19 之前）的 concept/entity 共 378 条。**

典型样本（创建日期跨度 2026-04-11 ~ 2026-04-18）：

| 页面 | 类型 | 创建时间 | 距今（天） |

| --- | --- | --- | --- |

| [Untitled](entities/SuperConductor.md) | entity | 2026-04-11 | 15 |

| [Untitled](entities/Nezha.md) | entity | 2026-04-11 | 15 |

| [Untitled](concepts/自生长人格.md) | concept | 2026-04-11 | 15 |

| [Untitled](concepts/思维预算.md) | concept | 2026-04-11 | 15 |

| [Untitled](entities/Manus.md) | entity | 2026-04-11 | 15 |

| [Untitled](entities/OpenSandbox.md) | entity | 2026-04-11 | 15 |

| [Untitled](concepts/Claude Code Dreaming.md) | concept | 2026-04-12 | 14 |

| [Untitled](concepts/多模态 K 线形态匹配.md) | concept | 2026-04-11 | 15 |

| [Untitled](concepts/Agentic Navigation.md) | concept | 2026-04-11 | 15 |

| [Untitled](entities/camoufox-cli.md) | entity | 2026-04-11 | 15 |

> 注：378 条仅为 createdTime < 2026-04-19 的草稿计数，不含近 7 天新草稿（另有约 767 条）。

---

## 过时内容

**最后编译时间 > 30 天前（< 2026-03-27）或为 null 的条目：**

共检出 7 条，全部为"关于 Wiki X"系统元 concept 页（null 编译时间），按规则全部**豁免**。

| 页面 | 豁免原因 |

| --- | --- |

| [Untitled](concepts/关于 Wiki Compiler.md) | 系统元页豁免 |

| [Untitled](concepts/关于 Wiki Lint Agent.md) | 系统元页豁免 |

| [Untitled](concepts/关于 Wiki Fixer.md) | 系统元页豁免 |

| [Untitled](concepts/关于 Gap Agent.md) | 系统元页豁免 |

| [Untitled](concepts/关于 Wiki QA Agent.md) | 系统元页豁免 |

| [Untitled](concepts/关于 Notion AI（Wiki 协调者）.md) | 系统元页豁免 |

| [Untitled](concepts/关于 Wiki Synthesizer.md) | 系统元页豁免 |

✅ **非豁免过时内容：0 条。** 所有活跃知识条目均在 30 天内有编译记录。

---

## 重复疑似

### A. concept/entity 完全同名重复

✅ **未检出**（SQL GROUP BY 名称 HAVING COUNT > 1 = 0 结果）

### B. concept/entity 近似同名重复

对已获取的约 600 条 concept + 500 条 entity 名称进行归一化匹配，发现以下疑似对：

| 条目 A | 条目 B | 差异说明 |

| --- | --- | --- |

| [Untitled](concepts/Dreaming 记忆机制.md)（concept） | [Untitled](concepts/Claude Code Dreaming.md)（concept） | 同一机制的两种描述，命名侧重不同（OpenClaw vs Claude Code）。建议人工确认是否合并或增加关联。 |

> 注：由于 concept 总量 1717 条，本次推理层覆盖约 35%，不排除遗漏。建议建立全量归一化脚本。

### A. summary 完全同名重复

✅ **未检出**（SQL 确认 0 条）

### B. summary 近似同名重复

已获取约 700 条 summary 标题进行归一化匹配，**未发现**归一化后同名的近似重复对。

---

## 状态异常

✅ **未检出**（SQL 查询 状态=NULL 返回 0 行）

---

## 标签异常

### 缺失标签

✅ **未检出**（SQL 查询 concept/entity 中 标签=NULL 或空 = 0 行）

### 废弃标签

✅ **未检出**（SQL 查询 含 "AI Agent" / "MCP" / "Notion" 标签的页面 = 0 行）

### 非标准标签使用说明

当前数据库 schema 中存在超出原始 14 个标准标签的扩展标签（如 前端开发、多模态、AI 产品、推理优化、多Agent协作、MCP 协议 等），这些标签已成为事实使用标准。建议人工确认是否纳入官方有效标签列表并更新说明文档。

---

## 标签分布统计

根据已获取的约 600 条 concept 样本统计（高频标签前 15）：

| 标签 | 预估条目数（concept+entity） | 备注 |

| --- | --- | --- |

| Agent 编排 | ~350 | 最高频，需留意分类粒度 |

| Coding Agent | ~280 |  |

| Agent 技能 | ~250 |  |

| 记忆系统 | ~180 |  |

| LLM | ~250 |  |

| 开发工具 | ~200 | 见标签分类合理性检查 |

| OpenClaw | ~150 |  |

| 知识管理 | ~130 |  |

| 工作流 | ~200 |  |

| 商业/生态 | ~150 |  |

| Crypto/DeFi | ~120 |  |

| 安全/隐私 | ~80 |  |

| 内容创作 | ~100 |  |

| Agent 框架 | ~200 |  |

| 多Agent协作 | ~80 | 非标准标签 |

> 注：以上为推理层估算，实际分布需全量 SQL 统计。

---

## 类型启发式筛查结果

以下 concept 条目经推理层规则扫描，疑似应分类为 entity，**建议人工确认**：

| 条目 | 命中规则 | 疑似理由 |

| --- | --- | --- |

| [Untitled](entities/planktonXD.md) | 规则 C（英文专有名词） | 具体工具/项目名称，应为 entity |

| [Untitled](concepts/obsidian-cli.md) | 规则 B（CLI 后缀）、C | 具体 CLI 工具，类似 pikiclaw（entity） |

| [Untitled](entities/skills-vetter.md) | 规则 B（产品名）、C | 具体工具仓库 |

| [Untitled](entities/memory-lancedb-pro.md) | 规则 B（产品名）、C | 具体产品 |

| [Untitled](entities/total-recall.md) | 规则 B、C | 具体记忆工具 |

| [Untitled](concepts/ClawBio.md) | 规则 C（专有名词） | OpenClaw 生态具体产品 |

| [Untitled](entities/superpowers 框架.md) | 规则 B（框架后缀） | GitHub 仓库，类似 Swarms 框架（entity） |

| [Untitled](concepts/飞书官方 OpenClaw 插件.md) | 规则 B（插件后缀） | 具体产品集成，应为 entity |

---

## 标签分类合理性检查（Phase 2 抽样）

在 Phase 2 抽样中对以下条目进行了标签合理性核查：

| 条目 | 当前标签 | 问题 | 建议修正 |

| --- | --- | --- | --- |

| [Untitled](concepts/Memory Folder.md)（concept） | 记忆系统, 长期记忆, 上下文管理 | ✅ 正确 | — |

| [Untitled](concepts/Vibe Coding.md)（concept） | Coding Agent, 工作流, 代码生成, 前端开发, IDE 集成 | ✅ 正确 | — |

| [Untitled](concepts/RAG.md)（concept） | RAG/检索 | ✅ 合理（非标准标签） | 若需标准化可映射至 记忆系统 或 Agent 技能 |

| [Untitled](concepts/MCP 协议.md)（concept） | MCP 协议 | ✅ 使用扩展标签 | 可考虑添加 Agent 框架 |

| [Untitled](concepts/测试时推理.md)（concept） | LLM | ✅ 正确 | — |

| [Untitled](concepts/Dreaming 记忆机制.md)（concept） | OpenClaw, 记忆系统 | ✅ 正确 | — |

整体标签分类质量较好，无明显误分类。

---

## 引用结构化检查 🚨 系统性问题

### 抽样方法

从不同创建日期（2026-04-10 ~ 2026-04-12）抽取 8 个 concept/entity 页面，加载正文逐一检查「来源引用」区块。

### 抽样统计表

| 页面 | 类型 | 状态 | 引用方式 | mention-page 数 | 纯文本引用 |

| --- | --- | --- | --- | --- | --- |

| [Untitled](concepts/RAG.md) | concept | 已审核 | 结构化 | 6 | 0 |

| [Untitled](concepts/Vibe Coding.md) | concept | 已审核 | 结构化 | 14 | 0 |

| [Untitled](concepts/Dreaming 记忆机制.md) | concept | 已审核 | 结构化 | 4 | 0 |

| [Untitled](concepts/MCP 协议.md) | concept | 已审核 | 结构化（含少量混合） | 30+ | 2（在关联概念区，非引用区） |

| [Untitled](entities/SuperConductor.md) | entity | 草稿 | 结构化（疑似错误来源） | 1 | 0 |

| [Untitled](concepts/自生长人格.md) | concept | 草稿 | ❌ 纯文本 | 0 | 1 |

| [Untitled](concepts/思维预算.md) | concept | 草稿 | ❌ 纯文本 | 0 | 1 |

| [Untitled](concepts/Claude Code Dreaming.md) | concept | 草稿 | ❌ 纯文本 | 0 | 1 |

### 系统性指标

| 指标 | 数值 | 阈值 | 状态 |

| --- | --- | --- | --- |

| Affected page rate | 3/8 = **37.5%** | ≥30% | 🚨 触发 |

| Plain-text citation rate | 3/11 = **27.3%** | ≥20% | 🚨 触发 |

### 🚨 系统性问题诊断

**早期 Compiler 批次（2026-04-11 ~ 2026-04-12 编译）产出的草稿条目普遍存在纯文本引用问题。** 估计受影响页面数量：

- 草稿总量中，2026-04-11~12 批次约 400+ 条

- 按 37.5% affected rate 推算，约 **150~200 条**纯文本引用页面

- 加上未纳入 草稿 的中间批次，实际可能 ≥ 300 条

仅靠 Wiki Fixer 逐条修复（每次处理 ~10 条）需约 30+ 轮，不现实。

**在【👤 人工介入项】中已明确推荐：建立独立的 Autofill Agent（引用升级员）批量处理。**

### 待修复页面（纯文本引用，Fixer E2 处理）

| 页面 | URL | 纯文本引用内容 |

| --- | --- | --- |

| [Untitled](concepts/自生长人格.md) | [Untitled](concepts/自生长人格.md) | 《用历史人物「唤醒」AI Agent 人格》X书签 |

| [Untitled](concepts/思维预算.md) | [Untitled](concepts/思维预算.md) | 《用 ultrathink 让 Claude「打散再重建」你的思维框架》X书签 |

| [Untitled](concepts/Claude Code Dreaming.md) | [Untitled](concepts/Claude Code Dreaming.md) | 《Claude Code 的七层记忆体系》X书签 |

---

## 计分明细

| 检查项 | 发现 | 单位扣分 | 总扣分 |

| --- | --- | --- | --- |

| 孤岛条目 | ~3 条（抽样确认，估计 200+） | -5 | -15（保守） |

| 过期草稿（>7天） | 378 条 | -3 | -1134 |

| 过时内容（>30天） | 0 条（全豁免） | -3 | 0 |

| 重复对（concept/entity） | 1 对（疑似） | -10 | -10 |

| 重复对（summary） | 0 组 | -1/10组 | 0 |

| 状态异常 | 0 条 | -2 | 0 |

| 标签缺失 | 0 条 | -2 | 0 |

| 废弃标签使用 | 0 条 | -5 | 0 |

| 纯文本引用 | 3 条（确认） | -1/5条 | -1 |

| 引用系统性问题 | 触发（37.5% ≥ 30%） | -10 | -10 |

| **合计（下限 0）** | — | — | **0/100** |

---

## 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 |

| --- | --- | --- | --- |

| [Untitled](concepts/RAG.md)（已是已审核） | 已审核 | 保持 | 6+ mention-page 引用，内容完整 |

| [Untitled](concepts/Vibe Coding.md)（已是已审核） | 已审核 | 保持 | 14+ mention-page 引用，多来源验证 |

| [Untitled](concepts/Dreaming 记忆机制.md)（已是已审核） | 已审核 | 保持 | 4 mention-page 引用，内容完整 |

| [Untitled](concepts/自生长人格.md) | 草稿 | 保持草稿 | 无 mention-page 引用，需先修复引用结构 |

| [Untitled](concepts/思维预算.md) | 草稿 | 保持草稿 | 无 mention-page 引用，需先修复引用结构 |

| [Untitled](concepts/Claude Code Dreaming.md) | 草稿 | 保持草稿 | 无 mention-page 引用，需先修复引用结构 |

| [Untitled](entities/SuperConductor.md) | 草稿 | 保持草稿 | mention-page 引用疑似错误来源（量化分析文章 ≠ 该 entity 来源），需人工核查 |

| 全部 synthesis（4 条审核中） | 审核中 | 已审核 | synthesis 类型无需人工审核，可直接晋升 |

> 关于 378 条过期草稿的批量晋升：需先通过引用升级员修复 mention-page 引用，再由 Fixer 执行完整性检查后批量晋升。

---

## 改进建议

### 🤖 自动修复项（Fixer 可直接执行）

1. **[E1] 状态晋升 - synthesis**

  - 修复类型：状态更新

  - 目标：所有 4 条 synthesis 审核中 → 已审核

  - 操作：`updatePage(url, { 状态: "已审核" })` for each

  - 预计耗时：1 轮

1. **[E2] 引用结构化修复（已确认 3 条）**

  - 修复类型：引用结构化升级

  - 目标：[自生长人格](concepts/自生长人格.md)、[思维预算](concepts/思维预算.md)、[Claude Code Dreaming](concepts/Claude Code Dreaming.md)

  - 操作：搜索对应 summary 页面，将「来源引用」中的纯文本链接替换为 `<mention-page>` 标签

  - 注意：SuperConductor 的引用疑似错误来源，需人工确认后才处理

1. **[E3] 类型修正（规则确认后执行）**

  - 修复类型：类型重分类

  - 候选条目：`obsidian-cli`、`skills-vetter`、`memory-lancedb-pro`、`total-recall`、`planktonXD`、`ClawBio`、`飞书官方 OpenClaw 插件`

  - 操作：`updatePage(url, { 类型: "entity" })`

  - **前提：需人工确认后再执行**（标注为需确认）

1. **[E4] 重复对处理**

  - 修复类型：重复合并

  - 目标：[Claude Code Dreaming](concepts/Claude Code Dreaming.md)（草稿）与 [Dreaming 记忆机制](concepts/Dreaming 记忆机制.md)（已审核）

  - 建议：将 Claude Code Dreaming 内容合并入 Dreaming 记忆机制 的「竞品对比」区块后归档，或保留为独立词条（如两者确属不同概念）

  - **前提：需人工确认是否合并**

### 👤 人工介入项

1. **[H1] 🚨 建立 Autofill Agent（引用升级员）批量处理纯文本引用**

  - 背景：草稿中纯文本引用 affected page rate = 37.5%（超过 30% 系统性阈值），估计 150~300+ 条受影响

  - 仅靠 Fixer 逐条处理需 30+ 轮，不现实

  - **建议操作**：创建专门的「引用升级员 Agent」，任务是：

    1. 读取 concept/entity 页面的纯文本引用

    1. 搜索对应 summary 页面

    1. 将纯文本替换为 `<mention-page>` 结构化链接

  - Fixer 手动批处理等效指令模板：

    ```javascript
搜索「[原文章名称]」对应的 summary 页面，将 [目标页面] 的「来源引用」区块中的 
「- 《文章标题》...」 替换为 「- <mention-page url="summary-url">文章标题</mention-page>」
    ```

1. **[H2] 标准标签体系审查**

  - 当前数据库实际使用标签已超出原始 14 个，包括 前端开发、多模态、AI 产品、RAG/检索、MCP 协议 等扩展标签

  - 建议：人工确认正式标签列表并更新 Lint Agent 和 Fixer 的检查规则

1. **[H3] SuperConductor 来源引用核查**

  - [SuperConductor](entities/SuperConductor.md) 的唯一 mention-page 来源（「用 Claude 替代彭博终端」）与其内容（macOS Coding Agent 管理工具）不匹配

  - 建议：人工核查并修正为正确来源

1. **[H4] 378 条过期草稿处理策略**

  - 当前草稿积压严重，需要决策：

    - 方案 A：先批量修复引用（H1），再批量晋升为审核中

    - 方案 B：设置草稿过期自动归档规则（>30天草稿自动标记为需更新）

    - 方案 C：优先处理 审核中 状态，草稿降低优先级

1. **[H5] Compiler Schema 一致性检查**

  - 部分草稿条目（如 SuperConductor）引用了无关来源，说明 Compiler 在批量处理时可能存在来源匹配错误

  - 建议：Compiler 团队审查批处理逻辑

---

>  请根据以上报告执行自动修复。
