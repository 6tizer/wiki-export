---
title: ReAct Agent
type: concept
tags:
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/4e43fe755f144c9cb91d127ec731f7cd
notion_id: 4e43fe75-5f14-4c9c-b91d-127ec731f7cd
---

**定义**

ReAct（Reasoning + Acting）是一种 AI Agent 推理框架，通过将推理（生成思考步骤）和行动（调用工具/执行操作）交替进行，让 Agent 像人类一样在与环境的动态交互中自主完成多步任务。

**核心循环**

```javascript
Thought（思考）→ Action（行动）→ Observation（观察）→ Thought（再思考）→ ...
```

- **Thought**：Agent 对当前状态的推理和下一步计划

- **Action**：调用外部工具、执行操作（浏览网页、运行代码等）

- **Observation**：执行结果的反馈，作为下一轮推理的输入

- **Final Answer**：当 Agent 判断任务完成时输出最终结果

**核心特性**

- **自适应性**：遇到错误自动调整策略，不需要预先定义所有情况的处理逻辑

- **工具调用**：通过 Tool Registry 注册工具，Agent 根据任务需要自主选择调用哪些工具

- **错误恢复**：Observation 包含失败信息时，Agent 能感知并尝试替代方案

- **与 CoT 的区别**：Chain-of-Thought 只生成推理步骤但不实际执行，ReAct 增加了与环境的真实交互

**典型应用**

- 智能爬虫（Clawer）：自主分析页面结构、处理翻页、提取数据

- AI 编程 Agent：分析代码库、执行修改、运行测试、修复错误

- 研究 Agent：搜索信息、综合分析、生成报告

**来源引用**

- [摘要：我用纯 Rust 写了一个 AI Agent 驱动的爬虫，万物皆可爬](summaries/摘要：我用纯 Rust 写了一个 AI Agent 驱动的爬虫，万物皆可爬.md)（老码小张，2026-04-02）

- [摘要：Harness Engineering：当 AI Agent 遇上七十年前的控制论](summaries/摘要：Harness Engineering：当 AI Agent 遇上七十年前的控制论.md)
