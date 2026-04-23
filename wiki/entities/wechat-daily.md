---
title: wechat-daily
type: entity
tags:
- Agent 技能
- Coding Agent
status: 草稿
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/0723d4bd0416498084be604a519f01c9
notion_id: 0723d4bd-0416-4980-84be-604a519f01c9
---

## 定义

wechat-daily 是 `yichen-skills` 仓库中的一个具体 Skill，用于从 macOS 本地微信数据库中提取聊天记录，并结合 AI 生成可浏览的每日日报。

## 关键要点

- 它把“微信数据解密、聊天记录提取、日报生成”封装进一个相对完整的 Skill 工作流。

- 该能力面向 Claude Code 等 Coding Agent 场景，强调把原始聊天数据转成更容易消费的摘要产物。

- 从仓库说明看，wechat-daily 依赖 Python 脚本、SQLCipher 数据库处理和首轮密钥提取流程。

## 关联概念

- [Claude Code Skills](concepts/Claude Code Skills.md)

- [SQLCipher 4](concepts/SQLCipher 4.md)

- [摘要：来了！来了！我把大家呼声最高的微信聊天记录解析全流程封装成了一个Skill](summaries/摘要：来了！来了！我把大家呼声最高的微信聊天记录解析全流程封装成了一个Skill.md)

## 来源引用

- [摘要：来了！来了！我把大家呼声最高的微信聊天记录解析全流程封装成了一个Skill](summaries/摘要：来了！来了！我把大家呼声最高的微信聊天记录解析全流程封装成了一个Skill.md)（[原文](https://x.com/gengdaJ/status/2046944097789993059)）
