---
title: 摘要：苹果新论文发出惊人一问：What do your logits know?
type: summary
tags:
- LLM
- 安全/隐私
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b6881b4af34fc9df5460fe1
notion_url: https://www.notion.so/893dc700d40748d1adf2a72df1f6e28d
notion_id: 893dc700-d407-48d1-adf2-a72df1f6e28d
---

## 一句话摘要

苹果最新论文指出：即使模型最终只输出看似无害的 top-k logits，这些表层概率分布依然可能泄露与任务无关的视觉细节，因此当前多模态模型并未真正遵守理想的信息瓶颈原则。

## 关键洞察

- 苹果团队用探针分别检查残差流与最终 logits，发现模型内部对原始图像信息的保留程度远高于直觉预期。

- 残差流几乎完整保留了目标属性、背景特征与噪声信息，说明深层隐藏状态并没有主动完成充分压缩。

- 即使只看最终层的少量 top-k logits，也能高准确率恢复目标属性、噪声类型，甚至提示词没有显式提到的特征。

- 当可见 logits 数量扩大到约 30-80 个时，泄露能力达到峰值，说明灰盒 API 暴露少量候选概率也可能带来真实隐私风险。

- 这项研究不仅是隐私问题，也解释了为什么模型顶层残留的无关信息可能在生成阶段干扰输出，进一步诱发幻觉或偏差。

## 提取的概念

- [信息瓶颈原则](concepts/信息瓶颈原则.md)

- [残差流](concepts/残差流.md)

- [Top-k Logits](concepts/Top-k Logits.md)

- [探针](concepts/探针.md)

- [灰盒 API](concepts/灰盒 API.md)

- [Tuned Lens](concepts/Tuned Lens.md)

## 原始文章信息

- 作者：机器之心

- 来源：微信

- 发布时间：2026-04-27 08:03

- 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651030149&idx=2&sn=963ed37cae4a5dd3e0b48da968103ece&chksm=859808b08729df737793e253933c5535aa28daafdcf794cff972d4b145547942a1f5468fb539#rd)

## 个人评注

这篇论文对 Tizer 的内容编译与 Agent 工作流很有提醒意义：如果未来在多模态 Agent、评测脚本或内容处理链路中开启 logprobs / top-k 概率输出，不应默认把它视为“无害调试信息”。对于涉及截图、文档、界面观察或用户上传素材的场景，top-k logits 本身就可能成为额外的数据泄露面，因此在 OpenClaw、HITL 或内容自动化管线里，最好把这类输出当成敏感中间态来最小化暴露与存储。
