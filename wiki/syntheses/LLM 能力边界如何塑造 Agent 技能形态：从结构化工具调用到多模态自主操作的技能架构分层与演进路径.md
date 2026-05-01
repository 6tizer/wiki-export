---
title: LLM 能力边界如何塑造 Agent 技能形态：从结构化工具调用到多模态自主操作的技能架构分层与演进路径
type: synthesis
tags: []
status: 已审核
confidence: high
last_compiled: '2026-04-19'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/fb9c9c53e2a4499dbc7a0cb799592f68
notion_id: fb9c9c53-e2a4-499d-bc7a-0cb799592f68
---

## 研究问题

**LLM 的架构能力与接口设计如何从根本上决定 Agent 技能的形态？从最基础的 JSON 工具调用到多模态视觉-语言-动作模型，Agent 技能经历了怎样的架构分层演进？不同层级的技能范式各自面临哪些工程瓶颈与选型权衡？**

本篇从 9 个「Agent 技能 × LLM」交叉标签概念和相关单标签材料中，提取 LLM 能力与 Agent 技能设计之间的共演关系，揭示技能架构从「模型外挂工具」向「模型内生能力」演进的底层逻辑。

## 综合分析

### 一、Agent 技能的三层架构光谱

从所有概念材料中，可以归纳出 Agent 技能相对于 LLM 的三种架构层级：

| **层级** | **技能形态** | **LLM 角色** | **代表概念** | **核心瓶颈** |

| --- | --- | --- | --- | --- |

| **L1：结构化调用层** | LLM 输出 JSON 请求 → 外部执行器调用工具 | 路由器（决定调什么） | Tool Calling、Chat Template、MCP 协议 | 参数准确率、上下文成本 |

| **L2：编程执行层** | LLM 输出可执行代码 → 沙箱批量处理 | 程序员（写代码执行） | Tool Calling 2.0（Programmatic Tool Calling） | 沙箱安全、调试复杂度 |

| **L3：多模态操作层** | LLM 直接感知环境 → 生成操作动作 | 操作者（看+想+做） | GUI-VLA、Agentic Vision、Mano-Action | 训练数据、实时性、鲁棒性 |

> **跨概念发现**：从 L1 到 L3，LLM 的角色从「调度中枢」向「执行主体」迁移。每一次层级跃迁都意味着 LLM 需要内化更多的环境理解能力，同时技能定义从「外部接口描述」转向「模型内在能力训练」。这不是简单的替代关系——高层级技能依赖低层级作为后备和补充。

### 二、L1 → L2 的跃迁：从 JSON 路由到代码执行

[Tool Calling](concepts/Tool Calling.md) 建立了 Agent 连接外部世界的基础范式：模型输出结构化请求，外部执行器调用真实工具，结果返回上下文。这个机制看似简单，但 [Chat Template](concepts/Chat Template.md) 揭示了其脆弱性——模板层对消息格式的假设一旦过窄，就会导致工具结果丢失或循环调用等「幽灵 Bug」。

[Tool Calling 2.0](entities/Tool Calling 2.0.md) 通过四大特性实现了质的跃迁：

| **特性** | **机制** | **效果** | **工程代价** |

| --- | --- | --- | --- |

| **Programmatic Tool Calling** | 模型输出代码而非 JSON，沙箱执行 | Token 减少 30%-50% | 沙箱隔离要求升级 |

| **Dynamic Filtering** | 代码过滤层插入网页抓取与上下文之间 | Token 平均降低 24% | 过滤逻辑可能误删关键信息 |

| **Tool Search** | 延迟加载，核心工具约 500 Token，其余按需 | 上下文优化最高 80% | 工具发现延迟增加 |

| **Tool Use Examples** | 工具定义中加入 Few-Shot 示范 | 复杂参数准确率 72%→90% | 工具描述体积膨胀 |

这四个特性的共同方向是：**让 LLM 从「被动路由」转向「主动编排」**。模型不再只是选择调用哪个工具，而是自己编写编排逻辑——这模糊了「技能定义」与「技能执行」的边界。

