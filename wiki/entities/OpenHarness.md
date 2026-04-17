---
title: OpenHarness
type: entity
tags:
- OpenClaw
- 工作流
status: 审核中
confidence: high
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/6b6f273febd242bf9ca08d4a8ec0906c
notion_id: 6b6f273f-ebd2-42bf-9ca0-8d4a8ec0906c
---

## 定义

OpenHarness 是清华 THUNLP 实验室发布的开源 Harness 框架，基于 Harness Engineering（驾驭工程）理念构建，支持 7*24 小时不间断自治运行的 AI 代理执行框架，是 OpenClaw 的黄金搭档。

GitHub: [https://github.com/thu-nmrc/OpenHarness](https://github.com/thu-nmrc/OpenHarness)

## 核心组件（对应 Harness Engineering 六大组件）

1. **工作区管理**：模板初始化、必需文件校验、配置占位符检测

1. **调度配置**：支持 Cron/时间间隔，兼容中英文配置格式

1. **状态生命周期**：管理启动、完成、失败、阻塞等状态，统计执行次数

1. **结果验证**：校验输出目录、心跳、进度健康度，生成验证报告

1. **系统稳定性**：日志归档、临时文件清理、状态一致性校验（熵控制）

1. **可视化追溯**：[heartbeat.md](http://heartbeat.md/) 实时状态、[progress.md](http://progress.md/) 执行详情

## v4.1 特性

### 三层自愈记忆架构

- **Layer 1**（指针索引层 [heartbeat.md](http://heartbeat.md/)）：始终保持在 2KB 以内，常驻上下文

- **Layer 2**（按需知识层）：只有当前任务步骤需要时才加载特定知识文件

- **Layer 3**（结构化日志层）：只追加的执行流日志，永远不被完整读取，只能通过 grep 检索

### 熔断机制

连续失败 3 次自动切断，防止 API 额度被恶意消耗

### KAIROS 梦境模式

`harness_dream.py`：系统空闲时分析执行日志，将提炼出的最佳实践反馈到 `playbook.md`

### 多智能体协同

基于文件系统 IPC，协调器通过 inbox/outbox 目录分发任务

## 关键设计

- **外部化验证**：验证脚本独立于 AI 主体，避免「自证完成」的偏见

- **熵控制机制**：防止长期运行后文件膨胀和状态混乱

## 安装

```bash
git clone https://github.com/thu-nmrc/OpenHarness ~/.openclaw/workspace/harness
```

OpenClaw 自动识别 [SKILL.md](http://skill.md/)，赋予 Harness 能力。

## 来源引用

- [摘要：首发开源7*24小时不停干活的Harness for OpenClaw！](summaries/摘要：首发开源724小时不停干活的Harness for OpenClaw！.md)

- [摘要：OpenHarness重构底层骨架：三层自愈记忆+KAIROS梦境模式](summaries/摘要：OpenHarness重构底层骨架：三层自愈记忆+KAIROS梦境模式.md)

- 《OpenHarness：港大实验室用 3% 的代码复刻了 80% 的 Claude Code 能力》｜X书签文章｜原文链接：[https://x.com/0xLogicrw/status/2039967740140867994](https://x.com/0xLogicrw/status/2039967740140867994)｜来源条目：[摘要：OpenHarness：港大实验室用 3% 的代码复刻了 80% 的 Claude Code 能力](summaries/摘要：OpenHarness：港大实验室用 3% 的代码复刻了 80% 的 Claude Code 能力.md)

- 《OpenHarness：港大开源的 Claude Code 轻量平替，44 倍瘦身只保留 98% 核心功力》｜X书签文章｜原文链接：[https://x.com/Jason23818126/status/2040624214303211626](https://x.com/Jason23818126/status/2040624214303211626)｜来源条目：[摘要：OpenHarness：港大开源的 Claude Code 轻量平替，44 倍瘦身只保留 98% 核心功力](summaries/摘要：OpenHarness：港大开源的 Claude Code 轻量平替，44 倍瘦身只保留 98% 核心功力.md)
