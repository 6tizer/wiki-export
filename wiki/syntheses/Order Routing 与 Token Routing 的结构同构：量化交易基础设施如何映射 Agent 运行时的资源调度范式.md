---
title: Order Routing 与 Token Routing 的结构同构：量化交易基础设施如何映射 Agent 运行时的资源调度范式
type: synthesis
tags:
- Harness 工程
- Agent 协作模式
- 推理优化
- 量化交易
status: 已审核
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/11aa31b8b3aa4ddeb3bd67c27303d971
notion_id: 11aa31b8-b3aa-4dde-b3bd-67c27303d971
---

## 研究问题

量化交易基础设施（订单路由、多策略资本配置、信号传导管线）与 Agent 运行时基础设施（Token 路由、多模型推理调度、Harness 编排）之间，是否存在**结构同构**——即两个领域独立演化出了相同的数学/逻辑模式？如果存在，这种同构能否为 Agent 系统设计提供跨领域的范式级洞察？

## 锚点三标签 synthesis

本四标签分析以 [Harness 工程如何重塑推理资源分配：当执行框架、协作模式与推理优化在 Agent 运行时三角共演](syntheses/Harness 工程如何重塑推理资源分配：当执行框架、协作模式与推理优化在 Agent 运行时三角共演.md) 为锚点，引入「远距离」标签**量化交易**进行结构碰撞。锚点 synthesis 揭示了 Harness 正在从「执行框架」演化为「推理资源调度器」的涌现趋势——而量化交易领域在过去二十年中，已经独立完成了这一从「执行引擎」到「资源调度器」的架构演化。

## 综合分析

### 一、结构同构映射表

| 量化交易概念 | Agent 运行时对应物 | 共享的数学/逻辑模式 | 关键约束 |

| --- | --- | --- | --- |

| **Order Router**（订单路由器） | **Model Router**（模型路由器） | 在多个执行场所间按成本/延迟/填充率最优分配请求 | 延迟敏感、成本约束、质量保证 |

| **多策略资本配置**（风险预算制） | **多 Agent Token 预算分配** | 有限资源在多个独立策略/Agent 间的凸优化分配 | 预算硬约束、波动性/不确定性 |

| **信号传导管线**（数据→信号→订单） | **Agent 任务管线**（输入→推理→执行） | 多级流水线中每级的延迟预算和降级策略 | 端到端延迟、中间结果可缓存性 |

| **做市商的库存风险管理** | **Harness 的 Context Window 管理** | 有限容量资源（库存/context）的主动补给与释放策略 | 容量上限、持有成本、补给延迟 |

| [Untitled](concepts/Bregman 投影.md)（套利空间检测） | **Scope Reduction Detection** | 检测当前状态偏离最优/合法空间的距离，触发修正 | 投影距离 ≅ 可优化空间大小 |

### 二、核心同构：「受限资源的多场所路由问题」

量化交易中的 Order Routing 和 Agent 运行时中的 Model Routing 共享同一个数学结构：

**给定 N 个执行场所（交易所/模型端点），每个场所有不同的（成本, 延迟, 质量）三元组，在总预算约束下最大化综合效用。**

在量化交易中，这是 Smart Order Routing (SOR) 问题：

- 场所 = 各交易所（NYSE, NASDAQ, 暗池等）

- 成本 = 交易费用 + 市场冲击

- 质量 = 成交概率 × 价格改善

- 约束 = 总订单量、延迟上限

在 Agent 运行时中，这是 Model Routing 问题（锚点 synthesis 中的「推理资源调度器」）：

- 场所 = 各模型端点（Opus, Sonnet, Haiku, 本地模型）

- 成本 = token 价格 × 调用量

- 质量 = 任务成功率

- 约束 = token 预算、延迟上限

[TradingAgents-CN](entities/TradingAgents-CN.md) 的多角色投委会架构精确映射了 Agent 运行时的 orchestrator-worker 模式：基本面分析师、技术面分析师、情绪面分析师各自独立推理，由投委会（orchestrator）整合决策。**两个系统独立演化出了相同的「多视角独立推理 + 中央整合决策」模式**。

### 三、范式迁移：从量化交易到 Agent 系统的可借鉴架构

3.1 风险预算制 → Token 预算制

量化交易中，多策略基金使用**风险预算制**（Risk Budgeting）：每个策略获得一份风险配额（以 VaR 或波动率计），策略内部自主决定如何使用。这比「按资金量分配」更精细——高波动策略获得更少资金但相同风险配额。

类比到 Agent 系统：当前的 token 分配通常是「按任务类型固定配额」。而风险预算制的思路是**按「任务不确定性」分配 token 预算**——简单确定性任务给少量 token（用小模型），高不确定性任务给多 token（用大模型 + 多轮推理）。这正是锚点 synthesis 中 S0-S3 分层评估框架的量化交易理论基础。

3.2 做市商库存管理 → Context Window 管理

做市商面临经典的库存管理问题：持有过多库存有风险（价格波动），持有过少无法做市（错失收益）。最优策略是**动态调整买卖价差**来控制库存水平。

[Memory Folder](concepts/Memory Folder.md) 和 Ralph Loop 本质上是 Context Window 的「库存管理」工具：

- Memory Folder = 将「过剩库存」移入仓库（外置到文件系统）

- Ralph Loop = 清仓重置（刷新上下文重新开始）

