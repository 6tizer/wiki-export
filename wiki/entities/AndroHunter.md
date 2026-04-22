---
title: AndroHunter
type: entity
tags:
- 安全/隐私
- 开发工具
status: 草稿
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/234afe1126a24ff1afacebc7b4ebf594
notion_id: 234afe11-26a2-4ff1-afac-ebc7b4ebf594
---

### 定义

AndroHunter 是一个面向 Android 应用安全测试的移动端工具集，强调**无需 Root、无需随身电脑**也能在手机上完成静态检查、组件分析、漏洞测试、流量拦截与动态调试辅助。

### 关键要点

- 可直接查看 APK 的包名、版本、权限、目标 SDK 与 AndroidManifest.xml 信息。

- 内置多类安全测试能力，包括 **Intent fuzzing**、**ContentProvider SQL 注入测试**、**FileProvider 路径遍历检测**。

- 提供 SharedPreferences 敏感信息审计、HTTP 代理抓包、Frida 脚本生成等实用功能。

- 更适合**授权安全测试**、漏洞研究与移动端应用审计，不适合未授权扫描。

### 资料线索

- GitHub 仓库：[ynsmroztas/AndroHunter](https://github.com/ynsmroztas/AndroHunter)

- 适用对象：Android 安全研究、移动应用渗透测试、漏洞赏金场景

### 来源引用

- 2026-04-15｜[源文章页面](https://www.notion.so/343701074b6881e08474cb7a908a0248)｜[原文链接](https://mp.weixin.qq.com/s?__biz=Mzg2MjY1NDIzNg%3D%3D&mid=2247499189&idx=1&sn=8fcf372b20c1da788cfa419cd911473f&chksm=cfb0f3427c5cea79a1473c595903b501634768596d5e10105b46f8ed80e825fdd35a03b3c2ed#rd)｜作者：github淘金
