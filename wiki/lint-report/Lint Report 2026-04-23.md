---
title: Lint Report 2026-04-23
type: lint-report
tags:
- 知识管理
status: 草稿
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/ebab925824044d5a9c8689d21deccb9c
notion_id: ebab9258-2404-4d5a-9c86-89d21deccb9c
---

## 检查日期

2026-04-23（北京时间 10:00，定时任务触发）

## 总体健康度

🔴 **0 / 100**

主要拖分项：**412 条过期草稿**（-1236 分，封底 0）、**2 对疑似重复**（-20 分）、**引用结构化问题持续存在**（样本 affected rate = 25%，plain-text rate ≈ 20%，与前几次报告一致，尚未达到封底前清零）。

---

## 全库统计

| 类型 | 草稿 | 审核中 | 已审核 | 需更新 | 合计 |

| --- | --- | --- | --- | --- | --- |

| entity | 482 | 221 | 2 | 0 | **705** |

| synthesis | 6 | 69 | 0 | 0 | **75** |

| **合计** | **1582** | **641** | **1136** | **1** | **3360** |

（不含 index / lint-report 系统页）

---

## 孤岛条目

当前 summary 无 relation 字段指向 concept/entity，无法通过纯 SQL 精确检测 `<mention-page>` 结构化引用。

本次采用「标题命中初筛 + Notion search 二次验证」方法，对 Anti-996、planktonXD、File-as-Bus 等抽样条目均在 search 中发现对应 summary 引用，**未确认孤岛**。

建议：Compiler 在产出 summary 时强制通过 `<mention-page>` 回填 concept/entity，以便未来精确孤岛检测。

---

## 过期草稿（草稿且创建 > 7 天）

SQL 精确计数：**412 条** concept/entity 处于草稿状态，创建于 2026-04-16 之前。

| 批次 | 估计数量 | 说明 |

| --- | --- | --- |

| 2026-04-10 ~ 04-11 | ~150 条 | 建库首批，历史最久 |

| 2026-04-12 ~ 04-13 | ~80 条 | 第二批 Compiler 产出 |

| 2026-04-14 ~ 04-15 | ~80 条 | 第三批 |

| 2026-04-16（含当天截止） | ~102 条 | 距今恰好 7 天 |

示例条目（全部创建于 2026-04-11）：

- [SuperHQ](entities/SuperHQ.md)（entity, Agent 编排）

- [混合模型策略](concepts/混合模型策略.md)（concept, OpenClaw）

- [SESSION.md](concepts/SESSION.md.md)（concept, 知识管理）

- [CLI Harness](concepts/CLI Harness.md)（concept, CLI 工具）

- [Agent Drift](concepts/Agent Drift.md)（concept, Agent 技能）

> 注：412 条为 SQL 精确值，与 2026-04-22 报告（251 条）相比增加 161 条，系本周 Compiler 新增入库的草稿尚未完成状态晋升流程。

---

## 过时内容（最后编译时间 > 30 天或为 null）

**0 条**（不含豁免项）✅

全库 concept/entity 最后编译时间均在 2026-03-24 之后。7 个系统元 concept 页（「关于 Wiki Compiler」等，last_compiled = null）已按规则豁免。

---

## 重复疑似

### Concept/Entity 重复

**A. 完全同名重复：0 对** ✅

**B. 归一化近似重复：2 对**

| 页面 A | 页面 B | 差异原因 | 建议 |

| --- | --- | --- | --- |

| [Untitled](entities/llm-wiki.md)（entity） | [Untitled](entities/LLM Wiki v2.md)（entity） | 版本差异（Rule A），疑似同一产品 v1 和 v2 | 人工确认是否为同一仓库，是则合并 |

### Summary 重复

**A. 完全同名重复：0 组** ✅

**B. 近似同名重复：0 组** ✅

（前几次 Fixer 已完成批量清理，当前全库 1113 条 summary 名称唯一。）

---

## 状态异常

**0 条** ✅ 全库所有条目均已设置状态字段。

---

## 标签异常

