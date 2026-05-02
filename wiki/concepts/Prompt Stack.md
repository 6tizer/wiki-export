---
title: Prompt Stack
type: concept
tags:
- 提示工程
- AI 设计
status: 草稿
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/bed84c4466354f859a5216e2f1d37393
notion_id: bed84c44-6635-4f85-9a52-16e2f1d37393
---

> 将多层内容按固定优先级拼接为结构化系统提示词的 Prompt 组合模式。

## 定义

Prompt Stack 是 Open Design 项目中的核心 Prompt 工程模式，将系统提示词拆分为六个优先级层次，按固定顺序拼接：Discovery 硬规则（最高优先级）→ 身份宪章 → Design System 视觉令牌 → Skill 工作流 + 预飞行指令 → 项目元数据 → Deck 框架指令（最低优先级）。

其核心设计原则是「前置硬规则 + 后置覆盖」——Layer 1 放在最前确保 RULE 不可绕过，Layer 6 放在最后确保特定场景的可靠性。

## 关键要点

- 六层分层组合：每层有明确职责和优先级，冲突时高优先级层覆盖低优先级层

- `derivePreflight` 动态生成预飞行指令：检测 Skill 是否附带模板文件，自动注入 Read 指令

- 条件注入：Design System、Skill、Deck 框架等层按需注入，减少不必要的 token 消耗

- 这种分层模式是一种可复用的 Prompt 工程设计模式，适用于需要组合多来源指令的复杂 Agent 系统

## 关联概念

- [Open Design](entities/Open Design.md)

- [Anti-AI-Slop](concepts/Anti-AI-Slop.md)

- [DESIGN.md](concepts/DESIGN.md.md)

## 来源引用

- [摘要：Open Design源码分析](summaries/摘要：Open Design源码分析.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2MjIwODc3Mw%3D%3D&mid=2247518546&idx=2&sn=b09ff622c0ea5ba39d0f9533fa955bf6&chksm=cffc0736bf58f08e4a1ea67ea6600b291bf6061dbc64a8a0b30ed6f6576dceec616fc3f6dff0#rd)）

- [摘要：Open Design开源AI设计平台操作指南](summaries/摘要：Open Design开源AI设计平台操作指南.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2MjIwODc3Mw%3D%3D&mid=2247518546&idx=1&sn=b7e340057327e37eaa414da8f73f2c54&chksm=cf03bb2e5e663169f8ac4d30e861142ad85293ab74b7795fb00b0d259549bef37aa984e1a38e#rd)）
