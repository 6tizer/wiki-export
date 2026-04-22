---
title: 摘要：OpenHarness重构底层骨架：三层自愈记忆+KAIROS梦境模式
type: summary
tags:
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, Cursor, OpenClaw, 自动化, harness, 港大开源
source_article_url: ''
notion_url: https://www.notion.so/92ae5a7165f14cd9a701297d2b9210cb
notion_id: 92ae5a71-65f1-4cd9-a701-297d2b9210cb
---

**一句话摘脁**：OpenHarness v4.1 吸收 Claude Code 泳露源码的架构精华，重构引入三层自愈记忆架构、熄断机制、KAIROS 梦境模式和多智能体协同，确保 Agent 长期运行时保持高效和清醒。

---

## 关键洞察

- **三层自愈记忆**：Layer 1（指针索引层 [heartbeat.md](http://heartbeat.md/)，始终<2KB）+ Layer 2（按需知识层）+ Layer 3（只追加的执行流日志，永远不被完整读取）

- **熄断机制**：连续失败3次自动切断执行，防止 API 额度被恶意消耗（参考某顶级 Agent 曾序天浪贵25万次 API 调用）

- **KAIROS 梦境模式**：新增 `harness_dream.py`，系统空闲时分析执行日志，合并碎片化知识，将提炼出的最佳实践反馈到 `playbook.md`

- **多智能体协同**：基于文件系统 IPC，协调器通过 inbox/outbox 分发任务，比跨进程消息队列更简单易调试

## 提取的概念

- OpenHarness

## 原始文章信息

- **作者**：清新研究

- **来源**：微信公众号

- **发布日期**：2026-04-01

- **链接**：[https://mp.weixin.qq.com/s?__biz=MzkyMDU4ODUwMw==&mid=2247491404](https://mp.weixin.qq.com/s?__biz=MzkyMDU4ODUwMw%3D%3D&mid=2247491404)

## 个人评注

OpenHarness 的三层记忆架构和 KAIROS 梦境模式与 Tizer 的 HITL 和内容管道需求高度相关。
