---
title: 摘要：OpenClaw 手机版部署教程：用旧安卓跑起你的专属 AI Agent
type: summary
tags:
- OpenClaw
- 模型部署
- Agent 协作模式
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: OpenClaw, Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/05d5951fb57b43e98ea07c3b62283b72
notion_id: 05d5951f-b57b-43e9-8ea0-7c3b62283b72
---

## 一句话摘要

用一部闲置安卓旧手机，通过 Termux 安装 OpenClaw，可以低成本体验「AI 在后台替你工作」——本文提供完整的零基础七步部署指南，作者亲身踩坑整理。

## 关键洞察

- **OpenClaw 现象级增速**：60 天内 Stars 突破 25 万，超越 React 成为 GitHub 史上增速最快开源项目

- **核心理念转变**：不是你去找 AI 对话，而是 AI 在你的基础设施里替你工作

- **Termux-chroot 是关键**：每次重新启动 Bot 前必须执行 `termux-chroot`，「欺骗」AI 让它以为运行在标准 Linux 环境

- **主要痛点**：发热耗电、网络切换掉线、手机版不支持部分高级 Skills（本地文件操作）

- **轻量替代品对比**：Nanobot（4000 行 Python 代码，适合学习）、PicoClaw（资源占用极低）

## 提取的概念

OpenClaw

## 原始文章信息

- **作者**：卡神 Karu

- **来源**：X 书签

- **链接**：[https://x.com/edwordkaru/status/2020764405584294275](https://x.com/edwordkaru/status/2020764405584294275)

## 个人评注

手机版部署作为低成本入门体验有价值，但稳定性和功能完整性不如 Mac/VPS 方案。对于 Tizer 的正式工作流建议还是使用 Mac Mini 或 VPS。
