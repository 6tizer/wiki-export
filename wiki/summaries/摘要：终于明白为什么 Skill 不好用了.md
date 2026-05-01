---
title: 摘要：终于明白为什么 Skill 不好用了
type: summary
tags:
- OpenClaw
- 代码生成
- Agent 协作模式
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化, skills
source_article_url: ''
notion_url: https://www.notion.so/Tizer/792c4e012ca54362b9dc07645472bbb8
notion_id: 792c4e01-2ca5-4362-b9dc-07645472bbb8
---

## 一句话摘要

OpenClaw Skill 存在高 Token 消耗和执行不准确两大问题，解决方案是将 Skill 规则 Python 化，而 AiPy 项目将这一思路推到极致：LLM 规划+写代码，Python 负责执行，彻底绕开模型幻觉。

## 关键洞察

- **Skill 的两大痛点**：①所有工作需模型深度参与，Token 消耗高；②Skill 以 MD 文档描述规则，模型幻觉导致执行不准确

- **解法：Skill Python 化**：将规则转化为 Python 代码，if-else 精确表达无幻觉，后续运行不消耗 Token

- **AiPy 的 Python-Use 理念**：`Task → Plan → Code → Execute → Feedback` 循环，LLM 规划和写代码，Python 执行

- **Code is Agent**：不需要 MCP、Workflow 编排、Tools 注册——Python 本身就是协议和接口

- **踩两个红利**：Python 生态红利（pandas/beautifulsoup/matplotlib）+ 模型 Coding 能力红利

## 提取的概念

- [AiPy / Python-Use](concepts/AiPy - Python-Use.md)

## 原始文章信息

- **作者**: AI产品阿颖

- **来源**: 微信公众号

- **发布时间**: 2026-03-23

- **AiPy**: [https://www.aipyaipy.com](https://www.aipyaipy.com/), [https://github.com/knownsec/aipyapp](https://github.com/knownsec/aipyapp)

## 个人评注

直接关联 Tizer 的 OpenClaw 使用场景。Skill Python 化这个方向对于需要高精度执行的内容 pipeline 很有价值，可以减少 Token 消耗同时提高准确性。
