---
title: 摘要：实测小米MiMo-V2.5-Pro，这可能是目前国内最适合Claude Code的新模型。
type: summary
tags:
- 代码生成
- 模型评测
- CLI 工具
status: 已审核
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b68811984acf16e04a1150c
notion_url: https://www.notion.so/Tizer/e471d3355d3a4c2999dff55b9fed07dc
notion_id: e471d335-5d3a-4c29-99df-f55b9fed07dc
---

## 一句话摘要

MiMo-V2.5-Pro 是目前配合 Claude Code 使用体验最好的国产模型之一，在工具调用、代码开发和复杂部署任务上接近前沿水平，且价格仅为 Opus 4.6 的约 40%。

## 关键洞察

- MiMo-V2.5-Pro 在 AA 榜（Artificial Analysis）上与 Kimi K2.6 并列开源第一，支持 100 万 token 上下文窗口

- API 价格 ¥7/¥21（输入/输出）每百万 token（256K 内），约比 Opus 4.6 便宜 60%；新 Token Plan 统一收费不区分上下文长度

- 通过 cc-switch 工具可在 Claude Code 中一键切换到 MiMo-V2.5-Pro，配置流程简单（选择 Xiaomi MiMo 供应商 → 填 API Key → 模型名 mimo-v2.5-pro）

- 实测完成了数据分析平台搭建（飞书多维表格→可视化网页）、服务器部署（含飞书企业认证）、统一登录中台接入等复杂工程链路，均一次性通过

- 前端审美能力仍有不足（类似 GPT-5.4/5.5），但核心逻辑、工具调用和代码能力表现优秀

## 提取的概念

- [Xiaomi MiMo-V2.5-Pro](entities/Xiaomi MiMo-V2.5-Pro.md)

- [Claude Code](entities/Claude Code.md)

- [CC Switch](entities/CC Switch.md)

## 原始文章信息

- 作者：@Khazix0918（数字生命卡兹克）

- 来源：X书签

- 发布时间：2026-04-24

- 原文链接：[https://x.com/Khazix0918/status/2047526414161965523](https://x.com/Khazix0918/status/2047526414161965523)

## 个人评注

这篇实测报告对 Tizer 的工作流有直接参考价值：当 Claude 原生 API 不可用或成本过高时，MiMo-V2.5-Pro 可作为国内替代方案，配合 cc-switch 实现无缝切换。文章中展示的「飞书数据分析平台 → 服务器部署 → 统一登录中台接入」的完整链路，是 HITL 工具链搭建和 Skills 分发的典型工程案例。作者还提到 Skills 同步平台的 BUG 修复也由 MiMo-V2.5-Pro 完成，进一步佐证了该模型在实际项目维护中的可用性。
