---
title: AlphaEvolve
type: entity
tags:
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/91c595a1ead041e6bec31b674e73d2a9
notion_id: 91c595a1-ead0-41e6-bec3-1b674e73d2a9
---

## 定义

AlphaEvolve是Google DeepMind于2025年5月发布的进化性编程研究工具，通过双 LLM变异策略（Flash广度+Pro深度）在内部运行了超过56年的算法优化突破。

## 核心要点

- **双 LLM变异策略**：Gemini Flash负责广度（大量廉价变异），Gemini Pro负责深度（对最有前途候选者做昇贵推理）

- **重要突破**：56年来首次改进Strassen矩阵乘法算法；Gemini架构中FlashAttention内核加速23%；Borg调度链永久回收谷歌0.7%全球计算资源

- **Pareto前沿**：父代选择时不只选最优者，分数差的程序可能携带其他目标的遗传材料

- **局限**：AlphaEvolve发现怎么更高效地计算一个给定架构，但不能发现该用什么架构

## 在可进化性阶梯的位置

L2：改代码（在给定架构内优化，不改架构本身）

## 来源引用

- 《循环即实验室：八个AI自主研究系统横评》——赛博禅心（微信，2026-04-10），原始文猫arXiv:2506.13131
