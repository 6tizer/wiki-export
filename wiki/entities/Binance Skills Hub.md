---
title: Binance Skills Hub
type: entity
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/b38538c788ca40048420ab6767771db4
notion_id: b38538c7-88ca-4004-8420-ab6767771db4
---

## 定义

Binance Skills Hub 是币安于 2026 年 3 月 3 日在 GitHub 开源的 **AI Agent 技能包仓库**，让任意 AI Agent（不管是 Claude、GPT 还是 LangChain/CrewAI 搭建的）都能通过统一接口直接调用币安的数据和交易能力。

## 首批 7 个技能（2026.3.3 上线）

- **Binance Spot Skill**：实时现货行情查询、直接执行现货下单（含 OCO/OPO/OTOCO 组合订单）

- **Query Token Info**：查询代币基本信息、市值、流通量

- **Crypto Narrative**：追踪市场热点叙事

- **Query Address Info**：查询链上地址余额、交易历史

- **Smart Money Tracking**：聪明钱地址监控

- **Contract Audit Skill**：对代币合约进行安全体检

- **Trading Signal**：提供附带触发价、maxGain、exitRate 等指标的交易信号

## 项目数据（2026 年 4 月）

- GitHub Stars：360

- Fork：63

- 开源，任何 Agent/框架均可接入

- 上线不到一周已有 97 个开放 PR

## 典型流程

叙事发酵 → 地址监控 → 合约体检 → 现货交易，全链路操作无需切换工具。

## 注意事项

- API Key 务必设置 IP 白名单，禁用提现权限，定期轮换密钥

- 主网交易前务必在 Testnet 跑通全流程

## 来源引用

- CyberMolt：一键领养带币安全套技能的 AI 交易 Agent

- [摘要：币安 Skills Hub：给你的 OpenClaw 龙虾装上「币安级大脑」](summaries/摘要：币安 Skills Hub：给你的 OpenClaw 龙虾装上「币安级大脑」.md)
