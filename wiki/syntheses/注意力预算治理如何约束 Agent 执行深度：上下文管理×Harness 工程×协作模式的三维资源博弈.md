---
title: 注意力预算治理如何约束 Agent 执行深度：上下文管理×Harness 工程×协作模式的三维资源博弈
type: synthesis
tags:
- Agent 协作模式
- Harness 工程
- 上下文管理
status: 已审核
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1096b43d91dc4f83ac28807d6cba7c06
notion_id: 1096b43d-91dc-4f83-ac28-807d6cba7c06
---

## 研究问题

上下文管理定义 Agent 的「注意力预算」，Harness 工程构建执行边界与状态持久层，协作模式决定多 Agent 间的信息流拓扑。**这三个维度如何在 Agent 运行时形成一个相互约束的资源博弈系统？当上下文窗口耗尽时，是 Harness 接管续跑、协作模式切换分工、还是上下文压缩策略激活——它们之间的优先级与调度逻辑是什么？**

## 综合分析

### 一、三维关系图谱：每条边的耦合机制

| 边 | 耦合关系 | 代表概念 | 核心张力 |

| --- | --- | --- | --- |

| **上下文管理 × Harness 工程** | Harness 负责上下文的外置持久化：Memory Folder、Compaction、文件系统即长期记忆 | [Untitled](concepts/Memory Folder.md)、[Untitled](concepts/Agent Harness.md)、[Untitled](concepts/Scope Reduction Detection.md) | 上下文窗口容量 vs. 外置读写延迟 |

| **Harness 工程 × 协作模式** | Harness 为协作提供状态快照、任务路由和沙箱隔离基底 | [Untitled](concepts/Harness Engineering.md)、[Untitled](concepts/Ralph Loop.md)、[Untitled](concepts/Sandbox 抽象.md) | 隔离粒度 vs. 协作通信开销 |

| **协作模式 × 上下文管理** | 协作拓扑决定上下文的共享/隔离策略：共享状态 vs. 消息传递 | [Untitled](concepts/thin control over thick state.md)、[Untitled](concepts/token效率.md)、[Untitled](concepts/长时程信用分配.md) | 信息完整性 vs. token 预算 |

### 二、涌现结构：「注意力预算治理」范式

当三条边同时施加约束时，一个只有同时观察三个维度才能发现的架构模式浮现——**Agent 运行时正在从「无限上下文假设」迁移到「注意力预算治理」范式**。

这一范式包含三层调度机制：

1. **预算分配层（上下文管理）**：每个任务根据复杂度获得一份 token 预算。简单任务直接用 context window 内信息完成；复杂任务需要向 Harness 申请「外部记忆读取配额」

1. **预算执行层（Harness 工程）**：当 context window 接近耗尽时，Harness 介入执行三种策略之一：

  - **Compaction**：压缩 context 内历史（保留密度最高的信息）

  - **Memory Folder 外置**：将当前状态写入文件系统，释放 context 空间

  - **Ralph Loop 续跑**：拦截执行流、刷新上下文并重启目标任务

1. **预算协调层（协作模式）**：在多 Agent 场景中，决定哪些信息在 Agent 之间共享、哪些隔离。[thin control over thick state](concepts/thin control over thick state.md) 模式给出了最清晰的答案——控制层保持轻量（低 context 消耗），状态层沉淀到文件系统（不占 context）

### 三、三条边的共演博弈：谁先响应上下文危机？

当 Agent 在长时程任务中遭遇上下文耗尽时，三个维度存在一个**优先级调度序列**：

**第一响应者：上下文管理（压缩策略）**

- 触发条件：context 使用率 > 80%

- 动作：Compaction 压缩历史轮次，保留高价值信息

- 成本：压缩信息损失，可能丢失关键上下文

**第二响应者：Harness 工程（外置持久化）**

- 触发条件：压缩后 context 仍不足，或任务需要跨会话延续

- 动作：[Memory Folder](concepts/Memory Folder.md) 写出当前状态，或触发 [Ralph Loop](concepts/Ralph Loop.md) 续跑

- 成本：文件读写延迟，上下文重建开销

**第三响应者：协作模式（任务分解重组）**

- 触发条件：单 Agent 即使外置记忆也无法胜任（如任务固有复杂度超过单次 context 容量）

- 动作：将任务拆分给多个 Agent，每个 Agent 处理独立子问题

- 成本：协调开销、信息同步延迟

这个优先级序列解释了一个关键现象：[长时程信用分配](concepts/长时程信用分配.md)** 之所以困难，是因为它横跨了所有三个响应层级**。当一个早期决策的影响需要在多轮压缩、多次外置持久化、甚至跨 Agent 分工后才能评估时，归因链条的完整性依赖于三个维度的协调质量。

### 四、反模式矩阵：三维失衡的六种形态

| 失衡组合 | 症状 | 根因 | 修复策略 |

| --- | --- | --- | --- |

| **上下文过贪 + Harness 缺位** | Agent 将所有信息塞进 context，最终溢出崩溃 | 缺少 Memory Folder 等外置机制 | 引入 Harness 层的主动外置策略 |

| **Harness 过重 + 上下文忽视** | Harness 的工具定义和系统提示本身消耗过多 context | Harness 设计未考虑 context 预算 | Thin Harness, Fat Skills 原则 |