web fetch 提供了一个有力的反例：看似最简单的网页抓取技能，实际是 Token 成本最高的操作之一。大页面和 PDF 会显著抬高上下文成本。这说明 **L1 层的成本问题不会因为 L2 的出现而消失**——Programmatic Tool Calling 和 Dynamic Filtering 正是为了解决 web fetch 这类高成本技能的效率问题。

### 三、L2 → L3 的跃迁：从代码执行到多模态操作

[GUI-VLA](concepts/GUI-VLA.md) 代表了技能架构的范式性转变：将视觉理解、自然语言理解与动作决策统一到同一模型中。与 L1/L2 依赖 API 或浏览器协议不同，GUI-VLA 直接观察屏幕、理解界面元素并生成操作动作——这意味着**技能不再需要被预先定义为工具描述，而是从视觉观察中涌现**。

[Mano-Action 双向自增强学习框架](concepts/Mano-Action 双向自增强学习框架.md) 进一步揭示了 L3 层技能的训练方法论：

- Text → Action（自然语言到操作）：理解指令并执行

- Action → Text（操作到自然语言）：理解动作背后的语义

- 双向一致性学习 + SFT + 离线/在线强化学习的递进训练

[Agentic Vision](concepts/Agentic Vision.md) 展示了另一种 L3 路径：不直接生成操作动作，而是通过视觉理解 + 分步推理 + 代码执行的组合来完成复杂视觉任务。[仪表读数识别](concepts/仪表读数识别.md) 是其典型应用——不只是 OCR，而是包含刻度理解、角度估算和数值推断的复合任务。

| **L3 路径** | **代表** | **感知方式** | **动作生成** | **适用场景** |

| --- | --- | --- | --- | --- |

| **端到端 VLA** | GUI-VLA、Mano-Action | 屏幕/环境视觉输入 | 模型直接输出操作坐标/动作序列 | GUI 自动化、机器人操控 |

| **视觉推理 + 代码执行** | Agentic Vision、仪表读数识别 | 图像/视频 + 中间步骤推理 | 生成代码处理视觉信息 | 工业巡检、复杂测量 |

> **跨概念发现**：端到端 VLA 追求的是「模型直接操作环境」的通用性，视觉推理 + 代码执行追求的是「先理解再精确处理」的可解释性。两条路径不互斥——前者适合高频重复的 GUI 操作，后者适合需要精确推理的复杂任务。

### 四、成本-能力权衡：Auxiliary 副驾模型的分工哲学

[Auxiliary 副驾模型](concepts/Auxiliary 副驾模型.md) 揭示了一个跨层级的核心设计原则：**不是所有技能都需要最强模型**。它在主 Agent 之外引入辅助模型路由层，把上下文压缩、视觉理解、会话搜索和工具调用辅助等子任务分发给更便宜或更专用的模型。

这个概念暗示了技能架构的实际演进方向不是简单的 L1→L2→L3 替代，而是**多层级共存的混合架构**：

- **L1 Tool Calling** 负责简单、确定性高的工具调用

- **L2 Programmatic** 负责需要编排逻辑的复合任务

- **L3 多模态** 负责需要感知环境的自主操作

- **副驾模型** 在各层级之间做成本优化路由

### 五、协议层的隐性约束：Chat Template 的教训

[Chat Template](concepts/Chat Template.md) 的案例提供了一个常被忽视但极其重要的洞察：**技能能力的天花板往往不取决于模型能力，而取决于协议层的兼容性**。GLM-5.1 的 Tool Calling 循环死锁，根源是旧模板只接受 string 形式的工具结果，无法兼容推理框架转换后的 array parts。

这个问题在 L1→L2 的跃迁中尤为突出：当模型从输出 JSON 转向输出代码时，现有的 Chat Template、推理框架和工具描述格式可能全部需要升级。**协议层的升级成本是技能架构演进中最容易被低估的变量。**

## 关键发现

1. **Agent 技能架构正从「LLM as Router」向「LLM as Engine」演进，但这不是替代而是分层共存**：Tool Calling 2.0 的 Programmatic 模式让模型从被动选择工具转向主动编写编排逻辑，GUI-VLA 更进一步让模型直接操作环境。但 web fetch 的成本困境说明，即使在最高级的技能层，L1 层的基础优化（如 Dynamic Filtering）仍然不可或缺

