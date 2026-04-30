---
title: 摘要：刚刚，DeepSeek最新成果，节前发布！
type: summary
tags:
- 多模态
- 推理优化
- AI 产品
status: 已审核
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: https://www.notion.so/352701074b68811fb5eec767aaee3c97
notion_url: https://www.notion.so/Tizer/6c89e19cf0904ee690d8eeeb45473112
notion_id: 6c89e19c-f090-4ee6-90d8-eeeb45473112
---

## 一句话摘要

DeepSeek 多模态组联合北大、清华发布论文《Thinking with Visual Primitives》，提出在思维链中嵌入坐标 token（视觉原语）解决多模态推理的「引用差距」问题，同时 DeepSeek 主产品首次上线识图模式。

## 关键洞察

- **Reference Gap 是真正瓶颈**：多模态模型在复杂任务上崩溃，常不是「看不见」而是「指不准」——自然语言无法在连续视觉空间中精确锚定物体，CoT 跑长会丢失对视觉实体的追踪

- **Visual Primitives 嵌入 CoT**：模型在推理时插入 bounding box 和 point 坐标 token 作为「思考的最小单位」，灵感来自人类用手指点数和目光追踪

- **极致 KV Cache 压缩**：756×756 图片从 2916 个 patch token 压缩到仅 81 条视觉 KV cache 条目，端到端压缩比 7,056 倍，与 V4-Flash 同款架构（284B 总参/13B 激活/CSA+HCA）

- **「先专家、再合并」训练流程**：分别训练 box 专家和 point 专家，各自 GRPO 强化学习后，通过 On-Policy Distillation 统一为一个模型

- **拓扑推理大幅领先**：迷宫导航 66.9 vs GPT-5.4 的 50.6（+16.3），路径追踪 56.7 vs 46.5（+10.2），所有前沿模型在这两项上集体卡在 50% 上下

## 提取的概念

- [Visual Primitives](concepts/Visual Primitives.md)：视觉原语，在 CoT 中嵌入 box/point 坐标 token

- [Reference Gap](concepts/Reference Gap.md)：引用差距，多模态推理的核心瓶颈

- [KV Cache 压缩](concepts/KV Cache 压缩.md)：DeepSeek 极致视觉 token 压缩技术

- [DeepSeek V4](entities/DeepSeek V4.md)：同款架构（284B-A13B），V4-Flash 变体

- [GRPO](concepts/GRPO.md)：强化学习优化器，用于训练 box/point 专家

- [On-Policy Distillation](concepts/On-Policy Distillation.md)：将两个专家模型统一蒸馏的训练方法

## 原始文章信息

- **作者**：Datawhale

- **来源**：微信公众号

- **发布时间**：2026-04-30

- **文章链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg%3D%3D&mid=2247722411&idx=1&sn=bdec00adace587c9737956cd7554bdb4&chksm=e900cea0128d25e4398f9e439ce550cf8de63aabb709f43fd4040baeceb7cd184cf5104f51f7#rd)

- **论文地址**：[GitHub - Thinking with Visual Primitives](https://github.com/deepseek-ai/Thinking-with-Visual-Primitives/)

## 个人评注

DeepSeek 的多模态路线与 OpenAI 的「Thinking with Images」形成差异化竞争：别人卷更多像素，DeepSeek 卷更少像素但更精准的指向。KV Cache 极致压缩是贯穿 V3→V4 全系列的核心工程能力，「省 token 预算→塞更贵能力」的设计哲学值得 OpenClaw 在资源受限场景下借鉴。拓扑推理能力的突破（迷宫/路径追踪）对 Agent 的空间推理和规划场景有直接启发。
