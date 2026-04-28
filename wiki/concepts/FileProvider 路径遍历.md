---
title: FileProvider 路径遍历
type: concept
tags:
- Agent 安全
status: 审核中
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/b3efd2d2f052491aadeee6d542587daa
notion_id: b3efd2d2-f052-491a-adee-e6d542587daa
---

### 定义

FileProvider 路径遍历 是指攻击者利用 Android FileProvider 的路径映射或配置错误，通过构造遍历 payload 访问原本不应暴露的文件内容。

### 关键要点

- 需要重点检查 `res/xml/` 中的 FileProvider 路径配置。

- `root-path` 或外部存储配置过宽时，容易导致高危甚至致命级文件暴露。

- 常见验证方式是拼接多种遍历 payload，测试是否能读取私有或敏感文件。

### 来源引用

- 2026-04-15｜[源文章页面](https://www.notion.so/343701074b6881e08474cb7a908a0248)｜[原文链接](https://mp.weixin.qq.com/s?__biz=Mzg2MjY1NDIzNg%3D%3D&mid=2247499189&idx=1&sn=8fcf372b20c1da788cfa419cd911473f&chksm=cfb0f3427c5cea79a1473c595903b501634768596d5e10105b46f8ed80e825fdd35a03b3c2ed#rd)｜作者：github淘金
