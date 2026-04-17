---
title: 摘要：OpenClaw 订阅套餐接入指南：用你已付的 $20 跑满三大顶级模型
type: summary
tags:
- OpenClaw
- LLM
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: OpenClaw, LLM, Agent, 自动化
source_article_url: ''
notion_url: https://www.notion.so/c2eb8e178ae1458197b09b650d27363c
notion_id: c2eb8e17-8ae1-4581-97b0-9b650d27363c
---

## 一句话摘要

Claude Pro、ChatGPT Plus、Gemini Advanced 三个 $20/月订阅套餐均可通过 OAuth/CLI 方式接入 OpenClaw，但需注意 Claude 侧有违反服务条款的封号风险，GPT + Gemini 组合相对稳定。

## 关键洞察

- **三大接入方式**：Claude 用 `claude setup-token`、GPT 用 `@openai/codex` OAuth、Gemini 用 `@google/gemini-cli` OAuth

- **Claude 封号风险真实存在**：Anthropic 已明确订阅套餐仅限 Claude Code，Reddit 已有大量被封号反馈

- **Gemini OAuth 频繁掉线**：GitHub Issue #7549 记录了 refresh token 不自动续期问题，每小时重新授权

- **Token 消耗偏高**：建议用 `/compact` 定期压缩长会话，避免 overhead 过大

- **GPT + Gemini 作为稳定底座**：Claude 如有合规顾虑，GPT + Gemini 组合是更稳妥选择

## 提取的概念

OpenClaw

## 原始文章信息

- **作者**：范凯说 AI

- **来源**：X 书签

- **链接**：[https://x.com/fankaishuoai/status/2022952496189313404](https://x.com/fankaishuoai/status/2022952496189313404)

## 个人评注

订阅套餐接入 OpenClaw 是极具性价比的配置方式，但 Claude 侧的合规问题值得认真评估。对于 Tizer 的 OpenClaw 工作流，GPT + Gemini 的稳定组合是当前最推荐的底座方案。
