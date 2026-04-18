---
title: Karpathy LLM Wiki 方法论
type: concept
tags:
- 知识管理
- LLM
status: 审核中
confidence: high
last_compiled: '2026-04-18'
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

## 关联概念

- [LanceDB](concepts/LanceDB.md)

- [Idea File](concepts/Idea File.md)

- [多源自动摄取](concepts/多源自动摄取.md)

- [知识图谱层](concepts/知识图谱层.md)

- [Wiki 健康检查](concepts/Wiki 健康检查.md)

- [CLAUDE.md](concepts/CLAUDE.md.md)

- [Obsidian](entities/Obsidian.md)

- [Claude Code](entities/Claude Code.md)

- [Dataview](entities/Dataview.md)

- [Memex](concepts/Memex.md)

- [llm-wiki](entities/llm-wiki.md)

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

## 来源引用

- [摘要：让 AI 帮你自动打理个人知识库，把你的各种文档自动整理成一套相互关联、持续更新的个人维基](summaries/摘要：让 AI 帮你自动打理个人知识库，把你的各种文档自动整理成一套相互关联、持续更新的个人维基.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2MjY1NDIzNg%3D%3D&mid=2247499264&idx=1&sn=4a31c6e7999e7ba2cac50fe8f189c5ca&chksm=cfd4f4f5944b48a7b7a4a628eb12f5ede6b88f74d5471ab8cc43a53c661ff1cc77689da97efb#rd)）

- [摘要：Karpathy 又双叒叕发新概念了，这次我替你找到了那个产品](summaries/摘要：Karpathy 又双叒叕发新概念了，这次我替你找到了那个产品.md)（花叔，2026-04-07）

- [摘要：实操指南：如何用 Karpathy 的 LLM + Markdown + Wiki 搭建个人知识库](summaries/摘要：实操指南：如何用 Karpathy 的 LLM + Markdown + Wiki 搭建个人知识库.md)（Alphana和大船的AI工作区，2026-04-10）

- [摘要：Andrej Karpathy 现在成了一个超级 AI 明星。他最近主推的一个 LLM+ MD + Wiki 的个人知识库特别火](summaries/摘要：Andrej Karpathy 现在成了一个超级 AI 明星。他最近主推的一个 LLM+ MD + Wiki 的个人知识库特别火.md)（MacTalk，2026-04-07）

- [摘要：11.4K Star！基于 AI 大神 Karpathy 的编程经验开源的 Claude Code 技能插件。](summaries/摘要：11.4K Star！基于 AI 大神 Karpathy 的编程经验开源的 Claude Code 技能插件。.md)（开源星探，2026-04-11）

- 《用 LLM 把 Obsidian 变成「会编译的知识库」：Karpathy 方法论落地实践》｜X书签文章｜原文链接：[https://x.com/yanhua1010/status/2039966047378583815](https://x.com/yanhua1010/status/2039966047378583815)｜来源条目：[摘要：用 LLM 把 Obsidian 变成「会编译的知识库」：Karpathy 方法论落地实践](summaries/摘要：用 LLM 把 Obsidian 变成「会编译的知识库」：Karpathy 方法论落地实践.md)

- [原文链接](https://x.com/karpathy/status/2040470801506541998)｜《Automated multi-source ingestion》｜源文章：Karpathy 的 LLM Wiki：用 AI 编译你的私人知识库，告别 RAG

- [原文链接](https://x.com/lxfater/status/2042848343949480173)｜《Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）》｜来源条目：[摘要：Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）](summaries/摘要：Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）.md)

- [原文链接](https://x.com/boniusex/status/2042994933146300463)｜《当我把 Claude 接进 Obsidian 后，笔记软件这个概念死了》｜来源条目：[摘要：当我把 Claude 接进 Obsidian 后，笔记软件这个概念死了](summaries/摘要：当我把 Claude 接进 Obsidian 后，笔记软件这个概念死了.md)

- 《Karpathy 的 LLM 知识库：让 AI 替你编译一个永不遗忘的个人 Wiki》｜X书签文章｜原文链接：[https://x.com/0xKingsKuan/status/2040416072353165764](https://x.com/0xKingsKuan/status/2040416072353165764)｜来源条目：[摘要：Karpathy 的 LLM 知识库：让 AI 替你编译一个永不遗忘的个人 Wiki](summaries/摘要：Karpathy 的 LLM 知识库：让 AI 替你编译一个永不遗忘的个人 Wiki.md)

- [原文链接](https://x.com/nash_su/status/2042441606616568263)｜《llm-wiki v0.2.0：用知识图谱和社区检测，让你的个人知识库真正「活」起来》｜源文章：llm-wiki v0.2.0：用知识图谱和社区检测，让你的个人知识库真正「活」起来

- [原文链接](https://x.com/sitinme/status/2043865262982869105)｜《别再用 RAG 了，让 AI 帮你养一个会长大的知识库！》｜来源条目：[摘要：别再用 RAG 了，让 AI 帮你养一个会长大的知识库！](summaries/摘要：别再用 RAG 了，让 AI 帮你养一个会长大的知识库！.md)

- [原文链接](https://x.com/shannholmberg/status/2044111115878326444)｜《AI Knowledge Layer (and why your agents are useless without it)》｜来源条目：[摘要：AI Knowledge Layer (and why your agents are useless without it)](summaries/摘要：AI Knowledge Layer (and why your agents are useless without it).md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIzNDE0Njk0Nw%3D%3D&mid=2247492713&idx=1&sn=697d58329dc78edaa065853085f14870&chksm=e9b942103b8b34109e2b7033053b11da342a126ea251fb119534dab8fadc86f8969f2a181ca7#rd)｜《科研智能自动化平台PaperClaw；大模型会话知识库llmwiki》｜源文章：科研智能自动化平台PaperClaw；大模型会话知识库llmwiki

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzI2MzA5NjA4MQ%3D%3D&mid=2665365507&idx=1&sn=8efb2e3bb093dcbda21aed892627d696&chksm=f0cdf306ccc0b7fcbef97f62e290b698001da1676e7ee11075b3dbb2b100e3c12bea51b047c6#rd)｜《Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki》｜源文章：Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki

- 《Claude + Obsidian | How to use your second brain》｜X书签文章｜原文链接：[https://x.com/defileo/status/2043762213597397179](https://x.com/defileo/status/2043762213597397179)｜来源条目：[摘要：Claude + Obsidian | How to use your second brain](summaries/摘要：Claude + Obsidian  How to use your second brain.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493206&idx=1&sn=7080809308368860641fd4df6601bef9&chksm=c0a8ea2ad24191e6e6e084a08eacab4b318f12dd484d75fe35bb554e96c6e9906e407e998911#rd)｜《Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱》｜来源条目：[摘要：Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱](summaries/摘要：Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzA3OTEwNjUwMw%3D%3D&mid=2451582189&idx=1&sn=5f669d3b8e480a52044f20c318c907f5&chksm=8989bab920c529851a230e42f6a695b110e2da878b190d07b8792b21b3e41274d73bfc02c081#rd)｜《用 werss-cli 将公众号历史文章重新保存到本地，再用 graphify 把 100 多篇文章变成知识图谱》｜来源条目：[摘要：用 werss-cli 将公众号历史文章重新保存到本地，再用 graphify 把 100 多篇文章变成知识图谱](summaries/摘要：用 werss-cli 将公众号历史文章重新保存到本地，再用 graphify 把 100 多篇文章变成知识图谱.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIwMzY3Njc2MA%3D%3D&mid=2247484484&idx=1&sn=b877810761905accec8c61a88f1d20f3&chksm=97732bf3c04982b7874037c0a69fa13851f4885059370a3951a7a9094c6b6aba2a24fd85addc#rd)｜《Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮》｜来源条目：[摘要：Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮](summaries/摘要：Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkwMzE4NjU5NA%3D%3D&mid=2247516072&idx=1&sn=63e5ebee8477b3c352c69191880e1954&chksm=c1fffa03ee2cb8ecc7d287ccb244b609eb32257697e4fc30e645b4741c13594ca18ef6b1bc9c#rd)｜《开源「仓颉.Skill」，你现在可以蒸馏任何书！》｜来源条目：[摘要：开源「仓颉.Skill」，你现在可以蒸馏任何书！](summaries/摘要：开源「仓颉.Skill」，你现在可以蒸馏任何书！.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIxNDU5NzMwNw%3D%3D&mid=2247483858&idx=1&sn=0d89d92a93d83ab503c4dfc1797051ab&chksm=96345dad0dd70c41fdec1f5f49ccd2d293f09985c0a929889a531f06081b33934b005886261b#rd)｜《从"人肉路由"到 Agent 网络——AI Native 组织的构想》｜来源条目：[摘要：从"人肉路由"到 Agent 网络——AI Native 组织的构想](summaries/摘要：从人肉路由到 Agent 网络——AI Native 组织的构想.md)
