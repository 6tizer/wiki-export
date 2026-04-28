---
title: Browser Use
type: entity
tags:
- 浏览器自动化
- Agent 技能
status: 审核中
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/26d73cc30a194e46b7438e3c9eaaffa6
notion_id: 26d73cc3-0a19-4e46-b743-8e3c9eaaffa6
---

## 定义

Browser Use 是一个开源 Python 库，让 AI Agent 能像人类一样操控网页浏览器。构建于 Playwright 之上，提供智能交互层，将杂乱 HTML 转化为模型可理解的结构化信息，支持 GPT、Claude、Gemini 等多种 LLM。

**GitHub**：browser-use/browser-use | ⭐ 85,000+ Stars | License: MIT | 创建于 2024 年 10 月

**官网**：[browser-use.com](http://browser-use.com/) | 创始人：Gregor Zunic & Magnus Müller | YC W25

## 核心能力

- **网页导航**：自动打开 URL、点击链接、填写表单

- **内容读取**：提取页面信息，理解动态加载内容

- **自主决策**：多步骤任务下自主制定操作计划

- **异常处理**：遇到验证码、弹窗时自适应调整

## 快速上手

```python
from browser_use import Agent, Browser
from langchain_openai import ChatOpenAI

agent = Agent(
    task="去 GitHub 搜索 browser-use，告诉我 Stars 数",
    llm=ChatOpenAI(model="gpt-4o"),
    browser=Browser(),
)
await agent.run()
```

## 已知局限

- 复杂任务推理较慢，不适合高频确定性任务

- LLM 非确定性导致可靠性有波动，生产环境需重试机制

- 部分网站会检测并封锁自动化行为

## 相关概念

与 Playwright Skill（确定性脚本自动化）形成对比；与 OpenClaw 的 Computer Use 能力有概念重叠；与 [Claude Code](entities/Claude Code.md) 的官方集成，使其进一步成为 Coding Agent 的云浏览器执行层；与 [云浏览器自动化](concepts/云浏览器自动化.md) 共同构成远程网页操作能力的典型组合；在本文语境下，它与 [Hermes Agent](entities/Hermes Agent.md)、[Hindsight](entities/Hindsight.md) 和 [OpenRouter](entities/OpenRouter.md) 共同构成“个人分析师”工作流中的执行、记忆与模型路由组合；在 [Video Use](entities/Video Use.md) 场景中，这套“结构化感知替代原始感知输入”的方法论被迁移到视频理解流程中；同时，[Browser Harness](entities/Browser Harness.md) 代表 Browser Use 生态中更薄、更可自愈的浏览器执行层实现。

## 来源引用

- [摘要：Enable Tool Gateway](summaries/摘要：Enable Tool Gateway.md)（[原文](https://x.com/NousResearch/status/2044878344592699744)）

- [原文链接](https://x.com/YuLin807/status/2042198758260158535)｜《Browser Use × Hermes Agent：每个开源 Agent 现在都有了免费的云端浏览器》｜来源条目：[摘要：Browser Use × Hermes Agent：每个开源 Agent 现在都有了免费的云端浏览器](summaries/摘要：Browser Use × Hermes Agent：每个开源 Agent 现在都有了免费的云端浏览器.md)

- Browser Use：让 AI 像人一样操控浏览器的开源利器（LangChain 推文）

- ai-gradio 多模型统一接口（内置 browser-use-agent）

- [摘要：如何使用Hermes Agent稳定爬取公众号文章](summaries/摘要：如何使用Hermes Agent稳定爬取公众号文章.md)（Draco正在VibeCoding，微信，2026-04-11）：Browser Use 官宣向 Hermes Agent 用户免费提供云端浏览器（无限时长、免费 proxy、持久化鉴权），可用于封装微信公众号爬取 skill

- [摘要：OpenClaw 养虾踩坑实录：如何用 CDP 把浏览器完全交给 AI Agent 控制](summaries/摘要：OpenClaw 养虾踩坑实录：如何用 CDP 把浏览器完全交给 AI Agent 控制.md)（未知，X书签）— 作为 OpenClaw 浏览器控制方案的对照工具被引用

- [原文链接](https://x.com/berryxia/status/2042941854015197395)｜《免费 + 无限云浏览器小时》｜来源条目：[摘要：免费 + 无限云浏览器小时](summaries/摘要：免费 + 无限云浏览器小时.md)

- [原文链接](https://x.com/0xJeff/status/2043656911044870203)｜《3 Things I learnt after 3 weeks of using Hermes as a personal analyst》｜来源条目：[摘要：3 Things I learnt after 3 weeks of using Hermes as a personal analyst](summaries/摘要：3 Things I learnt after 3 weeks of using Hermes as a personal analyst.md)

- [摘要：Video Use：用 Claude Code 把「对着镜头说话」变成一键出片](summaries/摘要：Video Use：用 Claude Code 把「对着镜头说话」变成一键出片.md)（[原文](https://x.com/gregpr07/status/2044554557221675380)）

- [摘要：self-healing](summaries/摘要：self-healing.md)（[原文](https://x.com/Gorden_Sun/status/2046228429662794153)）

- [摘要：The Bitter Lesson of Agent Harnesses](summaries/摘要：The Bitter Lesson of Agent Harnesses.md)（[原文](https://x.com/gregpr07/status/2047358189327520166)）

- [摘要：SOMEONE OPEN-SOURCED VIDEO EDITING FOR AI AGENTS.](summaries/摘要：SOMEONE OPEN-SOURCED VIDEO EDITING FOR AI AGENTS.md)（[原文](https://x.com/socialwithaayan/status/2047568884304367722)）
