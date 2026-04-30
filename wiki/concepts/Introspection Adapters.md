---
title: Introspection Adapters
type: concept
tags:
- AI 对齐
- 训练/微调
- 模型评测
status: 草稿
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/7bd828b0c85b4cd78314337f96a6f8fa
notion_id: 7bd828b0-c85b-4cd7-8314-337f96a6f8fa
---

## 定义

Introspection Adapters（内省适配器）是 Anthropic 联合剑桥大学于 2026 年 4 月提出的一种 AI 安全审计技术。其核心思路是：给大模型挂载一个极轻量的 LoRA 适配器，使模型能够用自然语言准确「坦白」自己在微调过程中学到的行为——包括隐蔽后门、偏见和加密恶意指令。

别名：IA

论文：《Introspection Adapters: Training LLMs to Report Their Learned Behaviors》（arXiv: 2604.16812v2）

## 关键要点

- 基于 LoRA（低秩适配）技术，参数量极小，不改变目标模型自身行为

- 采用三阶段训练：构建 682 个「模型有机体」→ 联合 SFT 训练 → DPO 精炼减少幻觉

- 在 AuditBench 基准上以 59% 成功率超越所有现有黑盒和白盒审计方法

- 首次成功检测加密微调攻击（CMFT），成功率 57.8%

- 训练完成后可无限复用于同一基础模型的所有微调变体，实现规模化审计

- 模型规模扩大是性能提升最核心的驱动力（Qwen3 从 0.6B 到 14B，准确率从 37.7% 升至 77.3%）

- 核心发现：大模型内部激活（尤其第 20-30 层）已包含所学行为的完整信息，IA 本质是「翻译官」而非「教师」

## 局限性

- 高误报率：对无特定行为的模型倾向于幻觉出行为

- 训练分布收益递减：行为类别超过 5 个后泛化性能进入平台期

- 无法揭示行为背后的根本动机

- 可能无法应对专门针对自报告的对抗训练

## 来源引用

- [摘要：AI 终于学会「自我坦白」！Anthropic最新论文震撼来袭，「内省适配器」让黑盒模型自己说出隐藏行为](summaries/摘要：AI 终于学会「自我坦白」！Anthropic最新论文震撼来袭，「内省适配器」让黑盒模型自己说出隐藏行为.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA5ODEzMjIyMA%3D%3D&mid=2247734195&idx=1&sn=e7ba307d92b758071f43af149a7c046d&chksm=91713367fb3fc33423f2b8e18868422e6dc43147b49cc046fac49f82b538c031b07ca5b4be66#rd)）
