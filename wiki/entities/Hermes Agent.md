---
title: Hermes Agent
type: entity
tags:
- Agent 框架
status: 已审核
confidence: high
last_compiled: '2026-04-14'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/e47e7d37ec9f452a80c270954a83ee35
notion_id: e47e7d37-ec9f-452a-80c2-70954a83ee35
---

## 定义

Hermes Agent 是一个具备三层记忆系统、技能自迭代和内置安全机制的自进化AI助手，定位为OpenClaw的实用互补工具，支持导入OpenClaw配置快速迁移。

## 核心要点

- **三层记忆系统**：工作记忆（当前任务）+ 情节记忆（历史经验）+ 语义记忆（领域知识）

- **技能自迭代**：Agent能自动记录解决方案并在后续任务中复用，实现持续自我优化

- **安全机制**：内置操作权限管理，防止Agent越界操作

- **与OpenClaw互补**：Hermes更适合需要自主学习的长期任务；OpenClaw更适合高控制场景

- **快速迁移**：支持导入OpenClaw的配置和设置

## 对比 OpenClaw

| 维度 | Hermes | OpenClaw |

| --- | --- | --- |

| 设计哲学 | 自动化+自主学习 | 透明度+高控制 |

| 技能系统 | 自动归纳经验 | 手动编写Skill |

| 适用场景 | 自主长期任务 | 高控制开发场景 |

## 项目数据

- GitHub Stars：20,700+

- 消息平台适配：18+（Telegram、Discord、Slack、WhatsApp、Signal、微信企业版等）

- MCP 协议原生支持：可接入任何 MCP 工具服务器

- 多 LLM Provider 支持：OpenRouter、OpenAI、Anthropic、本地模型一键切换

## hermes-rs：Rust 重写版

hermes-rs 是对 hermes-agent Python 版的 Rust 重写，将 50,000 行压缩到 5,000 行，13 个 crate 模块化设计。

