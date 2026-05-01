---
title: Command Hooks
type: concept
tags:
- 上下文管理
- CLI 工具
- Harness 工程
status: 审核中
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/08ad50e255eb4612b186b9a0321f8ad4
notion_id: 08ad50e2-55eb-4612-b186-b9a0321f8ad4
---

## 定义

Command Hooks 是 Claude Code Hooks 中最常用的一类执行方式：通过运行 shell 命令读取事件 JSON，并用退出码或结构化输出决定后续流程。

## 核心要点

- 速度快、实现简单，适合文件保护、自动格式化、日志记录、测试触发等本地自动化场景。

- 可直接读取 `tool_input`、文件路径、命令内容等上下文，把项目规范转成真正会执行的规则。

- 通过 `exit 0` 放行、`exit 2` 拦截，是把概率性提示升级成确定性工程守卫的主力方案。

## 来源引用

- [摘要：打造可靠的 AI 编程环境：Claude Code Hooks 完整开发者指南](summaries/摘要：打造可靠的 AI 编程环境：Claude Code Hooks 完整开发者指南.md)（[原文](https://mp.weixin.qq.com/s?__biz=MjM5NzA1NzMyOQ%3D%3D&mid=2247486947&idx=1&sn=92ca2b4f44cadd181eb6b40087a2531b&chksm=a7e11bb1d385c29bce1587e79207574fba3835086a7fbed287fbf12e86194e37111fb2982d78#rd)）

## 关联概念

- [Claude Code Hooks](concepts/Claude Code Hooks.md)

- [PreToolUse](concepts/PreToolUse.md)

- [PostToolUse](concepts/PostToolUse.md)
