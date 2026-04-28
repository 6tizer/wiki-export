---
title: AI Scientist
type: entity
tags:
- Agent 协作模式
- 多Agent协作
- AI 产品
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c3b2cde957794a578de41558a1915e01
notion_id: c3b2cde9-5779-4a57-8de4-1558a1915e01
---

## 简介

AI Scientist 是一类由 Agent 自动提出研究想法、实现实验、诊断问题并生成论文或报告的自动化科研系统，也常特指相关代表性项目。它关注的不是单点代码生成，而是围绕同一研究目标持续推进完整研究工程。

## 关键要点

- 目标覆盖想法、实验到写作的完整链路，比只做自动实验或单轮代码生成更长链条

- 关键能力在于跨轮次保留项目状态，让前一轮的实现、日志与诊断结果成为下一轮改进依据

- 常见设计包括分层编排、轻控制厚状态，以及把分析、代码、日志和中间结论沉淀为可复用资产

- 这类系统经常被拿来与 autoresearch 等更聚焦的自动实验框架对照理解

- 提供论文复现（paper）与机器学习工程（mle）两条主工作流，覆盖从阅读、规划到实验验证的完整闭环

## 关键数据

- 相关工作强调 machine learning research engineering 场景

- 典型评测包括 PaperBench 与 MLE-Bench Lite

- GitHub：[https://github.com/AweAI-Team/AiScientist](https://github.com/AweAI-Team/AiScientist)

## 来源引用

- [原文链接](https://x.com/yibie/status/2031222960372199523)｜《AutoResearch：Karpathy 让 AI 自主跑实验的方法论，以及它如何改变你的工作方式》｜来源条目：[摘要：AutoResearch：Karpathy 让 AI 自主跑实验的方法论，以及它如何改变你的工作方式](summaries/摘要：AutoResearch：Karpathy 让 AI 自主跑实验的方法论，以及它如何改变你的工作方式.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDgzMA%3D%3D&mid=2247557693&idx=1&sn=367f8f10f46f5c95eecef42bd9280dc9&chksm=cf967e47a56f2e2647889686f1659551c441eaf8328436186303bca812623542fdfc4e646bf3#rd)｜《AI 真能把一篇论文一路做到实验结果吗？人大团队提出 AiScientist，长程研究工程迈出关键一步》｜来源条目：[摘要：AI 真能把一篇论文一路做到实验结果吗？人大团队提出 AiScientist，长程研究工程迈出关键一步](summaries/摘要：AI 真能把一篇论文一路做到实验结果吗？人大团队提出 AiScientist，长程研究工程迈出关键一步.md)

- [原文链接](https://mp.weixin.qq.com/s/5hQGUC6o-vLdcHVxVsOQwg)｜《Hermes Agent 网页控制台； AI原生社交平台；自主机器学习研究平台》｜来源条目：[摘要：Hermes Agent 网页控制台； AI原生社交平台；自主机器学习研究平台](summaries/摘要：Hermes Agent 网页控制台； AI原生社交平台；自主机器学习研究平台.md)

## 相关概念

- [autoresearch](entities/autoresearch.md)

- [PaperBench](entities/PaperBench.md)

- [MLE-Bench Lite](entities/MLE-Bench Lite.md)

- [分层编排](concepts/分层编排.md)

- [File-as-Bus](concepts/File-as-Bus.md)
