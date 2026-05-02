---
title: 评测驱动的 Harness 迭代闭环：模型评测如何从外部度量演变为 Agent 运行时治理的内生反馈信号
type: synthesis
tags:
- 模型评测
- Harness 工程
status: 审核中
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c50a5520bec34605a8468751ba56352c
notion_id: c50a5520-bec3-4605-a846-8751ba56352c
---

## 研究问题

当 Agent 的核心能力不再仅由底层模型决定，而是由「Model + Harness」共同构成时，评测体系与运行时治理之间的边界在哪里？模型评测是否正在从一次性的外部打分工具，演变为 Harness 工程持续迭代的内生反馈信号？这两个看似分属不同阶段的工程实践，如何在 Agent 时代形成共演闭环？

## 综合分析

### 一、从「模型打分」到「Harness 梯度」：评测角色的范式跃迁

传统模型评测（如 HumanEval、SWE-bench）的设计假设是：**模型是唯一变量，基准是固定标尺**。但在 Agent 系统中，决定任务成败的因素远不止模型本身——提示词结构、工具描述、路由策略、验证循环等 Harness 层组件同样关键。

[Better-Harness](entities/Better-Harness.md) 方法论明确提出了这一转变：**把评测结果当作反馈信号，持续迭代 Agent 的执行底座，而不是优先更换底层模型**。这意味着 Evals 的角色从「一次性排名工具」跃迁为「持续优化的梯度信号」。

| **维度** | **传统模型评测** | **Harness 驱动评测** |

| --- | --- | --- |

| 评测对象 | 模型本身 | Model + Harness 整体 |

| 反馈用途 | 选型排名 | 持续迭代信号 |

| 迭代对象 | 换模型 | 调 prompt/工具/路由/验证 |

| 失败分析 | 模型能力不足 | Harness 配置缺陷 |

| 代表方法 | HumanEval, SWE-bench | Better-Harness, Trigger Evals |

### 二、评测粒度的分层：从「最终输出」到「中间路由」

传统评测只看最终结果——代码是否通过测试、回答是否正确。但 Harness 工程需要更细粒度的诊断信号。

[Trigger Evals](concepts/Trigger Evals.md) 开辟了一个全新的评测层面：**评测的不是输出内容本身，而是「是否由正确的能力被触发」**。它同时检测 false negative（该触发却没触发）和 false positive（触发了错误技能），将评测深入到 Harness 的路由层。

这揭示了一个重要模式：**评测粒度与 Harness 架构层次一一对应**。

- **路由层评测**（Trigger Evals）→ 诊断 Resolver 配置

- **执行层评测**（APEX-SWE、Pass^3）→ 诊断工具调用与验证循环

- **稳定性评测**（Pass^3 要求三次独立通过）→ 诊断系统整体鲁棒性

- **泛化评测**（Holdout Set）→ 诊断是否对已知样本过拟合

### 三、验证问题：评测-Harness 共演的瓶颈与突破

[验证问题](concepts/验证问题.md) 是这个闭环的核心瓶颈：**许多复杂任务中，系统难以通过程序化规则来判断模型输出是否正确**。只要任务结果可度量，模型能力就更容易被持续提升；反之，验证问题限制了 Agent 进入核心业务流程的深度。

这个瓶颈催生了多种 Harness 层的应对策略：

1. **LLM-as-a-Verifier**：用模型自身的判断能力来补充程序化验证的不足

1. **Review Agents**：把人工评审中可标准化的部分前移为自动验证

1. **假模型测试**：通过可预期的失败来验证真实路由是否生效——一种巧妙的「反向评测」

### 四、生成-自评能力差距：决定 Harness 投资回报的隐藏变量

[生成-自评能力差距](concepts/生成-自评能力差距.md) 提供了一个关键洞察：**只有当模型的「产出候选答案」能力与「判断哪个答案更好」能力之间存在足够差距时，结构化多轮评审才能带来显著增益**。

这意味着 Harness 工程的投资回报不是均匀分布的：

- **弱模型**：候选质量都不够好，复杂 Harness 带来的收益有限

- **中档模型**：生成-自评差距最大，Harness 投资回报最高

- **顶级模型**：自评已足够强，额外结构带来的收益缩小

这为 Harness 工程的资源分配提供了理论指导：**评测不仅告诉你系统表现如何，还告诉你 Harness 优化的边际收益在哪里**。

### 五、递归自我改进：评测-Harness 闭环的终极形态

[递归自我改进](concepts/递归自我改进.md) 指向了这个闭环的终极形态：AI 系统不仅执行任务，也开始参与改进自身的评测体系和 Harness 配置。当评测反馈、Harness 调整与模型能力提升三者形成自动化循环时，Agent 的进化速度可能从线性变为超线性。

## 关键发现

1. **评测正在从「外部标尺」变为「内部梯度」**：Better-Harness 方法论的核心突破不是发明了新的评测指标，而是重新定义了评测结果的消费方式——从选型排名变为持续迭代信号。这意味着评测体系本身成为 Harness 架构的一部分。

1. **评测粒度与 Harness 架构层次存在结构同构**：Trigger Evals 评路由、Pass^3 评稳定性、Holdout Set 评泛化——每一种评测方法都精确对应 Harness 的一个架构层次。这不是巧合，而是评测-治理共演的必然产物。

1. **生成-自评能力差距是 Harness 投资决策的隐藏变量**：中档模型是 Harness 优化回报最高的区间，这为 Tizer 的 OpenClaw 多模型路由策略提供了一个非直觉的选型维度——**不是选最强的模型，而是选 Harness 边际收益最大的模型**。

1. **验证问题是评测-Harness 闭环的硬性天花板**：无论 Harness 多精巧，如果任务结果本身不可验证，闭环就无法闭合。Review Agents 和 LLM-as-a-Verifier 是对这个天花板的「软突破」，但尚未根本解决问题。

1. **假模型测试揭示了「反向评测」范式**：通过故意制造可预期的失败来验证系统行为，这种思路将评测从「验证正确性」扩展到「验证可观测性」，是 Harness 工程独有的评测创新。

## 来源列表

- [APEX-SWE](concepts/APEX-SWE.md)

- [Better-Harness](entities/Better-Harness.md)

- [Evals](concepts/Evals.md)

- [Holdout Set](concepts/Holdout Set.md)

- [Pass^3](concepts/Pass^3.md)

- [Review Agents](concepts/Review Agents.md)

- [Trigger Evals](concepts/Trigger Evals.md)

- [假模型测试](concepts/假模型测试.md)

- [生成-自评能力差距](concepts/生成-自评能力差距.md)

- [递归自我改进](concepts/递归自我改进.md)

- [验证问题](concepts/验证问题.md)

## 行动建议

1. **在 OpenClaw 的多模型路由层引入 Trigger Evals 机制**：当前 OpenClaw 的 Resolver 配置主要依赖人工调试。建议为每个 Skill 维护一组 Trigger Eval 样本，每次 Resolver 配置变更后自动回归测试，将路由质量纳入持续集成管线。

1. **基于生成-自评能力差距做模型分档部署**：对于 Tizer 的 HITL 工作流中涉及的不同任务类型，评估各模型在该任务上的生成-自评差距，将 Harness 优化资源集中投入到差距最大的中档模型 + 高价值任务组合上，而非一律追求最强模型。

1. **建立「验证难度分级」标注体系**：为知识 Wiki 中的 concept 增加「验证难度」维度标注（程序可验证 / LLM 可判断 / 需人工裁决），帮助 Synthesizer 和 Compiler 在生成内容时自动匹配相应的质量保障策略。
