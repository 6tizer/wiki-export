---
title: 摘要：OpenClaw 进阶手册 Vol.3：跑稳之后，才是真的开始
type: summary
tags:
- OpenClaw
- 多Agent协作
- Agent 协作模式
- 浏览器自动化
status: 已审核
confidence: high
last_compiled: '2026-04-10'
source_tags: NewStuff
source_article_url: ''
notion_url: https://www.notion.so/Tizer/fcd1bacf91b449b0b523d155b0dbbcb5
notion_id: fcd1bacf-91b4-49b0-b523-d155b0dbbcb5
---

## 一句话摘要

OpenClaw 生产环境运维的 25 个实战技巧，涵盖成本控制、故障检测、可观测性、状态管理和长期维护五大主题，帮助用户从「能跑」过渡到「跑稳」。

## 关键洞察

- **成本控制的核心不是选模型，而是控制子 Agent 继承行为**：子 Agent 默认继承主 Agent 模型，5 个并行子任务可能让账单翻倍。通过 `subagents.model` 分级配置不同模型是最有效的成本手段。

- **最危险的故障是静默失败**：Agent 显示 `completed` 但没有实际输出，常见于 Heartbeat 推送目标不稳定、子 Agent 输出格式不匹配、Browser 截到登录页等场景。需通过心跳文件 + 监控 Cron 主动发现。

- **`runTimeoutSeconds`**** 是兜底机制而非解决方案**：超时后主 Agent 不会自动收到错误信号，需要在 task 中预写处理策略（允许不完整结果 vs 任意失败即终止）。

- **文件系统是 Agent 唯一的持久化存储**：推荐 `data/` 与 `workspace/` 分离，数据文件首行带更新时间戳，重要文件先写临时文件再重命名。

- **用 git 管理 ****`~/.openclaw/`**** 配置是长期运维的基础**：配置出问题时，「最近改了什么」比「哪里错了」更重要。

## 提取的概念

- [Agent 成本控制](concepts/Agent 成本控制.md)

- Fallback 模型

- [Agent 静默失败](concepts/Agent 静默失败.md)

- Webhook 幂等性

- [Agent 可观测性](concepts/Agent 可观测性.md)

- Cron 自动化（已有词条）

## 原始文章信息

- **作者**：[请致天下.AI](http://xn--ghqv4yd56a5mi.ai/)

- **来源**：微信公众号

- **发布时间**：2026-02-28

- **链接**：[https://mp.weixin.qq.com/s?__biz=MjM5MDQ3NzI3NA==&mid=2652094572&idx=1&sn=96da3c2d201d36180c5cf00f7ec0d0cb](https://mp.weixin.qq.com/s?__biz=MjM5MDQ3NzI3NA%3D%3D&mid=2652094572&idx=1&sn=96da3c2d201d36180c5cf00f7ec0d0cb)

## 个人评注

这篇文章对 Tizer 的 OpenClaw 运维实践高度相关。特别是静默失败检测（心跳文件方案）、成本控制（子 Agent 模型分级）、以及文件系统规范，可以直接应用到当前 HITL 和 content pipeline 的 Agent 工作流中。git 管理配置的建议也值得在 OpenClaw 部署中采纳。
