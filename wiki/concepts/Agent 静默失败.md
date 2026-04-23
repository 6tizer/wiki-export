---
title: Agent 静默失败
type: concept
tags:
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-10'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/c6fafd120b93496bbabd7eb60e75eb3e
notion_id: c6fafd12-0b93-496b-babd-7eb60e75eb3e
---

## 定义

Agent 静默失败是指 Agent 任务显示为已完成（completed），但实际没有产生有效输出的故障模式。这是最难发现的故障类型，因为表面上一切正常。

## 关键要点

- **三种典型情况**：① Heartbeat 推送目标不稳定（`target:"last"` 导致推送到没人看的频道）② 子 Agent 输出格式不匹配，主 Agent 解析失败后丢弃结果 ③ Browser 截到登录页/CAPTCHA，Agent 误以为拿到了数据

- **检测方法**：在每个重要 Cron job 末尾让 Agent 写心跳文件（时间戳），再配监控 Cron 检查文件更新，超 25 小时未更新即告警

- **与超时的区别**：超时是 Agent 明确停止，静默失败是 Agent 认为自己完成了但产出无效

- **预防关键**：检查输出内容本身而非只看任务状态

## 来源引用

- [摘要：OpenClaw 进阶手册 Vol.3：跑稳之后，才是真的开始](summaries/摘要：OpenClaw 进阶手册 Vol.3：跑稳之后，才是真的开始.md)（[请致天下.AI](http://xn--ghqv4yd56a5mi.ai/), 2026-02-28）— Tip 10 详细讲述静默失败检测方案
