---
title: 摘要：Addy Osmani 开源 Agent Skills ——专治 AI 偷懒
type: summary
tags:
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化, skills
source_article_url: ''
notion_url: https://www.notion.so/20915ad37728457aae8a5e5a644247fc
notion_id: 20915ad3-7728-457a-ae8a-5e5a644247fc
---

**一句话摘要**：Google 工程师 Addy Osmani 将 Google 工程文化封装为 19 个 Agent Skills，覆盖需求定义到上线的完整开发周期，内置反借口机制防止 AI 偷懒。

**关键洞察**

- **19 个技能**：覆盖 Define/Plan/Build/Verify/Review/Ship 全周期，每个技能内嵌 Google 工程硬约束

- **忽岑**：Spec before code（先写规格再动手）、Tests are proof（测试才是证据）、Faster is safer（更快的前提是更稳）

- **7 条快捷指令**：/spec, /plan, /build, /test, /review, /code-simplify, /ship

- **反借口機制**：直接把 AI 常见偿懒借口和反驳方案写进 Skill 文件

- **安装**：`npx skills add addyosmani/agent-skills`，支持 Claude Code、Cursor、Windsurf、GitHub Copilot

**提取的概念**

- agent-skills（Addy Osmani）

- Spec before code 原则

**原始文章信息**

- 作者：AI工程化

- 来源：微信公众号

- 发布时间：2026-04-06

- 链接：[https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ==&mid=2461159190](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ%3D%3D&mid=2461159190)

**个人评注**：对 Tizer 的 OpenClaw Skill 开发有实用参考价值。Spec before code 和反借口机制可直接远用于自定义 Skill 的设计，确保 Agent 按照工程实践标准执行。
