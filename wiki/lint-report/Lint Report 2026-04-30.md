---
title: Lint Report 2026-04-30
type: lint-report
tags:
- 知识管理
status: 草稿
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/80713e4aa00d4f32aeb3f27bbf8b95ef
notion_id: 80713e4a-a00d-4f32-aeb3-f27bbf8b95ef
---

## 检查日期

2026-04-30（北京时间 10:00 自动触发）

---

## 总体健康度

🔴 **0 / 100**（含废弃标签大规模迁移扣分）

🟡 **65 / 100**（内容质量参考分，排除架构迁移类废弃标签扣分）

> **说明**：本次标签系统新增 11 个退役标签（LLM、Agent 框架、Agent 编排等），导致 1582 个页面被标记为废弃标签用户。该问题属于**架构级 Schema 迁移**，应作为独立专项处理，不纳入常规内容质量评分。去除此项扣分后实际内容健康度为 65/100。

---

## 全库统计（类型 × 状态）

| 类型 | 草稿 | 审核中 | 已审核 | 需更新 | 合计 |

| --- | --- | --- | --- | --- | --- |

| concept | 434 | 1436 | 26 | 1 | **1897** |

| entity | 214 | 740 | 5 | 0 | **959** |

| summary | 0 | 0 | 1395 | 0 | **1395** |

| synthesis | 0 | 5 | 108 | 0 | **113** |

| qa | 0 | 0 | 4 | 0 | **4** |

| **合计** | **648** | **2181** | **1538** | **1** | **4368** |

---

## 孤岛条目

⚠️ **本次检测受技术限制，未能完成全量孤岛扫描。**

由于 `querySql` 不支持自连接，无法通过 SQL 精确检测哪些 concept/entity 未被任何 summary 的正文 `<mention-page>` 引用。以下为当前方法的局限与处理结果：

- **标题命中初筛**：已对大量 concept 名称与 summary 标题进行人工交叉比对，主流知名条目（OpenClaw、Claude、Hermes、Vibe Coding 等）均有对应 summary 收录，未发现明显孤岛

- **新增草稿条目**（create 时间 ≤ 7 天）：全部为本周新编译，通常尚未积累多个 summary 引用，不算孤岛

- **建议**：下次 Lint 运行时，考虑让 Fixer 或 Compiler 在 concept/entity 页面写入来源 summary URL，以便后续 SQL 反向查询

**本次孤岛扣分：0**（无法确认）

---

## 过期草稿（草稿状态 > 7 天）

共发现 **1** 个过期草稿：

| 页面 | 类型 | 创建时间 | 距今天数 |

| --- | --- | --- | --- |

| [Untitled](concepts/计算功能主义.md) | concept | 2026-04-22 | **8 天** |

> 内容完整（有定义、关键要点、来源引用），建议晋升为审核中。

---

## 过时内容（最后编译时间 > 30 天或为空）

共发现 **4** 个过时条目（编译时间为 null）：

| 页面 | 类型 | 最后编译时间 |

| --- | --- | --- |

| [Untitled](concepts/关于 Wiki Compiler.md) | concept | 空 |

| [Untitled](concepts/关于 Wiki Fixer.md) | concept | 空 |

| [Untitled](concepts/关于 Gap Agent.md) | concept | 空 |

| [Untitled](concepts/关于 Wiki QA Agent.md) | concept | 空 |

> 上述 4 页为「关于 xxx」系统说明页，名称与豁免名单（Gap Agent 等）不完全一致。建议人工确认是否归入豁免范围，或补充最后编译时间。

---

## 重复疑似

### A. concept/entity 完全同名重复

无。

### B. concept/entity 近似重复（归一化后相同）

共发现 **2** 对：

| 条目 A | 类型 | 状态 | 条目 B | 类型 | 状态 | 差异原因 |

| --- | --- | --- | --- | --- | --- | --- |

| [Untitled](entities/Hermes Agent.md) | entity | 已审核 | [Untitled](entities/Hermes.md) | entity | 草稿 | 同一产品，名称含/不含「Agent」后缀 |

