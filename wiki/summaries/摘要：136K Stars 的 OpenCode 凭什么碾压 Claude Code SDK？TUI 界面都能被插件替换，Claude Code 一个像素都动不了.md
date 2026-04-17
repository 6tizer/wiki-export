---
title: 摘要：136K Stars 的 OpenCode 凭什么碾压 Claude Code SDK？TUI 界面都能被插件替换，Claude Code 一个像素都动不了
type: summary
tags:
- Coding Agent
- Agent 编排
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b688183a19cd03f2304a620
notion_url: https://www.notion.so/14eaf4b28f1e438681e1a8e2bda40ed9
notion_id: 14eaf4b2-8f1e-4386-81e1-a8e2bda40ed9
---

## 一句话摘要

这篇文章认为，AI Coding Agent 的真正差异不在 Rules、Hooks、MCP 这类配置层开放性，而在能否深入改造 Agent Loop、工具、模型调用与上下文处理等**内核可编程性**。

## 关键洞察

- OpenCode 是四者中开放度最高的方案，几乎在 Agent Loop 周边的关键层都暴露了可编程接口，尤其在 provider、messages transform 与 TUI 插件体系上优势明显。

- Claude Agent SDK 的强项是把 Anthropic 的 Agent Runtime 封装成稳定 SDK，适合嵌入业务系统，但核心 loop、provider、推理参数与消息历史仍是黑盒。

- Codex 走的是“源码可 fork + 协议可嵌入”的路线，源码级自由度很高，但不 fork 时 Hook 层较薄，更多依赖 App Server 做外部集成。

- Cursor 的开放性主要停留在 IDE 内部的配置与插件生态层，重点是提升使用体验，而不是让开发者基于其内核继续造产品。

- 对 Tizer 的工作流来说，这篇文章最有价值的不是产品排行，而是提供了一个评估 Coding Agent 的统一框架：要区分“能不能用”与“能不能被改造成自己的基础设施”。

## 提取的概念

- [OpenCode](entities/OpenCode.md)

- [Claude Agent SDK](entities/Claude Agent SDK.md)

- [Codex](entities/Codex.md)

- [Cursor](entities/Cursor.md)

- [Agent Loop](concepts/Agent Loop.md)

- [内核可编程性](concepts/内核可编程性.md)

## 原始文章信息

- 作者：歪脖抠腚

- 来源：微信

- 发布时间：2026/04/14

- 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=MzY0MDAzNzk3MA%3D%3D&mid=2247484430&idx=1&sn=a8cd136df0161ab4a5fe53b3a6a65990&chksm=f1c76fc519e5fdfca727bfdba977647d756e2865da0de591baae80902002af1c8c1d324b1a9e#rd)

## 个人评注

这篇文章很适合作为 Tizer 后续评估 Agent 基础设施的参照模板。若目标是做 OpenClaw、HITL 或内容流水线背后的可演化底座，就不能只看产品是否好用，而要优先看它是否支持二次封装、权限治理、上下文重写与工具替换。
