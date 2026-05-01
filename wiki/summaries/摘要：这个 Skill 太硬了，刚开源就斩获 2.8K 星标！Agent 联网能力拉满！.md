---
title: 摘要：这个 Skill 太硬了，刚开源就斩获 2.8K 星标！Agent 联网能力拉满！
type: summary
tags:
- 浏览器自动化
- MCP 协议
- 多Agent协作
status: 已审核
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: https://www.notion.so/343701074b6881b78867efa691b4a117
notion_url: https://www.notion.so/Tizer/0e3be810f1624ca0833690f91128bcaa
notion_id: 0e3be810-f162-4ca0-8336-90f91128bcaa
---

## 一句话摘要

web-access 通过把 Skill 方法论与真实浏览器控制结合起来，让 Claude Code、Codex 一类 Agent 在需要登录态和动态渲染的网站上具备更可靠的联网执行能力。

## 关键洞察

- web-access 强调自己是 **Skill** 而不是单纯的 [MCP 协议](concepts/MCP 协议.md) 接口，除了给工具，还给工具调度与任务执行方法。

- 它把 [Chrome DevTools MCP](entities/Chrome DevTools MCP.md)、[Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md) 与新建的 [CDP Proxy](concepts/CDP Proxy.md) 组合起来，直接复用用户日常 Chrome 的登录态。

- 在普通网页可抓取时优先走轻量方案，遇到动态渲染、登录墙、反爬再升级到浏览器模式，体现了渐进式工具切换策略。

- 文章展示了竞品调研、小红书舆情整理、GitHub 提交周报三类场景，说明这种能力既适用于研究，也适用于开发工作流。

- 多子 Agent 并行分治是这套方案的重要效率层设计，使多个目标的调研时间接近单目标处理时间。

## 提取的概念

- [web-access](entities/web-access.md)

- [Chrome DevTools MCP](entities/Chrome DevTools MCP.md)

- [Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md)

- [CDP Proxy](concepts/CDP Proxy.md)

- [MCP 协议](concepts/MCP 协议.md)

## 原始文章信息

- 作者：沉默王二

- 来源：微信

- 发布时间：2026-03-31 14:05

- 原文链接：[https://mp.weixin.qq.com/s?__biz=MzIxNzQwNjM3NA==&mid=2247546207&idx=1&sn=772820dba9a7a0a037b4bad24eee51ad&chksm=962fbc784ab760b642a982a17ee1b7a251fc8dd1573eef97759423d6400035677c10ff9ab5ae#rd](https://mp.weixin.qq.com/s?__biz=MzIxNzQwNjM3NA%3D%3D&mid=2247546207&idx=1&sn=772820dba9a7a0a037b4bad24eee51ad&chksm=962fbc784ab760b642a982a17ee1b7a251fc8dd1573eef97759423d6400035677c10ff9ab5ae#rd)

## 个人评注

这篇文章对 Tizer 的价值不在于单个工具本身，而在于它提示了一条更适合内容采集与知识编译的联网路线：先用轻量抓取完成大多数任务，再在必要时切换到浏览器执行层。对 HITL 内容流水线、OpenClaw 相关浏览器自动化能力，以及后续需要处理登录态网页的知识采集场景，都有直接参考意义。
