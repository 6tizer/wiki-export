---
title: 摘要：首发开源7*24小时不停干活的Harness for OpenClaw！
type: summary
tags:
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-28'
source_tags: OpenClaw, Harness, 开源项目
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c51b3735c7aa4c1fb8f6e5686c1416be
notion_id: c51b3735-c7aa-4c1f-b8f6-e5686c1416be
---

## 一句话摘要

OpenHarness 是清华团队开源的基于 Harness Engineering 理念的长期自治 AI 代理执行框架，支持7x24小时不间断运行，实现任务全生命周期的工程化管理、状态可追溯和熵控制。

## 关键洞察

- **Harness vs Skills 的区别**：Skills 定义「能做什么」，Harness 定义「如何持续稳定地做完」

- **全生命周期管理**：初始化→配置→启动→状态跟踪→验证→熵控制，形成完整闭环

- **状态可追溯**：[heartbeat.md](http://heartbeat.md/) 记录执行状态，[progress.md](http://progress.md/) 存每次执行详情，连续失败≥3次自动告警

- **熵控制机制**：主动压缩日志、清理临时文件、校验状态一致性，防止长期运行后系统混乱

- **外部化验证**：验证脚本独立于 AI 主体，避免「自证完成」的偏见

- **极简安装**：克隆到 `~/.openclaw/workspace/harness`，一句话触发框架

## 提取的概念

- OpenHarness

- Harness Engineering

## 原始文章信息

- **作者**: 清新研究

- **来源**: 微信公众号

- **发布时间**: 2026-03-30

- **GitHub**: [https://github.com/thu-nmrc/OpenHarness](https://github.com/thu-nmrc/OpenHarness)

## 个人评注

直接关系 Tizer 的 OpenClaw 自动化工作流——OpenHarness 的熵控制和状态可追溯机制可以让长期运行的内容 pipeline 更稳定可靠。
