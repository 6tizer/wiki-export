---
title: Agent Reach
type: concept
tags:
- MCP 协议
status: 审核中
confidence: medium
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/7f816d82e59f418387468207349ba0b0
notion_id: 7f816d82-e59f-4183-8746-8207349ba0b0
---

## 定义

Agent Reach 是一个开源脚手架（scaffolding）工具，通过统一接口让 AI Agent 轻松访问 Twitter、YouTube、Reddit、B 站、小红书等 12+ 互联网平台内容，解决 Agent 联网难的问题。完全免费开源且隐私安全。

## 设计理念

- 定位是"脚手架"而非"框架"：安装后 Agent 直接调用上游工具（xreach/yt-dlp/gh CLI 等），不经过包装层

- 每个渠道对应独立上游工具，可插拔替换

- Cookie 只存本地，完全开源可审查

- 社区驱动持续更新，可集成到个人 skills 工具链或 Agent 框架中

## 支持平台

| 平台 | 上游工具 |

| --- | --- |

| 网页 | Jina Reader |

| YouTube | yt-dlp |

| Twitter/X | xreach |

| GitHub | gh CLI |

| 小红书 | xiaohongshu-mcp |

| Reddit | JSON API + Exa |

| B站/抖音 | yt-dlp / mcporter |

| 全网搜索 | Exa via mcporter |

## 安装方式

pip install 一键安装，或将以下指令发给任意 Agent 自动完成安装：

```javascript
帮我安装 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

## 来源引用

- [摘要：Agent Reach 开源 Agent 联网工具](summaries/摘要：Agent Reach 开源 Agent 联网工具.md)

- [摘要：给 OpenClaw 装上"全网眼睛"：Agent-Reach 集成实践](summaries/摘要：给 OpenClaw 装上全网眼睛：Agent-Reach 集成实践.md) — 将 Agent-Reach 集成到个人 Skills，强调「脚手架不是框架」的设计哲学和 Vibe Coding 实践

- [摘要：Agent Reach 一键解锁全网调研超能力](summaries/摘要：Agent Reach 一键解锁全网调研超能力.md) — 详细拆解可插拔 Channel 架构、健康检查机制和 Cookie 安全设计，对比 Perplexity/Tavily/Firecrawl 等方案

- [摘要：无需任何 API 费用，这个Agent 拥有"看遍全网"的超能力](summaries/摘要：无需任何 API 费用，这个Agent 拥有看遍全网的超能力.md)
