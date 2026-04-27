---
title: 摘要：Claude Code 工作流模板 v2
type: summary
tags:
- Harness 工程
- 上下文管理
- CLI 工具
status: 已审核
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b688154bc77eec18f6679a5
notion_url: https://www.notion.so/Tizer/fd4de88a1db647f2be3e457b36b6ca88
notion_id: fd4de88a-1db6-47f2-be3e-457b36b6ca88
---

## 一句话摘要

claude-code-workflow v2 通过新增 PreToolUse Hook 层（Layer 3），将 Claude Code 的规则执行从「希望模型自觉」升级为「工具调用前强制注入」，配合三层上下文加载、Memory Flush 和多档任务路由，构建了一套可持续、会自我改进的 AI 编程搭档系统。

## 关键洞察

- **Hook 才是强制拦截**：规则只是希望模型自觉，v2 新增 Layer 3（PreToolUse Hook）在工具调用前强制注入规则，不再赌模型记得

- **三层加载架构成本敏感**：Layer 0 常载规则仅 ~2K token，Layer 1 按需读文档，Layer 2 热数据随取随用，避免全量塞入浪费 token

- **验证 > 感觉**：完成前验证 Skill 要求必须跑验证命令并读输出才能声称完成，消灭「应该好了吧」失败模式

- **多档任务路由**：按任务复杂度自动匹配 Opus / Sonnet / Haiku / Codex / Local 档位，兼顾质量与成本

- **Memory Flush 自动落盘**：任务完成、提交、退出时自动保存进度，关窗不丢上下文

## 提取的概念

- [claude-code-workflow](entities/claude-code-workflow.md)

- [Claude Code Hooks](concepts/Claude Code Hooks.md)

- [L0/L1/L2 分层加载](concepts/L0-L1-L2 分层加载.md)

- [Memory Flush](concepts/Memory Flush.md)

- [完成前验证](concepts/完成前验证.md)

- [多档任务路由](concepts/多档任务路由.md)

- [SSOT 路由表](concepts/SSOT 路由表.md)

## 原始文章信息

- **作者**：@runes_leo（Leo）

- **来源**：X 书签

- **发布时间**：2026-04-25

- **原文链接**：[https://x.com/runes_leo/status/2048013195563172162](https://x.com/runes_leo/status/2048013195563172162)

- **GitHub 仓库**：[https://github.com/runesleo/claude-code-workflow（666](https://github.com/runesleo/claude-code-workflow（666) Stars）

## 个人评注

该工作流模板与 Tizer 的 Harness 工程理念高度吻合——通过结构化规则和 Hook 机制约束 AI 行为，而非依赖 prompt 层面的自觉。其 Layer 3 的 PreToolUse Hook 强制注入思路，可直接参考用于 OpenClaw 的 Skill 执行验证和安全边界设计。Memory Flush 和 SSOT 路由表模式也与知识管理流水线中的状态持久化需求相通。
