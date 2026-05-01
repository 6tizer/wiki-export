---
title: AST+LLM 双阶段提取
type: concept
tags:
- 知识管理
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f0e0fff9ec6d4a5287929ee9665aa2c4
notion_id: f0e0fff9-ec6d-4a52-8792-9ee9665aa2c4
---

## 定义

AST+LLM 双阶段提取是一种先用抽象语法树做确定性结构解析、再用大模型补充语义关系与设计动机的知识抽取方法。

## 关键要点

- 第一阶段依赖 AST 解析器提取类、函数、导入和调用关系，适合本地处理代码并保护隐私。

- 第二阶段用 LLM 处理文档、论文、图片等非结构化材料，补足概念、关系和上下文解释。

- 这种分层设计把“结构确定性”和“语义理解力”结合起来，适合代码库与知识库的混合编译场景。

## 来源引用

- [摘要：Graphify-让Karpathy方法构建的知识库实现71.5倍效率提升](summaries/摘要：Graphify-让Karpathy方法构建的知识库实现71.5倍效率提升.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzcwMjIwMDk2Mg%3D%3D&mid=2247483836&idx=1&sn=87efe38320d976ed8850cded7a9919e8&chksm=f5738db7a5afe6ffd094c3453e8877b6266c1beda961858dc1d414bc80f787a3f74103f66e4c#rd)）

## 关联概念

- [Graphify](entities/Graphify.md)

- [Tree-sitter](entities/Tree-sitter.md)

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)
