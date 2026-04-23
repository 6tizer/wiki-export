---
title: AI Agent 开发工具链全景：从协议标准到技能市场的能力获取路径演进
type: synthesis
tags:
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-10'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/175a3009f1b448898acd9e2f9d752267
notion_id: 175a3009-f1b4-4889-8acd-9e2f9d752267
---

## 研究问题

AI Agent 如何获得与外部世界交互的能力？从底层协议到上层技能市场，开发工具链经历了怎样的分层演进？不同层级的工具之间存在哪些竞争与互补关系？对 Tizer 的 OpenClaw 工作流有何实操启示？

## 综合分析

### 一、工具链四层架构：从连通到替代

跨越 33 个概念页面，可以清晰识别出 AI Agent 开发工具链的**四层架构**，每一层解决不同层次的问题：

| **层级** | **解决的问题** | **代表项目** | **成熟度** |

| --- | --- | --- | --- |

| L1 协议层 | AI 能连接什么？ | MCP 协议、A2UI、Tool Calling 2.0 | ⭐⭐⭐⭐ 快速收敛 |

| L2 接口层 | AI 怎么调用？ | CLI-Anything、钉钉 CLI、飞书 CLI、Claude Code Channels | ⭐⭐⭐ 活跃竞争 |

| L3 技能层 | AI 知道怎么用？ | Claude Cowork Skills、Playwright Skill、Apify Agent Skills、Scrapling | ⭐⭐⭐ 快速增长 |

| L4 平台层 | AI 能替代什么？ | Knowledge Work Plugins、Plugin Marketplace、Dify、Symphony | ⭐⭐ 早期探索 |

这四层之间存在**自下而上的依赖关系**：没有 MCP 的连通性，就没有 Skills 的执行力；没有 Skills 的经验沉淀，就没有 Plugin 的替代能力。

### 二、接口范式之争：MCP vs CLI vs Computer Use

Agent 获取外部能力的方式正经历一场**三路线并行**的竞争：

| **维度** | **MCP 协议** | **CLI 原生** | **Computer Use** |

| --- | --- | --- | --- |

| 交互方式 | JSON-RPC 标准协议 | 命令行直接调用 | 鼠标键盘屏幕操作 |

| 代表项目 | MCP 协议、Apify MCP Server | 钉钉 CLI、飞书 CLI、CLI-Anything | Claude Computer Use |

| 优势 | 标准化程度高、生态最广 | 覆盖 API 最全、Agent 原生设计 | 万能兜底、无需适配 |

| 劣势 | 只解决连通性、不含使用知识 | 需逐一适配、生态碎片化 | 速度慢、不稳定、仅 macOS |

| 适用场景 | 通用工具连接 | 企业协作平台深度集成 | 无 API 的遗留软件 |

值得注意的趋势：**钉钉和飞书同时选择了 CLI 路线而非 MCP**，其理由是 CLI 更贴近 Agent 的自然调用方式，且能覆盖平台全部 API 端点（飞书 CLI 覆盖 2500+ OpenAPI）。CLI-Anything 则从学术角度验证了「一条命令将任意软件转为 Agent 工具」的可行性。

三条路线并非互斥，而是形成**优先级瀑布**：优先用 MCP/CLI 的 API 方式 → 没有 API 时才用 Computer Use 兜底。

### 三、技能生态的两条演进路径

在 L3 技能层，出现了两条截然不同的演进路径：

**路径 A：垂直深耕型** — 针对特定能力打造专精技能

- [Playwright Skill](concepts/Playwright Skill.md)：浏览器自动化，解决 JS 渲染页面抓取

- [Scrapling](entities/Scrapling.md)：反反爬框架，三层抓取模式 + 自适应解析

- [Apify Agent Skills](concepts/Apify Agent Skills.md)：12 个预制数据采集技能，按结果付费

- [Pexo](entities/Pexo.md) / [LibTV](entities/LibTV.md)：AI 视频生成技能

**路径 B：平台整合型** — 将多技能组合为完整解决方案

- [Knowledge Work Plugins](concepts/Knowledge Work Plugins.md)：Skills + Connectors + Slash Commands + Sub-Agents 四合一

