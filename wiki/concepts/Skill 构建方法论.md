---
title: Skill 构建方法论
type: concept
tags:
- 提示工程
status: 草稿
confidence: medium
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/923a1c465d804b58b25b67b20f24fc6b
notion_id: 923a1c46-5d80-4b58-b25b-67b20f24fc6b
---

## 定义

Skill 构建方法论是一套将模糊的重复性工作需求转化为可被 AI Agent 稳定执行的 Skill 的系统化方法。核心思路是：先拆解工作模式，再查找现有能力，最后才动手固化流程。

## 关键要点

- **Skill ≠ 长提示词**：Skill 是一套小型工作流，回答的是「以后每次遇到这类工作，AI 应该按什么顺序做、读什么材料、产出什么、怎么检查」

- **三步走流程**：brainstorming（拆解工作模式）→ find-skills（查找现成能力）→ skill-creator（固化为 Skill 文件）

- **Skill 适用性四准则**：一项工作值得做成 Skill 的判据——会重复出现、步骤相对固定、输出格式稳定、可以检查好坏

- **先查后建原则**：在自建 Skill 之前先搜索现成 Skill 生态，覆盖 60%-80% 需求即可复用，缺口部分再自定义补齐

- **迭代验证**：Skill 很少一次写完就稳定，需要拿真实任务反复测试并调整触发条件、步骤粒度和输出格式

## 工作模式拆解表

建 Skill 前必须先回答的六个字段：

| 字段 | 说明 |

| --- | --- |

| 重复任务 | 反复让 AI 做的是什么 |

| 触发场景 | 用户说什么时应该启动这套流程 |

| 输入材料 | 需要文件、链接、笔记、数据还是上下文 |

| 固定步骤 | 每次都要按什么顺序做 |

| 输出格式 | 最后应该给文稿、表格、代码还是检查结果 |

| 检查方式 | 怎么判断这次做得好不好 |

## 关联概念

- [find-skills](concepts/find-skills.md)

- [skill-creator](concepts/skill-creator.md)

## 来源引用

- [摘要：分享如何寻找和构建属于自己的科研 Skill](summaries/摘要：分享如何寻找和构建属于自己的科研 Skill.md)