GitHub: [https://github.com/coder-brzhang/hermes-rs](https://github.com/coder-brzhang/hermes-rs)

## 来源引用

- [原文链接](https://x.com/LufzzLiz/status/2042237123865297267)｜《Hermes Agent 上手指南：安装后必试的十件事与八大亮点全解析》｜来源条目：[摘要：Hermes Agent 上手指南：安装后必试的十件事与八大亮点全解析](summaries/摘要：Hermes Agent 上手指南：安装后必试的十件事与八大亮点全解析.md)

- [原文链接](https://x.com/AnchorNode/status/2044675901775126986)｜《兄弟们，昨天配了一个新的bot，在我的失误下，把两个机器人部署到同一个目录下面，成功把旧bot搞炸了》｜来源条目：[摘要：兄弟们，昨天配了一个新的bot，在我的失误下，把两个机器人部署到同一个目录下面，成功把旧bot搞炸了](summaries/摘要：兄弟们，昨天配了一个新的bot，在我的失误下，把两个机器人部署到同一个目录下面，成功把旧bot搞炸了.md)

- [原文链接](https://x.com/YuLin807/status/2042198758260158535)｜《Browser Use × Hermes Agent：每个开源 Agent 现在都有了免费的云端浏览器》｜来源条目：[摘要：Browser Use × Hermes Agent：每个开源 Agent 现在都有了免费的云端浏览器](summaries/摘要：Browser Use × Hermes Agent：每个开源 Agent 现在都有了免费的云端浏览器.md)

- 《Hermes Agent实测，龙虾新对手是进化爱马仕》——卡尔的AI沃茨（微信，2026-04-08）

- 《？？不是，咋又来了一个 Hermes？》——cxuanAI（微信，2026-04-09）

- 摘要：10,000+ markdown files（@AYi_AInotes，2026-04-10）—— GBrain 作为 OpenClaw/Hermes Agent 的官方记忆后端开源

- 《如何使用Hermes Agent稳定爬取公众号文章》——Draco正在VibeCoding（微信，2026-04-11）：介绍了通过 Browser Use / Camoufox 封装微信公众号爬取 skill 的实战流程

- [原文链接](https://x.com/lxfater/status/2042848343949480173)｜《Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）》｜来源条目：[摘要：Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）](summaries/摘要：Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）.md)

- [原文链接](https://x.com/TheTuringPost/status/2040936147720048909)｜《Hermes WebUI：给 Hermes Agent 装上浏览器界面，CLI 党也能优雅用 AI》｜来源条目：[摘要：Hermes WebUI：给 Hermes Agent 装上浏览器界面，CLI 党也能优雅用 AI](summaries/摘要：Hermes WebUI：给 Hermes Agent 装上浏览器界面，CLI 党也能优雅用 AI.md)

- [原文链接](https://x.com/TheTuringPost/status/2040936147720048909)｜《Hermes WebUI：给 Hermes Agent 装上浏览器界面，CLI 党也能优雅用 AI》｜源文章：[摘要：Hermes WebUI：给 Hermes Agent 装上浏览器界面，CLI 党也能优雅用 AI](summaries/摘要：Hermes WebUI：给 Hermes Agent 装上浏览器界面，CLI 党也能优雅用 AI.md)

- [原文链接](https://x.com/YuLin807/status/2041667865477312551)｜《用 50 行 Python 跑通 Google A2A 协议：Hermes + OpenClaw 的多 Agent 互联实践》｜源文章：[摘要：用 50 行 Python 跑通 Google A2A 协议：Hermes + OpenClaw 的多 Agent 互联实践](summaries/摘要：用 50 行 Python 跑通 Google A2A 协议：Hermes + OpenClaw 的多 Agent 互联实践.md)

- [原文链接](https://x.com/servasyy_ai/status/2042951017462169812)｜《同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比》｜来源条目：[摘要：同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比](summaries/摘要：同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比.md)

- [原文链接](https://x.com/KKaWSB/status/2043119101028274268)｜《Evolutionary self-improvement for Hermes Agent》｜来源条目：[摘要：Evolutionary self-improvement for Hermes Agent](summaries/摘要：Evolutionary self-improvement for Hermes Agent.md)

- [原文链接](https://x.com/SHL0MS/status/2043415274196435325)｜《SHL0MS | HERMES AGENT》｜来源条目：[摘要：SHL0MS | HERMES AGENT](summaries/摘要：SHL0MS  HERMES AGENT.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzE5MTA3NzcxMQ%3D%3D&mid=2247488335&idx=1&sn=ece0fb7411d313acd1c583c84b748538&chksm=971ff5041a501710ae6c94e032c8f8d009fe38dd0edd9fbf16d3d392baedc9c670020c3bf213#rd)｜《MiniMax M2.7 × Hermes Agent：开启自我进化的 Agent 工作流》｜来源条目：[摘要：MiniMax M2.7 × Hermes Agent：开启自我进化的 Agent 工作流](summaries/摘要：MiniMax M2.7 × Hermes Agent：开启自我进化的 Agent 工作流.md)

- [原文链接](https://x.com/claudeai/status/2042308622181339453)｜《Claude 推出 Advisor Strategy》｜源文章：Claude Advisor Strategy：用 Sonnet 的钱，买 Opus 的脑子

- [原文链接](https://x.com/0xJeff/status/2043656911044870203)｜《3 Things I learnt after 3 weeks of using Hermes as a personal analyst》｜来源条目：[摘要：3 Things I learnt after 3 weeks of using Hermes as a personal analyst](summaries/摘要：3 Things I learnt after 3 weeks of using Hermes as a personal analyst.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ%3D%3D&mid=2653103929&idx=1&sn=2e50fcd0464ff901c9ed770fc5dc01ce&chksm=7fa47587eb83e5092d967cd46f7886f4d5697b473655d34cf8d8dffbdf101f3cd662464fd2bd#rd)｜《斯坦福报告：美国AI投资为中国23倍，但模型差距消失；Q1豆包海外版下载7200万次；OpenAI指控Anthropic：300亿收入80亿造假 | 极客早知道》｜来源条目：[摘要：斯坦福报告：美国AI投资为中国23倍，但模型差距消失；Q1豆包海外版下载7200万次；OpenAI指控Anthropic：300亿收入80亿造假 | 极客早知道](summaries/摘要：斯坦福报告：美国AI投资为中国23倍，但模型差距消失；Q1豆包海外版下载7200万次；OpenAI指控Anthropic：300亿收入80亿造假  极客早知道.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkyMDU4ODUwMw%3D%3D&mid=2247491544&idx=1&sn=74e54eb8e10fc81c93dae3e3d94bdf39&chksm=c0a9321173cd0bd2645a10b315050a4e45203835a1003f4b9f723b22140091f833bc5113a12f#rd)｜《用Hermes写的Hermes报告》｜来源条目：[摘要：用Hermes写的Hermes报告](summaries/摘要：用Hermes写的Hermes报告.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzk0NzQzOTczOA%3D%3D&mid=2247524083&idx=1&sn=91e2da0ea49f7a6dfe39ed118b3ccef1&chksm=c2b08eb2250002d244c3bc0c693ac6604e07ae4021320792b3d71baa679ed5d172196478ad6e#rd)｜《不想碰命令行？Hermes 现在有图形界面了》｜来源条目：[摘要：不想碰命令行？Hermes 现在有图形界面了](summaries/摘要：不想碰命令行？Hermes 现在有图形界面了.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzE5ODM0MDIyNg%3D%3D&mid=2247484011&idx=1&sn=588c8c9f5f8a8e56cb1d32c5ba91947a&chksm=976d338b09e0fcd9565bdfc1728262bd18a93f1408aecb26a19ba94a31968423d172955f1a51#rd)｜《Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比》｜来源条目：[摘要：Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比](summaries/摘要：Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比.md)

- [原文链接](https://x.com/BTCqzy1/status/2043210007358148893)｜《Hermes Agent 从入门到精通：25 个致命坑避坑实战指南》｜来源条目：[摘要：Hermes Agent 从入门到精通：25 个致命坑避坑实战指南](summaries/摘要：Hermes Agent 从入门到精通：25 个致命坑避坑实战指南.md)

- [原文链接](https://x.com/Saccc_c/status/2044018336673964207)｜《多Agent团队协作才是Hermes Agent的正确打开方式。》｜来源条目：[摘要：多Agent团队协作才是Hermes Agent的正确打开方式。](summaries/摘要：多Agent团队协作才是Hermes Agent的正确打开方式。.md)

- [原文链接](https://x.com/BTCqzy1/status/2044259795499450414)｜《Hermes Agent 从中级到高级进阶指南》｜来源条目：[摘要：Hermes Agent 从中级到高级进阶指南](summaries/摘要：Hermes Agent 从中级到高级进阶指南.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652692364&idx=1&sn=806ef08f63d5bf567d421f8808528c22&chksm=f047438bdb7b8b7734f13ec8b0c731b8c3a0085d501b9d6454c92b66b5d973bec5e7bce653ea#rd)｜《Hermes Agent抄袭中国团队代码实锤！被锤后回应：你删号》｜来源条目：[摘要：Hermes Agent抄袭中国团队代码实锤！被锤后回应：你删号](summaries/摘要：Hermes Agent抄袭中国团队代码实锤！被锤后回应：你删号.md)

- [原文链接](https://x.com/LufzzLiz/status/2044258384556556743)｜《抽丝剥茧：深度解析 Hermes Agent 万字系统提示词（System Prompt）构成》｜来源条目：[摘要：抽丝剥茧：深度解析 Hermes Agent 万字系统提示词（System Prompt）构成](summaries/摘要：抽丝剥茧：深度解析 Hermes Agent 万字系统提示词（System Prompt）构成.md)

- [原文链接](https://x.com/NeoAIForecast/status/2044252861710905685)｜《How Skills Work in Hermes Agent》｜来源条目：[摘要：How Skills Work in Hermes Agent](summaries/摘要：How Skills Work in Hermes Agent.md)

- [原文链接](https://x.com/Teknium/status/2044329280201732217)｜《⚠️ Pre-beta — GUI not yet wired to core functions.》｜来源条目：摘要：⚠️ Pre-beta — GUI not yet wired to core functions.

- [原文链接](https://x.com/nyk_builderz/status/2044472463279710344)｜《The Ultimate Hermes Guide - from one agent to a 4-profile team that still feels coherent on day 30》｜来源条目：[摘要：The Ultimate Hermes Guide - from one agent to a 4-profile team that still feels coherent on day 30](summaries/摘要：The Ultimate Hermes Guide - from one agent to a 4-profile team that still feels coherent on day 30.md)

- [原文链接](https://x.com/jiroucaigou/status/2044249069699428665)｜《Hermes Agent新手教程：从入门到精通，附带变现方式》｜来源条目：[摘要：Hermes Agent新手教程：从入门到精通，附带变现方式](summaries/摘要：Hermes Agent新手教程：从入门到精通，附带变现方式.md)

- 源文章页面：[OpenClaw 与 Hermes Agent 官方核心文档架构对比](https://www.notion.so/344701074b6880dd995acb5fdc19fb2a)｜来源条目：[摘要：OpenClaw 与 Hermes Agent 官方核心文档架构对比](summaries/摘要：OpenClaw 与 Hermes Agent 官方核心文档架构对比.md)

- 源文章：Hermes Agent 核心文档优化指南：让你的 AI 助手真正「越用越聪明」｜来源条目：[摘要：Hermes 核心文档架构详尽分析与优化方案指南](summaries/摘要：Hermes 核心文档架构详尽分析与优化方案指南.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIwMzY3Njc2MA%3D%3D&mid=2247484484&idx=1&sn=b877810761905accec8c61a88f1d20f3&chksm=97732bf3c04982b7874037c0a69fa13851f4885059370a3951a7a9094c6b6aba2a24fd85addc#rd)｜《Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮》｜来源条目：[摘要：Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮](summaries/摘要：Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮.md)

- [原文链接](https://x.com/AYi_AInotes/status/2044964220005965927)｜《2026年的开源社区，已经不是人在玩AI了，已经进化到 AI在玩AI，玩得比人类还好很多😆😆😆》｜来源条目：[摘要：2026年的开源社区，已经不是人在玩AI了，已经进化到 AI在玩AI，玩得比人类还好很多😆😆😆](summaries/摘要：2026年的开源社区，已经不是人在玩AI了，已经进化到 AI在玩AI，玩得比人类还好很多😆😆😆.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzg3MTk3NzYzNw%3D%3D&mid=2247506451&idx=1&sn=aec841a1c8c8ec2a99d64536babf7eae&chksm=cf1f5a4baf411e277ea71f2add117a204ea05d54a3884c6c63f8d79ec931d7d3a48694ae7f43#rd)｜《妈耶 HermesAgent直播回应抄没抄国内开发者》｜来源条目：[摘要：妈耶 HermesAgent直播回应抄没抄国内开发者](summaries/摘要：妈耶 HermesAgent直播回应抄没抄国内开发者.md)

## 关联概念

- [多 Agent 协作工作流](concepts/多 Agent 协作工作流.md)

- [SOUL.md](concepts/SOUL.md.md)

- [AGENTS.md](concepts/AGENTS.md.md)

- [Obsidian](entities/Obsidian.md)

- [Claude Code](entities/Claude Code.md)

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [OpenClaw](entities/OpenClaw.md)

- [文件即大脑](concepts/文件即大脑.md)

- [Hermes WebUI](entities/Hermes WebUI.md)

- [Gateway](concepts/Gateway.md)

- [delegate_task](concepts/delegate_task.md)

- [Subagents 并行](concepts/Subagents 并行.md)

- [Steer 机制](concepts/Steer 机制.md)

- [异步事件驱动编排](concepts/异步事件驱动编排.md)

- [Hermes Agent Self-Evolution](entities/Hermes Agent Self-Evolution.md)

- [GEPA](concepts/GEPA.md)

- [GEP 协议](concepts/GEP 协议.md)

- [DSPy](entities/DSPy.md)

- [技能自我进化](concepts/技能自我进化.md)

- [System Prompt 工程](concepts/System Prompt 工程.md)

- [Autoreason](concepts/Autoreason.md)

- [Advisor Strategy](concepts/Advisor Strategy.md)

- [Advisor Tool](concepts/Advisor Tool.md)

- [Ratchet-Driven Development](concepts/Ratchet-Driven Development.md)

- [持久化跨会话记忆](concepts/持久化跨会话记忆.md)

- [Hindsight](entities/Hindsight.md)

- [Browser Use](entities/Browser Use.md)

- [OpenRouter](entities/OpenRouter.md)

- [GLM-5.1](entities/GLM-5.1.md)

- [MiniMax M2.7](entities/MiniMax M2.7.md)

- [LLM 长期记忆](concepts/LLM 长期记忆.md)

- [自我进化 Skills 系统](concepts/自我进化 Skills 系统.md)

- [AI 研究 AI](concepts/AI 研究 AI.md)

- [MCP 协议](concepts/MCP 协议.md)

- [Honcho](entities/Honcho.md)

- [ClawShell](entities/ClawShell.md)

- [WSL2](entities/WSL2.md)

- [Ollama](entities/Ollama.md)

- [Context Bleed](concepts/Context Bleed.md)

- [Prompt Injection](concepts/Prompt Injection.md)

- [Agent-curated memory](concepts/Agent-curated memory.md)

- [Frozen Snapshot](concepts/Frozen Snapshot.md)

- [Agent-Managed Skills](concepts/Agent-Managed Skills.md)

- [EvoMap](entities/EvoMap.md)

- [Evolver](entities/Evolver.md)

- [AI洗代码](concepts/AI洗代码.md)

- [ModelBox](entities/ModelBox.md)

- [程序性记忆](concepts/程序性记忆.md)

- [Browser Connect](concepts/Browser Connect.md)

- [TinyAgentOS](entities/TinyAgentOS.md)

- [taOSmd](entities/taOSmd.md)

- [Memory KPI](concepts/Memory KPI.md)

- [Policy Gate](concepts/Policy Gate.md)

- [team-agents.md](concepts/team-agents.md.md)

- [Agent Skills](concepts/Agent Skills.md)

- [记忆分层架构](concepts/记忆分层架构.md)

- [多智能体编排](concepts/多智能体编排.md)

- [调用链验证](concepts/调用链验证.md)

- [Token 污染](concepts/Token 污染.md)

- [Polling 抢消息](concepts/Polling 抢消息.md)

- [USER.md](concepts/USER.md.md)

- [文件即大脑](concepts/文件即大脑.md)

- [Gemma 4](entities/Gemma 4.md)

- [Abliteration](concepts/Abliteration.md)

- [Refusal Direction](concepts/Refusal Direction.md)

- [过度对齐](concepts/过度对齐.md)
