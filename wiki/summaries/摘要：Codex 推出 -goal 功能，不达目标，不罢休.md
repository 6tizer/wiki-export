---
title: 摘要：Codex 推出 /goal 功能，不达目标，不罢休
type: summary
tags:
- Agent 协作模式
- Harness 工程
- CLI 工具
status: 已审核
confidence: high
last_compiled: '2026-05-01'
source_tags: ''
source_article_url: https://www.notion.so/353701074b688139ac74e9273635ce7b
notion_url: https://www.notion.so/Tizer/948a55c20e3e45abbfb162b4f591a0f4
notion_id: 948a55c2-0e3e-45ab-bfb1-62b4f591a0f4
---

## 一句话摘要

Codex CLI 新增 /goal 命令，实现目标驱动的持续循环执行，标志着人机协作从「对话式」向「委托式」转变。

## 关键洞察

- **从对话到委托**：/goal 改变了人与 AI 的协作界面——用户只需定义目标，Agent 全程负责路径规划和执行

- **进程内持续循环 vs 接力赛**：社区的 Ralph Loop 每轮换新上下文（靠 git 和进度文件交接），而 /goal 在同一会话内跨轮次保持目标活跃

- **三层防护机制**：零工具调用抑制（防空转）、token 预算控制（防失控）、完成审计协议（防过早关闭）

- **代理证据接受是最隐蔽的失败模式**：模型容易把「产出了 artifact」等同于「达成了目标」，/goal 通过注入 developer 指令强制逐项核验

- **Software 3.0 趋势注脚**：从 how（怎么做）→ show（示范做）→ what（要什么），/goal 是「以终为始」思维的最新工程实现

## 提取的概念

- [Codex](entities/Codex.md)

- [Ralph Loop](concepts/Ralph Loop.md)

- [Software 3.0](concepts/Software 3.0.md)

- [Goal-Driven Execution](concepts/Goal-Driven Execution.md)

- [代理证据接受](concepts/代理证据接受.md)

## 原始文章信息

- **作者**：AGI Hunt

- **来源**：微信公众号

- **发布时间**：2026-05-01

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MzA4NzgzMjA4MQ%3D%3D&mid=2453483290&idx=1&sn=904eb46992f4d152d712fd963e274f9f&chksm=864bb17a8af07573edffe69e9e5007899c121000987a37dc35d01aae2065033c2c8f9fdc3806#rd)

## 个人评注

/goal 的设计哲学与 Tizer 的 HITL 工作流高度契合——人类负责定义可验证的终态，Agent 自主完成过程。完成审计协议的思路可以借鉴到 OpenClaw 的任务验收机制中：不只看 Agent 是否「做了什么」，而是核验「交付物是否满足目标清单」。此外，/goal 的预算控制和零工具调用抑制机制，也可为 content pipeline 中的自动化循环提供防空转参考。
