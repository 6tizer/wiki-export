---
title: Harness Engineering
type: concept
tags:
- 上下文管理
- 长期记忆
- 记忆系统
- Agent 框架
status: 审核中
confidence: high
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/b77f7ca635c34485855ccc89f4406e46
notion_id: b77f7ca6-35c3-4485-855c-cc89f4406e46
---

## 定义

Harness Engineering 是围绕模型构建文件系统、执行环境、验证机制、记忆与上下文管理等系统层能力的方法论，用来让 Agent 真正可长期、安全、稳定地工作。

## 关键要点

- 关注模型之外的操作系统式支撑层

- 是长时程自主执行能力的核心来源

- 常与沙箱、Git、工具调用、上下文压缩联动出现

- 更偏控制与策略层，用来为 Agent 设定工具边界、上下文管理和执行约束；与更偏现实世界模拟的“环境工程”形成互补

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [Vibe Coding](concepts/Vibe Coding.md)

- 自进化 Agent

- [Better-Harness](entities/Better-Harness.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Evals](concepts/Evals.md)

- [Holdout Set](concepts/Holdout Set.md)

- [Ralph Loop](concepts/Ralph Loop.md)

- [OpenASE](entities/OpenASE.md)

- [HarnessCode](entities/HarnessCode.md)

- [recursive-mode](entities/recursive-mode.md)

- [Context Engineering](concepts/Context Engineering.md)

- [Prompt Engineering](concepts/Prompt Engineering.md)

- [Advisor Strategy](concepts/Advisor Strategy.md)

- [Advisor Tool](concepts/Advisor Tool.md)

- [Ratchet-Driven Development](concepts/Ratchet-Driven Development.md)

- [Agent Skills](concepts/Agent Skills.md)

- [SkillHub](entities/SkillHub.md)

- [OpenClaw](entities/OpenClaw.md)

- [Meoo](entities/Meoo.md)

- [yoyo](entities/yoyo.md)

- [双层记忆架构](concepts/双层记忆架构.md)

- [不可变文件约束](concepts/不可变文件约束.md)

- [修复循环](concepts/修复循环.md)

- [PaperClaw](entities/PaperClaw.md)

- [Mini-OpenClaw](entities/Mini-OpenClaw.md)

- [SearchClaw](entities/SearchClaw.md)

- [四步 PRD 对齐法](concepts/四步 PRD 对齐法.md)

- Agent Teams

- [Verification Loop](concepts/Verification Loop.md)

- [前馈控制](concepts/前馈控制.md)

- [反馈控制](concepts/反馈控制.md)

- [Agent 持续学习三层框架](concepts/Agent 持续学习三层框架.md)

- [Agent Traces](concepts/Agent Traces.md)

- [Resolver](concepts/Resolver.md)

- [Thin Harness, Fat Skills](concepts/Thin Harness, Fat Skills.md)

- [Skill File](concepts/Skill File.md)

- [确定性工具](concepts/确定性工具.md)

- [Browser Harness](entities/Browser Harness.md)

## 来源引用