| **协作过深 + 上下文爆炸** | orchestrator 收集所有 worker 输出，context 膨胀失控 | 缺少 Latent Briefing 等压缩传递机制 | thin control over thick state 模式 |

| **上下文压缩 + 协作信息丢失** | 压缩后丢失了其他 Agent 传递的关键信息 | 压缩策略不感知协作拓扑 | 标记跨 Agent 信息为不可压缩 |

| **Harness 外置 + 协作不感知** | Memory Folder 写出的文件对其他协作 Agent 不可见 | 外置存储未与协作层打通 | 共享文件系统 + 读取权限控制 |

| **协作分工 + Harness 无协调** | 多个 Agent 重复执行相同子任务 | Harness 缺少全局任务注册表 | 引入任务去重和状态同步机制 |

### 五、已有双标签 synthesis 的升维视角

已有的 [Harness 工程如何重塑推理资源分配：当执行框架、协作模式与推理优化在 Agent 运行时三角共演](syntheses/Harness 工程如何重塑推理资源分配：当执行框架、协作模式与推理优化在 Agent 运行时三角共演.md) 揭示了 Harness × 协作模式 × 推理优化的三角关系。本三标签分析引入**上下文管理**维度后，发现一个关键补充：

推理优化关注的是「每次模型调用花多少 token」（**单次成本**），而上下文管理关注的是「整个任务生命周期中 token 如何分配」（**生命周期预算**）。两者在 Harness 层的交汇点是 **Memory Folder**——它既是推理优化（减少重复读取成本）的工具，也是上下文管理（释放 window 空间）的机制，更是协作模式（跨 Agent 状态共享）的基础设施。

## 关键发现

1. **Agent 运行时存在一个三层优先级调度序列**——面对上下文耗尽，系统依次启动：压缩（上下文管理）→ 外置（Harness）→ 分工（协作模式）。这个序列不是人为设计，而是成本递增的自然排序

1. **thin control over thick state 是三维最优解的近似实现**——轻控制层（最小 context 消耗）+ 厚状态层（文件系统即 Harness 外置记忆）+ 委派式协作（控制层只做路由不做计算），同时满足了三个维度的约束

1. **Memory Folder 是三个维度的交汇枢纽**——它同时服务于上下文释放（上下文管理）、跨会话持久化（Harness 工程）和跨 Agent 状态共享（协作模式）。Anthropic 实测 Sonnet 4.5 准确率从 60.4% 提升至 67.2%，证明外置记忆不仅节省 token，更提升任务质量

1. **长时程信用分配是三维协调质量的试金石**——当归因需要穿越压缩、外置和分工三个层级时，任何一层的信息损失都会导致归因失败。这解释了为什么 Meta-Harness 的演化搜索有效——它同时优化了三个维度的参数

1. **「协作拓扑感知的压缩策略」是当前最大的架构缺口**——现有压缩算法不区分本地信息和跨 Agent 传递信息，导致协作场景中关键上下文被误删。需要引入「信息来源标签」机制

## 来源列表

- [Agent Harness](concepts/Agent Harness.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Ralph Loop](concepts/Ralph Loop.md)

- [长时程信用分配](concepts/长时程信用分配.md)

- [thin control over thick state](concepts/thin control over thick state.md)

- [token效率](concepts/token效率.md)

- [Memory Folder](concepts/Memory Folder.md)

- [Scope Reduction Detection](concepts/Scope Reduction Detection.md)

- [Sandbox 抽象](concepts/Sandbox 抽象.md)

- [Auxiliary 副驾模型](concepts/Auxiliary 副驾模型.md)

- [SGLang](entities/SGLang.md)

- [Claude Managed Agents](entities/Claude Managed Agents.md)

- [Agent 操作系统层](concepts/Agent 操作系统层.md)

- [Agent Hooks](concepts/Agent Hooks.md)

- [OpenClaw Context Engine](entities/OpenClaw Context Engine.md)

- [Agent Tool Interface](concepts/Agent Tool Interface.md)

- [Tool Wrapper 模式](concepts/Tool Wrapper 模式.md)

- [GSD](entities/GSD.md)

- [cc-harness](entities/cc-harness.md)

- [Harness 工程如何重塑推理资源分配：当执行框架、协作模式与推理优化在 Agent 运行时三角共演](syntheses/Harness 工程如何重塑推理资源分配：当执行框架、协作模式与推理优化在 Agent 运行时三角共演.md)（双标签 synthesis 引用）

## 行动建议

1. **在 OpenClaw 中实现「注意力预算治理」的三层调度机制**——为每个任务分配 context 预算，在 80% 使用率时自动触发压缩，压缩不足时自动外置到 Memory Folder，外置后仍不足时自动拆分为多 Agent 子任务。这能让长时程任务从「偶尔成功」变为「稳定可靠」

1. **为跨 Agent 信息标记「不可压缩」标签**——在 OpenClaw 的上下文压缩策略中，区分本地生成信息和其他 Agent 传递的信息，后者默认标记为高优先级不可压缩。这解决了当前协作场景中最常见的上下文丢失问题

1. **构建 Memory Folder 的协作层扩展**——将 Memory Folder 从单 Agent 私有存储升级为多 Agent 可读的共享状态层，通过读取权限控制实现协作安全性。参考 thin control over thick state 模式，让状态层成为团队共享的「项目证据库」