- **标签缺失：0 条** ✅

- **废弃标签（AI Agent / MCP / Notion）：0 条** ✅

---

## 标签分布统计

以下数据基于查询结果估算，精确数值可通过 Dashboard「📊 concept+entity 标签分布」查看：

| 标签 | 估计条目数 | 备注 |

| --- | --- | --- |

| OpenClaw | ~220 | 正常 |

| 开发工具 | ~200 | 需关注是否含 AI Coding Agent 误入 |

| Crypto/DeFi | ~170 | 正常 |

| Agent 技能 | ~300 | 正常，包含大量 skill 类条目 |

| 内容创作 | ~120 | 正常 |

| LLM | ~250 | 注意 LLM 标签下不应有具体模型产品 concept |

| 商业/生态 | ~110 | 正常 |

---

## 类型启发式筛查结果

以下 concept 条目经推理层规则筛查，疑似应为 entity 类型，建议人工确认：

| 条目名称 | 命中规则 | 理由 | [Untitled](concepts/obsidian-cli.md) | Rule B（CLI 后缀） | 特定命令行工具，属于具体产品 |

| --- | --- | --- | --- | --- | --- |

| [Untitled](entities/memory-lancedb-pro.md) | Rule B（-pro 后缀）+ Rule C（专有名） | 特定 LanceDB 增强工具，属于具体产品 | [Untitled](entities/total-recall.md) | Rule C（英文专有名词） | 特定记忆工具，属于具体产品 |

| [Untitled](entities/planktonXD.md) | Rule C（英文专有名词） | 特定 Polymarket 交易账户/机器人，属实体 | [Untitled](concepts/VBench.md) | Rule C（英文专有名词） | 具体视频生成基准测试工具，属实体 |

| [Untitled](concepts/Clawer.md) | Rule C（英文专有名词） | 疑似特定爬虫/抓取产品 | [Untitled](entities/SOL-ExecBench.md) | Rule D（大写缩写+Bench） | 具体基准测试工具，属实体 |

| [Untitled](concepts/HyperMem.md) | Rule C（驼峰专有名词） | 疑似特定记忆系统产品 | [Untitled](concepts/TON MCP.md) | Rule B（产品级协议名） | 特定区块链 MCP 服务，属实体 |

*以上仅为「建议人工确认」，不自动判定。*

---

## 标签分类合理性检查（Phase 2 抽样）

本次 Phase 2 抽样 16 页，重点关注 **开发工具** 和 **LLM** 标签下的误分类：

- **开发工具** 中发现 `Jina Reader`（entity，标签含 Agent 技能 + 开发工具）→ 标签合理，Jina Reader 是 Agent 数据抓取工具，不是 AI Coding Agent

- **LLM** 中发现 `MoE 架构`（concept，推理优化）→ 合理，属于模型架构理论概念 ✅

- **LLM** 中 `GR4AD`（concept）→ 名称含 AD 缩写，需确认是否为具体产品

- **Coding Agent** 中所有抽样条目归类合理 ✅

**发现 1 条建议修正**：

- [GR4AD](concepts/GR4AD.md)（concept，标签 LLM）→ 需确认含义：若为具体推荐系统框架名，建议改为 entity

---

## 引用结构化检查

### 抽样统计

抽样规模：**16 页**（来自 2026-04-10 ~ 2026-04-11 早期批次，分层抽样）

| 页面 | 类型 | 状态 | mention-page 数 | 纯文本引用数 | 评估 |

| --- | --- | --- | --- | --- | --- |

| LLM 知识编译 | concept | 审核中 | 3 | 1（原文URL） | ⚠️ 混合 |

| 插件化架构 | concept | 审核中 | 2 | 0 | ✅ 结构化 |

| 多步骤研究规划 | concept | 审核中 | 1 | 0 | ✅ 结构化 |

| AI 自修改代码 | concept | 已审核 | 1 | 0 | ✅ 结构化 |

| CLI Harness | concept | 草稿 | 1 | 0 | ✅ 结构化 |

