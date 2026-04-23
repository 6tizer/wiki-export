---
title: 知识 Wiki 系统大升级：V2 设计决策与执行全记录
type: synthesis
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/5b1488a84d2e4a94b725ca25369f61d5
notion_id: 5b1488a8-4d2e-4a94-b725-ca25369f61d5
---

## 研究问题

知识 Wiki 在 700+ 条目、279+ concept 的规模下，如何通过标签体系重构、条目类型分离、Agent 架构精简和自动化链路修复，实现可持续的知识治理？

## 背景

2026-04-11，知识 Wiki 经历了一轮跨越 6 个对话的系统性大升级。升级前的主要问题：

- 标签体系 V1 区分度崩塌（AI Agent 覆盖 72% concept）

- concept 与 entity 混为一谈（产品/模型被当作概念管理）

- 8 个 Agent 中有 2 个已失去存在价值

- ~600 个 summary 的来源标签为空

- 系统文档与实际架构脱节

本页记录这轮升级的 **全部关键决策与执行结果**。

---

## 决策一：标签体系 V1 → V2

### V1 的 5 个问题

1. **「AI Agent」沦为万能标签** — 279 个 concept 中 200+ 个带此标签，等于没有分类

1. **缺少关键领域标签** — Coding Agent、安全/隐私、内容创作等无对应标签

1. **「开发工具」太宽泛** — CLI、IDE、框架、量化算法全混在一起

1. **标签顺序不一致导致分组碎片化** — ["AI Agent", "开发工具"]（34 个）vs ["开发工具", "AI Agent"]（7 个）

1. **MCP / Notion 标签几乎没人用** — MCP 仅 3-4 个，Notion 为 0

### V2 核心设计原则

- **移除隐含主题标签**：整个库都是 AI Agent 相关，标注无意义

- **按用户筛选维度拆分**：产品（框架）、方法论（编排）、能力（技能）

- **每个标签有明确边界**：避免覆盖范围重叠

- **每个 concept 只需 1-2 个标签**：减少组合爆炸

### V2 标签变更明细（13 → 14 个）

| 操作 | 标签 | 定义 |

| --- | --- | --- |

| 🗑️ 移除 | ~~AI Agent~~ | → 拆为 Agent 框架 / Agent 编排 / Agent 技能 |

| 🗑️ 移除 | ~~MCP~~ | → 归入 Agent 技能 |

| 🗑️ 移除 | ~~Notion~~ | 无 concept 使用 |

| 🆕 新增 | Agent 框架 | 具体 Agent 产品/平台/OS |

| 🆕 新增 | Agent 编排 | 驾驭 Agent 的方法论/架构模式 |

| 🆕 新增 | Agent 技能 | Agent 使用的 Skill/Plugin/工具链 |

| 🆕 新增 | Coding Agent | 代码生成/编程助手/AI IDE（后续补增） |

| 🆕 新增 | 安全/隐私 | Agent 安全、隐私计算、沙箱 |

| 🆕 新增 | 内容创作 | AI 视频/音乐/设计/动画 |

| 🆕 新增 | 商业/生态 | Agent 经济模型、市场、支付 |

| ✅ 保留 | LLM | 模型本身、训练、推理优化 |

| ✅ 保留 | 记忆系统 | Agent 记忆、上下文管理 |

| ✅ 保留 | OpenClaw | OpenClaw 生态专有 |

| ✅ 保留 | Crypto/DeFi | 链上 Agent、Web3 |

| ✅ 保留 | 知识管理 | 知识库、Wiki 方法论 |

| 🔄 收窄 | 开发工具 | 仅 IDE/CLI/基础设施（Coding Agent 类条目迁出） |

| 🔄 收窄 | 工作流 | 仅非 Agent 的自动化/变现 |

---

## 决策二：双层标签体系

**问题**：14 个一级标签提供了粗分类，但用户经常需要更精细的二级维度（如「这篇 Agent 技能的文章来自哪个数据源」「原文的细分标签是什么」）。

**设计**：

- **一级标签**：14 个 select 属性（粗分类，由 Compiler/Lint/Fixer 管理）

- **二级来源标签**：text 属性「来源标签」，值从源文章数据库的 multi_select 标签透传

