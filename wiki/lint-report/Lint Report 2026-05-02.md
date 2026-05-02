---
title: Lint Report 2026-05-02
type: lint-report
tags:
- 知识管理
status: 草稿
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f6196a480a864d538bf0a8b4ac070f58
notion_id: f6196a48-0a86-4d53-8bf0-a8b4ac070f58
---

## 执行摘要

本报告由 Wiki Lint Agent 于 2026-05-02（Asia/Shanghai）自动生成，覆盖全库 concept / entity / summary / synthesis / qa 五种类型，共约 **4,622 条目**（不含 index 与 lint-report 自身）。

**核心结论：得分 44/100 🟡，本期最大问题为 4 对重复条目（-40 分），其次为 2 个确认孤岛（-10 分）与 2 个过期草稿（-6 分）。**

---

## 全库快照

| 类型 | 草稿 | 审核中 | 已审核 | 需更新 | 合计 |

| --- | --- | --- | --- | --- | --- |

| concept | 304 | 1,648 | 29 | 1 | 1,982 |

| entity | 177 | 831 | 5 | 0 | 1,013 |

| summary | 0 | 0 | 1,472 | 0 | 1,472 |

| synthesis | 0 | 43 | 108 | 0 | 151 |

| qa | 0 | 0 | 4 | 0 | 4 |

| **合计** | **481** | **2,522** | **1,618** | **1** | **4,622** |

所有 1,472 条 summary 已处于「已审核」，summary 层健康度优秀。concept + entity 共 2,995 条，其中草稿 481 条，最新批次来自 2026-05-02。

---

## 健康得分

**本期得分：44 / 100 🟡**

| 扣分项 | 数量 | 单项 | 小计 |

| --- | --- | --- | --- |

| 确认孤岛（无引用 + 无来源） | 2 | -5 | -10 |

| 过期草稿（≥7 天，缺来源引用） | 2 | -3 | -6 |

| 重复对（精确同名 + 中英近义） | 4 对 | -10 | -40 |

| 状态异常 | 0 | -5 | 0 |

| 废弃标签 | 0 | -2 | 0 |

| 过时内容（系统页豁免后） | 0 | -3 | 0 |

| **总扣分** |  |  | **-56** |

> 注：7 个疑似孤岛（仅标题初筛）暂不计入扣分，待 Fixer 验证后补录。

---

## 详细发现

### P0：精确同名重复（立即合并）

以下条目因 Wiki Compiler 疑似在同一时间段内重复触发，产生完全同名的 concept/entity 对。**应保留内容更完整者，删除另一个。**

**重复对 1 — Prompt Stack（concept）**

- [Prompt Stack](concepts/Prompt Stack.md) — 创建 2026-05-02 05:21:32Z，标签：提示工程，内容完整，来源引用齐全 ✅

- Prompt Stack — 创建 2026-05-02 05:20:50Z，标签：提示工程 / AI 设计，内容略简

- **建议：保留前者（内容更完整），删除后者**

**重复对 2 — Open Design（entity）**

- Open Design — 创建 2026-05-02 05:21:32Z，标签：AI 设计 / AI 产品

- [Open Design](entities/Open Design.md) — 创建 2026-05-02 05:20:48Z，标签：AI 设计 / 代码生成 / AI 产品（标签更完整）

- **建议：保留后者（标签更完整），删除前者**

---

### P0：中英文近义重复（确认后合并）

以下条目为同一概念的中英文版本，在同一 Wiki 中形成冗余知识节点。

**重复对 3 — Prompt Injection / 提示注入**

- Prompt Injection（concept，审核中，标签：Agent 安全 / 上下文管理 / AI 政策）

- [提示注入](concepts/提示注入.md)（concept，审核中，标签：Agent 安全）

- **建议：以「提示注入」为主条目，将 Prompt Injection 作为别名写入定义节，内容合并后删除英文版**

**重复对 4 — 反 AI-Slop 机制 / Anti-AI-Slop**

- 反 AI-Slop 机制（concept，草稿，标签：AI 设计 / 提示工程）

- [Anti-AI-Slop](concepts/Anti-AI-Slop.md)（concept，草稿，标签：AI 设计 / 提示工程，来源引用更完整）

- **建议：保留 Anti-AI-Slop（来源更清晰），将「反 AI-Slop 机制」作为中文别名写入并删除**

---

### P1：确认孤岛（补引用或人工复核）

以下 2 个条目经 loadPage 核查，「来源引用」章节完全为空，且无源文章 URL，无法追溯编译来源。内容本身完整，可能为手动创建或早期 Compiler 遗留。

- [画布式 Agent 编排](concepts/画布式 Agent 编排.md)（concept，草稿，2026-04-24，已 8 天，标签：多Agent协作 / Agent 协作模式）

- [Open Swarm](entities/Open Swarm.md)（entity，草稿，2026-04-24，已 8 天，标签：多Agent协作 / Agent 协作模式 / AI 产品）

**建议：补全来源引用后晋升「审核中」，或确认为独立知识节点并标注「手动创建」。**

疑似孤岛（标题初筛，待验证）

以下 7 个条目在全量 summary 标题扫描中无命中，疑似孤岛，建议 Fixer 进行 mention-page 内容核查后确认：