| [Untitled](concepts/Agent OS.md) | concept | 已审核 | [Untitled](entities/AgentOS.md) | entity | 草稿 | 空格差异，且类型不一致 |

### A. summary 完全同名重复

无。

### B. summary 近似重复

以下为疑似同源多摘要（同一产品/事件的不同文章，非重复，仅供参考）：

- Agent Vault：2 篇 summary，来自不同帖子，内容角度有差异，不建议合并

- Anthropic 封杀 OpenClaw 系列：3 篇，各自独立视角，正常

**本次 summary 近似重复计分扣分：0**

---

## 状态异常

**0** 个页面状态为空/null。✅

---

## 标签异常

### 缺失标签

**0** 个 concept/entity 页面标签为空。✅

### 废弃标签使用

🚨 **严重：1582 个页面使用了已退役标签（需架构级迁移）**

废弃标签分为两类：

**早期废弃（3 个）：** AI Agent、MCP、Notion

**新退役（11 个）：** LLM、Agent 框架、Agent 编排、Agent 技能、Coding Agent、开发工具、工作流、记忆系统、安全/隐私、Crypto/DeFi、内容创作

涉及页面（查询命中，hasMore=true）中含大量高频标签，受影响估计：

- 「LLM」类：约 150+ 页

- 「Agent 编排」类：约 200+ 页

- 「Coding Agent」类：约 100+ 页

- 「开发工具」类：约 120+ 页

- 「工作流」类：约 150+ 页

- 「Crypto/DeFi」类：约 200+ 页

- 其余类别合计：约 600+ 页

> **注意**：新退役标签是在本次 Wiki Schema 规则更新后新增的，属于**批量架构迁移任务**，不适合由 Fixer 逐条修复。详见改进建议→人工介入项。

---

## 标签分布统计

（基于 concept+entity 数据库 Schema 中当前活跃标签）

| 活跃标签（3维体系） | 观察 |

| --- | --- |

| OpenClaw | 使用率高，核心场景标签 |

| Harness 工程 | 近期新增，使用率上升中 |

| 多Agent协作 / Agent 协作模式 | 双标签并存，待观察是否需合并 |

| RAG/检索、长期记忆、上下文管理 | 使用正常，分层清晰 |

| 量化交易 / 链上协议 / 加密资产 / 稳定币 | Crypto 细分标签已替代旧 Crypto/DeFi |

| AI 产品 / 商业/生态 | 通用标签，高频使用 |

> 详细标签计数需等待 Fixer 完成废弃标签迁移后重新统计。

---

## 类型启发式筛查结果

以下 concept 条目经推理层批量筛查，疑似应为 entity 类型（**建议人工确认**）：

| 条目名 | 当前类型 | 命中规则 | 理由 |

| --- | --- | --- | --- |

| [Untitled](entities/MTProto.md) | concept | 规则 B（Protocol） | Telegram 专有加密协议产品，具备特定产品属性 |

| [Untitled](entities/ERC-7710.md) | concept | 规则 B（Protocol/标准） | 以太坊改进提案编号，是特定标准文档，非通用概念 |

| [Untitled](entities/ERC-8004.md) | concept | 规则 B（Protocol/标准） | 同上，EIP 标准编号 |

| [Untitled](entities/Darwin Gödel Machine.md) | concept | 规则 C（英文专有名词） | 特定研究项目/系统名称，非通用算法概念 |

| [Untitled](entities/Smallville.md) | concept | 规则 C（英文专有名词） | Stanford 特定模拟实验项目，不是通用方法论 |

计分：本轮 5 个疑似，待人工确认后计分（每 3 个确认误分类扣 -3）。

---

## 标签分类合理性检查

**Phase 2 抽样（8 页）中未发现明显标签误分类。**

以下来自 Phase 1 数据的潜在问题：

- [GPU 加速终端](concepts/GPU 加速终端.md)（concept，标签：开发工具）：标签本身已退役；内容属典型开发基础设施，应换为新维度标签

