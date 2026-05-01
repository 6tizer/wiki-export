---
title: 摘要：Claude Code源码泳露后：终端 Agent 只该接3类活
type: summary
tags:
- OpenClaw
status: 已审核
confidence: medium
last_compiled: '2026-04-28'
source_tags: Agent, LLM, 自动化, Claude
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4ccf3c0da65145d39867860d9afeaa32
notion_id: 4ccf3c0d-a651-45d3-9867-860d9afeaa32
---

**一句话摘脁**：终端 Agent 天生适合边界清楚、可验证、可回收的任务，应按“人定边界+Agent 跑第一轮+人做最后判断”的分工模式使用。

---

## 关键洞察

- **3 类适合任务**：① 边界清晰、验收明确的实现任务；② 重复出现、适合流程化的工作流任务；③ 先跑第一轮再由人拍板的探索任务

- **3 类不适合任务**：① 需求自己都没定清的活；② 高风险的真实动作（生产环境、账号权限）；③ 强依赖视觉判断和业务感觉的任务

- **判断表**：四问——目标能否一句话说清？验收标准是否客观？出错成本高不高？返工时谁来收尾？

- **核心观点**：AI 编程最贵的成本不是 token，而是把模糊需求交出去之后再收回来重做的那一轮又一轮

## 原始文章信息

- **作者**：孟健AI编程

- **来源**：微信公众号

- **发布日期**：2026-04-01

- **链接**：[https://mp.weixin.qq.com/s?__biz=Mzk0ODM5NTEyNA==&mid=2247505784](https://mp.weixin.qq.com/s?__biz=Mzk0ODM5NTEyNA%3D%3D&mid=2247505784)

## 个人评注

孟健提出的四开判断框架对 Tizer 的 OpenClaw 工作流很实用，尤其适合当前 HITL 流程设计的考量。
