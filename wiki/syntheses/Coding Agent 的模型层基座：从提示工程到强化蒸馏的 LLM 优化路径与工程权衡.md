---
title: Coding Agent 的模型层基座：从提示工程到强化蒸馏的 LLM 优化路径与工程权衡
type: synthesis
tags:
- 提示工程
- 训练/微调
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a73cf2ea3a6b4f8392ec9d386e5a2ab8
notion_id: a73cf2ea-3a6b-4f83-92ec-9d386e5a2ab8
---

## 研究问题

Coding Agent 的表现上限由底层 LLM 决定，但 LLM 的哪些优化路径对 Coding Agent 的实际工程效果影响最大？本文综合 7 个横跨 Coding Agent 与 LLM 两个标签的概念，回答：**在「换更大的模型」之外，有哪些针对性的 LLM 优化手段能系统性提升 Coding Agent 的工程表现。**

## 综合分析

### 一、三层优化栈：推理时、训练后、运行时

从 7 个概念中可以提炼出 Coding Agent 对 LLM 的优化需求分布在三个层次：

| **优化层** | **核心手段** | **代表概念** | **投入成本** | **效果特征** |

| --- | --- | --- | --- | --- |

| 推理时优化 | 提示设计 + 思考预算 | System Prompt 工程、ultrathink | 低（无需训练） | 即时见效，跨模型可迁移 |

| 训练后优化 | 蒸馏 + 强化学习 | Agentic 编程轨迹蒸馏、Simple Self-Distillation、可验证奖励 | 中-高（需要数据和计算） | 永久性能提升，但模型绑定 |

| 运行时优化 | 缓存 + API 适配 | Prompt Caching、OpenAI 兼容 API 代理 | 低-中（工程实现） | 降本提速，不改变模型能力 |

### 二、蒸馏路径的分化：轨迹蒸馏 vs. 自蒸馏

两种蒸馏方法代表了截然不同的哲学：

- **Agentic 编程轨迹蒸馏**：从强模型的完整操作序列（工具调用、修复过程、决策路径）中学习。蒸馏对象是「怎么干活」，而不仅是「答案是什么」。

- **Simple Self-Distillation**：模型用自身采样输出做监督微调，不依赖外部教师或验证器。代表「低资源高收益」的简单路线。

| **维度** | **轨迹蒸馏** | **自蒸馏** |

| --- | --- | --- |

| 数据来源 | 强模型真实执行轨迹 | 模型自身采样输出 |

| 学习目标 | 操作序列 + 工具使用模式 | 代码生成质量 |

| 外部依赖 | 需要教师模型 + 执行环境 | 几乎零依赖 |

| 适用模型 | 小模型追赶大模型 | 任意模型自我提升 |

| 提升维度 | 工具使用 + 任务恢复 + 多步执行 | 单次代码生成质量 |

### 三、可验证奖励：编程为何是 RL 的最佳训练场

**可验证奖励**揭示了一个结构性优势：编程任务的反馈信号天然清晰（测试通过/失败），这使得 RL 在 Coding Agent 场景中的效果远好于搜索、写作等主观任务。这意味着：

- Coding Agent 将持续成为 LLM 能力提升最快的应用领域

- 模型在编程任务上的进步速度会系统性地快于其他应用

- 投入 Coding Agent 的 RL 训练管线具有更高的投资回报率

### 四、System Prompt 工程：被低估的「免费午餐」

**System Prompt 工程**和 **ultrathink** 代表了推理时优化的两个方向：

- System Prompt 工程：通过系统化的角色设定、行为约束和问题求解流程设计，拉齐不同模型的执行质量。**比换模型本身更重要。**

- ultrathink：通过提高内部思考预算，在复杂推理和深度代码分析中换取更完整的输出。代价是延迟和 Token 成本。

两者的共同启示：在模型能力相同的前提下，**使用方式的差异**可以带来数倍的效果差距。

### 五、运行时基础设施：降本不等于降质

**Prompt Caching** 通过复用对话前缀缓存大幅降低重复上下文的 Token 成本。对长上下文编程 Agent（如 Claude Code）的影响尤为显著：

- 前缀顺序稳定性成为工程设计的硬约束

- 会反向影响 System Prompt 的结构设计（静态内容前置）

