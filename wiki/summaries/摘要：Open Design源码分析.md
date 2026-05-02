---
title: 摘要：Open Design源码分析
type: summary
tags:
- AI 设计
- 提示工程
- Harness 工程
status: 已审核
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: https://www.notion.so/354701074b688112add3ef19fb9e1bd5
notion_url: https://www.notion.so/Tizer/2324fbca985442869ed30b2484ffa424
notion_id: 2324fbca-9854-4286-9ed3-0b2484ffa424
---

## 一句话摘要

本文系统分析了 Open Design（Anthropic Claude Design 的开源替代方案）的三大核心系统源码架构：Agent 适配器层、Prompt Stack 组合引擎、Skill 注册表，揭示了其「提示词即产品」的核心设计理念。

## 关键洞察

- **多 CLI 统一适配**：通过约 200 行的 `AGENT_DEFS` 数组完成 10 个 Agent CLI 的适配，每个 Agent 只需 5 个核心字段（bin、versionArgs、buildArgs、streamFormat、promptViaStdin），平均约 20 行配置，`buildArgs` 使用闭包实现运行时动态参数构造

- **六层 Prompt Stack 分层编排**：按固定优先级组合系统提示词——Discovery 硬规则（最高优先级）→ 身份宪章 → Design System 视觉令牌 → Skill 工作流 → 项目元数据 → Deck 框架指令，采用「前置硬规则 + 后置覆盖」的双向控制模式

- **文件式零注册扩展**：Skill 即文件夹、Design System 即单个 Markdown 文件、Agent 即约 20 行配置，贡献门槛降到最低，采用发现而非验证模式

- **六重反 AI-Slop 质量控制**：强制初始化表单 → 品牌资产五步协议 → P0/P1/P2 检查清单 → 五维自评 → AI Slop 黑名单 → 诚实占位符，全部以 Prompt 指令实现而非运行时检查

- **Artifact 流式解析器**：生成器函数驱动的流式状态机，支持部分匹配和跨 chunk 闭合标签检测，将 Agent 输出统一转换为 text/artifact:start/artifact:chunk/artifact:end 四种事件

## 提取的概念

- [Open Design](entities/Open Design.md)

- [Prompt Stack](concepts/Prompt Stack.md)

- [多 CLI 统一适配](concepts/多 CLI 统一适配.md)

- [反 AI-Slop 机制](concepts/反 AI-Slop 机制.md)

- [文件式零注册架构](concepts/文件式零注册架构.md)

## 原始文章信息

- **作者**：Agent工程化

- **来源**：微信公众号

- **发布时间**：2026-05-02

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=Mzg2MjIwODc3Mw%3D%3D&mid=2247518546&idx=2&sn=b09ff622c0ea5ba39d0f9533fa955bf6&chksm=cffc0736bf58f08e4a1ea67ea6600b291bf6061dbc64a8a0b30ed6f6576dceec616fc3f6dff0#rd)

## 个人评注

Open Design 的架构哲学与 OpenClaw 的 Harness 工程思想高度共鸣——两者都强调「不内置 Agent 运行时，而是通过标准化接口适配已有工具」。其 Prompt Stack 的分层编排模式可以直接借鉴到 OpenClaw 的指令系统设计中。六重反 AI-Slop 机制展示了一种纯 Prompt 驱动的质量保障路径，对 HITL 内容管线中的自动生成环节有参考价值。文件式零注册架构（Skill 即文件夹）与 OpenClaw 的 Skill 体系也有异曲同工之妙。
