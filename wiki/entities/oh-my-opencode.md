---
title: oh-my-opencode
type: entity
tags:
- CLI 工具
- 多Agent协作
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/a66e2197489e49069ea11387bb953641
notion_id: a66e2197-489e-4906-9ea1-1387bb953641
---

## 定义

oh-my-opencode（简称 OMO）是 OpenCode 的官方插件，充当「Agent 注册表」。它内置 10 个具名 Agent 角色，每个角色有不同的定位和能力，开发者通过 `--agent <name>` 即可调度不同角色完成任务。

**别名**：OMO

## 关键要点

- 内置 10 个具名 Agent：Sisyphus（重型 worker）、Momus（怀疑论 critic）、Oracle（分析判断）、Librarian（文档检索）等

- 调用方式极简：`opencode run --agent momus "<prompt>"`

- 将 Agent 角色从代码级配置提升为命名级调度，降低多 Agent 系统的搭建门槛

- 与 OpenCode 的 subprocess + JSON 事件流架构配合，可在任意语言中组合使用

## 来源引用

- [摘要：OpenCode + OMO ：小白也能快速搭建AI Agent应用](summaries/摘要：OpenCode + OMO ：小白也能快速搭建AI Agent应用.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU0MDcyMDQ0Nw%3D%3D&mid=2247484791&idx=1&sn=8e0baa4136cf4b90cadf5e23e3dee12a&chksm=fa23c722fefdd30dfabd5ec53292f22f64bcd97ca133c36264b4804657c84ae1a0e8ed4e31c1#rd)）

## 关联概念

- [OpenCode](entities/OpenCode.md)

- [双 Agent 互查范式](concepts/双 Agent 互查范式.md)

- [Subprocess Agent 架构](concepts/Subprocess Agent 架构.md)
