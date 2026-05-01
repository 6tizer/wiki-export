---
title: 摘要：我给Claude Code 增加了多模型切换功能
type: summary
tags:
- CLI 工具
- 内容自动化
status: 已审核
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: https://www.notion.so/348701074b688139b118d602ced64613
notion_url: https://www.notion.so/Tizer/9a75ca95d5db4f90bbee4f703a53de2f
notion_id: 9a75ca95-d5db-4f90-bbee-4f703a53de2f
---

## 一句话摘要

这篇文章给出了一套面向国内用户的 Claude Code 多模型切换方案：通过维护多份 `~/.claude/settings.*.json` 配置和 shell alias，在 Claude Pro、MiniMax 与 GLM 之间快速切换，而不用反复重装或重配整个工作流。

## 关键洞察

- Claude Code 不是模型本身，而是基于 Anthropic API 形态工作的命令行宿主，因此可以接入兼容该接口的第三方模型服务。

- 方案的核心不是改造 Claude Code，而是把不同 provider 的配置拆成独立文件，再通过复制到 `settings.json` 实现切换。

- `use-pro`、`use-minimax`、`use-glm` 这类 alias，把原本零散的环境变量和配置管理压缩成了单命令操作，降低了非技术用户的上手门槛。

- 这套做法同时解决了官方订阅不稳定、额度贵、国产模型切换麻烦等实际问题，本质上是“稳定交互壳 + 可替换底层模型”的组合策略。

- 文章也说明了配置管理在 Coding Agent 场景中的重要性：真正可复用的不是某个单独模型，而是可迁移的工作流入口。

## 提取的概念

- [Claude Code](entities/Claude Code.md)

- [MiniMax M2.7](entities/MiniMax M2.7.md)

- [GLM-5.1](entities/GLM-5.1.md)

- [Anthropic API](entities/Anthropic API.md)

- [自定义模型接入](concepts/自定义模型接入.md)

## 原始文章信息

- 作者：剑宁

- 来源：微信

- 发布时间：2026-04-04 11:57

- 原文链接：[我给Claude Code 增加了多模型切换功能](https://mp.weixin.qq.com/s?__biz=MzIxNjM4MTMzOA%3D%3D&mid=2247484908&idx=1&sn=47c8fe19d582ad3d2a855cd0357a9078&chksm=96149bde764c82c85d8d9dca7aa660ae3913126cf6047a256cae541d3b55e91dadc9820ea101#rd)

- 源文章页面：我给Claude Code 增加了多模型切换功能

## 个人评注

这类“壳层不变、底层模型可替换”的做法，对 Tizer 的内容与 Agent 工作流很有启发：可以把 Claude Code 当成稳定的人机交互入口，再按照成本、稳定性和任务类型在不同模型之间切换。如果后续把这类配置继续模板化，并叠加 HITL 检查与知识沉淀，就能演化成更系统的内容生产与实验流水线。
