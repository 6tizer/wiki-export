---
title: 摘要：LLM Wiki 深度解读——比传统知识库多了哪一层
type: summary
tags:
- 知识管理
- 长期记忆
- RAG/检索
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: LLM, 自动化, Agent, wiki
source_article_url: ''
notion_url: https://www.notion.so/Tizer/bc9df14ae1b845ed81465bab27320c7a
notion_id: bc9df14a-e1b8-45ed-8146-5bab27320c7a
---

**一句话摘要**：LLM Wiki 比 RAG 多出的关键一层是持续存在的 Wiki 中间层，知识不只能被查询，还能被回写和校验，形成可供 Agent 使用的长期工作底稿。

**关键洞察**

- **与 RAG 的差异**：RAG 是“临时检索”，LLM Wiki 是“先编译，再查询”；回答次后知识不会蒸发而是被保留

- [**index.md**](http://index.md/)** vs **[**log.md**](http://log.md/)：前者是内容地图（空间导航），后者是按时间追加的永续记录（时间导航）

- **file back 最有价値**：问答完毕后将有价値的输出回写成新页面，知识开始复利

- **schema 层是关键**：没有 schema，LLM 每次整理方式可能不同；有了 schema，wiki 才是能长期维护的系统

- **尺度边界**：~100 篇资料/40 万词规模下不需复杂 RAG；更大规模需要更正式的检索+校验机制

**提取的概念**

- LLM Wiki

- Farzapedia

**原始文章信息**

- 作者：架构师

- 来源：微信公众号

- 发布时间：2026-04-05

- 链接：[https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ==&mid=2650408964](https://mp.weixin.qq.com/s?__biz=MzAwNjQwNzU2NQ%3D%3D&mid=2650408964)

**个人评注**：这篇文章与 Tizer 的 Wiki Compiler Agent 直接相关。file back 机制和 schema 层设计思路可直接应用于优化 Wiki Compiler 的输出沉淀策略。
