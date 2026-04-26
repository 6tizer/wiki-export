---
title: File-as-Bus
type: concept
tags:
- Agent 协作模式
- 长期记忆
- 多Agent协作
status: 草稿
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/c75ed41262934d80b02a6a40b8b1162c
notion_id: c75ed412-6293-4d80-b02a-6a40b8b1162c
---

> 一句话定义：File-as-Bus 是一种把文件工作区作为长期状态总线来传递和复用项目证据的 Agent 设计机制。

### 定义

该机制不把长期状态主要寄托在聊天上下文里，而是把论文分析、实现计划、代码、实验日志、错误记录和中间结论持续写回共享工作区，让后续 Agent 能重新读取并接着工作。

### 关键要点

- 文件既是状态载体，也是跨代理协作的事实来源（多代理协调协议视角）

- 它让系统形成 evidence-driven loop，而不是空转式重试

- 适合长周期任务，运行痕迹持续保留在磁盘中，便于审计、恢复和复用

- 它对后半程 refinement 的价值大于对项目初始搭建的价值

- 消融实验显示，移除后会显著削弱高水平结果的达成能力

- 通过让代理直接读写工作区文件，可以降低厚状态任务中的上下文丢失风险

### 来源引用

- [AI 真能把一篇论文一路做到实验结果吗？人大团队提出 AiScientist，长程研究工程迈出关键一步](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDgzMA%3D%3D&mid=2247557693&idx=1&sn=367f8f10f46f5c95eecef42bd9280dc9&chksm=cf967e47a56f2e2647889686f1659551c441eaf8328436186303bca812623542fdfc4e646bf3#rd)｜作者：机智流｜源页面：AI 真能把一篇论文一路做到实验结果吗？人大团队提出 AiScientist，长程研究工程迈出关键一步

- [原文链接](https://mp.weixin.qq.com/s/5hQGUC6o-vLdcHVxVsOQwg)｜《Hermes Agent 网页控制台； AI原生社交平台；自主机器学习研究平台》｜源文章：Hermes Agent 网页控制台； AI原生社交平台；自主机器学习研究平台
