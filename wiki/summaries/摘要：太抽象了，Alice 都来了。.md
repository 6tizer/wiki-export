---
title: 摘要：太抽象了，Alice 都来了。
type: summary
tags:
- 记忆系统
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 记忆
source_article_url: ''
notion_url: https://www.notion.so/5c479478715d4e1ba1868bfdfc4b2168
notion_id: 5c479478-715d-4e1b-a186-8bfdfc4b2168
---

**一句话摘要**：MemPalace将古希腌记忆宫段法映射为五层数据结构，采用完整性优先（不对对话进行摘要压缩）的策略，在LongMemEval语料库上达到96.6%召回率。

**关键洞察**：

- 五层数据结构：Wings（人/项目）→ Halls（记忆类型）→ Rooms（具体话题）→ Closets（摘要）→ Drawers（原始文件）

- 技术实现：ChromaDB向量存储（存原始对话不压缩）+ SQLite时序知识图谱 + MCP Server（19个工具，支持Claude/ChatGPT/Cursor/Gemini）

- 完整性优先策略：宁可检索慢一点，不要丢失细节；掌农窗口越来越大，存储成本越低

- 争议：维护者主动承认过度营销（AAAK压缩不成立、矛盾检测未完全实现），展示了开源社区的信任建设方式

- L0-L3分层设计：每次唤醒AI时只加载约170个 tokens

- LongMemEval上500题，R@5召回率96.6%，全部本地运行

**提取的概念**：MemPalace

**原始文章信息**：

- 作者：cxuanAI

- 来源：微信公众号

- 发布时间：2026-04-08

- GitHub：[https://github.com/milla-jovovich/mempalace](https://github.com/milla-jovovich/mempalace)

**个人评注**：MemPalace的完整性优先策略与Karpathy LLM Wiki方法论一脉相承。其五层结构映射也值得借鉴到Wiki知识库的组织方式上。
