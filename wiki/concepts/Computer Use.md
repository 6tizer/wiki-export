---
title: Computer Use
type: concept
tags:
- Agent 技能
status: 草稿
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/803dc813598e484c86c0469260d68d46
notion_id: 803dc813-598e-484c-86c0-469260d68d46
---

## 定义

Computer Use 是 Anthropic 为 Claude Cowork 和 Claude Code 推出的桌面控制能力（研究预览版），允许 Claude 直接控制鼠标、键盘、屏幕，像坐在桌前的同事一样操作任何应用，目前仅支持 macOS。

## 能力范围

- 打开应用、浏览器导航、填写电子表格

- 控制鼠标点击、键盘输入、屏幕截取

- 与 Dispatch 结合实现手机远程触发桌面任务

## 权限体系

1. 用户主动开启（显示确认框）

1. 逐个授权需要使用的 App

1. App 级别权限隔离（Finder 完全控制 vs Chrome 只读）

## 工作策略

- **API 优先**：优先使用已连接的 App 集成（Slack、Calendar 等）

- **屏幕控制兜底**：只有没有现成 API 接口时，才请求操作屏幕

- 执行时隐藏其他窗口，任务完成后恢复

## 限制

- 研究预览阶段，建议从可撤销任务开始

- 仅 Pro 和 Max 订阅用户可用

- 目前仅支持 macOS

## 典型场景

- Dispatch + Computer Use：出门在外用手机发指令，Claude 在电脑上自动处理，回来活已干完

- 定期扫描邮箱、自动拉报告等定时任务

## 来源引用

- [摘要：Claude Opus 4.7 自我越狱：当 AI 开始审计自己的「笼子」](summaries/摘要：Claude Opus 4.7 自我越狱：当 AI 开始审计自己的「笼子」.md)（[原文](https://x.com/elder_plinius/status/2045682830383231474)）

- [摘要：Cognition 用 $250M 抄底 Windsurf：当 IDE 变成 Agent 指挥中心，谁来审这些代码？](summaries/摘要：Cognition 用 $250M 抄底 Windsurf：当 IDE 变成 Agent 指挥中心，谁来审这些代码？.md)（[原文](https://x.com/aakashgupta/status/2044619554706604356)）

- [摘要：刚刚发布！Claude 能控制你的整个电脑了：鼠标、键盘、屏幕全接管](summaries/摘要：刚刚发布！Claude 能控制你的整个电脑了：鼠标、键盘、屏幕全接管.md)

- 《Holo3：用十分之一的成本，打败 GPT-5.4 的 Computer Use 模型》｜X书签文章｜原文链接：[https://x.com/hcompany_ai/status/2039021096649805937](https://x.com/hcompany_ai/status/2039021096649805937)｜来源条目：摘要：Holo3：用十分之一的成本，打败 GPT-5.4 的 Computer Use 模型

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzU0MDk3NTUxMA%3D%3D&mid=2247496517&idx=1&sn=d44a3ec92036cdd1c4b08d57f581f4e2&chksm=fa29fb0bb3df650b0f59072f68108d15c3ba7bef33636218b5cd36107aa8e18f137b62fb214b#rd)｜《没等来 Image 模型，等来了 Codex 大升级。》｜来源条目：[摘要：没等来 Image 模型，等来了 Codex 大升级。](summaries/摘要：没等来 Image 模型，等来了 Codex 大升级。.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ%3D%3D&mid=2247515602&idx=1&sn=1b46eb01028eae027c8670917c82299b&chksm=c39464836558ed516d629ccba40c5ce4691f4ac48cb60cb1204a46c672c42091dc39da720fa4#rd)｜《Codex 重大更新，全面解读》｜来源条目：[摘要：Codex 重大更新，全面解读](summaries/摘要：Codex 重大更新，全面解读.md)

- [摘要：Codex for (almost) everything.](summaries/摘要：Codex for (almost) everything.md)（[原文](https://x.com/OpenAI/status/2044827705406062670)）

- [摘要：Codex能够控制电脑了：](summaries/摘要：Codex能够控制电脑了：.md)（[原文](https://x.com/Pluvio9yte/status/2045222180766781666)）

## 关联概念

- [Codex](entities/Codex.md)

- [Open Computer Use](entities/Open Computer Use.md)

- [跨应用操作](concepts/跨应用操作.md)

- [持续任务自动化](concepts/持续任务自动化.md)

- [持久化跨会话记忆](concepts/持久化跨会话记忆.md)

- [Artifact](concepts/Artifact.md)

- [Agent Harness](concepts/Agent Harness.md)

- [红队演练](concepts/红队演练.md)
