---
title: Slim
type: entity
tags:
- CLI 工具
- 前端开发
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/d418df4bd5da4266bfe7a67ae8510dad
notion_id: d418df4b-d5da-4266-bfe7-a67ae8510dad
---

## 定义

Slim 是一款开源的本地开发辅助 CLI 工具，用于将 `localhost:端口` 映射为自定义 HTTPS 域名（如 `myapp.test`），并支持一键将本地服务临时暴露到公网。

别名：nilbuild/slim

GitHub：[https://github.com/nilbuild/slim](https://github.com/nilbuild/slim)

## 关键要点

- 将本地开发端口映射为 `*.test` 等自定义域名，自动配置 HTTPS 证书

- 支持路径分流（path-based routing），同一域名下不同路径代理到不同端口

- 通过 `.slim.yaml` 配置文件管理多服务，`slim up` / `slim down` 一键启停

- `slim share` 实现公网隧道，支持随机/自定义子域名、密码保护、过期时间

- 内置 `slim doctor` 诊断工具，检查证书、端口转发、hosts 配置

- 使用 Go 语言编写，需 Go 1.25+

## 来源引用

- [摘要：本地开发神器，一键给 localhost:3000 换个域名，还能把本地项目临时丢到公网上让别人访问。](summaries/摘要：本地开发神器，一键给 localhost-3000 换个域名，还能把本地项目临时丢到公网上让别人访问。.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2MjY1NDIzNg%3D%3D&mid=2247499414&idx=1&sn=3069ae2a1dec61ac1d704638bb4596b4&chksm=cfaa1267f0c9963110547669c39cbbb7140c3afbf58118abb71f8c73c992e77ad16553fc72ea#rd)）
