---
title: Obscura
type: entity
tags:
- 浏览器自动化
- CLI 工具
status: 草稿
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e743f9117ecb488a942ef2e2321acc1c
notion_id: e743f911-7ecb-488a-942e-f2e2321acc1c
---

## 定义

Obscura 是一个用纯 Rust 打造的轻量级无头浏览器引擎（GitHub: h4ckf0r0day/obscura），专为 AI Agent 自动化和大规模网页抓取设计。单二进制、无 Chrome/Node.js 依赖，内嵌 V8 引擎实现真实 JavaScript 执行，完整支持 Chrome DevTools Protocol (CDP)，可直接替代 Puppeteer 和 Playwright 的后端。

别名：obscura

## 关键要点

- **极致轻量**：内存仅 30MB（Chrome 200MB+），二进制 70MB（Chrome 300MB+），页面加载 85ms（Chrome ~500ms），瞬时启动

- **真实 JS 执行**：通过 deno_core 嵌入 V8 引擎，无需完整 Chromium 渲染引擎

- **CDP 全兼容**：支持 Target、Page、Runtime、DOM、Network、Fetch、Storage、Input 等 Domain，Puppeteer-core / playwright-core 零修改接入

- **Stealth Mode**：内置浏览器指纹随机化（GPU/Screen/Canvas/Audio/Battery）+ 3520 个 tracker 域名阻断

- **Cargo Workspace 多 crate 架构**：obscura-dom（Servo 解析器）、obscura-js（deno_core V8）、obscura-net（reqwest 网络层）、obscura-browser（生命周期协调）、obscura-cdp（WebSocket CDP 服务器）、obscura-cli（命令行入口）

- **三大使用模式**：CLI fetch/scrape、CDP serve（作为 Puppeteer/Playwright 后端）、代理/robots.txt 支持

## 适用场景

- AI Agent 网页自动化（低资源、高隐蔽）

- 大规模数据采集 / 爬虫

- 反检测浏览器自动化

- 轻量级 CDP 后端替代 Headless Chrome

## 来源引用

- [摘要：30MB Rust无头浏览器Obscura：击败Chrome、V8真实JS+CDP全兼容，AI Agent与爬虫的隐形核武器](summaries/摘要：30MB Rust无头浏览器Obscura：击败Chrome、V8真实JS+CDP全兼容，AI Agent与爬虫的隐形核武器.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ%3D%3D&mid=2247485078&idx=1&sn=84152e9774e0eab3d16839db3a7657de&chksm=f5696523a9b95b45d7ce029701ad0acd68b9d573d010a44500be214374bde17f0b4b04c3dc08#rd)）

## 关联概念

- [Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md)

- [浏览器指纹模拟](concepts/浏览器指纹模拟.md)

- [deno_core](entities/deno_core.md)
