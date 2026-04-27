---
title: Agent Harness
type: concept
tags:
- Harness 工程
- 上下文管理
status: 审核中
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/dcd58da1f13f4d10bb04047f0678e5c4
notion_id: dcd58da1-f13f-4d10-bb04-047f0678e5c4
---

## 定义

Agent Harness 是围绕模型构建的一层执行底座，负责提供工具调用、上下文管理、权限控制、记忆与监督循环等基础设施。

## 关键要点

- 它强调模型之外的“手、眼、记忆与护栏”能力

- 是把聊天模型变成可执行 Agent 的关键工程层

- 轻量 Harness 的价值常在于更透明、更容易读懂和二次开发

## 关联概念

- [OpenHarness](entities/OpenHarness.md)

- [Lifecycle Hooks](concepts/Lifecycle Hooks.md)

- [权限与安全层](concepts/权限与安全层.md)

- [agentmemory](entities/agentmemory.md)

- [持久化跨会话记忆](concepts/持久化跨会话记忆.md)

- [Better-Harness](entities/Better-Harness.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Sandbox Agents](concepts/Sandbox Agents.md)

- [编排与计算分离](concepts/编排与计算分离.md)

- [In Distribution](concepts/In Distribution.md)

- [Evals](concepts/Evals.md)

- [Holdout Set](concepts/Holdout Set.md)

- [Terminal Bench 2](entities/Terminal Bench 2.md)

- [Open Memory](concepts/Open Memory.md)

- [Memory Lock-in](concepts/Memory Lock-in.md)

- [Context Engineering](concepts/Context Engineering.md)

- [Prompt Engineering](concepts/Prompt Engineering.md)

- [Agent Skills](concepts/Agent Skills.md)

- [SkillHub](entities/SkillHub.md)

- [OpenClaw](entities/OpenClaw.md)

- [Thin Harness, Fat Skills](concepts/Thin Harness, Fat Skills.md)

- [Agent 协议层](concepts/Agent 协议层.md)

- [Mediator 层](concepts/Mediator 层.md)

- [Resolver](concepts/Resolver.md)

- [Latent vs. Deterministic](concepts/Latent vs. Deterministic.md)

- [Antigravity](entities/Antigravity.md)

- [Claude Managed Agents](entities/Claude Managed Agents.md)

- [Google ADK](entities/Google ADK.md)

- [A2A 协议](concepts/A2A 协议.md)

- [Gemini CLI](entities/Gemini CLI.md)

- [TPU](entities/TPU.md)

- [Cursor](entities/Cursor.md)

- [NVIDIA](entities/NVIDIA.md)

- [Blackwell 200 GPU](entities/Blackwell 200 GPU.md)

- [SOL-ExecBench](entities/SOL-ExecBench.md)

- [CUDA 内核优化](concepts/CUDA 内核优化.md)

- [CuTe DSL](concepts/CuTe DSL.md)

- [Coding Agent](concepts/Coding Agent.md)

- [软件工厂](concepts/软件工厂.md)

- [Notion 风格 Markdown](concepts/Notion 风格 Markdown.md)

- [MCP 协议](concepts/MCP 协议.md)

- [Notion Custom Agents](entities/Notion Custom Agents.md)

- [群体智能](concepts/群体智能.md)

- [认知碰撞](concepts/认知碰撞.md)

- [明日新程](entities/明日新程.md)

- [团子](entities/团子.md)

- [OpenMontage](entities/OpenMontage.md)

- [UniVA](entities/UniVA.md)

- [VideoAgent](entities/VideoAgent.md)

- [ViMax](entities/ViMax.md)

- [Claw Code](entities/Claw Code.md)

- [oh-my-codex](entities/oh-my-codex.md)

- [Parity Harness](concepts/Parity Harness.md)

- [Bug-for-bug 兼容](concepts/Bug-for-bug 兼容.md)

- [净室重写](concepts/净室重写.md)

- [反蒸馏](concepts/反蒸馏.md)

- [Computer Use](concepts/Computer Use.md)

- [红队演练](concepts/红队演练.md)

- [CrabTrap](entities/CrabTrap.md)

- [TLS 拦截](concepts/TLS 拦截.md)

- [流量归纳策略](concepts/流量归纳策略.md)

- [策略回放评测](concepts/策略回放评测.md)

- [LLM-as-a-Verifier](concepts/LLM-as-a-Verifier.md)

## 来源引用

