---
title: Intent Fuzzing
type: concept
tags:
- 安全/隐私
status: 草稿
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/79c22ffd82f64546ad45df8127085df1
notion_id: 79c22ffd-82f6-4546-ad45-df8127085df1
---

### 定义

Intent Fuzzing 是针对 Android 导出组件自动构造异常、越权或恶意参数的测试技术，用于发现 **Activity、Service、Broadcast Receiver** 在输入校验、权限控制与路径处理上的缺陷。

### 关键要点

- 常见目标包括导出组件、深度链接入口、文件路径参数与可序列化对象输入。

- 适合发现参数注入、路径遍历、认证绕过、开放重定向等问题。

- 自动化测试通常会配合 payload 模板批量发送不同类型的 Intent。

### 来源引用

- 2026-04-15｜[源文章页面](https://www.notion.so/343701074b6881e08474cb7a908a0248)｜[原文链接](https://mp.weixin.qq.com/s?__biz=Mzg2MjY1NDIzNg%3D%3D&mid=2247499189&idx=1&sn=8fcf372b20c1da788cfa419cd911473f&chksm=cfb0f3427c5cea79a1473c595903b501634768596d5e10105b46f8ed80e825fdd35a03b3c2ed#rd)｜作者：github淘金