- **透传机制**：Compiler 编译 summary 时，从源文章的「标签」multi_select 取值，逗号拼接后写入 summary 的「来源标签」text

**优势**：一级标签控制看板分组和筛选；二级标签保留源文章的细粒度分类信息，支持搜索和交叉分析。

---

## 决策三：entity 类型分离

**问题**：concept 类型定义为「可复用的抽象概念」，但大量条目实际是具体产品、模型、平台——它们不会被「综合分析」，只需作为实体档案存在。

**设计**：新增 `entity` 条目类型，定义为「具体产品/模型/平台/组织的实体档案」。

**迁移记录**：共 34 个 concept → entity：

- Agent 框架类产品（OpenClaw 生态产品等）

- LLM 模型类（MiMo-V2-Pro、MiniMax M2.5、Qwen3.5 ×2、Step 3.5 Flash、GLM-5-Turbo 等）

- 记忆系统产品（Mem0、Hindsight 等）

- 开发工具产品

- Crypto 平台

**影响**：

- Compiler 指令增加 concept vs entity 判断逻辑

- Lint 检查范围扩展到 entity（孤岛/重复/状态晋升）

- Fixer 修复范围包含 entity，新增 concept↔entity 类型迁移指令

- Synthesizer 读取范围增加 entity

- QA Agent 明确限制不创建 entity

- 系统工作流程图增加 entity 节点（B7）

---

## 决策四：Agent 架构精简（8 → 6）

**问题**：Wiki Batch Scheduler 和 Wiki Index Updater 两个 Agent 的职能已被其他机制覆盖：

- Scheduler 的调度职能 → Compiler/Lint/Synthesizer 各自独立 recurrence

- Index Updater 的索引维护 → 已归档 Index 导航页，Dashboard 替代

**执行**：

- 退役 Wiki Batch Scheduler：所有触发器已关闭

- 退役 Wiki Index Updater：所有触发器已关闭，Index 导航页已归档

- 清理 Lint 和 Synthesizer 的 interact Scheduler 权限

- Compiler 指令移除 Scheduler Signal 段落

- Schema Agent 职责表从 8 → 6 个 Agent

**当前 6 个活跃 Agent**：

1. **Wiki Compiler** — 独立 recurrence 每小时，编译源文章 → summary/concept/entity

1. **Wiki Lint Agent** — 独立 recurrence 每小时，检测标签/孤岛/重复/状态异常

1. **Wiki Fixer** — Lint 报告触发，自动修复 Lint 发现的问题

1. **Wiki Synthesizer** — 独立 recurrence，标签下 concept ≥10 时生成综合分析

1. **Wiki QA Agent** — 用户 mention 触发，基于 Wiki 回答问题并沉淀 qa 条目

1. **Notion AI** — 交互式协调者，兜底 Query 职责

---

## 决策五：存量一级标签修正

**问题**：V2 标签上线后，「开发工具」（128 个）和「LLM」（89 个）仍然过于庞大，内部混杂了应属于其他标签的条目。

**执行**：四轮共修正 167 个条目：

| 轮次 | 数量 | 主要操作 |

| --- | --- | --- |

| 第一轮 | 34 | 开发工具→Coding Agent 18 个 + LLM→记忆系统 5 个 + OpenClaw concept→entity 11 个 |

| 第二轮 | 39 | 开发工具深度清理：→Coding Agent 9、→Agent 技能 13、→Agent 框架/编排 4、→安全/隐私 3、→内容创作 2、→OpenClaw 4 |

| 第三轮 | 48 | 开发工具最终清洗：→Agent 编排 8、→Agent 技能 8、→Coding Agent 3、→知识管理 9、→内容创作 8、→LLM 4、→OpenClaw 3、→安全/隐私 2、→工作流 2 |

| 第四轮 | 23 | LLM 标签清洗：8 个 concept→entity + 15 个标签重分类 |

**结果**：开发工具 128→~42，LLM 89→~70。另发现 3 组重复待合并（Qwen 3.5/Qwen3.5、System Prompt 泄露 ×2、提示注入 ×2）。

**根因修复**：同步更新了所有 Agent 指令中的标签判断逻辑，防止 Compiler 继续错误打标。

