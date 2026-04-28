---
title: CC Switch
type: entity
tags:
- CLI 工具
- 模型部署
status: 审核中
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e959294c9ccb4a1bb4193081f488bcb6
notion_id: e959294c-9ccb-4a1b-b419-3081f488bcb6
---

## 定义

CC Switch 是一个开源桌面应用（GitHub 51K+ 星标），用于跨 Agent CLI 工具（Claude Code、Codex、Gemini CLI、OpenCode、OpenClaw、Hermes）的模型配置管理与一键切换。通过自动改写各工具的配置文件，将模型切换简化为「选供应商→填 API Key→选模型」三步操作，并提供热切换、用量追踪、本地代理故障转移路由等功能。

**别名**：cc-switch

**GitHub**：[https://github.com/farion1231/cc-switch](https://github.com/farion1231/cc-switch)

## 关键要点

- 全平台支持（Windows / Mac / Linux），数据存储在本地 SQLite（~/.cc-switch/cc-switch.db）

- 内置 40+ 家模型供应商预设（智谱、MiMo、DeepSeek、千问、Kimi、MiniMax 等国内主流厂商）

- 支持热切换：无需重启终端或关闭会话，模型空闲时菜单栏一键切换，下一轮对话即生效

- 本地代理故障转移：配置多家供应商优先级队列，主供应商故障时自动切到备选，支持熔断保护

- 用量追踪：查看 API 余额和 Coding Plan 额度，统计各时段成本消耗

- 会话管理、模型配置云同步等附加功能

## 来源引用

- [摘要：从0开始，在国内用上Claude Code的终极保姆教程来了。](summaries/摘要：从0开始，在国内用上Claude Code的终极保姆教程来了。.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA%3D%3D&mid=2647681650&idx=1&sn=ebe9c3f89ede3094c532f47dcd495081&chksm=f1848a70eb0ed8813b80a31c693a43c481d2e6a4d5180ff577c22c46d4146fd3e97b57ec5be4#rd)）

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzYyMzc4NjU0Mg%3D%3D&mid=2247485518&idx=1&sn=32379f84dd600df7b002ea9070cc38fd&chksm=feee7cfd7f2988db5205c021092c341fa9b97c0c0d9c8d02c4394af0d93862d6e968ab042e31#rd)｜[摘要：Claude Code 全屏渲染来了：长对话不再闪烁，还能用鼠标！](summaries/摘要：Claude Code 全屏渲染来了：长对话不再闪烁，还能用鼠标！.md)｜源页面：Claude Code 全屏渲染来了：长对话不再闪烁，还能用鼠标！

- [摘要：实测小米MiMo-V2.5-Pro，这可能是目前国内最适合Claude Code的新模型。](summaries/摘要：实测小米MiMo-V2.5-Pro，这可能是目前国内最适合Claude Code的新模型。.md)（[原文](https://x.com/Khazix0918/status/2047526414161965523)）

- [摘要：这个51K星标的开源神器，让任何Agent都能一键切换所有模型。](summaries/摘要：这个51K星标的开源神器，让任何Agent都能一键切换所有模型。.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA%3D%3D&mid=2647681944&idx=1&sn=e3f6218daedb4dbfc9931b6a3adcbc8c&chksm=f16914fa8815127eb4dc837b85b4005493b1572de01a24a2ae5d1a9a48a47169742d7150ac69#rd)）

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [GLM-5.1](entities/GLM-5.1.md)

- [CLAUDE.md](concepts/CLAUDE.md.md)

- [Xiaomi MiMo-V2.5-Pro](entities/Xiaomi MiMo-V2.5-Pro.md)

- [Agent 模型热切换](concepts/Agent 模型热切换.md)

- [API 故障转移路由](concepts/API 故障转移路由.md)
