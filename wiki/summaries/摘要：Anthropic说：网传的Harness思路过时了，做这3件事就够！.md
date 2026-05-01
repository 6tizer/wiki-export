---
title: 摘要：Anthropic说：网传的Harness思路过时了，做这3件事就够！
type: summary
tags:
- Harness 工程
- 上下文管理
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/8c0c6681ae4a4122984db3f4a3aa5219
notion_id: 8c0c6681-ae4a-4122-984d-b3f4a3aa5219
---

**一句话摘要**：Anthropic 提出更新版 Harness 思路：利用 Claude 已熟悉的工具、让模型自行编排上下文、赋予模型管理记忆的能力。

**关键洞察**

- 第一件事：尽量使用 Claude 已熟悉的工具，减少适配成本

- 第二件事：让模型自行编排工具调用和管理上下文，减少不必要的操作

- 第三件事：赋予模型管理记忆的能力，实现跨会话连续性

- 定期审视 Harness 中的每个组件，确保其必要性

- 谨慎评估缓存管理和安全边界的设计

**提取的概念**：Harness 工程、Context Engineering

**原始文章信息**

- 作者：探索AGI

- 来源：微信

- 发布时间：2026-04-03

- 链接：[https://mp.weixin.qq.com/s?__biz=MzkxNjcyNTk2NA==&mid=2247492030&idx=1&sn=2e0f6d225da3b07f9a9eae79007e1249](https://mp.weixin.qq.com/s?__biz=MzkxNjcyNTk2NA%3D%3D&mid=2247492030&idx=1&sn=2e0f6d225da3b07f9a9eae79007e1249)

**个人评注**：Harness 更新思路与 OpenClaw HITL 工作流直接相关。Tizer 应尽快审视现有 OpenClaw 项目中的 Harness 组件，识别失负并优化。