- 与 ultrathink 存在张力——更长的思考链会降低缓存命中率

**OpenAI 兼容 API 代理**则解决了另一个问题：让非 OpenAI 模型以统一接口接入现有工具链，降低多模型切换的工程成本。

## 关键发现

> **💡** **发现 1：Coding Agent 的「模型红利」具有结构性优势。** 因为可验证奖励的存在，编程领域的 RL 训练效率天然高于其他领域。这意味着 Coding Agent 的能力增速将长期快于通用 Agent。

> **💡** **发现 2：推理时优化和训练后优化存在「倍增效应」。** System Prompt 工程可以让蒸馏后的小模型发挥出接近大模型的效果——两者叠加的收益远大于单独使用。

> **💡** **发现 3：Prompt Caching 和 ultrathink 之间存在隐性矛盾。** 深度思考需要更多动态 Token，而缓存优化偏好静态前缀。工程实践中需要在「思考深度」和「运行成本」之间显式权衡。

> **💡** **发现 4：自蒸馏的出现标志着「模型自我改进闭环」的成熟。** 不再需要教师模型或外部验证器，模型可以通过自身采样持续提升代码生成能力。这对资源有限的团队尤其有价值。

> **💡** **发现 5：API 兼容层正在成为隐性的模型选择权。** OpenAI 兼容 API 代理让 Coding Agent 可以在不改代码的情况下切换底层模型。这把「模型选择」从架构决策降级为运维配置。

## 来源列表

### 概念页

- [Agentic 编程轨迹蒸馏](concepts/Agentic 编程轨迹蒸馏.md)

- [OpenAI 兼容 API 代理](concepts/OpenAI 兼容 API 代理.md)

- [Prompt Caching](concepts/Prompt Caching.md)

- [Simple Self-Distillation](concepts/Simple Self-Distillation.md)

- [System Prompt 工程](concepts/System Prompt 工程.md)

- [ultrathink](concepts/ultrathink.md)

- [可验证奖励](concepts/可验证奖励.md)

### 相关摘要

- [摘要：Qwen Code v0.14：用手机遥控你的服务器，终端 AI 编程助手的新玩法](summaries/摘要：Qwen Code v0.14：用手机遥控你的服务器，终端 AI 编程助手的新玩法.md)

- [摘要：Better-Harness：LangChain 用 Evals 当梯度信号，让 Agent 越跑越强](summaries/摘要：Better-Harness：LangChain 用 Evals 当梯度信号，让 Agent 越跑越强.md)

- [摘要：用半年 Claude Code 踩坑，我验证了 OpenAI/Cursor/Anthropic 三篇 Harness Engineering 的每一条](summaries/摘要：用半年 Claude Code 踩坑，我验证了 OpenAI-Cursor-Anthropic 三篇 Harness Engineering 的每一条.md)

- [摘要：auth2api：用 Claude Max 订阅伪装成真实 CLI 用户，自建 OpenAI 兼容 API 代理](summaries/摘要：auth2api：用 Claude Max 订阅伪装成真实 CLI 用户，自建 OpenAI 兼容 API 代理.md)

- [摘要：Gemma4-31B-Opus-4.6-reasoning：把 Claude 的推理方式「蒸馏」进开源模型](summaries/摘要：Gemma4-31B-Opus-4.6-reasoning：把 Claude 的推理方式「蒸馏」进开源模型.md)

## 行动建议

1. **优先投入 System Prompt 工程而非频繁换模型**：为 OpenClaw 的 Coding Agent 场景建立 System Prompt 模板库，将成功的提示模式（角色设定、验证流程、输出格式）沉淀为可复用资产。这是投入最低、见效最快的优化路径。

1. **探索 Agentic 轨迹蒸馏用于 OpenClaw 技能训练**：将 Claude 等强模型在实际 OpenClaw 工作流中的操作轨迹（工具调用序列、错误恢复路径）收集并蒸馏进小模型，降低日常运行的模型调用成本。

1. **在内容管线中实施 Prompt Caching 感知的上下文设计**：重新审视现有工作流的上下文拼接顺序，把静态内容（系统指令、知识库片段）前置、动态内容后置，最大化 Prompt Caching 命中率，预计可降低 30-50% 的 Token 成本。
