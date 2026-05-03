---
title: 双 Agent 互查范式
type: concept
tags:
- 多Agent协作
- Agent 协作模式
status: 审核中
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1d607bf696854e2292593ac984f3b8f8
notion_id: 1d607bf6-9685-4e22-9259-3ac984f3b8f8
---

## 定义

双 Agent 互查范式是一种多 Agent 协作模式：由一个 Worker Agent 生成结果，另一个独立的 Critic Agent 回到原始数据源进行逐条验证。Critic 不读取 Worker 的推理过程，而是独立去原文找证据，实现「独立验证」而非「二次确认」。

## 关键要点

- **核心原则**：Critic 独立访问原始数据，不依赖 Worker 的中间输出

- **典型角色**：Worker（如 Sisyphus）负责生成 findings；Critic（如 Momus）负责逐条验证 citation 真实性

- **输出分级**：每条 finding 标记为 verified ✓、suspect ⚠️ 或 rejected ❌

- **下游驱动**：验证结果直接驱动内容选择——verified 自动采纳，suspect 保留原文，rejected 丢弃

- **实测效果**：在医疗 SOP 合规场景中，将 citation 准确率从 82% 提升到 100%，hallucination 归零

- **代码量极低**：核心调度逻辑仅需几十行代码

## 与相关概念的区别

- **二次确认**：Critic 只检查 Worker 输出是否「看起来合理」→ 容易被同源偏差欺骗

- **双 Agent 互查**：Critic 独立回到原文验证 → 真正的独立证据链

## 来源引用

- [摘要：OpenCode + OMO ：小白也能快速搭建AI Agent应用](summaries/摘要：OpenCode + OMO ：小白也能快速搭建AI Agent应用.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU0MDcyMDQ0Nw%3D%3D&mid=2247484791&idx=1&sn=8e0baa4136cf4b90cadf5e23e3dee12a&chksm=fa23c722fefdd30dfabd5ec53292f22f64bcd97ca133c36264b4804657c84ae1a0e8ed4e31c1#rd)）

- [摘要：国企领导："现在都是 Agent自动开发了，你还在对话模式，太落后了！"](summaries/摘要：国企领导：现在都是 Agent自动开发了，你还在对话模式，太落后了！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIxNzQwNjM3NA%3D%3D&mid=2247546961&idx=1&sn=9c277dcdefba84a56f352c890d562bda&chksm=96c46750ea40bb030f4f0b98294df3d8d4485ee1751637d816106fcb0939494c6a135c377731#rd)）

## 关联概念

- [OpenCode](entities/OpenCode.md)

- [oh-my-opencode](entities/oh-my-opencode.md)

- [Subprocess Agent 架构](concepts/Subprocess Agent 架构.md)
