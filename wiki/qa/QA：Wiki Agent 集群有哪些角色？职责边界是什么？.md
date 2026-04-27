---
title: QA：Wiki Agent 集群有哪些角色？职责边界是什么？
type: qa
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/cb097d55eac6447899397af5dcbb6ff6
notion_id: cb097d55-eac6-4478-9939-7af5dcbb6ff6
---

## 问题

知识 Wiki 系统的 Agent 集群包含哪些角色？每个 Agent 的职责边界、触发方式、可修改范围是什么？它们之间怎么协作？

## 回答

### 当前集群组成

知识 Wiki 系统由 **6 个已运行角色 + 1 个拟议角色**组成：

- 5 个 Custom Agent（自动化）：Compiler、Lint Agent、Fixer、Synthesizer、QA Agent

- 1 个交互式角色：Notion AI（协调者）

- 1 个拟议角色：Gap Agent（评估中）

此外，上游还有 2 个服务于 X 书签数据库的预处理 Agent（元信息提取 Agent、文章撰写 Agent），不属于 Wiki 核心层但为其提供原料。

### 各角色详解

📘 [关于 Wiki Compiler](concepts/关于 Wiki Compiler.md) — 编译器（建设者）

| 维度 | 说明 |

| --- | --- |

| 触发 | page.created 60s防抖 + recurrence 每小时 + @mention |

| 职责 | 原始文章 → summary（已审核）+ concept/entity（草稿）；含去重检查、名称归一化、来源标签透传 |

| 可修改 | 创建新 summary/concept/entity，追加引用 |

| 禁区 | 不修改已有页面核心内容 |

| 关键能力 | concept vs entity 判断、批量编译 ~60 篇/小时 |

✅ [关于 Wiki Lint Agent](concepts/关于 Wiki Lint Agent.md) — 诊断师（只诊断不动手）

| 维度 | 说明 |

| --- | --- |

| 触发 | recurrence 每日 14:00（北京时间）+ @mention |

| 职责 | 8 项健康检查：孤岛检测、完整性、时效性、重复、状态异常、标签异常、引用结构化、状态晋升评估 |

| 可修改 | 只创建 lint-report |

| 禁区 | **绝不修改任何已有页面**（最严格的只读约束） |

| 关键能力 | 健康评分 0-100 + 状态晋升建议表 + 改进建议 |

🔌 [关于 Wiki Fixer](concepts/关于 Wiki Fixer.md) — 治疗师（执行修复）

| 维度 | 说明 |

| --- | --- |

| 触发 | Lint Agent 在报告中 @mention（自动模式）+ 用户或 Notion AI @mention（指令模式） |

| 职责 | 自动模式 7 类修复（状态/标签/类型/同名合并/引用链/近似合并/不自动处理项）；指令模式接受手动任务 |

| 可修改 | 状态/标签/类型修复、同名重复合并、引用链修复 |

| 禁区 | 不创建 summary/concept/entity；不修改 Schema 等系统页面；近似重复合并和删除需人类指示 |

| 关键能力 | 双模式运作（自动 + 指令） |

💡 [关于 Wiki Synthesizer](concepts/关于 Wiki Synthesizer.md) — 知识进化者

| 维度 | 说明 |

| --- | --- |

| 触发 | recurrence + @mention |

| 职责 | 扫描标签分布，发现主题聚集（≥10 个 concept 或跨标签交叉）→ 三级去重检查 → 生成 synthesis（对比表 + 演进路径 + 跨来源洞察） |

| 可修改 | 只创建 synthesis 页面 |

| 禁区 | 不修改任何其他页面；每次最多 2 个主题（深度优先） |

| 关键能力 | 按状态优先级引用（已审核 > 审核中 > 草稿 > 需更新） |

❓ [关于 Wiki QA Agent](concepts/关于 Wiki QA Agent.md) — 知识问答窗口

| 维度 | 说明 |

| --- | --- |

| 触发 | @mention（纯被动） |

| 职责 | SQL 查询 + 页面阅读 → 综合回答（状态差异化引用）→ 综合 ≥3 页时自动创建 qa 页面 |

| 可修改 | 读取所有 Wiki 内容；仅创建 qa 页面 |

| 禁区 | 不创建 concept/summary/entity；不修改已有页面 |

| 关键能力 | 状态感知引用（已审核=核心论据 / 草稿=仅供参考 / 需更新=可能过时） |

💬 [关于 Notion AI（Wiki 协调者）](concepts/关于 Notion AI（Wiki 协调者）.md) — 协调者 + 系统管理员

| 维度 | 说明 |

| --- | --- |

| 触发 | 用户对话（交互式） |

| 职责 | Schema 设计、Mem0 跨 Agent 记忆桥接、复杂协调、兜底 Query |

