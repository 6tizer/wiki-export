---
title: 摘要：DESIGN.md | The One File AI Needs to Match Your UI
type: summary
tags:
- AI 设计
- 代码生成
- 提示工程
status: 已审核
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b6881eca8a6e44f60a90fbe
notion_url: https://www.notion.so/Tizer/19bdfb8f802e462c9822c9cdba7400ff
notion_id: 19bdfb8f-802e-462c-9822-c9cdba7400ff
---

## 一句话摘要

当 AI 能在十分钟内生成十个界面时，真正的问题不再是"能不能做出来"，而是"这些屏幕看起来像不像同一个产品"——[DESIGN.md](http://design.md/) 正是把设计判断写成 Agent 可读文本的解法，而本文从 PM 视角给出了完整的落地清单。

## 关键洞察

- AI 生成 UI 的瓶颈已从"产出速度"转移到"品牌一致性"：多个 Agent 独立生成的界面放在一起，往往像四个不同产品套了同一个 logo

- [DESIGN.md](http://design.md/) 把设计系统从 Figma 搬进代码仓库，用 YAML（精确 token）+ Markdown（设计理由）双层结构让 Agent 同时拿到数值和判断依据

- PM 不需要成为设计师，但必须能写出足够具体的产品判断句（如"每屏只保留一个主 CTA"），而非模糊的形容词（"简洁""高级"）

- 最被低估的用法是让 Agent 反向引用 [DESIGN.md](http://design.md/) 做自检——生成界面后，要求 Agent 列出遵循了哪些规则、在哪里发明了新模式

- 更新 [DESIGN.md](http://design.md/) 的时机是"系统性问题"而非"个人偏好"：同一种卡片圆角出现三种不同值时才更新，而非某人不喜欢某个圆角时

## 提取的概念

- [DESIGN.md](concepts/DESIGN.md.md)

- [Google Stitch](entities/Google Stitch.md)

- [AGENTS.md](concepts/AGENTS.md.md)

- [Design Token](concepts/Design Token.md)

- [PM OS](entities/PM OS.md)

## 原始文章信息

- 作者：@nurijanian（George from [prodmgmt.world](http://prodmgmt.world/)）

- 来源：X书签

- 发布时间：2026-04-26

- 链接：[原文](https://x.com/nurijanian/status/2048327986777350425)

## 个人评注

本文的核心价值在于把 [DESIGN.md](http://design.md/) 从"开发者工具"视角拉到了"产品经理工作流"视角。对 Tizer 的启示是：OpenClaw 和内容 Agent 的输出一致性问题，本质上也是缺少一份可被 Agent 持续引用的"规则文件"——无论是视觉设计、写作风格还是知识编译规范，关键都在于把隐性判断编码为显式、可版本化、可自检的文本资产。文末附带的 PM OS v1.8.0 更新说明展示了一种以项目为单位组织 Agent 上下文的实践，与 OpenClaw 的工作区设计也有参考价值。
