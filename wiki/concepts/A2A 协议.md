---
title: A2A 协议
type: concept
tags:
- 商业/生态
status: 已审核
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f5a880f9619b42c488541b3d4616c371
notion_id: f5a880f9-619b-42c4-8854-1b3d4616c371
---

## 定义

A2A 协议（Agent-to-Agent 协议）是让不同 AI Agent 彼此发现、发送任务、交换结果并协调执行的通信标准，是多智能体协作的基础协议层。

## 关键要点

- 它把 Agent 间互联从临时消息传递提升为可标准化、可编排的协议接口。

- 常见能力包括服务发现、任务发送、结果回传与会话协调。

- 在 OpenClaw 等生态中，当前 A2A 实践仍常依赖 `sessions_send` 或通过外部通道间接传递，协议化的价值正在于降低这类手工搬运成本。

- 当 A2A 与支付、定价和身份信任层结合时，可进一步支撑代理间交易市场。

- 安全仍是关键前提，开放的 A2A 节点一旦直接暴露公网，就会成为新的攻击面。

## 代表项目 / 实践

- **AgentComm**：OpenClaw 生态里的 A2A 通信 Skill，强调分布式通信与文件传输，规划路径是通信 → 转账 → 群聊。

- **Hermes + OpenClaw**：用极简 Python Server 把不同 CLI Agent 封装为 A2A 节点，验证了跨机器、低成本互联的可行性。

## 关联概念

- [A2UI 协议](concepts/A2UI 协议.md)

- [AG2](entities/AG2.md)

- [json-render](entities/json-render.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Google ADK](entities/Google ADK.md)

- [Gemini CLI](entities/Gemini CLI.md)

- [Antigravity](entities/Antigravity.md)

- [ClawTip](entities/ClawTip.md)

- [Agent 经济闭环](concepts/Agent 经济闭环.md)

- [MCP 协议](concepts/MCP 协议.md)

- [AG-UI](concepts/AG-UI.md)

- [外部化](concepts/外部化.md)

## 来源引用

- [摘要：没有「身份证」的 Agent，接管不了世界](summaries/摘要：没有「身份证」的 Agent，接管不了世界.md)（[原文](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ%3D%3D&mid=2653104491&idx=1&sn=9d2e0837580b4d9cc5cb5af901faef7c&chksm=7f84afe217328ff0a83664012a2c38639db2a6cb1572651e9b0b6aec39ef8aab9d5263cf1715#rd)）

- [摘要：OpenClaw正在成为新的交互入口，AI投资人：这4个生态位，短期内会爆发机会](summaries/摘要：OpenClaw正在成为新的交互入口，AI投资人：这4个生态位，短期内会爆发机会.md)（[原文](https://x.com/0xKingsKuan/status/2035029914844635315)）

- [摘要：用 50 行 Python 跑通 Google A2A 协议：Hermes + OpenClaw 的多 Agent 互联实践](summaries/摘要：用 50 行 Python 跑通 Google A2A 协议：Hermes + OpenClaw 的多 Agent 互联实践.md)（[原文](https://x.com/YuLin807/status/2041667865477312551)）

- [摘要：别人都在卷Harness， 而Google 的沉默振聋发聩](summaries/摘要：别人都在卷Harness， 而Google 的沉默振聋发聩.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkyNjU2ODM2NQ%3D%3D&mid=2247627539&idx=1&sn=da04448ed2172c5381d68b24e0454247&chksm=c31182e7c7ef6bde7a36b46d0bcde4b0b20f049b7cdbbe53d6ae77d1d83ea99c2250b5f96f56#rd)）

- [摘要：开发者的福音来了！ 京东ClawTip让你的Skill自动赚钱！](summaries/摘要：开发者的福音来了！ 京东ClawTip让你的Skill自动赚钱！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzAxMjUyNDQ5OA%3D%3D&mid=2653588165&idx=1&sn=0e0410e1d88cc5ad869c483fbd623864&chksm=8117dbc85ccbaa434bf29379eae62e8bcf7369e5d40eb167b51fe0d75aedc4c94a5c5efd5171#rd)）

- [摘要：Google发布A2UI 0.9：AI直接生成界面](summaries/摘要：Google发布A2UI 0.9：AI直接生成界面.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzY5MjE2OTU5Mg%3D%3D&mid=2247484380&idx=1&sn=86632002fdf6fcdd5a9c2e5bedae3252&chksm=f5bdb6949b80daed06d25e00b23e76dec8e7771b3f9a448172ebb4de6731c3811c33c0061231#rd)）

- [摘要：上交大54页综述讲透Agent认知外部化的演进之路](summaries/摘要：上交大54页综述讲透Agent认知外部化的演进之路.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651029194&idx=2&sn=d468f16ac694682f072e150ac531e5a2&chksm=85cd02c33fc1ca1088db4f4f1a5b2219ed652157b32c004b7ef2cfb994654cfdfdd0d38512e7#rd)）

- [摘要：Hermes-a2a](summaries/摘要：Hermes-a2a.md)（[原文](https://x.com/0xViviennn/status/2047626457191780527)）
