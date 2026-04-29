---
title: 摘要：实测Hy3 preview后我发现小看腾讯做大模型决心了
type: summary
tags:
- 模型评测
- AI 产品
status: 已审核
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b6881d1b953f7ad2e77b73a
notion_url: https://www.notion.so/Tizer/df8b7169083d4643b4ee71a76decea32
notion_id: df8b7169-083d-4643-b4ee-71a76decea32
---

## 一句话摘要

作者通过 WorkBuddy 对腾讯混元 Hy3 preview 进行了多维度实测（编程、Agent、网页设计、信息调研、人感），认为这款 295B MoE 模型虽非现阶段最强，但已具备进入真实工作流的能力，标志着混元在姚顺雨主导下完成底层重建后重新获得被认真测试的资格。

## 关键洞察

- Hy3 preview 采用快慢思考融合的 MoE 架构（总参 295B / 激活 21B / 256K 上下文），定位为可嵌入真实产品的模型，而非刷榜型

- 姚顺雨加入后三个月内完成预训练、强化学习、基础设施的全面重建，速度极快但也意味着打磨仍在进行中

- 在 WorkBuddy 上的 Agent 测试表现稳定：长文转书籍 Skill 能保持主线逻辑、3D 小游戏四五轮迭代即可运行、信息调研能区分来源层级并附链接

- 定价极具竞争力（输入 1.2 元 / 输出 4 元每百万 tokens），OpenRouter 免费试用至 5 月 8 日

- 人感维度仍有「模型装人」痕迹，但与 GPT 5.4 对比后差距并不明显，正式版若改善此项将为元宝、ima 等高频入口加分

## 提取的概念

- [Hy3 preview](entities/Hy3 preview.md)

- [MoE 架构](concepts/MoE 架构.md)

- [Workbuddy](entities/Workbuddy.md)

- [ReAct Agent](concepts/ReAct Agent.md)

- [SWE-agent](entities/SWE-agent.md)

## 原始文章信息

- **作者**：卡尔的AI沃茨

- **来源**：微信公众号

- **发布时间**：2026-04-28

- **原文链接**：[实测Hy3 preview后我发现小看腾讯做大模型决心了](https://mp.weixin.qq.com/s?__biz=Mzg3MTk3NzYzNw%3D%3D&mid=2247506706&idx=1&sn=0ddf8c92a703a8eba003560eb9cc75b5&chksm=cf3b2d9a092249426bcaaeec74a3511426d134adae8ec03e81caae3124cbb7db3151e8dc023f#rd)

## 个人评注

文章的测试方法论值得借鉴——不用聊天/知识问答来评估模型，而是放进真实 Agent 工作流（写书 Skill、网页设计、信息调研）中观察稳定性和任务完成度。这与 Tizer 的 HITL 理念一致：模型好不好，要看它能不能在 pipeline 里跑起来。Hy3 preview 的低价策略 + 产品端深度集成（元宝、CodeBuddy、WorkBuddy）也为 OpenClaw 选择国产模型做 fallback 提供了参考。