- [Dify](entities/Dify.md)：插件市场 120+ 插件，模型/工具/Agent 策略解耦

- [Plugin Marketplace](concepts/Plugin Marketplace.md)：类 App Store 模式，开放第三方开发

两条路径的关系是：**垂直技能是平台整合的原材料**。Anthropic 的演进路线 MCP → Skills → Plugin 清晰地展示了这一点。

### 四、AI 编程范式的三代演进

在开发者工具领域，AI 编程范式经历了明显的代际演进：

| **代际** | **范式** | **代表工具** | **人的角色** |

| --- | --- | --- | --- |

| 第一代 | Copilot 补全 | GitHub Copilot | 写代码，AI 补全 |

| 第二代 | Vibe Coding / Vibe Design | Claude Code、Cursor、Stitch 2.0 | 描述需求，AI 写代码 |

| 第三代 | 规范驱动开发 SDD | OpenSpec、BMAD Method、Symphony | 定义规范，AI 自主执行和验证 |

第三代的核心突破在于：**人从「写代码」退到「定义规范和审批结果」**。Symphony 的「工作证明机制」尤其值得关注——Agent 提交代码时必须附上 CI 结果、PR review 反馈和复杂度分析，人只需要看报告做审批。

[AI 自修改代码](concepts/AI 自修改代码.md) 则代表了更极端的方向：AI 不仅写代码，还能修改自己的代码，实现自我进化。NanoClaw 的案例表明，在 AI 时代，DRY 原则可能过时——适度代码重复反而成为有效的物理隔离。

### 五、安全与信任基础设施

随着 Agent 能力的增强，安全问题从可选项变为必选项：

- **执行隔离**：[AI 沙箱](concepts/AI 沙箱.md)（Session 级 / 代码执行级 / 网络级三层隔离）

- **操作安全**：钉钉 CLI 的 `--dry-run` 预览 + 批量熔断、飞书 CLI 的 `--as` 身份切换

- **数据主权**：[DataClaw](entities/DataClaw.md) 让开发者掌控 AI 编程对话数据

- **事件去重**：[Webhook 幂等性](concepts/Webhook 幂等性.md) 防止重复处理

- **Tool Calling 2.0 的沙箱挑战**：从 JSON 到可执行代码，调试难度呈指数级上升

## 关键发现

1. **协议层正在收敛，接口层正在分裂**。MCP 在协议层已取得事实标准地位，但在接口层，CLI 路线正在挑战 MCP 的统治——钉钉和飞书的集体转向不是偶然，而是因为 CLI 天然更适合 Agent 的命令式调用模式。这意味着未来 Agent 工具链可能是「MCP 做标准 + CLI 做接口」的混合架构。

1. **「给 AI 的知识」正在成为独立资产类别**。Claude Cowork Skills 的核心洞察是：文档是给人看的，Skills 是给 AI 用的。这个区分催生了一个全新的内容类别——不是代码、不是文档、不是配置，而是「AI 可读的结构化工作经验」。谁能最快地将领域经验转化为 Skills，谁就在 Agent 时代占据先发优势。

1. **开发者工具正从「赋能开发者」转向「赋能 Agent」**。传统开发工具（IDE、CLI、SDK）的目标用户是人类开发者；新一代工具（CLI-Anything、钉钉 CLI 的 `--yes` 参数、OpenFang 的 Hands 机制）的目标用户是 AI Agent。这一范式转变意味着工具设计的核心指标从「人类易用性」变为「AI 可调用性」。

1. **「兜底方案」的战略价值被低估**。Computer Use 看似粗暴（鼠标键盘操作），但它是唯一能覆盖所有软件的方案；Scrapling 的三层抓取模式（普通 → 动态 → 反反爬）本质也是逐级兜底。在 Agent 工具链设计中，「优雅方案 + 兜底方案」的组合比单一路线更具鲁棒性。

1. **AI 编程的质量瓶颈已从「模型能力」转移到「输入规范质量」**。规范驱动开发（SDD）的兴起（OpenSpec 27K⭐、BMAD 37.5K⭐）和 Symphony 的工作证明机制表明：当前 AI 编程的天花板不是 LLM 写不好代码，而是人类给不出好规范。这与 Tizer 的 HITL 工作流哲学高度一致。