- [存在姿态三角形](concepts/存在姿态三角形.md)（concept，审核中）

- [梦境思考](concepts/梦境思考.md)（concept，审核中）

- [随机心跳机制](concepts/随机心跳机制.md)（concept，审核中）

- [XXYY](entities/XXYY.md)（entity，审核中）

- [读写分离控制面板](concepts/读写分离控制面板.md)（concept，审核中）

- [ZCT Momentum Filter](concepts/ZCT Momentum Filter.md)（concept，审核中）

- [GR4AD](entities/GR4AD.md)（entity，审核中）

---

### P1：过期草稿（≥7 天，缺来源引用）

全库 481 条草稿中，仅以下 2 条创建时间超过 7 天（截至 2026-05-02）。其余 479 条均为 2026-04-25 之后创建，尚在正常积压周期内。

| 条目 | 类型 | 创建日期 | 已积压 | 问题 |

| --- | --- | --- | --- | --- |

| [Untitled](concepts/画布式 Agent 编排.md) | concept | 2026-04-24 | 8 天 | 来源引用为空 |

| [Untitled](entities/Open Swarm.md) | entity | 2026-04-24 | 8 天 | 来源引用为空 |

---

### P2：类型启发式筛查（人工复核）

以下 concept 条目经启发式规则判断，**疑似应分类为 entity**，建议人工确认后更新类型字段。

**Rule A — 含版本号（产品/基准版本）：**

- [FSRS-6](concepts/FSRS-6.md)（concept → 疑似 entity）

- [ARC-AGI-3](concepts/ARC-AGI-3.md)（concept → 疑似 entity）

**Rule B — 含产品/协议后缀（Tool/SDK/Protocol/API）：**

- [Tool Registry](concepts/Tool Registry.md)（concept → 疑似 entity）

- [A2UI 协议](concepts/A2UI 协议.md)（concept → 疑似 entity）

**Rule C — 英文专有名词（基准/工具/平台）：**

- [SWE-bench](concepts/SWE-bench.md) · [SkillsBench](concepts/SkillsBench.md) · [GEO-bench](concepts/GEO-bench.md) · [pgvector](concepts/pgvector.md) · [Farside Investors](concepts/Farside Investors.md) · [LoopLM](concepts/LoopLM.md) · [Verse](concepts/Verse.md) · [Muon 优化器](concepts/Muon 优化器.md) · [menugen](concepts/menugen.md) · [AuditBench](concepts/AuditBench.md)

**Rule D — 全大写缩写产品名：**

- [SONA](concepts/SONA.md) · [DERP](concepts/DERP.md) · [ECL 管道](concepts/ECL 管道.md) · [TAOR 循环](concepts/TAOR 循环.md) · [APEX 多槽位编排器](concepts/APEX 多槽位编排器.md)

---

### P2：引用结构化检查（抽样 10 页）

对近期草稿进行分层抽样（2026-04-24 / 04-30 / 05-01 / 05-02 各时间段），结果如下：

- **8/10** 页包含规范的 `<mention-page>` 结构化引用 ✅

- **2/10** 页来源引用为空（即上述两个确认孤岛）

- 纯文本引用（无 mention-page）：0 条

- **结论：整体引用规范性良好，未触发系统性风险阈值（affected rate < 30%）**

---

## 标签分布（concept + entity，出现 ≥20 次）

| 标签 | 出现次数 |

| --- | --- |

| 商业/生态 | 184 |

| 知识管理 | 148 |

| OpenClaw | 56 |

| Harness 工程 | 42 |

| Agent 安全 | 33 |

| 推理优化 | 27 |

| 量化交易 | 25 |

| 模型评测 | 25 |

| 长期记忆 | 24 |

| 训练/微调 | 24 |

| Agent 协作模式 | 23 |

无废弃标签命中，无标签分布异常。

---

## 状态晋升建议

- **Summary → 无需操作**：1,472 条 summary 全部已处于「已审核」，本期无晋升动作。

- **草稿 → 审核中**：2 个过期草稿（画布式 Agent 编排、Open Swarm）内容完整但缺来源引用，**补引用后方可晋升**，不满足自动晋升条件，需人工介入。

- **审核中 → 需更新**：过时内容检查中，4 个系统说明页（关于 Wiki Compiler / Fixer / Gap Agent / QA Agent）compile_time 为 null，属豁免范畴，不触发「需更新」流转。

---

## 系统运行状态

- 触发方式：Recurrence Trigger（每 12 小时，14:00 Asia/Shanghai）

- 本次运行时间：2026-05-02 22:01 CST

- 执行阶段：Phase 1 SQL 全量扫描 ✅ · Phase 2 loadPage 抽样 ✅

- 豁免页面（compile_time = null）：[关于 Wiki Compiler](concepts/关于 Wiki Compiler.md) · [关于 Wiki Fixer](concepts/关于 Wiki Fixer.md) · [关于 Gap Agent](concepts/关于 Gap Agent.md) · [关于 Wiki QA Agent](concepts/关于 Wiki QA Agent.md)

---

>  请根据以上报告执行自动修复。优先处理 P0 重复合并（4 对），其次处理 P1 孤岛补引用（2 个确认 + 7 个疑似），最后进行 P2 类型启发式复核（15 个 concept 疑似应为 entity）。