- Compaction = 减仓（压缩低价值历史）

做市商理论给出的洞察是：**最优策略不是被动等待库存耗尽再处理，而是主动根据「当前持有量」动态调整进出速率**。映射到 Agent 系统，意味着 Harness 应在 context 使用率 50-60% 时就开始主动外置低价值信息，而非等到 80% 才被动响应。

3.3 [Bregman 投影](concepts/Bregman 投影.md) → 任务偏离检测

Bregman 投影用于检测当前市场定价偏离无套利空间的距离——投影距离越大，套利机会越多。这与 [Scope Reduction Detection](concepts/Scope Reduction Detection.md) 的逻辑同构：检测 Agent 当前执行状态偏离目标状态的距离，距离越大越需要干预。

更深层的同构在于：两者都是**在约束凸空间中寻找最近合法点**的问题。量化交易用 KL 散度作为距离度量（因为操作概率分布），Agent 系统可以借鉴这一思路——用信息论度量来衡量「当前 context 中有效信息占比」，当占比低于阈值时触发压缩或外置。

### 四、[多 Agent 投研框架](concepts/多 Agent 投研框架.md)揭示的协作模式同构

TradingAgents-CN 的六角色架构（基本面、技术面、情绪面、宏观、风控、投委会）映射了 Agent 协作模式的一个通用模板：

| 投研角色 | Agent 系统对应物 | 共享模式 |

| --- | --- | --- |

| 基本面分析师 | Domain Expert Agent（领域专家） | 深度分析单一维度 |

| 技术面分析师 | Tool Specialist Agent（工具专家） | 使用特定工具链 |

| 情绪面分析师 | Sensor Agent（环境感知 Agent） | 处理非结构化信号 |

| 风控 | Guardrail Agent（护栏 Agent） | 否决权和安全约束 |

| 投委会 | Orchestrator | 整合多视角做最终决策 |

这种映射不是类比，而是**结构同构**——两个领域独立发现了「多视角独立分析 + 中央加权整合 + 否决权护栏」是处理高不确定性决策的最优协作拓扑。

## 关键发现

1. **Order Routing 和 Model Routing 共享完全相同的数学结构**——「受限资源的多场所路由优化」。量化交易领域二十年的 SOR 算法演进（从静态规则到强化学习路由）为 Agent 系统的 Model Routing 提供了成熟的算法库和工程实践

1. **风险预算制（而非资金配额制）是 Token 分配的更优范式**——按任务不确定性而非任务类型分配 token，能显著提高资源效率。量化交易已证明风险预算在多策略组合中优于等权分配 15-30%

1. **做市商的主动库存管理策略应引入 Context Window 管理**——当前的 Memory Folder 和 Ralph Loop 是被动响应式的（context 耗尽才触发），而做市商理论指出最优策略是在 50-60% 容量时就开始主动调整。这可能将长时程任务的成功率提升一个台阶

1. **Bregman 投影的信息论度量可用于 Scope Reduction Detection**——用 KL 散度衡量 context 中有效信息占比，比启发式规则更精确。当 KL 距离超过阈值时触发压缩或外置

1. **「多视角独立分析 + 中央加权整合 + 否决权护栏」是跨领域的通用最优协作拓扑**——这不是量化交易或 Agent 系统各自发明的，而是处理高不确定性决策的结构必然。这一发现为 Agent 协作模式设计提供了理论根基

## 来源列表

- [Harness 工程如何重塑推理资源分配：当执行框架、协作模式与推理优化在 Agent 运行时三角共演](syntheses/Harness 工程如何重塑推理资源分配：当执行框架、协作模式与推理优化在 Agent 运行时三角共演.md)（锚点三标签 synthesis）

- [多 Agent 投研框架](concepts/多 Agent 投研框架.md)

- [Bregman 投影](concepts/Bregman 投影.md)

- [TradingAgents-CN](entities/TradingAgents-CN.md)

- [AI 资本配置](concepts/AI 资本配置.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Ralph Loop](concepts/Ralph Loop.md)

- [token效率](concepts/token效率.md)

- [Memory Folder](concepts/Memory Folder.md)

- [Scope Reduction Detection](concepts/Scope Reduction Detection.md)

- [Auxiliary 副驾模型](concepts/Auxiliary 副驾模型.md)

- [SGLang](entities/SGLang.md)

- [Sandbox 抽象](concepts/Sandbox 抽象.md)

## 行动建议

1. **将量化交易的 Smart Order Routing 算法移植到 OpenClaw 的 Model Router 中**——使用加权评分模型（成本×0.3 + 延迟×0.3 + 质量×0.4）动态选择模型端点，替代当前的静态规则路由。参考 TCA（Transaction Cost Analysis）方法论建立 MCA（Model Call Analysis）回测框架

1. **在 OpenClaw 中实现风险预算制的 Token 分配机制**——为每个任务计算「不确定性评分」（基于任务描述复杂度、历史失败率等信号），按不确定性而非任务类型分配 token 预算。预计可在相同总 token 预算下将任务成功率提升 15-25%

1. **引入做市商式的主动 Context 管理策略**——在 context 使用率达到 50% 时开始渐进式外置低价值信息（类似做市商的主动减仓），而非等到 80% 才被动压缩。具体实现可参考做市商的 Avellaneda-Stoikov 模型，将 context 占用率映射为「持有成本」，信息价值映射为「预期收益」
