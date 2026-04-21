---
title: autoresearch
type: entity
tags:
- 工作流
status: 审核中
confidence: high
last_compiled: '2026-04-22'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/6a8cb9b4e0474053be1b5f821ce03cef
notion_id: 6a8cb9b4-e047-4053-be1b-5f821ce03cef
---

**定义**

autoresearch 是 Andrej Karpathy 开源的 AI 自主研究框架，让 Agent 在固定时间预算内对 LLM 训练代码进行自主实验迭代，通过结构化 Eval 自动找到最优解，无需人工持续介入。

**核心架构（三文件）**

- `program.md`：人类编写的研究策略/指令文档，类似超轻量 Skill

- `train.py`：Agent 唯一可修改的文件，包含模型架构、优化器、超参数

- `prepare.py`：固定的基础设施（数据加载、分词器），禁止 Agent 修改

**工作原理**

- 自主循环：读取 [program.md](http://program.md/) → 修改 [train.py](http://train.py/) → 固定 5 分钟训练 → 评估 val_bpb 指标 → 保留/丢弃 → 循环

- 节奏：约 12 次实验/小时，约 100 次/夜，全程自动

- 评估指标：val_bpb（验证集 bits per byte），与词表大小无关，架构变更后仍可公平比较

**Eval 设计原则**

- 黄金法则：每条 Eval 必须是 yes/no 二元问题（不是量表，不是感觉判断）

- 好 Eval 三问：① 两个不同 Agent 能否打出一致的分？② AI 能否靠钻空子通过这条 Eval？③ 这条 Eval 测的是用户真正在乎的东西吗？

- Eval 数量：3-6 条，太少约束不够，太多开始刷题

**可迁移性**

- Skill 优化：将成功率从 56% 提升至 92%

- 代码性能：页面加载从 1100ms 降至 67ms（67 轮迭代）

- 适用于任何"能被量化评分"的优化场景

**来源引用**

- 《56% → 92%：Karpathy autoresearch 让 skill 成功率直接起飞》（字节前端，2026-03-27）

- 《AutoResearch：Karpathy 让 AI 自主跑实验的方法论，以及它如何改变你的工作方式》｜文章链接：[https://x.com/yibie/status/2031222960372199523](https://x.com/yibie/status/2031222960372199523)

- [原文链接](https://x.com/wangray/status/2031312140788023421)｜《sim-predict：用多Agent社会模拟预测FDA事件如何在金融市场「扩散」》｜来源条目：sim-predict：用多Agent社会模拟预测FDA事件如何在金融市场「扩散」

- [原文链接](https://x.com/_0xKenny/status/2032557322078400527)｜《GitHub 飙升榜：过去两周最火的 7 个 AI 开源项目盘点》｜来源条目：[摘要：GitHub 飙升榜：过去两周最火的 7 个 AI 开源项目盘点](summaries/摘要：GitHub 飙升榜：过去两周最火的 7 个 AI 开源项目盘点.md)

- [原文链接](https://x.com/timyangnet/status/2033436288679075840)｜《Autoresearch：纪律与记忆，让 Agent 成为真正的研究者》｜来源条目：[摘要：Autoresearch：纪律与记忆，让 Agent 成为真正的研究者](summaries/摘要：Autoresearch：纪律与记忆，让 Agent 成为真正的研究者.md)

- 《一周暴涨 8.4k Star：GitHub Coding AI 开源项目周榜 Top 20 深度解析》（@_0xKenny (Kenny.eth)，X书签，2026-03-16）— 将 autoresearch 视为当周最具想象力的自主科研项目之一。

- 《一周暴涨 8.4k Star：GitHub Coding AI 开源项目周榜 Top 20 深度解析》— X书签，2026-03-16：将 autoresearch 列为自主科研方向的代表项目

- 《用 Karpathy 的 autoresearch 方法，让你的 Claude Skill 自动进化》｜X书签文章｜原文链接：[https://x.com/MinLiBuilds/status/2034533228162187444](https://x.com/MinLiBuilds/status/2034533228162187444)

- 《AutoAgent：让 AI 自己调自己，跑一晚上超越所有人工方案》｜X书签文章｜原文链接：[https://x.com/runes_leo/status/2040221812483936727](https://x.com/runes_leo/status/2040221812483936727)｜来源条目：[摘要：AutoAgent：让 AI 自己调自己，跑一晚上超越所有人工方案](summaries/摘要：AutoAgent：让 AI 自己调自己，跑一晚上超越所有人工方案.md)

- [原文链接](https://x.com/SHL0MS/status/2043415274196435325)｜《SHL0MS | HERMES AGENT》｜来源条目：[摘要：SHL0MS | HERMES AGENT](summaries/摘要：SHL0MS  HERMES AGENT.md)

- 《达尔文.skill正式发布，一个无限进化的skill系统！》｜X书签文章｜原文链接：[https://x.com/AlchainHust/status/2043709317296361851](https://x.com/AlchainHust/status/2043709317296361851)｜来源条目：[摘要：达尔文.skill正式发布，一个无限进化的skill系统！](summaries/摘要：达尔文.skill正式发布，一个无限进化的skill系统！.md)

- 《Github 上的硅基生物 —— 一手达尔文、一手女娲 ，先造人后进化》｜微信文章｜原文链接：[https://mp.weixin.qq.com/s?__biz=MzkyNDYyODg0MQ==&mid=2247493022&idx=1&sn=624a417e7c20389f39d7c12d68db105c&chksm=c03f662e4b855b2d7f8982c96394e2f3f90f128f81904761993d26762b66605dac072cafc190#rd](https://mp.weixin.qq.com/s?__biz=MzkyNDYyODg0MQ%3D%3D&mid=2247493022&idx=1&sn=624a417e7c20389f39d7c12d68db105c&chksm=c03f662e4b855b2d7f8982c96394e2f3f90f128f81904761993d26762b66605dac072cafc190#rd)｜源文章：Github 上的硅基生物 —— 一手达尔文、一手女娲 ，先造人后进化

- 《Claude + Obsidian | How to use your second brain》｜X书签文章｜原文链接：[https://x.com/defileo/status/2043762213597397179](https://x.com/defileo/status/2043762213597397179)｜来源条目：[摘要：Claude + Obsidian | How to use your second brain](summaries/摘要：Claude + Obsidian  How to use your second brain.md)

- [原文链接](https://x.com/shannholmberg/status/2043983746094026984)｜《how to use autoreason for marketing》｜来源条目：[摘要：how to use autoreason for marketing](summaries/摘要：how to use autoreason for marketing.md)

- [原文链接](https://x.com/ShopifyEng/status/2044477537200550383)｜《Shopify 开源 pi-autoresearch，用自主实验循环持续挖掘性能优化》｜来源条目：[摘要：Shopify 开源 pi-autoresearch，用自主实验循环持续挖掘性能优化](summaries/摘要：Shopify 开源 pi-autoresearch，用自主实验循环持续挖掘性能优化.md)

- [摘要：Compound Engineering - 4/17/2026](summaries/摘要：Compound Engineering - 4-17-2026.md)（[原文](https://x.com/trevin/status/2045245249392607443)）

- [摘要：custom slash commands](summaries/摘要：custom slash commands.md)（[原文](https://x.com/hasantoxr/status/2046174499226403038)）

## 关联概念

- [Compound Engineering](concepts/Compound Engineering.md)

- [LLM-as-judge](concepts/LLM-as-judge.md)

- [Autoreason](concepts/Autoreason.md)

- [Borda count](concepts/Borda count.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [达尔文.skill](entities/达尔文.skill.md)

- [Human in the Loop](concepts/Human in the Loop.md)

- [棘轮机制](concepts/棘轮机制.md)

- [claude-obsidian](entities/claude-obsidian.md)

- [盲评裁判团](concepts/盲评裁判团.md)

- [隔离式 Agent](concepts/隔离式 Agent.md)

- [对抗式评审](concepts/对抗式评审.md)

- [组织级知识层](concepts/组织级知识层.md)

- [置信度评分](concepts/置信度评分.md)

- [Extension / Skill 分离](concepts/Extension - Skill 分离.md)
