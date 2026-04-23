---
title: Cursor Skills 生态
type: concept
tags:
- Agent 技能
- 开发工具
- 工作流
- Agent 编排
- 知识管理
status: 审核中
confidence: medium
last_compiled: '2026-04-19'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/b6efbd7fd8bf48dab13e1920845fd5a8
notion_id: b6efbd7f-d8bf-48da-b13e-1920845fd5a8
---

## 定义

Cursor Skills 生态是 Cursor 从 2.4 版本开始支持的 **Agent Skills（智能体技能）扩展体系**，允许用户安装可移植、可版本控制的能力包，教会 Cursor 如何完成特定领域的任务。

## 技术细节

- 技能以 `.md` 文件形式存储在 `.cursor/skills/` 目录中

- Agent 在对话中自动判断何时调用哪个技能

- 2026 年 2 月正式推出 [Cursor Marketplace](https://cursor.com/marketplace)，集成 Amplitude、AWS、Figma、Linear、Stripe 等呈余官方插件

## 主要技能（新手建议）

1. **Capability Evolver**：市场下载量霖榜第一，观察用户习惯自动调整 Cursor 行为

1. **Self-Improving Agent**：任务完成后自动复盘、越用越聪明

1. **Summarize**：支持合同、财报、论文、视频、网页等一键摘要

1. **Agent Browser**：让 Cursor 能操作浏览器，实现网页抓取、表单填写

## 与同类方案对比

| 方案 | 定位 | 特点 |

| --- | --- | --- |

| Cursor Skills | 编辑器内置扩展 | 与代码库深度集成 |

| Claude MCP 插件 | 基于 MCP 协议 | 跨平台通用性更强 |

| Windsurf 规则系统 | 竞品编辑器 | 生态规模小于 Cursor |

## 注意事项

- Cursor Marketplace 于 2026 年 2 月才正式上线，生态尚在成长期

- Capability Evolver / Self-Improving Agent 为社区技能，非 Cursor 官方出品

- 技能自动触发准确率依赖 `description` 字段的质量

## 来源引用

- [摘要：新手必装的 6 个 Cursor 技能：让你的 AI 编程助手越来越懂你](summaries/摘要：新手必装的 6 个 Cursor 技能：让你的 AI 编程助手越来越懂你.md)