| MiniMax M2.5 | entity | 草稿 | 1 | 0 | ✅ 结构化 |

| Context Agent | concept | 草稿 | 0 | 1 | ❌ 纯文本 |

| 时间线监控 Agent | concept | 草稿 | 0 | 1 | ❌ 纯文本 |

**汇总指标**：

- Affected page rate（含纯文本的页面占比）：**4/16 = 25%**（接近 30% 阈值）

- Plain-text citation rate（纯文本引用/总引用数）：**6/30 ≈ 20%**（达到 20% 阈值）

### ⚠️ 接近系统性问题阈值

与前几次报告对比：

- 2026-04-20：affected rate = 50% → **🚨 系统性问题**

- 2026-04-22：~25–37%（根据报告推算）

- **2026-04-23（本次）：25%** → 有所改善，但 plain-text rate 仍处于 20% 阈值

本次不升级为 🚨，但此问题尚未解决。**若下次报告 affected rate 仍 ≥ 25%，建议优先推进引用升级员 Agent。**

**待修复页面（本次抽样中的纯文本引用页）**：

- [SESSION.md](concepts/SESSION.md.md)（2 条纯文本 URL，无对应 mention-page）

- [Context Agent](concepts/Context Agent.md)（1 条纯文本 URL）

- [SuperHQ](entities/SuperHQ.md)（2 条「未匹配」格式，需找到对应 summary）

- [时间线监控 Agent](concepts/时间线监控 Agent.md)（1 条纯文本 URL）

---

## 计分明细

| 检查项 | 发现数 | 单项扣分 | 小计 | 孤岛条目 | 0（抽样未确认） | -5/条 | 0 |

| --- | --- | --- | --- | --- | --- | --- | --- |

| 过期草稿（>7 天） | **412 条** | -3/条 | **-1236** | 过时内容（>30 天） | 0 | -3/条 | 0 |

| 疑似重复对（concept/entity） | 2 对 | -10/对 | -20 | 状态异常 | 0 | -2/条 | 0 |

| 标签缺失/空 | 0 | -2/条 | 0 | 废弃标签 | 0 | -5/条 | 0 |

| 纯文本引用（6 处） | 6 处 | -1/5处 | -1.2 | **合计** |  |  | **-1257.2 → 最低 0** |

**最终健康分：🔴 0 / 100**

---

## 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 | [Untitled](concepts/混合模型策略.md) | 草稿 | 审核中 | 创建 >7 天，定义 ✓，核心逻辑 ✓，1 个 mention-page 引用 ✓ |

| --- | --- | --- | --- | --- | --- | --- | --- |

| [Untitled](concepts/CLI Harness.md) | 草稿 | 审核中 | 创建 >7 天，定义 ✓，关键要点 ✓，1 个 mention-page 引用 ✓ | [Untitled](concepts/Agent Drift.md) | 草稿 | 审核中 | 创建 >7 天，定义 ✓，关键要点 ✓，1 个 mention-page 引用 ✓ |

| [Untitled](entities/MiniMax M2.5.md) | 草稿 | 审核中 | 创建 >7 天，定义 ✓，核心数据 ✓，1 个 mention-page 引用 ✓ | [Untitled](concepts/Agent OS.md) | 审核中 | 已审核 | 4 个来自不同 summary 的 mention-page 引用，多源交叉验证通过 |

| [Untitled](concepts/LLM 知识编译.md) | 审核中 | 已审核 | 3 篇不同 summary 的 mention-page 引用（Hermes+AutoCLI、Karpathy Wiki 方法论等），多源验证通过 | [Untitled](concepts/SESSION.md.md) | 草稿 | **暂缓** | 纯文本引用，需先完成引用结构化升级 |

| [Untitled](concepts/Context Agent.md) | 草稿 | **暂缓** | 纯文本引用，需先修复 | [Untitled](entities/SuperHQ.md) | 草稿 | **暂缓** | 「未匹配」引用格式，需先找到对应 summary |

