---
title: Agent Skills
type: concept
tags:
- Agent 技能
- 工作流
- 知识管理
status: 审核中
confidence: high
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/f017ef06f33f4f6fb3f9f09740bd4063
notion_id: f017ef06-f33f-4f6f-b3f9-f09740bd4063
---

## 定义

Agent Skills 是给 AI Agent 封装领域知识、操作规范和资源入口的可复用能力单元，通常按任务场景按需加载。

## 关键要点

- 它比单个提示词更结构化，通常包含元数据、指令和附加资源

- 核心价值是复用高质量操作知识，同时控制上下文成本

- 在插件生态中，Skills 往往是连接工作流模板与具体执行能力的基础层

## 来源引用

- [摘要：Memory](summaries/摘要：Memory.md)（[原文](https://x.com/akshay_pachaar/status/2045510648474530263)）

- [摘要：本周增长最快的 GitHub 仓库：](summaries/摘要：本周增长最快的 GitHub 仓库：.md)（[原文](https://x.com/pritipatelfgoo/status/2045105855662809267)）

- [原文链接](https://mp.weixin.qq.com/s?__biz=MjM5OTE0ODA2MQ%3D%3D&mid=2650996439&idx=1&sn=b0e8f9460d31651bdd374eae18db74f6&chksm=bdd2ba711515b068254cc8fae7b1d613c0f7602c73faca901e0862da74272e110b494db13b0f#rd)｜《汤道生：人工智能正式进入 Harness 时代》｜来源条目：[摘要：汤道生：人工智能正式进入 Harness 时代](summaries/摘要：汤道生：人工智能正式进入 Harness 时代.md)

- [原文链接](https://x.com/RocM301/status/2042155081764893083)｜《微信支付推出 AI 原生接入 Skills：一句话完成支付接入》｜来源条目：[摘要：微信支付推出 AI 原生接入 Skills：一句话完成支付接入](summaries/摘要：微信支付推出 AI 原生接入 Skills：一句话完成支付接入.md)

- 《wshobson/agents：用 72 个插件把 Claude Code 变成 AI 开发部队》

- 《Impeccable：让 AI 写出真正有设计感的前端界面》（GitHubDaily，2026-03-09）— 展示了 Skills 如何承载设计知识、命令和约束

- 《OpenClaw find-skills：让你的 AI 龙虾「不会就自动学」》（axiaisacat，X书签）— 补充 Skills 生态中“自动发现能力”的元技能层

- 《腾讯 SkillHub：专为中国用户打造的 OpenClaw 技能社区》（LaurenceMister，X书签）— 补充 Skills 分发、本土镜像与安全审核的生态竞争维度

- [原文链接](https://x.com/oragnes/status/2031376812190871718)｜《Agent Skills 生态全景：四大技能市场横评，让你的 AI 解锁超能力》｜来源条目：Agent Skills 生态全景：四大技能市场横评，让你的 AI 解锁超能力

- [原文链接](https://x.com/jakevin7/status/2031412457537704358)｜《卡比卡比的五件套：用 CLI 工具让 AI Agent 直接操控社交平台》｜来源条目：卡比卡比的五件套：用 CLI 工具让 AI Agent 直接操控社交平台

- [原文链接](https://x.com/yan5xu/status/2032858943874281782)｜《bb-browser：用你真实的 Chrome 登录态，把整个互联网变成 AI Agent 的 CLI》｜来源条目：[摘要：bb-browser：用你真实的 Chrome 登录态，把整个互联网变成 AI Agent 的 CLI](summaries/摘要：bb-browser：用你真实的 Chrome 登录态，把整个互联网变成 AI Agent 的 CLI.md)

- [原文链接](https://blog.chainbase.com/chainbase-newsletter-february-2026)｜《Chainbase 2026 年 2 月月报：AI Agent 的链上数据层正在成形》｜来源条目：[摘要：Chainbase 2026 年 2 月月报：AI Agent 的链上数据层正在成形](summaries/摘要：Chainbase 2026 年 2 月月报：AI Agent 的链上数据层正在成形.md)

- [原文链接](https://x.com/sitinme/status/2033418986898207072)｜《everything-claude-code：把 Claude Code 调教成 AI 工程团队的完整配置系统》｜来源条目：[摘要：everything-claude-code：把 Claude Code 调教成 AI 工程团队的完整配置系统](summaries/摘要：everything-claude-code：把 Claude Code 调教成 AI 工程团队的完整配置系统.md)

- [原文链接](https://x.com/0xshawnpang/status/2033433838278623398)｜《startup-founder-skills：一个创始人的 50 个 AI 外挂，把融资、销售、招聘全自动化》｜来源条目：[摘要：startup-founder-skills：一个创始人的 50 个 AI 外挂，把融资、销售、招聘全自动化](summaries/摘要：startup-founder-skills：一个创始人的 50 个 AI 外挂，把融资、销售、招聘全自动化.md)

- [原文链接](https://x.com/berryxia/status/2042749070050234451)｜《TinyFish CLI + Skills》｜来源条目：[摘要：TinyFish CLI + Skills](summaries/摘要：TinyFish CLI + Skills.md)

- 《女娲.skill：输入一个名字，让芒格、费曼、马斯克给你打工》｜X书签文章｜原文链接：[https://x.com/AlchainHust/status/2040653665422201218](https://x.com/AlchainHust/status/2040653665422201218)｜来源条目：[摘要：女娲.skill：输入一个名字，让芒格、费曼、马斯克给你打工](summaries/摘要：女娲.skill：输入一个名字，让芒格、费曼、马斯克给你打工.md)

- 《Claude 官方 Skills 仓库：11 万 Star 背后，AI Agent 的新工作方式》｜X书签文章｜原文链接：[https://x.com/Crypto_QianXun/status/2040716833112887597](https://x.com/Crypto_QianXun/status/2040716833112887597)｜来源条目：[摘要：Claude 官方 Skills 仓库：11 万 Star 背后，AI Agent 的新工作方式](summaries/摘要：Claude 官方 Skills 仓库：11 万 Star 背后，AI Agent 的新工作方式.md)

- 《20 Powerful Agentic-Skills for Claude, ChatGPT & Gemini.》｜X书签文章｜原文链接：[https://x.com/exploraX_/status/2039269234253934811](https://x.com/exploraX_/status/2039269234253934811)｜来源条目：[摘要：20 Powerful Agentic-Skills for Claude, ChatGPT & Gemini.](summaries/摘要：20 Powerful Agentic-Skills for Claude, ChatGPT & Gemini.md)

- [原文链接](https://x.com/garrytan/status/2042925773300908103)｜《Thin Harness, Fat Skills》｜源文章：Thin Harness, Fat Skills：Garry Tan 的 AI Agent 生产力架构

- [原文链接](https://x.com/Khazix0918/status/2043555868902637845)｜《分享一个我用了2年的深度研究Prompt，半小时帮你搞懂任何陌生领域。》｜源文章：横纵分析法：数字生命卡兹克用了2年的深度研究框架，半小时出一份万字报告

- [原文链接](https://x.com/sujingshen/status/2043898494818410731)｜《三省六部幻觉：为什么"虚拟公司"式多Agent架构在工程上不成立》｜来源条目：三省六部幻觉：为什么「虚拟公司」式多 Agent 架构在工程上走不通

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzg5Mjc3MjIyMA%3D%3D&mid=2247581731&idx=1&sn=ed24d1a78487a8d58023279ca2eaf54a&chksm=c18c60055fdebff977a60b40c7dda8197ea38fd50c0a38d307c2b55757b4454729c8033d9778#rd)｜《阿里下场做了中国版的 Lovable，好用到炸。》｜来源条目：[摘要：阿里下场做了中国版的 Lovable，好用到炸。](summaries/摘要：阿里下场做了中国版的 Lovable，好用到炸。.md)

- [原文链接](https://x.com/LufzzLiz/status/2044258384556556743)｜《抽丝剥茧：深度解析 Hermes Agent 万字系统提示词（System Prompt）构成》｜来源条目：[摘要：抽丝剥茧：深度解析 Hermes Agent 万字系统提示词（System Prompt）构成](summaries/摘要：抽丝剥茧：深度解析 Hermes Agent 万字系统提示词（System Prompt）构成.md)

- [原文链接](https://x.com/NeoAIForecast/status/2044252861710905685)｜《How Skills Work in Hermes Agent》｜来源条目：[摘要：How Skills Work in Hermes Agent](summaries/摘要：How Skills Work in Hermes Agent.md)

- [原文链接](https://x.com/jiroucaigou/status/2044249069699428665)｜《Hermes Agent新手教程：从入门到精通，附带变现方式》｜来源条目：[摘要：Hermes Agent新手教程：从入门到精通，附带变现方式](summaries/摘要：Hermes Agent新手教程：从入门到精通，附带变现方式.md)

- [摘要：这个开源牛马Skills180+大合集，专注牛马优雅干活](summaries/摘要：这个开源牛马Skills180+大合集，专注牛马优雅干活.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzk0MjM4Mjc1Mw%3D%3D&mid=2247491139&idx=1&sn=2171d0f8e6e16fc6ba280948b5afa2c6&chksm=c361e5fb85975dba21cb8a655c8654d851dbbf508e8114d091e09d81824750ab3f13c0de9549#rd)）

- [摘要：Here are the 3 Core Pillars of Every AI Agent's Context](summaries/摘要：Here are the 3 Core Pillars of Every AI Agent's Context.md)（[原文](https://x.com/Ai_Vaidehi/status/2045050337149513974)）

- [摘要：什么才是真正的 Harness Engineering？](summaries/摘要：什么才是真正的 Harness Engineering？.md)（[原文](https://x.com/SaitoWu/status/2045458721929892345)）

- [摘要：Interesting insights, especially this: Hermes starts off as any other agent does, inefficient and often not sure how to complete a task that is training didnt have priors for. However, solve it once a](summaries/摘要：Interesting insights, especially this- Hermes starts off as any other agent does, inefficient and often not sure how to complete a task that is training didnt have priors for. However, solve it once a.md)（[原文](https://x.com/Teknium/status/2046001396819067008)）

- [原文链接](https://x.com/iamzhihui/status/2046063506609635552)｜《统一编排 Skill，按项目精准分发到不同 Agent CLI。》｜来源条目：[摘要：统一编排 Skill，按项目精准分发到不同 Agent CLI。](summaries/摘要：统一编排 Skill，按项目精准分发到不同 Agent CLI。.md)

- [摘要：开源Turix，你可以把任何App当Agent Skill用！比如微信...](summaries/摘要：开源Turix，你可以把任何App当Agent Skill用！比如微信.md)

## 关联概念

- [CLAUDE.md](concepts/CLAUDE.md.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [claude-mem](entities/claude-mem.md)

- [Multica](entities/Multica.md)

- [RAG](concepts/RAG.md)

- [find-skills](concepts/find-skills.md)

- [SkillHub](entities/SkillHub.md)

- [ClawHub](entities/ClawHub.md)

- [TinyFish CLI + Skills](entities/TinyFish CLI + Skills.md)

- [Bash 浏览器自动化](concepts/Bash 浏览器自动化.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Context Engineering](concepts/Context Engineering.md)

- [Prompt Engineering](concepts/Prompt Engineering.md)

- [OpenClaw](entities/OpenClaw.md)

- [Meoo](entities/Meoo.md)

- [Thin Harness, Fat Skills](concepts/Thin Harness, Fat Skills.md)

- [Resolver](concepts/Resolver.md)

- [Diarization](concepts/Diarization.md)

- [hv-analysis](concepts/hv-analysis.md)

- [横纵分析法](concepts/横纵分析法.md)

- [三省六部式多 Agent 架构](concepts/三省六部式多 Agent 架构.md)

- [显式外部状态](concepts/显式外部状态.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [ModelBox](entities/ModelBox.md)

- [Agent-Managed Skills](concepts/Agent-Managed Skills.md)

- [程序性记忆](concepts/程序性记忆.md)

- [渐进式披露](concepts/渐进式披露.md)

- [SKILL.md](concepts/SKILL.md.md)

- [记忆分层架构](concepts/记忆分层架构.md)

- [Agent 协议层](concepts/Agent 协议层.md)

- [Mediator 层](concepts/Mediator 层.md)

- [Gateway](concepts/Gateway.md)

- [MCP 协议](concepts/MCP 协议.md)

- [多智能体编排](concepts/多智能体编排.md)

- [Cron 自动化](concepts/Cron 自动化.md)

- [awesome-niuma-skills](entities/awesome-niuma-skills.md)

- [填坑式写作](concepts/填坑式写作.md)

- [面试追问链](concepts/面试追问链.md)

- [标题公式](concepts/标题公式.md)

- [Guardrails](concepts/Guardrails.md)

- [Review Agents](concepts/Review Agents.md)

- [skills-manage](entities/skills-manage.md)

- [SkillStar](entities/SkillStar.md)

- [符号链接注入](concepts/符号链接注入.md)

- [项目级 Skills 分发](concepts/项目级 Skills 分发.md)

- [Computer Use](concepts/Computer Use.md)

- [Turix CUA](entities/Turix CUA.md)

- [RPA](concepts/RPA.md)
