---
title: Schema Drift Detection
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/188f0402790a436d8a3ac5ea384f8020
notion_id: 188f0402-790a-436d-8a3a-c5ea384f8020
---

## 定义

Schema Drift Detection 是一种质量门禁，用于检测 AI 在多轮生成过程中是否偏离了既定结构、字段约束或输出格式。

## 关键要点

- 关注“规则是否还在持续生效”，而不只检查单次结果是否看起来正确

- 适合用在表单、接口、配置文件、PR 产出等结构约束明确的任务里

- 是缓解 Context Rot 和多轮返工失真的关键检测机制之一

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzk0MjcxOTM2Nw%3D%3D&mid=2247502908&idx=1&sn=781cf89e36526cf2ced56337406ae43c&chksm=c2ee5c17dbde042bf7dbe3e5b84da84512262606a3d3b9259740ab2613aab4fcde99397b23c2#rd)｜《GSD框架解析：解决AI编程工具Context Rot的工程化方案》｜源文章：GSD框架解析：解决AI编程工具Context Rot的工程化方案