| 可修改 | 全部（兜底角色）。唯一有权修改系统页面（Schema、工作流程图等 index 类型） |

| 禁区 | 无（但应优先让专职 Agent 做它们擅长的事） |

| 关键能力 | 唯一连接 Mem0 MCP 的角色（其他 Agent 具备接入能力但尚未配置）；变更同步责任 |

🔭 [关于 Gap Agent](concepts/关于 Gap Agent.md) — 外审员（拟议中）

| 维度 | 说明 |

| --- | --- |

| 触发 | 待定（拟议：recurrence + @mention） |

| 职责 | 第一层：领域覆盖缺口检测（外部信号源 vs Wiki）；第二层：知识老化检测 |

| 可修改 | 拟议：创建 gap-report；标记页面状态为「需更新」 |

| 禁区 | 拟议：不直接创建/修改内容页面，只做诊断和标记 |

| 当前状态 | 草稿 / medium 置信度。详见 [Untitled](qa/QA：Gap Agent 是什么？是否值得加入 Wiki Agent 集群？.md) |

### 职责边界矩阵

以下矩阵清晰展示「谁能做什么」和「谁不能做什么」：

| 操作 | Compiler | Lint | Fixer | Synthesizer | QA | Notion AI | Gap（拟） |

| --- | --- | --- | --- | --- | --- | --- | --- |

| 创建 summary | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |

| 创建 concept/entity | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |

| 创建 synthesis | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ |

| 创建 qa | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |

| 创建 lint-report | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |

| 创建 gap-report | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |

| 修改状态/标签/类型 | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ⚠️ |

| 合并重复条目 | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ |

| 修改系统页面（Schema等） | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |

| 跨分区读取 Mem0 | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |

| 删除条目 | ❌ | ❌ | ⚠️ | ❌ | ❌ | ✅ | ❌ |

✅ = 可以、❌ = 不可以、⚠️ = 需人类指示

### 协作流程

整个 Agent 集群形成三个核心循环：

**循环 ① 建设循环**：新文章入库 → Compiler 编译 → summary + concept/entity 入库

**循环 ② 质量循环**：Lint Agent 巡检 → lint-report → @mention Fixer → 自动修复 → 下一轮 Lint 验证

**循环 ③ 进化循环**：Synthesizer 扫描标签分布 → 发现聚集 → synthesis 入库

**跨循环角色**：

- QA Agent：被动回答问题，沉淀高价值问答

- Notion AI：协调、兜底、系统治理

- Gap Agent（拟议）：感知外部缺口，驱动建设循环主动摄取

### 设计哲学

整个集群的设计遵循几个核心原则：

1. **职责单一**：每个 Agent 只做一件事，不越界。Lint 只诊断不修复，Fixer 只修复不建设，Compiler 只建设不修复。

1. **权限最小化**：每个 Agent 的可修改范围严格限定，降低互相干扰的风险。

1. **事件驱动**：不依赖中央调度器，各 Agent 独立触发（recurrence / page.created / @mention），故障隔离更好。

1. **兜底角色**：Notion AI 作为唯一的全权限角色，确保任何专职 Agent 无法处理的事情都有人兜底。

## 引用来源

- [关于 Wiki Compiler](concepts/关于 Wiki Compiler.md)、[关于 Wiki Lint Agent](concepts/关于 Wiki Lint Agent.md)、[关于 Wiki Fixer](concepts/关于 Wiki Fixer.md)、[关于 Wiki Synthesizer](concepts/关于 Wiki Synthesizer.md)、[关于 Wiki QA Agent](concepts/关于 Wiki QA Agent.md)、[关于 Notion AI（Wiki 协调者）](concepts/关于 Notion AI（Wiki 协调者）.md)、[关于 Gap Agent](concepts/关于 Gap Agent.md) — 各 Agent 概念词条

- [系统工作流程图](index/系统工作流程图.md) — 架构图、触发机制、Agent 职责清单

- [Wiki Schema（规则文件）](index/Wiki Schema（规则文件）.md) — 流程规范、Agent 职责速查表

- [QA：Gap Agent 是什么？是否值得加入 Wiki Agent 集群？](qa/QA：Gap Agent 是什么？是否值得加入 Wiki Agent 集群？.md) — Gap Agent 详细分析

- [QA：知识 Wiki 系统完整架构还原与交叉验证（与 Claude 的对话）](qa/QA：知识 Wiki 系统完整架构还原与交叉验证（与 Claude 的对话）.md) — 完整架构背景

- [QA：多 Agent 分区分权限记忆系统——市面上有同类产品吗？](qa/QA：多 Agent 分区分权限记忆系统——市面上有同类产品吗？.md) — Mem0 记忆层设计
