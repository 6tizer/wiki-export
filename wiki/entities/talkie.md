---
title: talkie
type: entity
tags:
- 训练/微调
- 模型评测
status: 草稿
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/32e9c9bba34243e788453da57d03800b
notion_id: 32e9c9bb-a342-43e7-8845-3da57d03800b
---

## 定义

talkie 是由 Alec Radford、Nick Levine 和 David Duvenaud 共同开发的「复古语言模型」项目。其核心理念是**仅使用 1931 年 1 月 1 日之前的英文文本**训练大型语言模型，以研究 LLM 在训练数据分布之外的泛化能力。

别名：talkie-1930、talkie-1930-13b、talkie-web-13b（现代对照组）

## 关键要点

- **参数规模**：130 亿参数，训练于 2600 亿 tokens 的 1931 年前英文语料（书籍、报纸、期刊、科学杂志等）

- **知识截止点**：1930 年 12 月 31 日，选择该日期是因为美国版权法的公有领域边界

- **核心发现 1**：模型对 1930 年后事件的「惊讶值」在 1950-60 年代达到峰值（晶体管、电视普及），之后趋于平缓

- **核心发现 2**：尽管从未见过任何编程语言，talkie 通过 in-context learning 能够解出 HumanEval 编程测试题，且能力随模型规模增大而提升（Scaling Law）

- **核心发现 3**：剔除超出知识范围的题目后，与现代数据训练的同架构模型差距缩小一半；在语言理解和数学计算上表现几乎一致

- **对齐方式**：使用 1930 年前的礼仪手册、书信指南等天然问答语料做 instruction tuning，避免注入现代风格

- **已知问题**：使用 Claude Sonnet 4.6 做 RLHF 老师时，模型学会了现代互联网的列表体风格（风格泄漏）

- **团队路线图**：计划发布 GPT-3 级别复古模型，将语料扩展至一万亿 tokens 并涵盖非英语世界

## 关联概念

- [Alec Radford](entities/Alec Radford.md)

- [Scaling Law](concepts/Scaling Law.md)

- [Thinking Machines Lab](entities/Thinking Machines Lab.md)

- [RLHF](concepts/RLHF.md)

## 来源引用

- [摘要：GPT之父：只用上世纪数据训AI，它居然也会写Python？！](summaries/摘要：GPT之父：只用上世纪数据训AI，它居然也会写Python？！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247887945&idx=1&sn=4ae7aef7f33377a3b2bda14bc320f454&chksm=e9fe95de1c4f7605027c82909abd4a6e791ed37aa6ba23b5e165b4402f416faa98811d2c6bcc#rd)）
