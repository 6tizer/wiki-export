---
title: Lint Report 2026-04-12
type: lint-report
tags:
- 知识管理
---

## 检查日期
- 2026-04-12
## 总体健康度
- 0/100 🔴
- 扣分构成：重复疑似 18 组 × 10 分 = 180 分
- 本轮未发现以下硬性问题：过期草稿、过时内容、缺失状态、缺失标签、废弃标签
- 说明：当前健康度被重复条目集中拉低，说明 Wiki 的主要风险已从“字段缺失”转向“概念分叉与重复沉淀”
## 孤岛条目
- 本轮未确认孤岛 concept 条目
- 说明：现有 summary 页面里，部分“提取的概念”仍以普通文本呈现，而非统一的页面 mention 或反向关系，因此 concept / entity 的孤岛检测仍有漏判风险
- 当前结论：暂无已确认孤岛条目
## 过期草稿
- 无
## 过时内容
- 无
## 重复疑似
- 6551-twitter-to-binance-square ↔ 6551-twitter-to-binance-square：名称完全一致
- ClawHub ↔ ClawHub：名称完全一致
- Coinglass ↔ Coinglass：名称完全一致
- CryptoQuant ↔ CryptoQuant：名称完全一致
- DeFiLlama ↔ DeFiLlama：名称完全一致
- FRED ↔ FRED：名称完全一致
- Gate MCP Skills ↔ Gate MCP Skills：名称完全一致
- IDENTITY.md ↔ IDENTITY.md：名称完全一致
- memory-lancedb-pro ↔ memory-lancedb-pro：名称完全一致
- OnchainOS Signal ↔ OnchainOS Signal：名称完全一致
- OpenClaw ↔ OpenClaw：同名且出现 concept / entity 双轨分裂
- System Prompt 泄露 ↔ System Prompt 泄露：名称完全一致
- total-recall ↔ total-recall：名称完全一致
- wshobson/agents ↔ wshobson/agents：名称完全一致
- 指纹浏览器 ↔ 指纹浏览器：名称完全一致
- 提示注入 ↔ 提示注入：名称完全一致
- 跨交易所套利 ↔ 跨交易所套利：名称完全一致
- 静态住宅 IP ↔ 静态住宅 IP：名称完全一致
## 状态异常
- 无
## 标签异常
- 缺失标签：无
- 使用废弃标签（AI Agent / MCP / Notion）：无
- 备注：本轮未发现 concept / entity 的标签空值问题，标签体系完整度良好
## 标签分布统计
## 标签分类合理性检查
- 开发工具 → Coding Agent
- LLM → 记忆系统 / entity
- 开发工具 / OpenClaw → Agent 技能
## 类型分类检查
- 建议 concept → entity
- 建议 entity → concept
- 需要二选一去重并统一类型
## 状态晋升建议
## 改进建议
1. 先做去重，不要继续扩量：优先处理上方 18 组同名重复条目，建议一组只保留 1 个 canonical page，另一页转为内容并入或删除。
1. 统一“产品 = entity，方法/机制 = concept”的判定规则：尤其是 OpenFang、Second Me、Whisper.cpp、Gemini CLI、MemOS、EdgeClaw 这类条目，已经明显偏向实体页。
1. 把 summary 中的“提取的概念”统一改成页面 mention 或结构化关系：否则未来孤岛检测、引用计数、状态晋升都会持续失真。
1. 为版本化产品建立主词条机制：例如 MemBrain / MemBrain1.5、Qwen3.5 / Qwen 3.5，避免“版本号 = 新页面”导致重复膨胀。
1. 对 Skill 类条目单独收口：Gate MCP Skills、OpenClaw-Medical-Skills、6551-twitter-to-binance-square 等应统一进入 Agent 技能体系，减少标签漂移。
1. 将 OpenClaw 从 concept/entity 双轨合并为单一实体主词条：当前这是最典型的结构性重复，且会持续污染后续统计。
