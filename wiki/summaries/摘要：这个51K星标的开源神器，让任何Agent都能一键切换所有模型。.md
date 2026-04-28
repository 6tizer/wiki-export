---
title: 摘要：这个51K星标的开源神器，让任何Agent都能一键切换所有模型。
type: summary
tags:
- CLI 工具
- 模型部署
status: 已审核
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: https://www.notion.so/350701074b688179bdbbdaffee317bbd
notion_url: https://www.notion.so/Tizer/8802320dbe4a42c48cf9522b4ea18bc8
notion_id: 8802320d-be4a-42c4-8cf9-522b4ea18bc8
---

## 一句话摘要

CC Switch 是一个 51K 星标的开源桌面工具，通过自动改写配置文件实现跨 Agent CLI 工具（Claude Code、Codex、OpenClaw 等）的一键模型切换、热切换、用量追踪与故障转移路由。

## 关键洞察

- **配置文件痛点**：手动编辑 Agent 工具的 settings.json（填写 base_url、auth_token、model name 等字段）对非程序员极不友好，CC Switch 将操作简化为「选供应商→填 API Key→选模型」三步

- **热切换能力**：无需重启终端或关闭 Claude Code 会话，在模型空闲时通过菜单栏一键切换，下一轮对话立即使用新模型，适合按任务复杂度动态调整成本

- **故障转移路由**：本地代理服务拦截请求，当主供应商宕机/额度耗尽/超时时自动切到备选供应商，支持熔断保护，适合长时间无人值守任务

- **广泛兼容**：支持 Claude Code、Codex、Gemini CLI、OpenCode、OpenClaw、Hermes 六大 Agent 工具，内置 40+ 家模型供应商预设（含国内主流：智谱、MiMo、DeepSeek、千问、Kimi 等）

- **本地数据安全**：所有配置存储在本地 SQLite 数据库（~/.cc-switch/cc-switch.db），不依赖云端

## 提取的概念

- [CC Switch](entities/CC Switch.md)

- [Agent 模型热切换](concepts/Agent 模型热切换.md)

- [API 故障转移路由](concepts/API 故障转移路由.md)

## 原始文章信息

- **作者**：数字生命卡兹克

- **来源**：微信公众号

- **发布时间**：2026-04-28

- **原文链接**：[这个51K星标的开源神器，让任何Agent都能一键切换所有模型。](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA%3D%3D&mid=2647681944&idx=1&sn=e3f6218daedb4dbfc9931b6a3adcbc8c&chksm=f16914fa8815127eb4dc837b85b4005493b1572de01a24a2ae5d1a9a48a47169742d7150ac69#rd)

## 个人评注

CC Switch 对于使用多个 Agent CLI 工具的开发者来说是一个实用的基础设施工具。其故障转移路由功能与 OpenClaw 的长时间自主运行场景高度契合——在 OpenClaw 执行 overnight 任务时，如果某个模型供应商出现问题可以自动切换，避免任务中断。成本管理功能也值得关注，可以在 content pipeline 中根据任务复杂度动态选择模型。