> 注：412 条过期草稿中还有大量可晋升候选，建议 Fixer 按「创建时间升序、有 mention-page 引用」原则批量扫描晋升。

---

## 改进建议

### 🤖 自动修复项（Fixer 可直接执行）

1. **重复合并：File-as-Bus vs 文件即总线**

  - 修复类型：重复页面合并

  - 目标：[File-as-Bus](concepts/File-as-Bus.md) + 文件即总线

  - 操作：保留 File-as-Bus（内容更丰富），将「文件即总线」内容合并后删除，或在 File-as-Bus 的定义中添加中文别名

1. **引用结构化升级（4 条草稿纯文本引用）**

  - 修复类型：引用升级（纯文本 → mention-page）

  - 目标页面：[SESSION.md](http://session.md/)、Context Agent、SuperHQ、时间线监控 Agent

  - 操作：为每页查找「来源引用」段中的原文 URL，找到对应 summary 页面，将纯文本引用替换为 `<mention-page>` 链接

1. **状态晋升（4 条草稿 → 审核中）**

  - 修复类型：批量状态更新

  - 目标：混合模型策略（`https://www.notion.so/1530908058f246378df0d56550fd6fe9`）、CLI Harness（`https://www.notion.so/a00925f83b254b9e8e7a95445a21545e`）、Agent Drift（`https://www.notion.so/f69b5a7820f04a2ebb02fdc364466d40`）、MiniMax M2.5（`https://www.notion.so/bb112c94669e4eae9ade4a7d6402d6b4`）

  - 操作：将以上 4 条状态从「草稿」更新为「审核中」

1. **状态晋升（2 条审核中 → 已审核）**

  - 修复类型：多源验证晋升

  - 目标：Agent OS（`https://www.notion.so/231115259903408ca77760fd94041e1d`）、LLM 知识编译（`https://www.notion.so/a0b2ab8fea9c47eb9a9fec57a199157b`）

  - 操作：将以上 2 条状态更新为「已审核」

1. **过期草稿批量晋升（约 300+ 条引用结构化的草稿）**

  - 修复类型：批量状态更新（草稿 → 审核中）

  - 操作：对 412 条过期草稿，按创建时间升序，每批 30 条 loadPage 检查「来源引用」段，含 ≥1 个 mention-page 且定义非空者晋升为「审核中」。估计约 60–70% 可直接晋升（~250 条）。

### 👤 人工介入项（需人类确认）

1. **近似重复人工确认：llm-wiki vs LLM Wiki v2**

  - 请确认 `https://www.notion.so/e595dd16830d485290ffd625650b401f`（llm-wiki）和 `https://www.notion.so/78a045d56fc94358b2791a3e919b726b`（LLM Wiki v2）是否为同一 GitHub 仓库的不同版本。若是，则由 Fixer 合并保留 v2；若为不同项目，则标记为独立条目。

1. **类型误分类确认（9 条疑似 entity）**

  - 见「类型启发式筛查结果」章节，请人工确认 obsidian-cli、memory-lancedb-pro、total-recall、planktonXD、VBench、Clawer、SOL-ExecBench、HyperMem、TON MCP 是否需改为 entity 类型。

1. **过期草稿晋升策略确认**

  - 当前 412 条草稿导致健康分锁在 0。建议讨论：

    - 是否调整草稿阈值从 7 天改为 14 天？

    - 是否授权 Fixer 在本次修复中批量扫描全部 412 条并执行晋升？

1. **synthesis 草稿积压（6 条）处理方式**

  - 6 条 synthesis 处于草稿状态，69 条处于审核中（均未到已审核）。请确认是否需要 Synthesizer 重新审查并推进到已审核。

1. **引用升级员 Agent 建设**

  - 引用结构化问题持续存在（本次第 4 次报告仍有 25% affected rate）。历次 Fixer 手动处理进展有限（全库估计仍有 100+ 条纯文本引用）。建议正式立项 **Autofill Agent（引用升级员）**，专门批量处理「来源引用中纯文本 URL → mention-page」的转换任务。

---

>  请根据以上报告执行自动修复。
