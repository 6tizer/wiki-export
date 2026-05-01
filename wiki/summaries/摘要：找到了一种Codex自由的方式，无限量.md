---
title: 摘要：找到了一种Codex自由的方式，无限量
type: summary
tags:
- 浏览器自动化
- CLI 工具
- Agent 安全
status: 已审核
confidence: low
last_compiled: '2026-04-27'
source_tags: Agent, LLM, 自动化, codex, openai
source_article_url: ''
notion_url: https://www.notion.so/Tizer/ccc3fe3c2d7449e5a30c228635e10be7
notion_id: ccc3fe3c-2d74-49e5-a30c-228635e10be7
---

## 一句话摘要

通过自动化注册脚本批量创建 OpenAI 账号，结合 CLiProxy 路由工具实现 Codex 无限量使用，涉及 TLS 指纹伪装、OAuth PKCE 授权流和临时邮箱集成等逆向工程技术。

## 关键洞察

- **核心方案**：自动化注册脚本 + CLiProxy 路由管理 + Codex 配置

- **技术手段**：TLS 指纹伪装、OAuth 2.0 PKCE 授权流、反爬虫绕过、临时邮箱 API、随机等待模拟人类操作

- **关键环节**：注册脚本获取账号 JSON → CLiProxy 管理路由 → 本地 base_url 配置

## 原始文章信息

- **作者**：老码小张

- **来源**：微信公众号

- **发布时间**：2026-03-02

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247492732&idx=1&sn=baf48f460abb60bebe5b5fadf685076c)

## 个人评注

此文内容涉及灰色地带（批量注册滥用 API），仅作技术参考记录。TLS 指纹伪装和反爬虫绕过的技术手段有一定参考价值，但不建议实际采用。
