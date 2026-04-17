---
title: 摘要：我用纯 Rust 写了一个 AI Agent 驱动的爬虫，万物皆可爬
type: summary
tags:
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, OpenClaw, 自动化
source_article_url: ''
notion_url: https://www.notion.so/e26543b940a749b0a5c17bd06d7ed49e
notion_id: e26543b9-40a7-49b0-a5c1-7bd06d7ed49e
---

**一句话摘要**

Clawer 是用纯 Rust 实现的 AI Agent 驱动智能爬虫，结合 ReAct Agent 框架让 LLM 自主决策页面分析和数据提取，实现"目标驱动"而非"规则驱动"的爬取范式。

**关键洞察**

- 范式转变：传统爬虫"规则驱动"（人写选择器）→ Clawer"目标驱动"（告诉 Agent 要什么，Agent 自己想办法）

- ReAct 循环：Thought（思考）→ Action（行动）→ Observation（观察）→ 再思考，Agent 遇到报错换方案，遇到翻页自动翻，遇到动态加载自动等待

- 10 个内置工具：browse_page/click/input_text/scroll/extract/execute_js/screenshot/download/web_search/save_result，Agent 自主选择调用顺序

- 架构：CDP 协议控制真实 Chrome 浏览器，支持 JS 渲染 SPA、需要登录的页面

- 技术栈：Rust + Tokio + chromiumoxide + Tauri v2，打包体积比 Electron 小 10 倍

**提取的概念**

- ReAct Agent

- Clawer

**原始文章信息**

- 作者：老码小张

- 来源：微信公众号

- 发布时间：2026-04-02

- 链接：[https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg==&mid=2247493098](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493098)

**个人评注**

Clawer 的 ReAct 驱动爬虫思路对 OpenClaw 生态有参考价值——用 Agent 替代手写规则是 Web Scraping 的方向，与 content pipeline 的数据采集环节直接相关。Rust + Tauri 的技术选型也值得关注。
