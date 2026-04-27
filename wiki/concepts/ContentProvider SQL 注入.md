---
title: ContentProvider SQL 注入
type: concept
tags:
- Agent 安全
status: 草稿
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/0bb93e86714743e09279503f4abb6745
notion_id: 0bb93e86-7147-43e0-9279-503f4abb6745
---

### 定义

ContentProvider SQL 注入 是指攻击者通过 Android 应用暴露的 ContentProvider 接口拼接恶意查询参数，从而读取、篡改或枚举本地数据的一类注入风险。

### 关键要点

- 重点检查导出的 ContentProvider 是否允许未授权访问。

- 常见测试方式包括报错型、布尔盲注、UNION 注入与时间延迟 payload。

- 风险后果包括 schema 泄露、敏感数据读取、任意查询与权限边界失效。

### 来源引用

- 2026-04-15｜[源文章页面](https://www.notion.so/343701074b6881e08474cb7a908a0248)｜[原文链接](https://mp.weixin.qq.com/s?__biz=Mzg2MjY1NDIzNg%3D%3D&mid=2247499189&idx=1&sn=8fcf372b20c1da788cfa419cd911473f&chksm=cfb0f3427c5cea79a1473c595903b501634768596d5e10105b46f8ed80e825fdd35a03b3c2ed#rd)｜作者：github淘金
