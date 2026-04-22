---
title: 摘要：Karpathy 又双叒叕发新概念了，这次我替你找到了那个产品
type: summary
tags:
- 知识管理
- LLM
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: LLM, 自动化, Cursor, Agent, Karpathy, wiki
source_article_url: ''
notion_url: https://www.notion.so/d3b61a3ec29342519e922977c3c2911e
notion_id: d3b61a3e-c293-4251-9e92-2977c3c2911e
---

**一句话摘要**

Karpathy 提出用 LLM 算力构建个人知识库（原始资料→LLM编译→Markdown Wiki），有道宝库是目前门槛最低的中文产品化实现。

**关键洞察**

- Karpathy 将 LLM 算力从写代码转向"建知识库"，积累100+篇文章、40万字可问答的 Wiki

- 核心思想：raw/ 目录 → LLM 自动整理关联 → Markdown Wiki → 问答/可视化

- Karpathy 本人承认需要"一个真正的产品，而不是一堆拼凑的脚本"

- 有道宝库：支持 PDF/网页/论文多格式导入，回答带引用溯源（可点击跳转原文段落），生成思维导图、信息图、PPT、播客

- 有道宝库还提供 CLI，支持本地文件批量处理和 Agent 工作流集成

- 对比 NotebookLM：有道宝库对中文内容/发音支持更好，且不需要科学上网

- 当前产品仍不等于 Karpathy 描述的"主动梳理知识图谱"的理想——需等待模型进一步演进

**提取的概念**

- LLM+Markdown+Wiki知识库

- [有道宝库](concepts/有道宝库.md)

- NotebookLM（对比参照）

**原始文章信息**

- 作者：花叔

- 来源：微信

- 发布时间：2026-04-07

- 链接：[https://mp.weixin.qq.com/s?__biz=Mzg2OTA1OTAxNA==&mid=2247489422](https://mp.weixin.qq.com/s?__biz=Mzg2OTA1OTAxNA%3D%3D&mid=2247489422)

**个人评注**

这篇文章与本知识库的建设逻辑高度一致——Tizer 正在用类似的方式（Wiki Compiler Agent）将原始文章自动编译为 Wiki 条目。有道宝库提供了一个可测试的「面向非开发者」的替代方案，值得对比评估。
