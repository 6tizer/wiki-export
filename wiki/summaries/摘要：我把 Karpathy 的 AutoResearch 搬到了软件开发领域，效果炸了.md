---
title: 摘要：我把 Karpathy 的 AutoResearch 搬到了软件开发领域，效果炸了
type: summary
tags:
- Harness 工程
- 多Agent协作
- 代码生成
status: 已审核
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: https://www.notion.so/352701074b688181b1c9e17443e1ee3c
notion_url: https://www.notion.so/Tizer/84c658c6aa7a42d3a31a8fc15180c393
notion_id: 84c658c6-aa7a-42d3-a31a-8fc15180c393
---

## 一句话摘要

将 Karpathy 的 autoresearch 自主实验循环方法从 ML 研究迁移到软件开发领域，通过多 Agent 交叉审核、5 维度加权评分和反馈驱动迭代，实现从 GitHub Issue 到代码合并的全自动闭环。

## 关键洞察

- **多 Agent 交叉审核优于单 Agent 自审**：让 Codex 和 Claude 轮流担任实现者和审核者，利用不同模型的盲区互补，代码质量远超单 Agent 模式

- **5 维度加权评分量化代码质量**：正确性 35% + 测试 25% + 代码质量 20% + 安全 10% + 性能 10%，总分 ≥ 9.0 才自动合并，把主观判断变成量化指标

- **反馈驱动迭代替代盲循环**：审核反馈直接注入下一轮 Agent 提示词，Agent 针对性改进而非漫无目的重试

- [**program.md**](http://program.md/)** 作为规则核心**：定义权限边界、代码规范、测试标准，Agent 只在规则允许范围内操作

- **实测 10 分钟完成中等复杂 Issue**：全程零人工干预，最终评分 9.0/10，显著提升效率

## 提取的概念

- [autoresearch](entities/autoresearch.md)：核心方法论来源，从 ML 研究迁移到软件开发

- [多 Agent 交叉审核](concepts/多 Agent 交叉审核.md)：本文的核心创新——双 Agent 轮流实现+审核

- [acpx](entities/acpx.md)：实现多 Agent 协作的 CLI 控制工具

- [Ralph Wiggum 方法](concepts/Ralph Wiggum 方法.md)：单 Agent 无限循环的前代模式

- [program.md](concepts/program.md.md)：Agent 的规则宪法文件

## 原始文章信息

- **作者**：鸟窝（百度Geek说）

- **来源**：微信公众号

- **发布时间**：2026-04-20

- **原文链接**：[微信文章](https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ%3D%3D&mid=2247606664&idx=1&sn=34e95bd76d66935c85b61ed791983041&chksm=c14a0674bcce5652baa86c6abc2cd4e4c262f81d5315768d929af6f36022a87c42917c19224f#rd)

- **项目地址**：[github.com/smallnest/autoresearch](http://github.com/smallnest/autoresearch)

## 个人评注

本文的多 Agent 交叉审核模式与 OpenClaw 的 HITL 理念高度契合——都是在自动化循环中引入外部验证机制来保证质量。5 维度评分体系可以借鉴到 content pipeline 的质量检查中。acpx 作为 CLI Agent 编排工具，可能适用于 OpenClaw 的多 Agent 协作场景。文中提到的达尔文.skill 也是 autoresearch 方法论在 Skill 领域的类似应用，说明这套「量化目标 + 自主循环 + 只保留改进」的范式正在向各个领域扩散。
