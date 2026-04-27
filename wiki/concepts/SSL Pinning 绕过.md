---
title: SSL Pinning 绕过
type: concept
tags:
- Agent 安全
status: 草稿
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/1b1abd9b7b884b578063cc6d758dc078
notion_id: 1b1abd9b-7b88-4b57-8063-cc6d758dc078
---

### 定义

SSL Pinning 绕过 是在移动应用动态分析中，通过 Hook 或运行时修改证书校验逻辑，绕过应用内置证书绑定检查，从而恢复 HTTPS 流量观察与调试能力的技术。

### 关键要点

- 常用于调试或审计启用了证书绑定的 Android 应用网络请求。

- 常见实现方式是借助 Frida Hook OkHttp3、TrustManager、Conscrypt、BoringSSL 等校验点。

- 该技术应仅用于授权测试和研究场景，避免落入未授权拦截流量的高风险用法。

### 来源引用

- 2026-04-15｜[源文章页面](https://www.notion.so/343701074b6881e08474cb7a908a0248)｜[原文链接](https://mp.weixin.qq.com/s?__biz=Mzg2MjY1NDIzNg%3D%3D&mid=2247499189&idx=1&sn=8fcf372b20c1da788cfa419cd911473f&chksm=cfb0f3427c5cea79a1473c595903b501634768596d5e10105b46f8ed80e825fdd35a03b3c2ed#rd)｜作者：github淘金