- [LanceDB](entities/LanceDB.md)（concept，标签：记忆系统+开发工具）：LanceDB 是特定数据库产品，类型应为 entity，标签中「记忆系统」和「开发工具」均已退役

- 多个使用「内容创作」标签的 entity 条目（如 Pexo、Lovart、Nova）：内容创作已退役，应迁移为 AI 设计 / 内容自动化 / 图像生成 等具体标签

---

## 引用结构化检查

### 抽样统计

| 指标 | 数值 |

| --- | --- |

| 抽样页面数 | 8 |

| 含结构化 mention-page 的页面 | 8 (100%) |

| 含纯文本引用的页面 | 0 (0%) |

| 纯文本引用总数 | 0 |

| affected page rate | 0%（阈值 30%） |

| plain-text rate | 0%（阈值 20%） |

✅ **未触发系统性问题警报。** 当前 Compiler 输出的 concept/entity 引用均使用结构化 `<mention-page>`，引用质量良好。

### 抽样页面列表

| 页面 | 状态 | 引用类型 |

| --- | --- | --- |

| [Untitled](concepts/计算功能主义.md) | 草稿 | ✅ 结构化 |

| [Untitled](concepts/Spec and Verify.md) | 草稿 | ✅ 结构化 |

| [Untitled](concepts/Hermes Skills.md) | 草稿 | ✅ 结构化 |

| [Untitled](concepts/记忆漂移.md) | 草稿 | ✅ 结构化 |

| [Untitled](concepts/Agent 命令安全拦截.md) | 草稿 | ✅ 结构化 |

| [Untitled](concepts/Large Memory Model.md) | 草稿 | ✅ 结构化 |

| [Untitled](entities/SWE-agent.md) | 草稿 | ✅ 结构化 |

| [Untitled](concepts/ACT-R 激活模型.md) | 草稿 | ✅ 结构化 |

---

## 计分明细

| 检查项 | 发现数量 | 单项扣分 | 小计 |

| --- | --- | --- | --- |

| 孤岛条目 | 未确认（检测受限） | -5/个 | 0 |

| 过期草稿（>7天） | 1 | -3/个 | -3 |

| 过时内容（>30天或null） | 4 | -3/个 | -12 |

| 重复对（concept/entity） | 2 | -10/对 | -20 |

| 状态异常 | 0 | -2/个 | 0 |

| 缺失标签 | 0 | -2/个 | 0 |

| 废弃标签使用（架构迁移类） | 1582 页 | -5/个 | -7910（→ 最低 0） |

| 纯文本引用 | 0 | 0 |  |

| **内容质量参考分（排除架构迁移）** |  |  | **65 / 100 🟡** |

| **含架构迁移扣分总分** |  |  | **0 / 100 🔴** |

---

## 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 |

| --- | --- | --- | --- |

| [Untitled](concepts/计算功能主义.md) | 草稿 | 审核中 | 创建 8 天，有完整定义、关键要点、1 个 mention-page 来源引用 |

> 其他草稿条目（648 个）均为 7 天内新创建，暂不符合晋升标准。待下次 Lint 运行时重新评估。

---

## 改进建议

### 🤖 自动修复项

以下项目 Wiki Fixer 可直接执行：

1. **重复合并：Hermes Agent / Hermes**

  - 目标页：[Hermes](entities/Hermes.md)（草稿，新创建）

  - 操作：将 Hermes 草稿的有效内容合并至 [Hermes Agent](entities/Hermes Agent.md)（已审核），然后删除草稿重复页

1. **重复合并：Agent OS / AgentOS**

  - 目标页：[AgentOS](entities/AgentOS.md)（entity，草稿）

  - 操作：AgentOS 是特定产品（Anthropic 托管 Agent 服务），应为 entity 类型；而 [Agent OS](concepts/Agent OS.md) 是通用概念；两者性质不同，实际上**可能不是重复**——建议 Fixer 先阅读两页内容再判断，若确为不同内容则保留，若为同一产品则合并至 entity 版本

