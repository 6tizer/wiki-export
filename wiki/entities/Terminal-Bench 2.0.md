---
title: Terminal-Bench 2.0
type: entity
tags:
- 模型评测
- CLI 工具
- 代码生成
status: 审核中
confidence: high
last_compiled: '2026-04-25'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/0c445748e9294f00a39b12a0c0c2ecca
notion_id: 0c445748-e929-4f00-a39b-12a0c0c2ecca
---

## 定义

Terminal-Bench 2.0 是一个面向终端场景的编程能力测试基准，用于衡量模型在 Shell 操作、文件管理、进程控制等真实命令行任务中的完成能力。

## 关键要点

- 相比静态问答，它更接近开发者真实使用终端完成任务的场景

- 这类基准强调工具使用、命令执行与长链路任务完成，而不只是代码补全

- 文中将其作为 Qwen 3.6-Plus 在 Agentic Coding 方向的重要硬指标之一

## 关联概念

- [GPT-5.5](entities/GPT-5.5.md)

- [Agentic Coding](concepts/Agentic Coding.md)

- [Qwen3.6-27B](entities/Qwen3.6-27B.md)

- [Qwen3.6-35B-A3B](entities/Qwen3.6-35B-A3B.md)

- [Dense 模型](concepts/Dense 模型.md)

- [SWE-bench](concepts/SWE-bench.md)

- [Meta-Harness](concepts/Meta-Harness.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [长时程信用分配](concepts/长时程信用分配.md)

- [Kimi K2.6](entities/Kimi K2.6.md)

- [Cline](entities/Cline.md)

- [Vercel AI Gateway](entities/Vercel AI Gateway.md)

- [Claude Opus 4.7](entities/Claude Opus 4.7.md)

- [SWE-bench Pro](concepts/SWE-bench Pro.md)

- [OSWorld-Verified](entities/OSWorld-Verified.md)

- [Agentic Workflow](concepts/Agentic Workflow.md)

- [自托管](concepts/自托管.md)

- [LLM-as-a-Verifier](concepts/LLM-as-a-Verifier.md)

- [SWE-Bench Verified](entities/SWE-Bench Verified.md)

## 来源引用

- [摘要：Introducing GPT-5.5](summaries/摘要：Introducing GPT-5.5.md)（[原文](https://x.com/OpenAI/status/2047376561205325845)）

- [摘要：With 3.6-27b release, the dense-over-MoE gap is shrinking, which is good for local AI as MoE like 35b-a3b are more friendly on low-budget GPU and support much longer context (256k full easily on 24gb](summaries/摘要：With 3.6-27b release, the dense-over-MoE gap is shrinking, which is good for local AI as MoE like 35b-a3b are more friendly on low-budget GPU and support much longer context (256k full easily on 24gb.md)（[原文](https://x.com/hxiao/status/2047004358500614152)）

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzA5ODEzMjIyMA%3D%3D&mid=2247733292&idx=1&sn=e39369ea00846c222739652d5b47bcc8&chksm=913f8f245def967dec5b7fa87346d1d1fb0f05e5f0084f9bccfc6aeaf678203157c80fe2767b#rd)｜《「双线实测」Qwen 3.6-Plus，Agentic Coding 已经这么能“扛活儿”了？》｜源文章：「双线实测」Qwen 3.6-Plus，Agentic Coding 已经这么能“扛活儿”了？

- [原文链接](https://x.com/yoonholeee/status/2044442372864700510)｜《Meta-Harness 代码开源：让 Agent 在新领域自主优化 Harness》｜来源条目：[摘要：Meta-Harness 代码开源：让 Agent 在新领域自主优化 Harness](summaries/摘要：Meta-Harness 代码开源：让 Agent 在新领域自主优化 Harness.md)

- [摘要：刚刚，千问最强模型发布，登顶国产最佳](summaries/摘要：刚刚，千问最强模型发布，登顶国产最佳.md)（[原文](https://mp.weixin.qq.com/s?__biz=MjM5MjAyNDUyMA%3D%3D&mid=2651088482&idx=1&sn=f82d4a5697aef837b57ea6353285d4be&chksm=bcff0435172cd02b80b80bc26991b8c0718cb409d76938cfb784f9aa171331118262579e5653#rd)）

- [摘要：Kimi K2.6 is free on Cline for the next 3 days in partnership with @vercel AI Gateway.](summaries/摘要：Kimi K2.6 is free on Cline for the next 3 days in partnership with @vercel AI Gateway.md)（[原文](https://x.com/cline/status/2047038658470142148)）

- [摘要：我用 DeepSeek V4 测了一把 GPT 5.5 和 Opus 4.7 ，结果很离谱。。。](summaries/摘要：我用 DeepSeek V4 测了一把 GPT 5.5 和 Opus 4.7 ，结果很离谱。。。.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI0ODk2NDIyMQ%3D%3D&mid=2247503221&idx=1&sn=3abe9c7d236f01328eff06cd93eb7286&chksm=e82a4c1d62d3dd1ee3fd07f99ef1de65c916585b4cb636d26a2e714edc4dfd62c9315a534f8c#rd)）

- [摘要：3B的成本，35B的智力：Qwen 3.6 正在暴力拆解 AI 商业化的成本围墙](summaries/摘要：3B的成本，35B的智力：Qwen 3.6 正在暴力拆解 AI 商业化的成本围墙.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU4OTY4MDU4MQ%3D%3D&mid=2247490900&idx=1&sn=823e360812006af69f9c2e01cf2d3601&chksm=fc955696662d95b68a7dfab13245552377720ba90794116217337957a434e9e8544f71d19a9d#rd)）

- [摘要：超越Claude Mythos和GPT-5.5！斯坦福推出Agent验证框架「LLM-as-a-Verifier」](summaries/摘要：超越Claude Mythos和GPT-5.5！斯坦福推出Agent验证框架「LLM-as-a-Verifier」.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651030107&idx=2&sn=dcf949e41eb246cd78463ec2ac79eb17&chksm=85f6580c4d8619e4dbb67c7144f147a8bc41f01f639924649cbbb134ea5daa9c1e2bdebb2928#rd)）
