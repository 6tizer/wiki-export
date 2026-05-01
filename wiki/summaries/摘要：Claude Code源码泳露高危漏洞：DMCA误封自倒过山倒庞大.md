---
title: 摘要：Claude Code源码泳露高危漏洞：DMCA误封自倒过山倒庞大
type: summary
tags:
- Agent 安全
- AI 产品
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化, Claude
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4874634c4b7a414a8c2c0c8d621556bc
notion_id: 4874634c-4b7a-414a-8c2c-0c8d621556bc
---

**一句话摘脁**：Anthropic 展开 DMCA 封杀却误封了 8100 个仓库（8000 个误伤），并暴露了 Claude Code 中 CVE-2025-59536 高危远程控制漏洞，并展现了其“无责备文化”的平和回应。

---

## 关键洞察

- **DMCA 混乱**：Anthropic 针对 97 个仓库发出 DMCA，但 GitHub 触发连锁封杀 8100 个库，其中大部分与泳露无关

- **CVE-2025-59536**：高危远程控制漏洞，在被动过手脚的项目目录下输入 `claude` 可能让黑客远程控制设备，调用摄像头、窃取密鑰

- **无责备文化**：CC 之父 Boris Cherny 回应“这是流程/基础设施问题，不是个人责任”，引发全网好评

- **建议**：立即升级 Claude Code 到最新版本

## 原始文章信息

- **作者**：新智元

- **来源**：微信公众号

- **发布日期**：2026-04-02

- **链接**：[https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652689091](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652689091)
