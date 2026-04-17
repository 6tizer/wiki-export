---
title: 摘要：Claude Code泳露的代码里，处处写着：这家公司人品不行
type: summary
tags:
- Coding Agent
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化, Claude
source_article_url: ''
notion_url: https://www.notion.so/657aa52b237447d788390ff031306f58
notion_id: 657aa52b-2374-47d7-8839-0ff031306f58
---

**一句话摘脁**：AI 前线分析 Claude Code 泳露源码中隐蒙的数据采集机制和隐私问题，指出其对用户设备的控制能力远超协议条款描述，并探讨 AI 生成代码的版权保护合法性。

---

## 关键洞察

- **数据采集**：每次启动发送用户ID、邮筱、终端类型等；每个被 Claude 读过的文件、每次 Bash 命令输出均存本地 JSONL，断网后补发

- **AI 生成代码版权问题**：技术律师指出按当前美国版权法需具备实质性人类创作，这些主要由 AI 自己生成的代码在法律意义上可能不受保护

- **autoDream 沉默扫描**：未发布的 autoDream 功能会后台扫描所有会话记录，提取信息写入 [MEMORY.md](http://memory.md/) 并最终回传到 API

## 原始文章信息

- **作者**：AI前线

- **来源**：微信公众号

- **发布日期**：2026-04-02

- **链接**：[https://mp.weixin.qq.com/s?__biz=MzU1NDA4NjU2MA==&mid=2247660286](https://mp.weixin.qq.com/s?__biz=MzU1NDA4NjU2MA%3D%3D&mid=2247660286)
