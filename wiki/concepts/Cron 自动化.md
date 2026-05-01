---
title: Cron 自动化
type: concept
tags:
- 内容自动化
- Agent 协作模式
- OpenClaw
status: 审核中
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/53e7e87584384ab985023fee76a437ac
notion_id: 53e7e875-8438-4ab9-8502-3fee76a437ac
---

## 定义

Cron 自动化是 AI Agent 系统中通过定时任务调度实现 7×24 小时无人值守运行的核心能力，使 Agent 从被动响应转变为主动执行。

## 关键要点

- 核心理念：「你是 Agent，不是人，没有深夜的概念」

- OpenClaw 中通过 Cron 定时任务实现自动化：信息扫描、内容创作、邮件处理、日程管理

- 傅盛的龙虾系统在 14 天内建立了 20+ 个 Cron 定时任务

- OpenFang 的 Hands 机制是 Cron 自动化的进阶形态

- CoPaw、Eggent 等平台也内置 Cron 支持

- 关键挑战：Agent「真诚地以为」自己做了但实际没做——做完必须验证

## 关联概念

- [Hermes WebUI](entities/Hermes WebUI.md)

- [Qwen Code](entities/Qwen Code.md)

- [Channels 远程控制](concepts/Channels 远程控制.md)

- [Sub-agent 模型分配](concepts/Sub-agent 模型分配.md)

- [/plan 规划模式](concepts/-plan 规划模式.md)

- [Policy Gate](concepts/Policy Gate.md)

- [team-agents.md](concepts/team-agents.md.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [Gateway](concepts/Gateway.md)

- [MCP 协议](concepts/MCP 协议.md)

- [多智能体编排](concepts/多智能体编排.md)

## 来源引用

- [摘要：龙虾养成日记PPT看不过瘾？内部版逐字稿来了](summaries/摘要：龙虾养成日记PPT看不过瘾？内部版逐字稿来了.md)（傅盛，2026-02-28）

- [摘要：一个 Rust 写的 Agent OS——OpenFang](summaries/摘要：一个 Rust 写的 Agent OS——OpenFang.md)（老码小张，2026-02-28）

- [摘要：OpenClaw 进阶手册 Vol.3：跑稳之后，才是真的开始](summaries/摘要：OpenClaw 进阶手册 Vol.3：跑稳之后，才是真的开始.md)（[请致天下.AI](http://xn--ghqv4yd56a5mi.ai/)，2026-02-28）— Cron 并发控制（`maxConcurrentRuns`）、Cron 日志位置和配置、健康检查 Cron job 设计

- [摘要：我用OpenClaw搭了11个AI Agent，它们学会了自我进化](summaries/摘要：我用OpenClaw搭了11个AI Agent，它们学会了自我进化.md)（孟健AI编程，2026-03-01）— 11 个 Agent 错开 10 分钟 Cron 调度避免资源冲突，每晚定时复盘驱动自我进化闭环

- [原文链接](https://x.com/Alibaba_Qwen/status/2042551216769765449)｜《Qwen Code v0.14：用手机遥控你的服务器，终端 AI 编程助手的新玩法》｜来源条目：[摘要：Qwen Code v0.14：用手机遥控你的服务器，终端 AI 编程助手的新玩法](summaries/摘要：Qwen Code v0.14：用手机遥控你的服务器，终端 AI 编程助手的新玩法.md)

- [原文链接](https://x.com/nyk_builderz/status/2044472463279710344)｜《The Ultimate Hermes Guide - from one agent to a 4-profile team that still feels coherent on day 30》｜来源条目：[摘要：The Ultimate Hermes Guide - from one agent to a 4-profile team that still feels coherent on day 30](summaries/摘要：The Ultimate Hermes Guide - from one agent to a 4-profile team that still feels coherent on day 30.md)

- [原文链接](https://x.com/jiroucaigou/status/2044249069699428665)｜《Hermes Agent新手教程：从入门到精通，附带变现方式》｜来源条目：[摘要：Hermes Agent新手教程：从入门到精通，附带变现方式](summaries/摘要：Hermes Agent新手教程：从入门到精通，附带变现方式.md)

- [摘要：我把Hermes官方UI卸载了，换成了这个（强烈推荐）](summaries/摘要：我把Hermes官方UI卸载了，换成了这个（强烈推荐）.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI2NjY5MjQzNQ%3D%3D&mid=2247484066&idx=1&sn=ce0a80a4e845c299dfcd7657277dfcab&chksm=eb567d729812b0d01454660a9b5ca7be3bd1ae5455eaf0ea2cba904bfa35775ad0e17f1bd1d6#rd)）
