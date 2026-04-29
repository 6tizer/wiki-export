---
title: sentrux
type: entity
tags:
- Harness 工程
- CLI 工具
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a25663325947437e84883930998de798
notion_id: a2566332-5947-437e-8488-3930998de798
---

## 定义

sentrux 是一个纯 Rust 编写的开源实时架构传感器，专为 AI 编码 Agent（如 Claude Code、Cursor、Windsurf 等）提供闭环架构质量反馈。通过实时扫描代码库结构（而非 diff 或终端输出），将文件、依赖关系、架构关系可视化为交互式树状图（Treemap），并基于 5 个根本原因指标给出 0-10000 分的连续质量评分。

## 关键要点

- **语言**：纯 Rust 实现，毫秒级扫描速度

- **可视化**：实时交互式树状图，显示依赖关系边；Agent 修改文件时文件会发光

- **MADER 五维指标**：Modularity（模块化）、Acyclicity（无环性）、Depth（深度）、Equality（均衡性）、Redundancy（冗余性）

- **质量门禁**：`sentrux gate --save .` 保存基线，`sentrux gate .` 对比基线捕获架构退化

- **规则引擎**：定义架构约束，`sentrux check .` 在 CI 中强制执行

- **MCP 集成**：通过 `--mcp` 参数为 AI Agent 提供实时架构健康数据

- **52 种语言支持**：基于 tree-sitter 插件体系

- **核心理念**：传感器 + 规则引擎 + 执行器（AI Agent）闭环，将 AI 生成的代码从「失控的创造力」转化为「受约束的架构演进」

## 仓库信息

- GitHub: [sentrux/sentrux](https://github.com/sentrux/sentrux)

- 协议：开源

- 安装方式：Homebrew (macOS)、curl (Linux)、二进制下载 (Windows)

## 来源引用

- [摘要：sentrux：一个开源的代码架构传感器，让大模型守住代码底线！](summaries/摘要：sentrux：一个开源的代码架构传感器，让大模型守住代码底线！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484673&idx=1&sn=9a52bf97b7c11eef0414da5f957caba2&chksm=f544a6ba6d1eae6bf4261adba920e882c604a63f51e87a21903d6ed42087d1a09eb0224e9d2d#rd)）

## 关联概念

- [架构质量门禁](concepts/架构质量门禁.md)

- [Tree-sitter](entities/Tree-sitter.md)

- [MCP 协议](concepts/MCP 协议.md)
