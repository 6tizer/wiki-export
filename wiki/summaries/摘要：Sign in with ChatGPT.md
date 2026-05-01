---
title: 摘要：Sign in with ChatGPT
type: summary
tags:
- CLI 工具
- 长期记忆
- Harness 工程
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b68818fb2cecdb2e0ab92af
notion_url: https://www.notion.so/Tizer/c788d364e7ee4c4ca258e724f6bdfab2
notion_id: c788d364-e7ee-4c4c-a258-e724f6bdfab2
---

## 一句话摘要

Codex 0.121.0 把插件市场安装、TUI 历史反向搜索、可查看与清理的记忆控制，以及基于 bubblewrap 的开发容器沙箱整合进同一轮发布，显示出 Coding Agent 正在同时补齐可扩展性、可控性与安全性。

## 关键洞察

- 这次更新不只是功能堆叠，而是在补齐 Coding Agent 产品走向日常可用所需的关键基础设施。

- `codex marketplace add` 说明 Codex 正在把插件分发能力产品化，平台生态接口开始成形。

- 记忆控制从“默认记住”升级为“用户可查看、重置、删除”，本质上是在增强人对 Agent 状态的掌控。

- `Ctrl+R` 反向搜索把成熟终端交互能力带回 Agent CLI，降低高频操作摩擦。

- bubblewrap 沙箱强调本地 Agent 在执行代码与操作开发容器时，安全边界会越来越重要。

## 提取的概念

- [Codex](entities/Codex.md)

- [Codex 插件系统](concepts/Codex 插件系统.md)

- [Plugin Marketplace](concepts/Plugin Marketplace.md)

- [记忆控制](concepts/记忆控制.md)

- [TUI 历史反向搜索](concepts/TUI 历史反向搜索.md)

- [bubblewrap](concepts/bubblewrap.md)

## 原始文章信息

- 作者：@Codex_Changelog

- 来源：X书签

- 发布时间：2026-04-15

- 原文链接：[https://x.com/Codex_Changelog/status/2044526487119007827](https://x.com/Codex_Changelog/status/2044526487119007827)

- 源文章页面：Codex CLI 0.121.0：插件市场、Memory 控制与沙箱安全全面升级

## 个人评注

- 对 Tizer 的工作流来说，这类更新值得重点关注，因为它直接影响 Coding Agent 在内容生产、自动修补、终端操作与安全执行中的可落地性。

- 如果后续 Codex 的插件安装、记忆控制与沙箱能力继续开放配置接口，它会更接近可纳入 HITL 内容流水线的通用执行端。