---

## 决策六：来源标签回填

**问题**：~612 个已编译 summary 的「来源标签」text 属性为空（双层标签体系上线前编译的存量）。

**执行方法**：SQL JOIN 将 Wiki summary 标题（去除「摘要：」前缀）与源文章数据库标题精确匹配，从源文章的「标签」multi_select 取值，转为逗号分隔字符串写入。

**结果**：

- 精确标题匹配：307/307 可匹配 summary 全部回填完毕

  - 微信文章数据库源：98/100

  - X书签文章数据库源：209/207（含重复条目匹配）

- 剩余 ~307 个 summary 因标题被 Compiler 改写，无法精确匹配

**后续渐进策略（待执行）**：

| 阶段 | 策略 | 预期 |

| --- | --- | --- |

| D1 | 修改 Compiler 指令，编译时自动透传来源标签（止血） | 新增不再产生空值 |

| D2 | summary 增加「源文章URL」属性（铺路） | 后续 A 可纯 SQL |

| B | 关键词模糊匹配（LIKE '%keyword%'） | 命中 40-60% |

| A | 逐页 loadPage 提取内容中链接反向匹配 | 慢但精确 |

| (C) | 全量内容解析三维度匹配 | 仅在 A 残余时考虑 |

---

## 决策七：Wiki Schema 全面重写

将 Wiki Schema（规则文件） 从简单的属性定义升级为完整的系统宪法，新增：

- **条目类型定义**：summary / concept / entity / synthesis / qa / lint-report / index 七种类型的创建规则

- **对话产出分类规则**：定义什么样的对话产出应以什么形式沉淀

- **Query 流程**：Notion AI 的标准查询路径

- **Lint 流程**：Lint Agent 的检查清单

- **Agent 职责速查表**：与系统工作流程图一致的 6 Agent 速查

---

## 决策八：系统工作流程图 V2 更新

将 系统工作流程图 全面改写：

- 架构 mermaid 图：移除 Scheduler 和 Index Updater 节点，新增 entity（B7）节点

- Agent 总数从 7→5 个自动化角色 + Notion AI 交互式 = 6 个

- Agent 职责清单重写：匹配 Schema 中的速查表

- 自动化运行机制：3 个独立循环（Compiler / Lint→Fixer / Synthesizer）

- 已知问题段落：Scheduler 和 Index Updater 标记为已退役

- Compiler/Lint/Fixer/Synthesizer/QA Agent 职责全部补充 entity 相关逻辑

- Notion AI 增加兜底 Query 职责

---

## 关键发现

1. **标签体系的核心价值是区分度而非覆盖度** — 一个覆盖 72% concept 的标签等于没有标签

1. **concept 和 entity 的边界清晰化是知识库扩展的必要条件** — 当条目超过 500，类型混杂会导致 Synthesizer 和 Lint 产出质量下降

1. **Agent 数量不是越多越好** — 退役 2 个 Agent 后系统更简洁，触发链路更可靠

1. **存量治理比新增规则更耗时** — 标签修正 4 轮 167 个条目 + 来源回填 307 个，占升级总工作量的 60%+

1. **治本优先于治标** — D1（Compiler 指令修改）比 B/A/C（存量补救）更重要，否则新增永远在产生新问题

1. **Schema 是系统的宪法** — 所有 Agent 指令和工作流程图都应从 Schema 派生，而非独立维护

## 来源列表

- Wiki Schema（规则文件）：系统宪法，标签+类型+流程的权威定义

- 系统工作流程图：Agent 架构与自动化运行机制

- Untitled：编译器指令（含来源标签透传、entity 判断）

- Untitled：标签异常+entity 检测

- Untitled：自动修复（含 concept↔entity 迁移）

- Untitled：主题聚集+跨标签交叉分析

## 后续行动

1. **来源标签回填剩余 ~307 个**：按 D1+D2 → B → A → (C) 渐进策略执行

1. **重复条目合并**：Qwen 3.5/Qwen3.5、System Prompt 泄露 ×2、提示注入 ×2

1. **存量 Coding Agent 条目重打标**：待 Phase 3 完成

1. **持续观察 Lint 报告**：验证新体系下标签碎片化和孤岛问题是否消失
