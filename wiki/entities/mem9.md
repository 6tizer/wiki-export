---
title: mem9
type: entity
tags:
- 记忆系统
- OpenClaw
status: 审核中
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/7fffd600e0c24cb381a0fe1864087fde
notion_id: 7fffd600-e0c2-4cb3-81a0-fe1864087fde
---

## 定义

mem9 是 TiDB（PingCAP）团队推出的开源 AI Agent 持久化记忆基础设施，通过云端存储让 Agent 记忆跟着人走而不是跟着设备走，解决 OpenClaw、Claude Code 等工具的跨会话失忆问题。

## 技术架构

**两段式提取流水线：**

1. **事实提取**：对话结束后，只提取用户消息中的原子事实（不提取 AI 回复），用整数 ID 替代 UUID 防幻觉

1. **记忆调和**：新事实与已有记忆比对，做出 ADD/UPDATE/DELETE/NOOP 四种判断，年龄越大的记忆在冲突时越容易被标记为过时

**混合搜索：**

- TiDB `EMBED_TEXT` 函数在数据库侧直接生成向量嵌入

- jieba 分词器做中文全文检索

- RRF（Reciprocal Rank Fusion）算法合并排序

- 手动置顶记忆获得1.5倍权重加成

## 特色功能

- **记忆脉搏**：按时间段检索记忆，查看某人某事某段时间发生了什么

- **记忆洞察**：关系图谱分析记忆之间的关联

- **防循环设计**：上一轮注入的记忆内容在存储时自动剥离

## 安装

- 云端版：给 OpenClaw 发一条安装指令即可

- 自部署：完整开源 Go 服务端，支持 MySQL 兼容数据库

## 来源引用

- [摘要：QClaw：腾讯把 AI Agent 装进微信，12 亿人的入口之争](summaries/摘要：QClaw：腾讯把 AI Agent 装进微信，12 亿人的入口之争.md)

- [摘要：QClaw：腾讯把 AI Agent 装进微信，12 亿人的入口之争](summaries/摘要：QClaw：腾讯把 AI Agent 装进微信，12 亿人的入口之争.md)
