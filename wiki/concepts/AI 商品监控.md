---
title: AI 商品监控
type: concept
tags:
- 浏览器自动化
- 内容自动化
status: 草稿
confidence: medium
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6cf5a6550abb418b9246a19086e963d6
notion_id: 6cf5a655-0abb-418b-9246-a19086e963d6
---

## 定义

AI 商品监控是一种利用浏览器自动化爬取电商/二手平台商品信息、再通过大语言模型进行智能筛选和推荐的技术模式。核心流程为：定时爬取 → AI 分析（图文理解、卖家画像评估、性价比判断）→ 条件过滤 → 实时推送通知。

## 关键要点

- 典型技术栈：Playwright/Puppeteer（浏览器自动化）+ LLM（智能分析）+ 推送服务（[ntfy.sh](http://ntfy.sh/)、企业微信等）

- 与传统关键词监控的区别：AI 可理解图片内容、分析卖家可信度、综合判断商品性价比

- 需处理反爬机制：模拟真人操作、Cookie 管理、请求频率控制

- 应用场景：闲鱼捡漏、限量商品监控、价格追踪

- 法律合规注意：需遵守平台用户协议，避免过于频繁的请求

## 来源引用

- [摘要：AI圈公认最强的二手好物监控工具，懂的人已经开始躺着捡漏了](summaries/摘要：AI圈公认最强的二手好物监控工具，懂的人已经开始躺着捡漏了.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzk0MjM4Mjc1Mw%3D%3D&mid=2247491231&idx=1&sn=69bff8744d38de55a8c206628ca58e94&chksm=c3df7fa32e5c05721c188c4fdc84de9a7289b15b6de4d38a2444654dbd34c79f0081fec56a10#rd)）
