---
title: Karpathy LLM Wiki 方法论
type: concept
tags:
- 知识管理
- 工作流
- RAG/检索
- 笔记工具
status: 审核中
confidence: high
last_compiled: '2026-04-25'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/71e1b901a32e499a95475faf4e53bce5
notion_id: 71e1b901-a32e-499a-9547-5faf4e53bce5
---

## 定义

Karpathy LLM Wiki方法论是Andrej Karpathy提出的一种用LLM算力「编译」个人知识库的工作流：将原始资料（文章、论文、代码仓库）存入raw/目录，由LLM自动编译为结构化的Markdown Wiki，支持深度问答、幻灯片生成和可视化分析。

## 核心架构：三层分离

1. **raw/ 层**（原始资料）：只读，不改。所有来源文档原始存放。

1. **wiki/ 层**（编译产物）：LLM自动生成并维护，人工只负责审核。包含indexes/、concepts/、summaries/、syntheses/、entities/等子目录。

1. **schema/ 层**（宪法文件）：定义wiki的组织规则、命名规范、Ingest/Query/Lint流程，对Claude [Code即CLAUDE.md](http://xn--codeclaude-8x4q.md/)，[对Codex即AGENTS.md](http://xn--codexagents-z91si00g.md/)。

## 四个关键操作

- **Ingest**：攒够5-10篇再批量处理（单篇处理无法建立跨文档关联）

- **Query**：[先读index.md](http://xn--index-fk5hj026a.md/)定位，再直接阅读具体页面；1000篇以下无需RAG

- **Output归档**：每次复杂问答结果以带元数据的Markdown存入outputs/qa/

- **Lint健康检查**：每周检查一致性、完整性、孤岛检测

## 与RAG的对比

- 中小规模（100篇/40万词以内）：LLM直接读取Markdown，[维护好index.md](http://xn--index-lu5iu06cxn7c.md/)即可

- 超过1000篇时：考虑向量数据库

- Karpathy方案更透明、可溯源，但工程门槛高；有道宝库等产品化方案降低了门槛

## 关键洞察

> Wiki不是给人看的，是给Agent看的——Farza

文件结构要简单（纯Markdown+图片），Backlinks要完整，Index要维护好，Agent才能在其上高效工作。

## 相关工具

- Obsidian Web Clipper（原始资料采集）

- CacheZero（Claude Code用户，支持向量搜索）

- obsidian-llm-wiki-local（100%本地+Ollama）

- 有道宝库（国内产品化方案，带溯源问答）

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzI1MjkyNjI4NQ%3D%3D&mid=2247486639&idx=1&sn=afab9bd6fc7a268a719127ebbf1c368a&chksm=e8fcaa80f3faf33cce6201ed6bc26ddccfa5d6d6fc0c8dc4f51adf0fe53479ebd7ed270f0d14#rd)｜《Hermes+AutoCLI+Obsidian： 打造自动入库、自动整理、自动微信汇报的知识系统》｜来源条目：[摘要：Hermes+AutoCLI+Obsidian： 打造自动入库、自动整理、自动微信汇报的知识系统](summaries/摘要：Hermes+AutoCLI+Obsidian： 打造自动入库、自动整理、自动微信汇报的知识系统.md)

## 关联概念

- [Knowledge MEMO](concepts/Knowledge MEMO.md)

- [Human in the Loop](concepts/Human in the Loop.md)

- [Retain 记忆闭环](concepts/Retain 记忆闭环.md)

- [FSRS-6](concepts/FSRS-6.md)

- [LLM Wiki v2](entities/LLM Wiki v2.md)

- [人的四个未来化](concepts/人的四个未来化.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [OpenCLI](entities/OpenCLI.md)

- [AutoCLI.ai](entities/AutoCLI.ai.md)

- [LLM 知识编译](concepts/LLM 知识编译.md)

- [ClawBot](entities/ClawBot.md)

- [LanceDB](concepts/LanceDB.md)

- [Idea File](concepts/Idea File.md)

- [多源自动摄取](concepts/多源自动摄取.md)

- [知识图谱层](concepts/知识图谱层.md)

- [Wiki 健康检查](concepts/Wiki 健康检查.md)

- [异步审查](concepts/异步审查.md)

- [CLAUDE.md](concepts/CLAUDE.md.md)

- [Obsidian](entities/Obsidian.md)

- [Claude Code](entities/Claude Code.md)

- [Dataview](entities/Dataview.md)

- [Memex](concepts/Memex.md)

- [llm-wiki](entities/llm-wiki.md)

- [llm-wiki-compiler](entities/llm-wiki-compiler.md)

- [Louvain 社区检测](concepts/Louvain 社区检测.md)

- [图谱洞察](concepts/图谱洞察.md)

- [Deep Research](entities/Deep Research.md)

- [OpenKB](entities/OpenKB.md)

- [编译式知识库](concepts/编译式知识库.md)

- [Ingest 摄入流程](concepts/Ingest 摄入流程.md)

- [AI Knowledge Layer](concepts/AI Knowledge Layer.md)

- [Knowledge Base Layer](concepts/Knowledge Base Layer.md)

- [Brand Foundation](concepts/Brand Foundation.md)

- [llm-wikid](entities/llm-wikid.md)

- [wechat-cli](entities/wechat-cli.md)

- [Graphify](entities/Graphify.md)

- [AST+LLM 双阶段提取](concepts/AST+LLM 双阶段提取.md)

- [Leiden 图聚类](concepts/Leiden 图聚类.md)

- [超边表示](concepts/超边表示.md)

- [we-mp-rss](entities/we-mp-rss.md)

- [werss-cli](entities/werss-cli.md)

- [Agent 可抓取 Wiki](concepts/Agent 可抓取 Wiki.md)

- [暗知识编译](concepts/暗知识编译.md)

- [SQLCipher 4](concepts/SQLCipher 4.md)

- [claude-obsidian](entities/claude-obsidian.md)

- [Claim 断言模型](concepts/Claim 断言模型.md)

- [RRF 融合检索](concepts/RRF 融合检索.md)

- [Outbox 模式](concepts/Outbox 模式.md)

- [仓颉.Skill](entities/仓颉.Skill.md)

- [知识精馏](concepts/知识精馏.md)

- [AI Native 组织](concepts/AI Native 组织.md)

- [Agent 网络](concepts/Agent 网络.md)

- [Git 组织协议](concepts/Git 组织协议.md)

- [个人 Agent](concepts/个人 Agent.md)

- [Tolaria](entities/Tolaria.md)

- [YAML frontmatter](concepts/YAML frontmatter.md)

- [Architecture Decision Records](concepts/Architecture Decision Records.md)

- [FalkorDB](entities/FalkorDB.md)

- [知识漂移](concepts/知识漂移.md)

- [行号级溯源](concepts/行号级溯源.md)

- [确定性检索](concepts/确定性检索.md)

- [四信号知识图谱](concepts/四信号知识图谱.md)

- [SHA256 增量缓存](concepts/SHA256 增量缓存.md)

## 来源引用

- [摘要：queryable Property Graph database to leverage sparse matrices](summaries/摘要：queryable Property Graph database to leverage sparse matrices.md)（[原文](https://x.com/akshay_pachaar/status/2047220248081015110)）

- [摘要：llm_wiki：基于 Karpathy 思想的个人知识库，有人做成桌面应用了！](summaries/摘要：llm_wiki：基于 Karpathy 思想的个人知识库，有人做成桌面应用了！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484633&idx=1&sn=311e49b83bfa4f98e042c17c90cc4aaf&chksm=f55972c32b51ea33bf6130aee2a9d5b519a1f41f3905bdf9249b9ffa3524e430c8fd577026ba#rd)）

- [摘要：The Ultimate Open-Source Dev Stack](summaries/摘要：The Ultimate Open-Source Dev Stack.md)（[原文](https://x.com/AlphaSignalAI/status/2047014600713842728)）

- [摘要：AI researchers and engineers](summaries/摘要：AI researchers and engineers.md)（[原文](https://x.com/ollama/status/2045282803387158873)）

- [摘要：Karpathy或许答错了一个根本问题：wiki 是为谁准备的？](summaries/摘要：Karpathy或许答错了一个根本问题：wiki 是为谁准备的？.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg3MTEwMzQ2OA%3D%3D&mid=2247483810&idx=1&sn=fcd68f9a5f2134ca0abad5f744566a7c&chksm=cf7a6df266c8aeb90040a7ce83e0446ecb6187f3ae9527d78573b6803138c64a677ca46eabcc#rd)）

- [摘要：让 AI 帮你自动打理个人知识库，把你的各种文档自动整理成一套相互关联、持续更新的个人维基](summaries/摘要：让 AI 帮你自动打理个人知识库，把你的各种文档自动整理成一套相互关联、持续更新的个人维基.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2MjY1NDIzNg%3D%3D&mid=2247499264&idx=1&sn=4a31c6e7999e7ba2cac50fe8f189c5ca&chksm=cfd4f4f5944b48a7b7a4a628eb12f5ede6b88f74d5471ab8cc43a53c661ff1cc77689da97efb#rd)）

- [摘要：Karpathy 又双叒叕发新概念了，这次我替你找到了那个产品](summaries/摘要：Karpathy 又双叒叕发新概念了，这次我替你找到了那个产品.md)（花叔，2026-04-07）

- [摘要：实操指南：如何用 Karpathy 的 LLM + Markdown + Wiki 搭建个人知识库](summaries/摘要：实操指南：如何用 Karpathy 的 LLM + Markdown + Wiki 搭建个人知识库.md)（Alphana和大船的AI工作区，2026-04-10）

- [摘要：Andrej Karpathy 现在成了一个超级 AI 明星。他最近主推的一个 LLM+ MD + Wiki 的个人知识库特别火](summaries/摘要：Andrej Karpathy 现在成了一个超级 AI 明星。他最近主推的一个 LLM+ MD + Wiki 的个人知识库特别火.md)（MacTalk，2026-04-07）

- [摘要：11.4K Star！基于 AI 大神 Karpathy 的编程经验开源的 Claude Code 技能插件。](summaries/摘要：11.4K Star！基于 AI 大神 Karpathy 的编程经验开源的 Claude Code 技能插件。.md)（开源星探，2026-04-11）

- 《用 LLM 把 Obsidian 变成「会编译的知识库」：Karpathy 方法论落地实践》｜X书签文章｜原文链接：[https://x.com/yanhua1010/status/2039966047378583815](https://x.com/yanhua1010/status/2039966047378583815)｜来源条目：[摘要：用 LLM 把 Obsidian 变成「会编译的知识库」：Karpathy 方法论落地实践](summaries/摘要：用 LLM 把 Obsidian 变成「会编译的知识库」：Karpathy 方法论落地实践.md)

- [原文链接](https://x.com/karpathy/status/2040470801506541998)｜Karpathy 的 LLM Wiki：用 AI 编译你的私人知识库，告别 RAG｜源文章：Karpathy 的 LLM Wiki：用 AI 编译你的私人知识库，告别 RAG

- [摘要：Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）](summaries/摘要：Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）.md)｜来源条目：[摘要：Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）](summaries/摘要：Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）.md)

- [摘要：当我把 Claude 接进 Obsidian 后，笔记软件这个概念死了](summaries/摘要：当我把 Claude 接进 Obsidian 后，笔记软件这个概念死了.md)｜来源条目：[摘要：当我把 Claude 接进 Obsidian 后，笔记软件这个概念死了](summaries/摘要：当我把 Claude 接进 Obsidian 后，笔记软件这个概念死了.md)

- [摘要：Karpathy 的 LLM 知识库：让 AI 替你编译一个永不遗忘的个人 Wiki](summaries/摘要：Karpathy 的 LLM 知识库：让 AI 替你编译一个永不遗忘的个人 Wiki.md)｜来源条目：[摘要：Karpathy 的 LLM 知识库：让 AI 替你编译一个永不遗忘的个人 Wiki](summaries/摘要：Karpathy 的 LLM 知识库：让 AI 替你编译一个永不遗忘的个人 Wiki.md)

- llm-wiki v0.2.0：用知识图谱和社区检测，让你的个人知识库真正「活」起来｜源文章：llm-wiki v0.2.0：用知识图谱和社区检测，让你的个人知识库真正「活」起来

- [摘要：别再用 RAG 了，让 AI 帮你养一个会长大的知识库！](summaries/摘要：别再用 RAG 了，让 AI 帮你养一个会长大的知识库！.md)｜来源条目：[摘要：别再用 RAG 了，让 AI 帮你养一个会长大的知识库！](summaries/摘要：别再用 RAG 了，让 AI 帮你养一个会长大的知识库！.md)

- [摘要：AI Knowledge Layer (and why your agents are useless without it)](summaries/摘要：AI Knowledge Layer (and why your agents are useless without it).md)｜来源条目：[摘要：AI Knowledge Layer (and why your agents are useless without it)](summaries/摘要：AI Knowledge Layer (and why your agents are useless without it).md)

- 科研智能自动化平台PaperClaw；大模型会话知识库llmwiki｜源文章：科研智能自动化平台PaperClaw；大模型会话知识库llmwiki

- Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki｜源文章：Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki

- [摘要：Claude + Obsidian | How to use your second brain](summaries/摘要：Claude + Obsidian  How to use your second brain.md)｜来源条目：[摘要：Claude + Obsidian | How to use your second brain](summaries/摘要：Claude + Obsidian  How to use your second brain.md)

- [摘要：Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱](summaries/摘要：Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱.md)｜来源条目：[摘要：Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱](summaries/摘要：Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱.md)

- [摘要：用 werss-cli 将公众号历史文章重新保存到本地，再用 graphify 把 100 多篇文章变成知识图谱](summaries/摘要：用 werss-cli 将公众号历史文章重新保存到本地，再用 graphify 把 100 多篇文章变成知识图谱.md)｜来源条目：[摘要：用 werss-cli 将公众号历史文章重新保存到本地，再用 graphify 把 100 多篇文章变成知识图谱](summaries/摘要：用 werss-cli 将公众号历史文章重新保存到本地，再用 graphify 把 100 多篇文章变成知识图谱.md)

- [摘要：Graphify-让Karpathy方法构建的知识库实现71.5倍效率提升](summaries/摘要：Graphify-让Karpathy方法构建的知识库实现71.5倍效率提升.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzcwMjIwMDk2Mg%3D%3D&mid=2247483836&idx=1&sn=87efe38320d976ed8850cded7a9919e8&chksm=f5738db7a5afe6ffd094c3453e8877b6266c1beda961858dc1d414bc80f787a3f74103f66e4c#rd)）

- [摘要：Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮](summaries/摘要：Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮.md)｜来源条目：[摘要：Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮](summaries/摘要：Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮.md)

- [摘要：开源「仓颉.Skill」，你现在可以蒸馏任何书！](summaries/摘要：开源「仓颉.Skill」，你现在可以蒸馏任何书！.md)｜来源条目：[摘要：开源「仓颉.Skill」，你现在可以蒸馏任何书！](summaries/摘要：开源「仓颉.Skill」，你现在可以蒸馏任何书！.md)

- [摘要：从"人肉路由"到 Agent 网络——AI Native 组织的构想](summaries/摘要：从人肉路由到 Agent 网络——AI Native 组织的构想.md)｜来源条目：[摘要：从"人肉路由"到 Agent 网络——AI Native 组织的构想](summaries/摘要：从人肉路由到 Agent 网络——AI Native 组织的构想.md)

- [摘要：custom slash commands](summaries/摘要：custom slash commands.md)（[原文](https://x.com/hasantoxr/status/2046174499226403038)）

- [摘要：markdown knowledge bases](summaries/摘要：markdown knowledge bases.md)（[原文](https://x.com/lucaronin/status/2046877445748322418)）

- [摘要：llm Wiki 养了三周，开始出毛病了](summaries/摘要：llm Wiki 养了三周，开始出毛病了.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI3NjE4OTAyMg%3D%3D&mid=2247488578&idx=1&sn=bd42d9c055bdc8ed9b7c46feb5b0e26d&chksm=ea6d6762607f43554101098e9913cd15d2e58637de0dbb68b7f67d697c0f2d68b998beff99e7#rd)）

- [摘要：3K Star！基于 Andrej Karpathy 提出的 LLM Wiki 方法论打造的 AI 知识库应用！](summaries/摘要：3K Star！基于 Andrej Karpathy 提出的 LLM Wiki 方法论打造的 AI 知识库应用！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ%3D%3D&mid=2247505963&idx=1&sn=b590481b7f9c1dd86ea25cf168a2d7a4&chksm=c117c2239e6f0d9f4bcb402b081126525c06d59d365925b3d4a00f67978b1b98416d0fadb10a#rd)）
