---
title: 摘要：耦时2天，搞了个手机 Agent App：语音唤醒+视频通话（MobileClaw）
type: summary
tags:
- OpenClaw
- 开发工具
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: OpenClaw, Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/e330f9086a964112b73c11b8bc89a9e2
notion_id: e330f908-6a96-4112-b73c-11b8bc89a9e2
---

**一句话摘脁**：开发者开源了 MobileClaw——支持语音唤醒和视频内容的手机 App，将 OpenClaw 打造成随时随地待命 AI 助手，底层使用 GLM-5V-Turbo + Task-Harness Skill。

---

## 关键洞察

- **核心技术**：语音唤醒词匹配 → ASR 转文字 → 意图识别（GLM-4.7-Flash）→ 按需抓取关键帧 → 打包给 OpenClaw（GLM-5V-Turbo）

- **按需调用视觉模块**：延迟识别意图，无视觉意图时不传图片，大幅节省带宽和算力成本

- **工具项目本身用 Claude Code + GLM-5V-Turbo 开发**，配合 Task-Harness Skill

- **GitHub**: [https://github.com/kangarooking/mobileclaw](https://github.com/kangarooking/mobileclaw)

## 原始文章信息

- **作者**：袋鼠帝AI客栈

- **来源**：微信公众号

- **发布日期**：2026-04-02

- **链接**：[https://mp.weixin.qq.com/s?__biz=MzkwMzE4NjU5NA==&mid=2247515881](https://mp.weixin.qq.com/s?__biz=MzkwMzE4NjU5NA%3D%3D&mid=2247515881)
