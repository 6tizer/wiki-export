---
title: System Prompt 注入
type: concept
tags:
- Agent 安全
status: 草稿
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/58f914c9ebef4667adb6637c592b4716
notion_id: 58f914c9-ebef-4667-adb6-637c592b4716
---

## 定义

System Prompt 注入是指平台或中间层在用户不可见的情况下，向模型请求中额外加入隐藏系统提示词，以改变模型行为、限制输出或操纵成本结构的做法。

## 关键要点

- 它可能被用于风格控制、权限限制，也可能被滥用于掩盖模型身份或增加 Token 消耗。

- 在第三方中转链路里，这类注入往往难以被普通用户直接观察。

- 对 Agent 与自动化工作流来说，隐藏注入会放大安全与可预测性风险。

## 来源引用

- [摘要：AI“中转站”月入百万？五问揭开Token交易真相！](summaries/摘要：AI“中转站”月入百万？五问揭开Token交易真相！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkxMjg4NDA4MA%3D%3D&mid=2247485160&idx=1&sn=d734afb62981fed9281c650fcaa77711&chksm=c0c8f1cd58f09c451cd4a511df4fb355f7ae37cdf737006e55f66d5900394ab3990bc7969fed#rd)）