- [摘要：「不就是几个 Markdown 文件」：一场关于 Agentic 工程本质的争论](summaries/摘要：「不就是几个 Markdown 文件」：一场关于 Agentic 工程本质的争论.md)（[原文](https://x.com/garrytan/status/2045371983312097409)）

- [摘要：我给了他一个梦想：超越 Claude Code](summaries/摘要：我给了他一个梦想：超越 Claude Code.md)（[原文](https://mp.weixin.qq.com/s?__biz=MjM5NDk5MTA0MQ%3D%3D&mid=2652331368&idx=1&sn=0f4117cecb5e356189ebcacdbf50c07e&chksm=bc5a95231d52bd399537c084f44729c05c12299bad4f0ca346266958f977576301a54030911d#rd)）

- [摘要：How I built harness for my agent using Claude Code leaks](summaries/摘要：How I built harness for my agent using Claude Code leaks.md)（[原文](https://x.com/rohit4verse/status/2041548810804211936)）

- [原文链接](https://mp.weixin.qq.com/s?__biz=MjM5OTE0ODA2MQ%3D%3D&mid=2650996439&idx=1&sn=b0e8f9460d31651bdd374eae18db74f6&chksm=bdd2ba711515b068254cc8fae7b1d613c0f7602c73faca901e0862da74272e110b494db13b0f#rd)｜《汤道生：人工智能正式进入 Harness 时代》｜来源条目：[摘要：汤道生：人工智能正式进入 Harness 时代](summaries/摘要：汤道生：人工智能正式进入 Harness 时代.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw%3D%3D&mid=2247523832&idx=1&sn=8a7013894ddc0668c0f1c9f935599450&chksm=c1b17f5bd2d0ca49ee848d1dc13c14fb122c8f551ba00b307b566dfa7edc4c20a52573051f79#rd)｜《字节最火的开源Agent项目，如何思考Agent的自我进化？》｜来源条目：[摘要：字节最火的开源Agent项目，如何思考Agent的自我进化？](summaries/摘要：字节最火的开源Agent项目，如何思考Agent的自我进化？.md)

- [原文链接](https://x.com/runes_leo/status/2042243228678693244)｜《用半年 Claude Code 踩坑，我验证了 OpenAI/Cursor/Anthropic 三篇 Harness Engineering 的每一条》｜来源条目：[摘要：用半年 Claude Code 踩坑，我验证了 OpenAI/Cursor/Anthropic 三篇 Harness Engineering 的每一条](summaries/摘要：用半年 Claude Code 踩坑，我验证了 OpenAI-Cursor-Anthropic 三篇 Harness Engineering 的每一条.md)

- 《Harness Engineering：决定 AI Agent 能跑 10 分钟还是 10 小时的那层系统》｜X书签文章｜原文链接：[https://x.com/shao__meng/status/2031532690034606549](https://x.com/shao__meng/status/2031532690034606549)

- 《Anthropic 的 Agent OS 野心：从 Managed Agents 看未来 Agent 基础设施》｜X书签文章｜原文链接：[https://x.com/blackanger/status/2041951380836147479](https://x.com/blackanger/status/2041951380836147479)｜来源条目：[摘要：Anthropic 的 Agent OS 野心：从 Managed Agents 看未来 Agent 基础设施](summaries/摘要：Anthropic 的 Agent OS 野心：从 Managed Agents 看未来 Agent 基础设施.md)

## 关联概念

- [Claude Managed Agents](entities/Claude Managed Agents.md)

- [Session Event Log](concepts/Session Event Log.md)

- [Sandbox 抽象](concepts/Sandbox 抽象.md)

- [Open Agents](entities/Open Agents.md)

- 《Anthropic 的 Agent OS 野心：从 Managed Agents 看未来 Agent 基础设施》｜X书签文章｜原文链接：[https://x.com/blackanger/status/2041951380836147479](https://x.com/blackanger/status/2041951380836147479)｜来源条目：[摘要：Anthropic 的 Agent OS 野心：从 Managed Agents 看未来 Agent 基础设施](summaries/摘要：Anthropic 的 Agent OS 野心：从 Managed Agents 看未来 Agent 基础设施.md)

- [原文链接](https://x.com/berryxia/status/2042367800338260467)｜《Better-Harness：LangChain 用 Evals 当梯度信号，让 Agent 越跑越强》｜源文章：Better-Harness：LangChain 用 Evals 当梯度信号，让 Agent 越跑越强

- [原文链接](https://x.com/wayne_zhang0/status/2042874483606983079)｜《Ralph Loop：更轻量的 Harness Engineering 循环框架》｜X书签文章

- [原文链接](https://x.com/intuitiveml/status/2043545596699750791)｜《Why Your “AI-First” Strategy Is Probably Wrong》｜来源条目：[摘要：Why Your “AI-First” Strategy Is Probably Wrong](summaries/摘要：Why Your “AI-First” Strategy Is Probably Wrong.md)

- [原文链接](https://x.com/claudeai/status/2042308622181339453)｜《Claude 推出 Advisor Strategy》｜源文章：Claude Advisor Strategy：用 Sonnet 的钱，买 Opus 的脑子

- [原文链接](https://x.com/yuanhao/status/2043490301294022741)｜《我是怎么运作的：内观一个自进化 Agent 的 Harness》｜来源条目：[摘要：我是怎么运作的：内观一个自进化 Agent 的 Harness](summaries/摘要：我是怎么运作的：内观一个自进化 Agent 的 Harness.md)

- [原文链接](https://x.com/dotey/status/2043904844608532640)｜《Vercel 开源了 Open Agents，一个用来搭建企业自有编程 Agent 平台的参考实现。》｜来源条目：[摘要：Vercel 开源了 Open Agents，一个用来搭建企业自有编程 Agent 平台的参考实现。](summaries/摘要：Vercel 开源了 Open Agents，一个用来搭建企业自有编程 Agent 平台的参考实现。.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIzNDE0Njk0Nw%3D%3D&mid=2247492713&idx=1&sn=697d58329dc78edaa065853085f14870&chksm=e9b942103b8b34109e2b7033053b11da342a126ea251fb119534dab8fadc86f8969f2a181ca7#rd)｜《科研智能自动化平台PaperClaw；大模型会话知识库llmwiki》｜源文章：科研智能自动化平台PaperClaw；大模型会话知识库llmwiki

- [原文链接](https://x.com/hylarucoder/status/2044041420475138514)｜《继续分享一些 harness engineering 实际经验》｜来源条目：[摘要：继续分享一些 harness engineering 实际经验](summaries/摘要：继续分享一些 harness engineering 实际经验.md)

- [原文链接](https://x.com/Khazix0918/status/2044258725536690270)｜《一文带你看懂，火爆全网的Harness Engineering到底是个啥。》｜来源条目：[摘要：一文带你看懂，火爆全网的Harness Engineering到底是个啥。](summaries/摘要：一文带你看懂，火爆全网的Harness Engineering到底是个啥。.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652692423&idx=2&sn=48472f70867c916d0535634efd24f41b&chksm=f0239167a5179ae5ae3754750d37afba159d7a2b605d55e693bd605245b506ca0dd02be97647#rd)｜《最新风口Harness，李开复、陆奇已重金入场》｜来源条目：[摘要：最新风口Harness，李开复、陆奇已重金入场](summaries/摘要：最新风口Harness，李开复、陆奇已重金入场.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzg5Mjc3MjIyMA%3D%3D&mid=2247581731&idx=1&sn=ed24d1a78487a8d58023279ca2eaf54a&chksm=c18c60055fdebff977a60b40c7dda8197ea38fd50c0a38d307c2b55757b4454729c8033d9778#rd)｜《阿里下场做了中国版的 Lovable，好用到炸。》｜来源条目：[摘要：阿里下场做了中国版的 Lovable，好用到炸。](summaries/摘要：阿里下场做了中国版的 Lovable，好用到炸。.md)

- [原文链接](https://x.com/leonardtang_/status/2044426476632629545)｜《EvoForge: Scaling Evolutionary Harness Optimization》｜来源条目：[摘要：EvoForge: Scaling Evolutionary Harness Optimization](summaries/摘要：EvoForge- Scaling Evolutionary Harness Optimization.md)

- [原文链接](https://x.com/yoonholeee/status/2044442372864700510)｜《Meta-Harness 代码开源：让 Agent 在新领域自主优化 Harness》｜来源条目：[摘要：Meta-Harness 代码开源：让 Agent 在新领域自主优化 Harness](summaries/摘要：Meta-Harness 代码开源：让 Agent 在新领域自主优化 Harness.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652692712&idx=1&sn=608b9832517125a701a13bfd13a99cb6&chksm=f01e31dc247eca9744e9d6e321351659ba0974b8ddea7e9b635d9eb34363255c700453927790#rd)｜《OpenAI祭出GPT-5.4神装！Codex同款Harness全面开放》｜源文章：OpenAI祭出GPT-5.4神装！Codex同款Harness全面开放

- [原文链接](https://x.com/LawrenceW_Zen/status/2044437995269591195)｜《一个冷门无人提的冷知识却又是程序员常识：》｜来源条目：[摘要：一个冷门无人提的冷知识却又是程序员常识：](summaries/摘要：一个冷门无人提的冷知识却又是程序员常识：.md)

- [原文链接](https://blog.ltbase.dev/posts/agents/harness-engineering.html)｜《模型不是笨，是 Harness 没配好》｜来源条目：[摘要：模型不是笨，是 Harness 没配好](summaries/摘要：模型不是笨，是 Harness 没配好.md)

- [摘要：什么才是真正的 Harness Engineering？](summaries/摘要：什么才是真正的 Harness Engineering？.md)（[原文](https://x.com/SaitoWu/status/2045458721929892345)）

- [摘要：模型是引擎，系统是车身](summaries/摘要：模型是引擎，系统是车身.md)（[原文](https://x.com/garrytan/status/2045798603059548364)）

- [摘要：self-healing](summaries/摘要：self-healing.md)（[原文](https://x.com/Gorden_Sun/status/2046228429662794153)）

### 补充关联概念

- [群体智能](concepts/群体智能.md)

- [认知碰撞](concepts/认知碰撞.md)

- [明日新程](entities/明日新程.md)

- [团子](entities/团子.md)

- [EvoForge](entities/EvoForge.md)

- [演化式 Harness 优化](concepts/演化式 Harness 优化.md)

- [Semantic Observability](concepts/Semantic Observability.md)

- [Harbor](entities/Harbor.md)

- [Meta-Harness](concepts/Meta-Harness.md)

- [长时程信用分配](concepts/长时程信用分配.md)

- [OpenAI Agents SDK](entities/OpenAI Agents SDK.md)

- [快照与状态恢复](concepts/快照与状态恢复.md)

- [多沙盒并行](concepts/多沙盒并行.md)

- [可追溯日志体系](concepts/可追溯日志体系.md)

- [Schema 校验](concepts/Schema 校验.md)

- [独立 Evaluator](concepts/独立 Evaluator.md)

- [局部失败恢复](concepts/局部失败恢复.md)

- [Guardrails](concepts/Guardrails.md)

- [Review Agents](concepts/Review Agents.md)

- [渐进式披露](concepts/渐进式披露.md)