1. **协议层兼容性是技能架构演进中最隐蔽的瓶颈**：Chat Template 的幽灵 Bug 证明，模型能力的提升如果没有协议层（模板、推理框架、工具描述格式）的同步升级，不仅无法发挥效果，还可能引发更难调试的系统故障。这解释了为什么 Tool Calling 2.0 需要同时推出四个特性而非逐个迭代

1. **多模态技能的两条路径（端到端 VLA vs 视觉推理+代码）解决的是不同类别的问题**：GUI-VLA/Mano-Action 追求跨应用通用操作能力，Agentic Vision 追求精确推理与可解释性。前者适合「替代人类重复操作」，后者适合「增强人类精确判断」——这两条路径将长期并行而非合并

1. **Auxiliary 副驾模型揭示了技能架构的真正演进方向是多层级混合而非单一替代**：最强模型做最难决策，专用模型做脏活累活——这种成本-能力分层设计比「用一个超强模型做所有事」更具工程可行性和经济性。技能架构的核心设计题不是选择哪个层级，而是设计层级之间的路由策略

1. **Tool Calling 2.0 的 Tool Search 机制暗示了技能发现将成为 Agent 能力的核心差异点**：当工具数量从十几个增长到数百上千个时，「知道有哪些工具可用」本身成为一种元技能。延迟加载 + 按需发现的模式让技能空间从静态列表进化为动态搜索空间——这与 MCP 协议的动态工具发现方向高度一致

## 来源列表

### 概念词条（Agent 技能 × LLM 交叉标签）

web fetch · [Tool Calling 2.0](entities/Tool Calling 2.0.md) · [Auxiliary 副驾模型](concepts/Auxiliary 副驾模型.md) · [GUI-VLA](concepts/GUI-VLA.md) · [Mano-Action 双向自增强学习框架](concepts/Mano-Action 双向自增强学习框架.md) · [Agentic Vision](concepts/Agentic Vision.md) · [仪表读数识别](concepts/仪表读数识别.md) · [Tool Calling](concepts/Tool Calling.md) · [Chat Template](concepts/Chat Template.md)

### 相关概念词条（补充材料）

[MCP 协议](concepts/MCP 协议.md) · [动态工具发现](concepts/动态工具发现.md) · [浏览器控制层](concepts/浏览器控制层.md) · [Accessibility Tree](concepts/Accessibility Tree.md)

### 摘要来源

[摘要：Anthropic Tool Calling 2.0——Agent 上下文消耗降80%](summaries/摘要：Anthropic Tool Calling 2.0——Agent 上下文消耗降80%.md) · [摘要：Agent 的"手"长出来了，但为什么还是不可靠？](summaries/摘要：Agent 的手长出来了，但为什么还是不可靠？.md) · 全球第一，13个SOTA！我们找到了龙虾界掌管GUI的神 · 谷歌深夜大招！机器人学会看仪表盘干活，成功率飙升300% · GLM-5.1 的 Tool Calling 循环死锁：一个 Chat Template 引发的「幽灵 Bug」

## 行动建议

1. **为 OpenClaw 的技能层建立 L1/L2/L3 分层路由机制**：参考 Auxiliary 副驾模型的思路，不要让主 Agent 用最贵的模型处理所有工具调用。建议为 OpenClaw 设计技能路由层：简单 API 调用走 L1（轻量模型 + JSON），需要编排逻辑的走 L2（主模型 + 代码执行），需要视觉感知的走 L3（多模态模型）。路由决策本身可以用轻量分类器完成

1. **优先在 web fetch 等高成本技能上应用 Tool Calling 2.0 的 Dynamic Filtering 模式**：当前 OpenClaw 的 web fetch 是 Token 消耗大户。建议在网页抓取结果返回主模型之前，插入一个代码过滤层，用小模型或规则引擎预处理网页内容，只保留与当前任务相关的信息。预期可降低 20-30% 的上下文成本

1. **关注 GUI-VLA 赛道的端侧部署进展，为 OpenClaw 预留视觉操作接口**：Mano-Action 已证明端侧 GUI-VLA 的可行性。建议在 OpenClaw 的技能协议中预留视觉输入 + 动作输出的接口定义，即使当前不实现 L3 层能力，也要确保未来可以无缝接入——协议层的前瞻性设计比模型能力更难事后补救
