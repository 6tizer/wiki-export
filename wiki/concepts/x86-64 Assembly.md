---
title: x86-64 Assembly
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e67eb2397af7432b96801cd0c419fb21
notion_id: e67eb239-7af7-432b-9680-1cd0c419fb21
---

## 定义

x86-64 Assembly 是面向 x86-64 指令集架构的低级编程形式，开发者需要直接处理寄存器、内存地址、调用约定和指令级运算。

## 关键要点

- 与高级语言不同，数据布局、状态保存和函数调用副作用都需要显式管理。

- 在性能敏感或教学型场景中，汇编可以帮助观察程序如何被拆解成最基础的计算步骤。

- 文章用它来手写一个 XOR 神经网络，突出神经网络训练在底层其实仍是数据搬运、乘加计算与状态更新。

## 适用边界

- 适合做体系结构理解、性能优化、逆向分析和底层系统开发。

- 不适合承担大规模模型训练的日常工程实现，但很适合作为理解抽象层之下机制的教学材料。

## 来源引用

- [摘要：Building a Neural Network from Scratch in Pure x86-64 Assembly](summaries/摘要：Building a Neural Network from Scratch in Pure x86-64 Assembly.md)
