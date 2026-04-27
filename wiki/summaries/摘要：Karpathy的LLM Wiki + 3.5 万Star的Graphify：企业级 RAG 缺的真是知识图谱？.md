---
title: 摘要：Karpathy的LLM Wiki + 3.5 万Star的Graphify：企业级 RAG 缺的真是知识图谱？
type: summary
tags:
- 知识管理
- RAG/检索
- Harness 工程
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b68814892c3fa56254dba8e
notion_url: https://www.notion.so/c884483331e24695bde591a641205464
notion_id: c8844833-31e2-4695-bde5-91a641205464
---

## 一句话摘要

用 30 份合成合同和 48 个测试问题实测对比基础向量 RAG、LLM Wiki 知识预编译、受控 schema 综合方案，结论是企业级知识库真正缺的不是酷炫工具，而是受控 schema、结构化字段、原文引用、权限边界和可复跑评测。

## 关键洞察

- **LLM Wiki 的价值是知识预编译层**：传统 RAG 每次提问都从零检索拼接，LLM Wiki 在资料进入时先编译成摘要页、实体页和综合分析页，把高频复杂问题提前整理好，减少重复推理成本

- **Graphify 在代码场景有用但不能照搬到文档场景**：代码有 AST 和 import 等确定性结构兜底，合同文档的关系是业务约束（主补关系、违约金、质保期），必须用受控 schema 而非自由抽取

- **基础 RAG 的局限性被量化**：层级父子分块在简单事实题上 100% 正确，但跨合同综合、全局筛选和关系推理的准确率降至 0%，Recall@5 仅 45.8%

- **受控 schema 综合方案在 24 题核心集上达到 100%**：先把合同字段进 SQLite 表，再用关系表显式表达主补关系和风险事件，向量库只负责原文回链，模型只负责答案组织

- **LLM Wiki 的企业级降维用法**：不做全量编译，只对高频复杂问题预生成综合页，综合页必须附带原文引用和结构化字段回链，跟随合同变更自动更新

## 提取的概念

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [Graphify](entities/Graphify.md)

- [LLM 知识编译](concepts/LLM 知识编译.md)

- [受控 schema RAG](concepts/受控 schema RAG.md)

- [层级父子分块](concepts/层级父子分块.md)

## 原始文章信息

- 作者：韦东东

- 来源：微信

- 发布时间：2026-04-26

- 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=MzI1ODIxNjk1OQ%3D%3D&mid=2649611293&idx=1&sn=7a85ba26ae5121b0eab159fd98346ff4&chksm=f368a598fd4532f7831bd0cf30ff657fce0d46d85cc880bb29b91c24a504ad1a2e9b01e71d2e#rd)

- 源文章：Karpathy的LLM Wiki + 3.5 万Star的Graphify：企业级 RAG 缺的真是知识图谱？

## 个人评注

这篇文章对 Tizer 的 Wiki Compiler 和内容编译流水线有直接参考价值。文章核心论点——「个人知识库的最佳实践不一定是企业知识库的最佳实践」——恰好映射了 Wiki Compiler 当前面临的规模化挑战：当前 Wiki 以 LLM 自动编译为主，但随着条目增长，需要考虑引入更多受控 schema（如字段约束、关系表、条款级引用）来提升稳定性和可审计性。文章提出的「五层架构」（文件解析 → 结构化抽取 → 条款索引与受控图谱 → 混合检索问答 → 评测审计）可以作为 OpenClaw 知识工程化的参考蓝图。