## 来源列表

### 概念页面（29 篇）

[MCP 协议](concepts/MCP 协议.md) · [A2UI 协议](concepts/A2UI 协议.md) · [Tool Calling 2.0](entities/Tool Calling 2.0.md) · [CLI-Anything](entities/CLI-Anything.md) · [钉钉 CLI](entities/钉钉 CLI.md) · [飞书 CLI](entities/飞书 CLI.md) · [Claude Code Channels](concepts/Claude Code Channels.md) · [Claude Cowork Skills](concepts/Claude Cowork Skills.md) · [Knowledge Work Plugins](concepts/Knowledge Work Plugins.md) · [Plugin Marketplace](concepts/Plugin Marketplace.md) · [Apify Agent Skills](concepts/Apify Agent Skills.md) · [Playwright Skill](concepts/Playwright Skill.md) · [Scrapling](entities/Scrapling.md) · [OpenFang](entities/OpenFang.md) · [CoPaw](entities/CoPaw.md) · [Dify](entities/Dify.md) · [Symphony](concepts/Symphony.md) · Computer Use · [Generative UI](concepts/Generative UI.md) · [Jina Reader](entities/Jina Reader.md) · [AI 沙箱](concepts/AI 沙箱.md) · [AI 自修改代码](concepts/AI 自修改代码.md) · [规范驱动开发 SDD](concepts/规范驱动开发 SDD.md) · [BMAD Method](concepts/BMAD Method.md) · [Vibe Design](concepts/Vibe Design.md) · [DataClaw](entities/DataClaw.md) · [Webhook 幂等性](concepts/Webhook 幂等性.md) · [Pexo](entities/Pexo.md) · [LibTV](entities/LibTV.md)

### 摘要页面（5 篇）

[摘要：Claw-code：一个人用AI，8小时重写Claude Code](summaries/摘要：Claw-code：一个人用AI，8小时重写Claude Code.md) · [摘要：Claude Code 开源编译版来了！45+实验功能全开，隐私无遥测，开发者终于等到了](summaries/摘要：Claude Code 开源编译版来了！45+实验功能全开，隐私无遥测，开发者终于等到了.md) · [摘要：Claude Code 51万行代码泄露，Anthropic为什么不慌？顶级团队的"不怕"哲学](summaries/摘要：Claude Code 51万行代码泄露，Anthropic为什么不慌？顶级团队的不怕哲学.md) · [摘要：Rust 实现的 tect-brain 大更新：增加了 GitHub Trending & mcp 能力，交互体验大幅上升](summaries/摘要：Rust 实现的 tect-brain 大更新：增加了 GitHub Trending & mcp 能力，交互体验大幅上升.md) · [摘要：7天用Claude+Codex实现谷歌 TurboQuant 算法（已开源）](summaries/摘要：7天用Claude+Codex实现谷歌 TurboQuant 算法（已开源）.md)

## 行动建议

1. **为 OpenClaw 构建 CLI 接口层**。钉钉和飞书的 CLI 实践证明，CLI 是 Agent 最自然的调用方式。建议参考飞书 CLI 的三层架构（Shortcuts → API Commands → Raw API），为 OpenClaw 的核心 Skill 提供 CLI 封装，使其他 Agent（如 Claude Code）能直接通过命令行调用 OpenClaw 能力。

1. **将现有工作流经验转化为 Skills 格式**。Tizer 在 HITL 工作流、内容管道、知识编译等方面积累了大量隐性经验。参照 Claude Cowork Skills 的思路，将这些经验结构化为「AI 可读的工作流 Skill 文件」，不仅提升自身工作效率，还可通过 ClawHub 分享给社区。

1. **在 Agent 工具链中实施「优雅 + 兜底」双路线策略**。具体做法：数据采集优先用 Apify Skills / Scrapling（结构化、稳定），兜底用 Playwright Skill / Computer Use（万能但慢）；外部平台集成优先用 MCP/CLI（标准化），兜底用 Computer Use（无 API 场景）。这种分层策略能最大化工具链的鲁棒性。
