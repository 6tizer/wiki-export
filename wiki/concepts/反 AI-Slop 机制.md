---
title: 反 AI-Slop 机制
type: concept
tags:
- AI 设计
- 提示工程
status: 草稿
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/351072d2c1e94b57a4e0177c037a2363
notion_id: 351072d2-c1e9-4b57-a4e0-177c037a2363
---

> 通过多层 Prompt 指令控制 AI 生成设计质量、防止低质量模式化输出的系统方法。

## 定义

反 AI-Slop 机制是 Open Design 项目中嵌入的六重质量管理体系，全部以 Prompt 指令形式实现（而非运行时代码检查），用于防止 AI 生成千篇一律的低质量设计（即 AI Slop）。

## 关键要点

- **第一重：强制初始化表单**——Turn 1 必须返回 `<question-form>`，禁止直接生成代码，将设计决策权前置给用户

- **第二重：品牌资产五步协议**——定位 → 下载 → 提取色值 → 编码 [brand-spec.md](http://brand-spec.md/) → 复述确认，绝不允许 Agent 从记忆中猜测品牌色值

- **第三重：P0/P1/P2 检查清单**——每个 Skill 可附带检查清单，Agent 必须逐项自检

- **第四重：五维自评**——Agent 在输出前从哲学/层次/执行/具体性/克制五个维度评分，低于 3 分必须修复

- **第五重：AI Slop 黑名单**——明确禁止紫色渐变、通用 Emoji 图标、圆角左边框卡片、Inter 作为 Display 字体等模式

- **第六重：诚实占位符**——无真实数据时写 `—` 或灰块标注，禁止编造虚假数据

## 来源引用

- [摘要：Open Design源码分析](summaries/摘要：Open Design源码分析.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2MjIwODc3Mw%3D%3D&mid=2247518546&idx=2&sn=b09ff622c0ea5ba39d0f9533fa955bf6&chksm=cffc0736bf58f08e4a1ea67ea6600b291bf6061dbc64a8a0b30ed6f6576dceec616fc3f6dff0#rd)）
