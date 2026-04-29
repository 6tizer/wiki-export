---
title: RULER
type: concept
tags:
- 训练/微调
- 模型评测
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f81734803dc24c2f83cc92165f2fa0d1
notion_id: f8173480-3dc2-4c2f-83cc-92165f2fa0d1
---

## 定义

RULER（Rule-based Universal LLM Evaluation via Ranking）是 OpenPipe ART 框架内置的通用奖励函数，利用 LLM-as-judge 对同一场景下的多条 Agent 轨迹做**相对排名打分**，替代手写 reward function，为 GRPO 训练提供标量奖励信号。

## 关键要点

- **相对评分优于绝对评分**：将同组 N 条轨迹（通常 4-8 条）同时提交给 judge LLM，让其按「哪条最符合 system prompt」排序；LLM 在比较任务上表现远优于绝对打分

- **System Prompt 即隐式 reward function**：judge 直接阅读 Agent 的 system prompt 来理解评判标准，无需额外编写 Python 评分逻辑

- **与 GRPO 天然契合**：GRPO 本身就做组内归一化，RULER 输出的相对分数恰好是 GRPO 所需的输入

- **支持自定义 rubric**：可用自然语言附加评估维度（如「惩罚 emoji」「奖励引用来源」），迭代速度远快于修改代码

- **judge 模型灵活**：可用 o3、o4-mini、Qwen3 32B 甚至本地 Ollama 模型，成本-质量可调

- **自动去重与缓存**：共享前缀自动去重以节省 token，评分结果缓存到磁盘避免重复调用

## 适用场景

- RAG Agent 的忠实性/幻觉检测

- 客服 Agent 的回复质量评估

- 摘要 Agent 的多维度评分

- 任何无法用 string-match 验证的 agentic 任务

## 与相关概念的关系

- 是 RLVR 的泛化：RLVR 用确定性验证器（数学/代码），RULER 用 LLM judge 处理非可验证任务

- 依赖 GRPO 做策略优化

- 属于 LLM-as-judge 方法论的训练端应用

## 来源引用

- [摘要：How top AI labs are building RL agents in 2026 (using Karpathy's system prompt learning idea)](summaries/摘要：How top AI labs are building RL agents in 2026 (using Karpathy's system prompt learning idea).md)（[原文](https://x.com/_avichawla/status/2049037299334472015)）
