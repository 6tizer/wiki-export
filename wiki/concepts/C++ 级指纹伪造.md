---
title: C++ 级指纹伪造
type: concept
tags:
- 安全/隐私
- 开发工具
status: 草稿
confidence: medium
last_compiled: '2026-04-25'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/497b9923799f41269a4bcc22932f7cfc
notion_id: 497b9923-799f-4126-9a4b-cc22932f7cfc
---

## 定义

C++ 级指纹伪造是指在浏览器底层实现 Canvas、WebGL、AudioContext 等指纹特征的伪装，而不是仅在 JavaScript 层做表面修补。

## 关键要点

- 更难被页面脚本直接识别和绕过

- 比常见的前端 stealth 补丁更接近真实设备

- 常用于高风控浏览器自动化场景

## 来源引用

- 未匹配：camoufox-cli：让 AI Agent 的浏览器不再被识破
