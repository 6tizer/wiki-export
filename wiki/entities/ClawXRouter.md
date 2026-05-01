---
title: ClawXRouter
type: entity
tags:
- OpenClaw
status: 审核中
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/fc072c45acea4076a4bbb1207906206e
notion_id: fc072c45-acea-4076-a4bb-b1207906206e
---

## 定义

ClawXRouter 是清华 THUNLP、中国人大、面壁智能与 OpenBMB 联合开源的端云协同 AI 智能体路由插件，适配 OpenClaw 生态，通过三级隐私路由和性价比感知路由实现成本陆58%、性能提6.3%。

GitHub: [https://github.com/Openbmb/ClawXRouter](https://github.com/Openbmb/ClawXRouter)

## 核心机制

### 三级隐私路由

- **S3（私密）**： SSH 私鑰、硬编码密码——物理隔离，完全局端处理

- **S2（敖感）**：内网 IP、手机号——智能脱敏（如将“王小二”替换为 `[REDACTED:NAME]`）后上云

- **S1（安全）**：普通公开问题——直接发往云端

### 性价比感知路由

- LLM-as-Judge 小模型评估任务复杂度，自动分发给最合适模型

### 双轨记忆

- 云端只看到脱敏后的 `MEMORY.md`，局端保留完整 `MEMORY-FULL.md`

## 来源引用

- [摘要：龙虾成本狂陆58%！ClawXRouter开源智能调度员](summaries/摘要：龙虾成本狂陆58%！ClawXRouter开源智能调度员.md)
