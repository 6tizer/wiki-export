---
title: CLAUDE.md
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0927d29642cb48a0b3bfc1243bde0b88
notion_id: 0927d296-42cb-48a0-b3bf-c1243bde0b88
---

## 定义

[**CLAUDE.md**](http://claude.md/) 是 Claude Code 的项目级配置文件，放置在项目根目录后，Claude Code 在每次对话开始时会自动读取其内容，作为持久化的系统指令注入 AI 的行为规范。类似于 `.cursorrules`（Cursor）或 `AGENTS.md`（Codex）的角色。

## 核心作用

- 为特定项目定义 AI 编程行为准则（如禁止过度设计、要求提问而非假设）

- 可包含项目特定规则（使用的语言规范、错误处理模式、测试要求等）

- 支持多份规则合并叠加（全局 + 项目级）

## 典型用法

```bash
# 新项目：直接下载
curl -o CLAUDE.md https://raw.githubusercontent.com/.../CLAUDE.md

# 现有项目：追加
curl https://raw.githubusercontent.com/.../CLAUDE.md >> CLAUDE.md
```

- [摘要：The solo founder stack of 2026](summaries/摘要：The solo founder stack of 2026.md)（[原文](https://x.com/rohit4verse/status/2047699770308014406)）

## 关联概念

- [规划/检索/执行三层隔离](concepts/规划-检索-执行三层隔离.md)

- [自退火循环](concepts/自退火循环.md)

- [内容创作工程化](concepts/内容创作工程化.md)

- [Agent Skills](concepts/Agent Skills.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [claude-mem](entities/claude-mem.md)

- [Multica](entities/Multica.md)

- [Claude Code](entities/Claude Code.md)

- [GLM-5.1](entities/GLM-5.1.md)

- [CC Switch](entities/CC Switch.md)

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [Idea File](concepts/Idea File.md)

- [Obsidian](entities/Obsidian.md)

- [三层知识架构](concepts/三层知识架构.md)

- [andrej-karpathy-skills](entities/andrej-karpathy-skills.md)

- [Think Before Coding](concepts/Think Before Coding.md)

- [Simplicity First](concepts/Simplicity First.md)

- [Surgical Changes](concepts/Surgical Changes.md)

- [Goal-Driven Execution](concepts/Goal-Driven Execution.md)

- [Claude Code Hooks](concepts/Claude Code Hooks.md)

- [Claude Code Routines](concepts/Claude Code Routines.md)

- [Skill 分类学](concepts/Skill 分类学.md)

- [可追溯日志体系](concepts/可追溯日志体系.md)

- [Caveman Mode](concepts/Caveman Mode.md)

- [caveman](entities/caveman.md)

- [Codebase Q&A](concepts/Codebase Q&A.md)

## 来源引用

- [摘要：how I automate my X contents pipeline using claude code.](summaries/摘要：how I automate my X contents pipeline using claude code.md)（[原文](https://x.com/exploraX_/status/2046950874237337808)）

- [摘要：30 分钟精通 Claude Code](summaries/摘要：30 分钟精通 Claude Code.md)（[原文](https://x.com/SaitoWu/status/2046952505947648217)）

- [摘要：本周增长最快的 GitHub 仓库：](summaries/摘要：本周增长最快的 GitHub 仓库：.md)（[原文](https://x.com/pritipatelfgoo/status/2045105855662809267)）

- [摘要：从0开始，在国内用上Claude Code的终极保姆教程来了。](summaries/摘要：从0开始，在国内用上Claude Code的终极保姆教程来了。.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA%3D%3D&mid=2647681650&idx=1&sn=ebe9c3f89ede3094c532f47dcd495081&chksm=f1848a70eb0ed8813b80a31c693a43c481d2e6a4d5180ff577c22c46d4146fd3e97b57ec5be4#rd)）

- [原文链接](https://x.com/runes_leo/status/2042243228678693244)｜《用半年 Claude Code 踩坑，我验证了 OpenAI/Cursor/Anthropic 三篇 Harness Engineering 的每一条》｜来源条目：[摘要：用半年 Claude Code 踩坑，我验证了 OpenAI/Cursor/Anthropic 三篇 Harness Engineering 的每一条](summaries/摘要：用半年 Claude Code 踩坑，我验证了 OpenAI-Cursor-Anthropic 三篇 Harness Engineering 的每一条.md)

- [摘要：11.4K Star！基于 AI 大神 Karpathy 的编程经验开源的 Claude Code 技能插件。](summaries/摘要：11.4K Star！基于 AI 大神 Karpathy 的编程经验开源的 Claude Code 技能插件。.md)（开源星探，2026-04-11）

- [原文链接](https://x.com/karpathy/status/2040470801506541998)｜《Automated multi-source ingestion》｜源文章：Karpathy 的 LLM Wiki：用 AI 编译你的私人知识库，告别 RAG

- [原文链接](https://x.com/lxfater/status/2042848343949480173)｜《Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）》｜来源条目：[摘要：Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）](summaries/摘要：Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）.md)

- 《Karpathy 的 LLM 知识库：让 AI 替你编译一个永不遗忘的个人 Wiki》｜X书签文章｜原文链接：[https://x.com/0xKingsKuan/status/2040416072353165764](https://x.com/0xKingsKuan/status/2040416072353165764)｜来源条目：[摘要：Karpathy 的 LLM 知识库：让 AI 替你编译一个永不遗忘的个人 Wiki](summaries/摘要：Karpathy 的 LLM 知识库：让 AI 替你编译一个永不遗忘的个人 Wiki.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzU3NTg5MjU1Mw%3D%3D&mid=2247496984&idx=1&sn=98f3a18047c1908f1b961052640e85a9&chksm=fc1c6bb03b47cbb0ba7d773e7d7e2f214a2492c4f081e9d9750d237912643aabf4e8b6628c58#rd)｜《一个 [CLAUDE.md](http://claude.md/) 文件竟然拿下 1.7 万 star，它到底写了什么》｜来源条目：[摘要：一个 CLAUDE.md 文件竟然拿下 1.7 万 star，它到底写了什么](summaries/摘要：一个 CLAUDE.md 文件竟然拿下 1.7 万 star，它到底写了什么.md)

- [原文链接](https://x.com/claudeai/status/2044131493966909862)｜《Learn more in the official documentation》｜来源条目：[摘要：Learn more in the official documentation](summaries/摘要：Learn more in the official documentation.md)

- [原文链接](https://x.com/axiaisacat/status/2044260023161831620)｜《Looking for a managed agents platform?》｜来源条目：[摘要：Looking for a managed agents platform?](summaries/摘要：Looking for a managed agents platform.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA%3D%3D&mid=2647681530&idx=1&sn=d5c714699089e31276c667cda1edefdb&chksm=f153676ae06e0dadad8df80becf797662c0126d74a5c1a314ecac659ebf41da34625aac44a6b#rd)｜《Skill其实就是分类学。》｜源文章：Skill其实就是分类学。

- [原文链接](https://x.com/LawrenceW_Zen/status/2044437995269591195)｜《一个冷门无人提的冷知识却又是程序员常识：》｜来源条目：[摘要：一个冷门无人提的冷知识却又是程序员常识：](summaries/摘要：一个冷门无人提的冷知识却又是程序员常识：.md)

- [原文链接](https://x.com/zaimiri/status/2044769304923529383)｜《How to Set Up Claude Code: Caveman Mode (Save 75% off)》｜来源条目：[摘要：How to Set Up Claude Code: Caveman Mode (Save 75% off)](summaries/摘要：How to Set Up Claude Code- Caveman Mode (Save 75% off).md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIwMzY3Njc2MA%3D%3D&mid=2247484484&idx=1&sn=b877810761905accec8c61a88f1d20f3&chksm=97732bf3c04982b7874037c0a69fa13851f4885059370a3951a7a9094c6b6aba2a24fd85addc#rd)｜《Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮》｜来源条目：[摘要：Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮](summaries/摘要：Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮.md)

- [摘要：How to Build a JARVIS Inside Obsidian With Claude Code — The Full Setup From Scratch](summaries/摘要：How to Build a JARVIS Inside Obsidian With Claude Code — The Full Setup From Scratch.md)（[原文](https://x.com/cyrilXBT/status/2047246104421388461)）
