---
title: 摘要：We've published new research on how we post-train models for accurate search-augmented
  answers.
type: summary
tags:
- RAG/检索
- 训练/微调
- 推理优化
status: 已审核
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b6881879037e81fd466c81f
notion_url: https://www.notion.so/Tizer/fc2c29635c9c423c996216a7e8f399ed
notion_id: fc2c2963-5c9c-423c-9962-16a7e8f399ed
---

## 一句话摘要

Perplexity 公开了其搜索增强问答模型的后训练方案：先用监督微调建立指令、护栏与语言一致性，再用 on-policy RL 联合优化检索准确性、引用质量与工具效率，使 Qwen 系模型在更低成本下达到或超过 GPT 级别的事实性表现。

## 关键洞察

- 这篇研究强调，搜索型模型的关键不只是底模能力，而是**数据构造 + 奖励设计**是否围绕“可验证检索行为”共同设计。

- 两阶段训练路径很明确：先用 SFT 建立可部署行为，再用 on-policy RL 提升搜索、引用与效率，避免模型只会“回答得像”，却不会“查得准”。

- 奖励函数不是单一偏好分，而是把正确性、用户偏好、效率三者绑定；其中“只有答案正确时，偏好奖励才生效”是防止模型为了更顺耳而牺牲事实性的关键设计。

- 研究给出的信号很强：在搜索增强任务里，开源底模 + 精细后训练，已经能在事实性/成本曲线上逼近甚至压过闭源 GPT 系模型。

- 对 Agent 产品而言，这意味着竞争壁垒正在从“谁的底模更大”转向“谁的检索链路、训练数据和 reward engineering 更强”。

## 提取的概念

- [搜索增强语言模型](concepts/搜索增强语言模型.md)

- [监督微调](concepts/监督微调.md)

- [On-Policy RL](concepts/On-Policy RL.md)

- [正确性门控奖励](concepts/正确性门控奖励.md)

- [Qwen3.5](entities/Qwen3.5.md)

## 原始文章信息

- 作者：@perplexity_ai

- 来源：X书签

- 发布时间：2026-04-22

- 原文链接：[https://x.com/perplexity_ai/status/2047016400292839808](https://x.com/perplexity_ai/status/2047016400292839808)

- 研究链接：[https://research.perplexity.ai/articles/advancing-search-augmented-language-models](https://research.perplexity.ai/articles/advancing-search-augmented-language-models)

## 个人评注

这篇文章对 Tizer 当前的内容编译与 Agent 工作流很有参考价值：一方面，它证明了 **搜索/引用质量** 可以通过后训练被系统性优化，而不是只能依赖更强底模；另一方面，它也提示 OpenClaw 一类工作流型 Agent 的优化重点，应该放在检索轨迹、工具调用与奖励信号闭环，而不是单纯追求更大的模型参数。对于需要 HITL 审核、知识沉淀和内容管线复用的系统，这类“正确性优先、偏好次之、效率受约束”的训练思路尤其值得借鉴。
