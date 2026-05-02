---
title: gnhf
type: entity
tags:
- 代码生成
- CLI 工具
- Harness 工程
status: 草稿
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6057512449c940c7a511ca260d6578f7
notion_id: 60575124-49c9-40c7-a511-ca260d6578f7
---

## 定义

gnhf（good night, have fun）是一个开源的 Coding Agent 隔夜编排器（orchestrator），用 TypeScript 编写，支持 macOS、Linux 和 Windows。它让用户在睡前设定一个编码目标，由 AI 编码助手在无人值守的情况下按照严格的 Git 纪律持续迭代改进代码。

**别名**：good night, have fun

## 关键要点

- 采用「成功提交、失败回滚」的 Git 纪律迭代循环，每次成功改动生成独立 commit，失败则 `git reset --hard`

- Agent-agnostic 设计，开箱支持 Claude Code、Codex、Rovo Dev、OpenCode、GitHub Copilot CLI、Pi 等多种 Coding Agent

- 通过 [notes.md](http://notes.md/) 实现跨迭代的共享记忆，后续迭代可读取前序迭代的上下文

- 支持 git worktree 模式，允许多个 Agent 在同一仓库上并行工作互不干扰

- 连续 3 次失败自动中止，支持 `--max-iterations` 和 `--max-tokens` 控制运行上限

- GitHub 星标 1.3K+

## 档案信息

- **GitHub**: [https://github.com/kunchenguid/gnhf](https://github.com/kunchenguid/gnhf)

- **语言**: TypeScript

- **安装**: `npm install -g gnhf`

- **许可证**: 未明确

- **类似工具**: ralph、autoresearch

## 关联概念

- [Agent 隔夜编排](concepts/Agent 隔夜编排.md)

- [Git 纪律迭代循环](concepts/Git 纪律迭代循环.md)

- [autoresearch](entities/autoresearch.md)

## 来源引用

- [摘要：1.3K Star！让 Coding Agent 在你睡觉时持续工作的神奇开源工具！](summaries/摘要：1.3K Star！让 Coding Agent 在你睡觉时持续工作的神奇开源工具！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ%3D%3D&mid=2247506012&idx=1&sn=59df2a6364a3fa6f7b5c6fd4fc260317&chksm=c19e01c3a46ee4fa7c969e3448080d0d1b886bf7118572e4e3e26f60022a32a35d7c8ab3b2da#rd)）
