---
title: TAOR 循环
type: concept
tags:
- Harness 工程
- 代码生成
status: 审核中
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4505ec4d15e7413c8d5e71d7f1e346cf
notion_id: 4505ec4d-15e7-413c-8d5e-71d7f1e346cf
---

## 定义

TAOR 循环（Think-Act-Observe-Repeat）是 Claude Code 的执行引擎设计哲学：Orchestrator 被设计得极其「愚赋」，只负责驱动循环、执行工具调用、感知结果；所有推理、决策、何时停止全部交给模型。

## 核心哲学

- **运行时越笨，架构越稳定**：不应在框架层做“聰明编排”

- **将智能下沉到模型**，**把确定性留给框架**

- 和早期 LangChain 尝试在框架层做各种“聰明编排”的路线形成鲜明对比

## 实现细节

- TAOR 循环核心逻辑大约只有 **50 行**，但给了模型无限的操作空间

- 工具采用四种原语：Read、Write、Execute、Connect，不配备 100 个专项工具，给模型一个 shell 让它自己组合

- **随着模型变得更强，脚手架应该变薄，而不是变厚**

## 来源引用

- [摘要：Claude Code Harness设计：Agent工程化的真正难点](summaries/摘要：Claude Code Harness设计：Agent工程化的真正难点.md)