1. **状态晋升：计算功能主义 → 审核中**

  - 目标页：[计算功能主义](concepts/计算功能主义.md)

  - 操作：将状态从「草稿」改为「审核中」

1. **类型修正（5 个疑似 entity 的 concept）**

  - [MTProto](entities/MTProto.md)：concept → entity

  - [ERC-7710](entities/ERC-7710.md)：concept → entity（待确认）

  - [ERC-8004](entities/ERC-8004.md)：concept → entity（待确认）

  - [Darwin Gödel Machine](entities/Darwin Gödel Machine.md)：concept → entity（待确认）

  - [Smallville](entities/Smallville.md)：concept → entity（待确认）

1. **LanceDB 类型修正**

  - [LanceDB](entities/LanceDB.md)：当前为 concept，是具体数据库产品，应改为 entity

1. **过时内容处理**

  - 为 4 个「关于 Wiki…」页面（[关于 Wiki Compiler](concepts/关于 Wiki Compiler.md)、[关于 Wiki Fixer](concepts/关于 Wiki Fixer.md)、[关于 Gap Agent](concepts/关于 Gap Agent.md)、[关于 Wiki QA Agent](concepts/关于 Wiki QA Agent.md)）补填当前时间戳作为 最后编译时间

---

### 👤 人工介入项

1. **🚨 架构级标签迁移（最高优先级）**

  - 问题：1582 个页面使用已退役标签（LLM、Agent 框架、Agent 编排、Agent 技能、Coding Agent、开发工具、工作流、记忆系统、安全/隐私、Crypto/DeFi、内容创作）

  - 规模估计：约 1500+ 条需修改，远超 Fixer 逐条处理能力

  - **强烈建议**：建立专用 **标签迁移 Autofill Agent**，批量读取每个 concept/entity 的现有标签，按映射规则替换为新 3 维标签体系，并写回 Wiki 数据库

  - 迁移映射参考（需 Wiki Schema 规则文件 [Wiki Schema（规则文件）](index/Wiki Schema（规则文件）.md) 提供完整映射表）：

    - `LLM` → 按内容拆分为：推理优化 / 训练/微调 / 模型评测 / 多模态 / AI 产品

    - `Agent 框架` → 拆分为：Agent 协作模式 / Harness 工程 / AI 产品

    - `Agent 编排` → Agent 协作模式 / 多Agent协作

    - `Agent 技能` → Harness 工程 / Agent 协作模式

    - `Coding Agent` → 代码生成 / IDE 集成 / Harness 工程

    - `开发工具` → CLI 工具 / 模型部署 / 算力基础设施（视内容而定）

    - `工作流` → Agent 协作模式 / 内容自动化（视内容而定）

    - `记忆系统` → 长期记忆 / 上下文管理 / RAG/检索

    - `安全/隐私` → Agent 安全 / 身份准入

    - `Crypto/DeFi` → 链上协议 / 稳定币 / 加密资产 / 量化交易

    - `内容创作` → 内容自动化 / AI 设计 / 图像生成 / 社交媒体

1. **「关于 Wiki…」豁免规则确认**

  - 4 个过时 concept 页（关于 Wiki Compiler/Fixer/Gap Agent/QA Agent）名称与豁免名单不完全匹配

  - 请确认是否将这些页面加入豁免名单，或要求 Compiler 定期更新其编译时间

1. **多Agent协作 vs Agent 协作模式 双标签审查**

  - 目前两个活跃标签含义高度重叠，建议明确使用边界或合并为一个标签

  - 需要在 Wiki Schema 规则文件中补充「易混淆标签定义」

1. **孤岛检测系统化方案**

  - 当前 SQL 不支持自连接，无法精确检测孤岛。建议在 Compiler 写入 concept/entity 时，同步在页面属性中记录来源 summary URL（已有「源文章URL」字段），以支持后续精确孤岛检测

---

>  请根据以上报告执行自动修复。
