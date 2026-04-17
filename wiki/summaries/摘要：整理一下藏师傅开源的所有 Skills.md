---
title: 摘要：整理一下藏师傅开源的所有 Skills
type: summary
tags:
- OpenClaw
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化, skills
source_article_url: ''
notion_url: https://www.notion.so/d8321e93c1c64e8d94948c5d36e5dbe5
notion_id: d8321e93-c1c6-4e8d-9494-8c5d36e5dbe5
---

**一句话摘要**

歸藏（op7418）开源的六个高星 OpenClaw Skill，覆盖即时通信控制、视频处理、文档配图、AI去味和PPT生成等核心场景。

**关键洞察**

- **Claude-to-IM-skill**（1800⭐）：将 Claude Code/Codex 接入任意聊天软件，实现远程控制

- **Video-Wrapper-Skills**（200⭐）：自动为视频添加"小Lin说"式解释特效（高亮卡片、关键词卡片等）

- **Youtube-clipper-skill**（1700⭐）：下载 YouTube 长视频，自动剪辑并加中英双语字幕

- **Document-illustrator-skill**（300⭐）：分析文档内容，按分段自动生成多张配图（16:9/4:3）

- **Humanizer-zh**（5600⭐）：两段式处理，去除AI生成内容中的"AI味"表述，提升可读性

- **NanoBanana-PPT-Skills**（2100⭐）：基于AI自动生成高质量 PPT 图片和视频，支持智能转场

**提取的概念**

- Claude-to-IM-skill

- Humanizer-zh

- NanoBanana-PPT-Skills

- Skill 蒸馏（Agent Skill开源生态）

**原始文章信息**

- 作者：歸藏的AI工具箱

- 来源：微信

- 发布时间：2026-04-07

- 链接：[https://mp.weixin.qq.com/s?__biz=MzU0MDk3NTUxMA==&mid=2247496373](https://mp.weixin.qq.com/s?__biz=MzU0MDk3NTUxMA%3D%3D&mid=2247496373)

**个人评注**

Humanizer-zh（5600⭐）与内容生产管线高度相关——Tizer 的公众号内容产出如果借助 AI 生成初稿，此 Skill 可作为最后一道「人味过滤器」。Claude-to-IM-skill 则直接打通了 OpenClaw 与微信生态的远程控制链路。
