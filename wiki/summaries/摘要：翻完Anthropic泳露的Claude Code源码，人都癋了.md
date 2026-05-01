---
title: 摘要：翻完Anthropic泳露的Claude Code源码，人都癋了
type: summary
tags:
- 多Agent协作
- 长期记忆
- Agent 协作模式
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化, Claude
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0228819877794c47be87df4e9f44edea
notion_id: 02288198-7779-4c47-be87-df4e9f44edea
---

**一句话摘脁**：轻松詈谐地揭示 Claude Code 源码内实际代码质量（460 条 eslint-disable、"duck" 十六进制编码等）并展示其中隐藏的重大功能（Kairos 四阶段记忆、Ultraplan、多 Agent 协同、隐身模式）。

---

## 关键洞察

- **代码内呓刻**：460 条 eslint-disable、803,924 字节的 main.tsx、50 个 _DEPRECATED 函数仍在生产、用十六进制编码 "duck" 避免构建扫描器检测

- **Kairos 四阶段记忆**：Orient→Collect→Consolidate→Prune，离线时 autoDream 整合记忆，限制在 200 行/25KB内

- **Ultraplan**：内部员工专用，在远程服务器启动独立 Opus 会话用最多 30 分钟深度规划复杂任务

- **隐身模式**：Anthropic 内部员工在公开仓库工作时自动隐藏身份，提交信息不包含 Anthropic 内部信息

- **鞦社默重于安全的公司，连续两次在最基础的运维层面翻车**

## 原始文章信息

- **作者**：CourseAI

- **来源**：微信公众号

- **发布日期**：2026-04-01

- **链接**：[https://mp.weixin.qq.com/s?__biz=MzkzNjgwNzMwNQ==&mid=2247488176](https://mp.weixin.qq.com/s?__biz=MzkzNjgwNzMwNQ%3D%3D&mid=2247488176)

## 个人评注

轻松詈谐的视角，但 Kairos 四阶段记忆、Ultraplan、隐身模式等泄露的未发布功能对 Tizer 理解 Anthropic 产品路线图很有帮助。
