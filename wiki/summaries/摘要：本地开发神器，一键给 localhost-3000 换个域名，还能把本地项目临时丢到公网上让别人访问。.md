---
title: 摘要：本地开发神器，一键给 localhost:3000 换个域名，还能把本地项目临时丢到公网上让别人访问。
type: summary
tags:
- CLI 工具
- 前端开发
status: 已审核
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b68817bab1af4efc5c0de71
notion_url: https://www.notion.so/Tizer/316212bcc9f342bdbddfdad120a1db2c
notion_id: 316212bc-c9f3-42bd-bddf-dad120a1db2c
---

## 一句话摘要

Slim 是一款开源 CLI 工具，能将本地开发的 `localhost:端口` 一键映射为自定义 HTTPS 域名，并支持临时公网隧道分享，解决本地开发地址难记、跨域调试和临时演示三大痛点。

## 关键洞察

- **本地域名美化**：将 `localhost:3000` 替换为 `myapp.test` 等自定义域名，自动配置 HTTPS，开发体验接近生产环境

- **路径分流**：同一域名下 `/api`、`/ws` 等路径可代理到不同后端端口，前后端 + WebSocket 共享一个地址，彻底消除跨域问题

- **配置文件驱动**：`.slim.yaml` 声明式管理多服务，`slim up` / `slim down` 一键批量启停，团队成员无需逐个配置端口

- **公网临时分享**：`slim share` 生成公网可访问的子域名，支持密码保护和过期时间，适合甲方演示、QA 验收等场景

- **自检诊断**：`slim doctor` 一键检查证书、端口转发、hosts 配置状态，降低排障成本

## 提取的概念

- [Slim](entities/Slim.md)：本文介绍的核心工具，Go 编写的开源 CLI

- [本地域名映射](concepts/本地域名映射.md)：将 [localhost](http://localhost/) 映射为自定义域名的技术模式

- [公网隧道分享](concepts/公网隧道分享.md)：将本地服务临时暴露到公网的技术

## 原始文章信息

- **作者**：github淘金

- **来源**：微信公众号

- **发布时间**：2026-04-29

- **原文链接**：[查看原文](https://mp.weixin.qq.com/s?__biz=Mzg2MjY1NDIzNg%3D%3D&mid=2247499414&idx=1&sn=3069ae2a1dec61ac1d704638bb4596b4&chksm=cfaa1267f0c9963110547669c39cbbb7140c3afbf58118abb71f8c73c992e77ad16553fc72ea#rd)

## 个人评注

这类轻量级本地开发工具对日常开发效率有直接提升。`slim share` 的临时公网分享功能与 ngrok、Cloudflare Tunnel 形成竞争，但集成了域名映射 + 隧道分享的一体化体验更简洁。对于 Tizer 的工作流而言，在本地调试 OpenClaw 或 MCP 服务时，自定义域名和路径分流可以简化多服务联调；`slim share` 也可用于临时向协作者展示本地运行的 Agent 效果。
