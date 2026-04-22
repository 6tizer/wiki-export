---
title: x87 FPU
type: concept
tags:
- 开发工具
status: 草稿
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/c01e0823c6b84d4fa0f81a6898490721
notion_id: c01e0823-c6b8-4d4f-a0f8-1a6898490721
---

## 定义

x87 FPU 是 x86 体系上的传统浮点运算单元，采用堆栈式寄存器模型，在现代 SSE/AVX 普及之前承担大量浮点计算任务。

## 关键要点

- 它不是通用寄存器式接口，而是 ST0～ST7 的堆栈结构，因此编程和调试心智负担更高。

- 文章借助 `fldl2e`、`f2xm1`、`fscale` 等指令近似实现 `exp()`，再构造出 sigmoid。

- 这个案例说明高层语言里的一个数学函数，落到旧式浮点指令层时会变成一整套数值计算流程。

## 适用边界

- 对理解历史兼容性、底层数学实现和旧式汇编代码很有帮助。

- 在现代高性能实现里，更多会被 SSE/AVX 等向量指令替代。

## 来源引用

- [摘要：Building a Neural Network from Scratch in Pure x86-64 Assembly](summaries/摘要：Building a Neural Network from Scratch in Pure x86-64 Assembly.md)
