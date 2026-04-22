---
title: 摘要：Deep Research Web UI 开源深度研究助手
type: summary
tags:
- LLM
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-10'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/70854c0018e743f49637fa8a8fe1396e
notion_id: 70854c00-18e7-43f4-9637-fa8a8fe1396e
---

## 一句话摘要

Deep Research Web UI 是一款基于强化学习的开源 AI 研究助手，通过多轮搜索和推理自动拆解研究课题、生成树状图谱和结构化报告。

## 关键洞察

- **多步骤研究规划**：基于强化学习自主规划研究路径，能根据实时信息动态调整搜索策略，支持回溯和适应

- **树状可视化**：以树状图展示每个节点的搜索内容和推理逻辑，让 AI 的研究路径透明可追踪

- **多语言跨域检索**：支持中英等多语言搜索，配合 Tavily、Firecrawl 等搜索服务实现实时联网检索

- **多模态数据处理**：能解析文本、图像、表格等多种数据格式，进行结构化处理后生成研究报告

- **浏览器端隐私保护**：所有配置和 API 请求在浏览器端完成，用户数据不上传服务器

- **Docker 快速部署**：一行命令即可启动，兼容 OpenAI、DeepSeek、Ollama 等多种 AI 服务

## 提取的概念

- [Deep Research](entities/Deep Research.md)

- [多步骤研究规划](concepts/多步骤研究规划.md)

- 搜索可视化（树状图谱）

## 原始文章信息

- **作者**：蚝油菜花

- **来源**：微信公众号

- **发布时间**：2025-03-13

- **链接**：[原文链接](http://mp.weixin.qq.com/s?__biz=MzkyMzc2MDY1OA%3D%3D&mid=2247494047&idx=1&sn=38b5ac71b611b680d86851f10b51099d)

## 个人评注

这个工具的「多步骤研究规划 + 可视化」模式很有参考价值。对 Tizer 的知识管理工作流来说，可以作为「深度调研 → 知识提取 → Wiki 编入」流水线的前端。端到端强化学习的思路也值得关注——不是简单 RAG，而是让 AI 自主规划研究策略。