- [摘要：Lightweight agent harness for building AI agents!](summaries/摘要：Lightweight agent harness for building AI agents!.md)（[原文](https://x.com/Sumanth_077/status/2046929191795593517)）

- [摘要：What is an Agent Harness](summaries/摘要：What is an Agent Harness.md)（[原文](https://x.com/aparnadhinak/status/2046980769747533830)）

- [摘要：CrabTrap: an LLM-as-a-judge HTTP proxy to secure agents in production](summaries/摘要：CrabTrap- an LLM-as-a-judge HTTP proxy to secure agents in production.md)（[原文](https://x.com/pedroh96/status/2046604993982009825)）

- [摘要：Claude Opus 4.7 自我越狱：当 AI 开始审计自己的「笼子」](summaries/摘要：Claude Opus 4.7 自我越狱：当 AI 开始审计自己的「笼子」.md)（[原文](https://x.com/elder_plinius/status/2045682830383231474)）

- [摘要：Memory](summaries/摘要：Memory.md)（[原文](https://x.com/akshay_pachaar/status/2045510648474530263)）

- [摘要：local-first AI assistant built for personal AI sovereignty](summaries/摘要：local-first AI assistant built for personal AI sovereignty.md)（[原文](https://x.com/ghumare64/status/2045291112454402194)）

- [原文链接](https://mp.weixin.qq.com/s?__biz=MjM5OTE0ODA2MQ%3D%3D&mid=2650996439&idx=1&sn=b0e8f9460d31651bdd374eae18db74f6&chksm=bdd2ba711515b068254cc8fae7b1d613c0f7602c73faca901e0862da74272e110b494db13b0f#rd)｜《汤道生：人工智能正式进入 Harness 时代》｜来源条目：[摘要：汤道生：人工智能正式进入 Harness 时代](summaries/摘要：汤道生：人工智能正式进入 Harness 时代.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493153&idx=1&sn=72c2e68a8f7d0643e26798536ebdcddf&chksm=c0f2fc5aeb871deb50d997025e1dec3f07677e1f3f1fa9185c61aca0e43ef4093d44ff6ec270#rd)｜《用 Rust 重写的 Claw Code ,已经178K Star !有些东西看了后，睡不着觉》｜来源条目：[摘要：用 Rust 重写的 Claw Code ,已经178K Star !有些东西看了后，睡不着觉](summaries/摘要：用 Rust 重写的 Claw Code ,已经178K Star !有些东西看了后，睡不着觉.md)

- [原文链接](https://x.com/LangChain/status/2042268554364592543)｜《LangChain Deep Agents Deploy：开源 Agent 部署的生产级方案》｜来源条目：[摘要：LangChain Deep Agents Deploy：开源 Agent 部署的生产级方案](summaries/摘要：LangChain Deep Agents Deploy：开源 Agent 部署的生产级方案.md)

- [原文链接](https://x.com/Jason23818126/status/2040624214303211626)｜《OpenHarness：港大开源的 Claude Code 轻量平替，44 倍瘦身只保留 98% 核心功力》｜源文章：OpenHarness：港大开源的 Claude Code 轻量平替，44 倍瘦身只保留 98% 核心功力

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ%3D%3D&mid=2461159297&idx=1&sn=e1d1550d8c29f6c57f344e9bd7619931&chksm=8645d4fd11f0bef28663c05083551df88d222c61fd3c8390df4b43f46267e00d6b3a54bcfe38#rd)｜《Harrison Chase：你的 Agent Harness 就是你的记忆，一旦选了闭源，数据就不是你的了》｜源文章：Harrison Chase：你的 Agent Harness 就是你的记忆，一旦选了闭源，数据就不是你的了

- [原文链接](https://x.com/berryxia/status/2042367800338260467)｜《Better-Harness：LangChain 用 Evals 当梯度信号，让 Agent 越跑越强》｜源文章：Better-Harness：LangChain 用 Evals 当梯度信号，让 Agent 越跑越强

- [原文链接](https://x.com/hwchase17/status/2042978500567609738)｜《Your harness, your memory》｜源文章：Harrison Chase：你的 Agent Harness，就是你的记忆

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzg3MTk3NzYzNw%3D%3D&mid=2247506328&idx=1&sn=d03e32eb701b71176450f7b8bda36481&chksm=cf8ba6a23e6803733918f630b2e14ee243187d68061fbad56d96e4c3b04b6a39ba50ef7611a8#rd)｜《Mythos造假/Opus降智/Agent新平台，Anthropic所有更新一次性看懂》｜源文章：Mythos造假/Opus降智/Agent新平台，Anthropic所有更新一次性看懂

- [原文链接](https://x.com/sarahwooders/status/2040121230473457921)｜《Why memory isn't a plugin (it's the harness)》｜源文章：记忆不是插件，它是 Harness 本身：Letta 对 Agent 架构的重新定义

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzE5MTA3NzcxMQ%3D%3D&mid=2247488335&idx=1&sn=ece0fb7411d313acd1c583c84b748538&chksm=971ff5041a501710ae6c94e032c8f8d009fe38dd0edd9fbf16d3d392baedc9c670020c3bf213#rd)｜《MiniMax M2.7 × Hermes Agent：开启自我进化的 Agent 工作流》｜来源条目：[摘要：MiniMax M2.7 × Hermes Agent：开启自我进化的 Agent 工作流](summaries/摘要：MiniMax M2.7 × Hermes Agent：开启自我进化的 Agent 工作流.md)

- [原文链接](https://x.com/garrytan/status/2042925773300908103)｜《Thin Harness, Fat Skills》｜源文章：Thin Harness, Fat Skills：Garry Tan 的 AI Agent 生产力架构

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkyNjU2ODM2NQ%3D%3D&mid=2247627539&idx=1&sn=da04448ed2172c5381d68b24e0454247&chksm=c31182e7c7ef6bde7a36b46d0bcde4b0b20f049b7cdbbe53d6ae77d1d83ea99c2250b5f96f56#rd)｜《别人都在卷Harness， 而Google 的沉默振聋发聩》｜源文章：别人都在卷Harness， 而Google 的沉默振聋发聩

- [原文链接](https://cursor.com/blog/multi-agent-kernels)｜《Speeding up GPU kernels by 38% with a multi-agent system》｜源文章：Cursor × NVIDIA：多智能体系统用 3 周把 CUDA kernel 加速了 38%

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw%3D%3D&mid=2247523808&idx=1&sn=0a6aea0c1f3f9c5c6e86eff9592fd30b&chksm=c17464df982ee29fa92c7272b71d87b2dc6c54287a5fd8e61657920ebeb34565f22f3d893ff4#rd)｜《Notion Custom Agents复盘：三年重写5次，Notion 历史上最成功的新功能之一》｜源文章：Notion Custom Agents复盘：三年重写5次，Notion 历史上最成功的新功能之一

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652692423&idx=2&sn=48472f70867c916d0535634efd24f41b&chksm=f0239167a5179ae5ae3754750d37afba159d7a2b605d55e693bd605245b506ca0dd02be97647#rd)｜《最新风口Harness，李开复、陆奇已重金入场》｜来源条目：[摘要：最新风口Harness，李开复、陆奇已重金入场](summaries/摘要：最新风口Harness，李开复、陆奇已重金入场.md)

- 源文章：开源视频 Agent 框架全景扫描：八个项目，哪个适合你？（文中将视频 Agent 的能力差异部分归因于 harness 设计）

- [原文链接](https://x.com/jxnlco/status/2044469127696556153)｜《Sandboxes are coming to the Agents SDK》｜源文章：OpenAI Agents SDK 沙盒：让 AI Agent 真正「留下工作成果」

- [摘要：超越Claude Mythos和GPT-5.5！斯坦福推出Agent验证框架「LLM-as-a-Verifier」](summaries/摘要：超越Claude Mythos和GPT-5.5！斯坦福推出Agent验证框架「LLM-as-a-Verifier」.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651030107&idx=2&sn=dcf949e41eb246cd78463ec2ac79eb17&chksm=85f6580c4d8619e4dbb67c7144f147a8bc41f01f639924649cbbb134ea5daa9c1e2bdebb2928#rd)）

- [摘要：SkVM：优化你的Skills能够跨模型、跨Harness、跨环境稳定运行 ｜SJTU最新](summaries/摘要：SkVM：优化你的Skills能够跨模型、跨Harness、跨环境稳定运行 ｜SJTU最新.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg4MzYxODkzMg%3D%3D&mid=2247508119&idx=1&sn=8576b881967cee0b33dc2c424c9853a5&chksm=ce7a42ad8a773a9cdc3297389c1915b62ee8ee06d86ae09cbf47c11c9141230f4f6a7f8916f7#rd)）

- [摘要：The Bitter Lesson of Agent Harnesses](summaries/摘要：The Bitter Lesson of Agent Harnesses.md)（[原文](https://x.com/gregpr07/status/2047358189327520166)）

- [摘要：Design principles for building an Agent harness](summaries/摘要：Design principles for building an Agent harness.md)（[原文](https://x.com/akshay_pachaar/status/2047671145475068038)）

- [摘要：Introducing "create-agent-tui"](summaries/摘要：Introducing create-agent-tui.md)（[原文](https://x.com/OpenRouter/status/2047701992798392484)）
