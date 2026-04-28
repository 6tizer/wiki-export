---
title: 摘要：小米 MiMo-V2.5 系列开源 & Orbit 百万亿 Token 计划启动
type: summary
tags:
- 商业/生态
- 模型部署
- 算力基础设施
status: 已审核
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: https://www.notion.so/350701074b68815aa707e50bfa6ad96f
notion_url: https://www.notion.so/Tizer/156dc21b7f2c43a69b5958cac386f297
notion_id: 156dc21b-7f2c-43a6-9b59-58cac386f297
---

## 一句话摘要

小米正式以 MIT 协议全量开源 MiMo-V2.5 系列模型（含 Base 权重），并同步启动 MiMo Orbit 计划——面向全球开发者发放 100 万亿 Token 权益、面向 Agent 框架团队提供生态共建支持。

## 关键洞察

- MiMo-V2.5 系列包含两款模型：**MiMo-V2.5-Pro**（面向 Agent + Coding，GDPVal-AA 与 Claw-Eval 开源模型第一）和 **MiMo-V2.5**（原生全模态，支持文/图/视频/音频理解），均支持 100 万上下文窗口。

- 全量开源采用 **MIT 协议**，允许自由商用、二次训练与微调，无需额外授权——这在国产大模型中属于较激进的开放策略。

- **MiMo Orbit 计划**分两部分：百万亿 Token 创造者激励计划（30 天内发放 100T Token，最高 16 亿 Credits / 659 元）和 Agent 生态共建计划（为框架团队提供 Token 限免 + Hackathon 赞助）。

- 芯片生态适配首日覆盖阿里平头哥、亚马逊 Trainium2、AMD ROCm、百度昆仑芯、燧原科技、沐曦、天数智芯等七家厂商，同时完成 SGLang 和 vLLM 推理框架的 Day-0 适配。

- 已与 OpenCode、Hermes Agent、KiloCode 等 Agent 框架厂商建立深度合作，生态布局从模型→推理→应用层全面铺开。

## 提取的概念

- [Xiaomi MiMo-V2.5-Pro](entities/Xiaomi MiMo-V2.5-Pro.md)

- [Xiaomi MiMo-V2.5](entities/Xiaomi MiMo-V2.5.md)

- [Xiaomi MiMo Orbit](entities/Xiaomi MiMo Orbit.md)

- [GDPVal](concepts/GDPVal.md)

- [Claw-Eval](entities/Claw-Eval.md)

## 原始文章信息

- 作者：Xiaomi MiMo

- 来源：微信公众号

- 发布时间：2026-04-27

- 原文链接：[小米 MiMo-V2.5 系列开源 & Orbit 百万亿 Token 计划启动](https://mp.weixin.qq.com/s?__biz=Mzk3NTkxMTM2NA%3D%3D&mid=2247484681&idx=1&sn=60241f47e569b8105e66bf704cd4c98b&chksm=c50137dcd08f21a4eb67a631268f2b59dcc62a811ba5f31be372f09d38e5300b8474690cc111#rd)

## 个人评注

小米在 MiMo-V2.5 上的动作从模型开源、Token 激励到芯片/框架适配一条龙推进，商业化路径清晰：用免费 Token 圈开发者生态，再用 Agent 框架合作绑定上游应用。对 Tizer 的内容管线而言，MiMo-V2.5-Pro 的长上下文 + Agent 能力值得在 OpenClaw harness 里做一轮基准测试，尤其是其 Claw-Eval 表现。MIT 协议也意味着可以安心做二次微调实验。
