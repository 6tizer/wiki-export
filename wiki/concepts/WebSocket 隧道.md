---
title: WebSocket 隧道
type: concept
tags:
- 开发工具
status: 审核中
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/c62e37d490914496bf0762b20343065e
notion_id: c62e37d4-9091-4496-bf07-62b20343065e
---

## 定义

WebSocket 隧道是指在公网接入层与本地服务之间维持双向长连接通道的实现方式，使实时消息能够穿过内外网边界稳定转发。

## 关键要点

- 相比只支持 HTTP 的穿透方案，它更适合聊天、协作、流媒体和实时控制场景。

- 关键能力在于连接升级、双向帧转发、断线重连与加密传输。

- 在 hostc 中，这一能力是区别于传统轻量穿透工具的重要卖点。

## 来源引用

- [摘要：hostc：轻量级内网穿透神器，一行命令获得公网 HTTPS 隧道！](summaries/摘要：hostc：轻量级内网穿透神器，一行命令获得公网 HTTPS 隧道！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484582&idx=1&sn=12136276fdabf532ee53c87f82f3099a&chksm=f5804d315efc5071a98c61a25dccd36154710d4012c08932729736c2dc84333992b80904ae75#rd)）
