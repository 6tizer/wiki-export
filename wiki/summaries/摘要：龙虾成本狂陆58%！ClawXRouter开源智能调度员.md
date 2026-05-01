---
title: 摘要：龙虾成本狂陆58%！ClawXRouter开源智能调度员
type: summary
tags:
- OpenClaw
- 多Agent协作
- Agent 协作模式
- 长期记忆
- 商业/生态
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: OpenClaw, Agent, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1f19c381702b44e0a32dd43c7e38600c
notion_id: 1f19c381-702b-44e0-a32d-d43c7e38600c
---

**一句话摘要**：清华 THUNLP、人大、面壁等开源 ClawXRouter，通过三级隐私路由+性价比感知路由+局端云协同，实现成本陆58%、性能提6.3%，解决 Agent 进行局端云协同时“不敬用、用不起、用不好”三大痛点。

---

## 关键洞察

- **三大痛点**：云端“不敬用”（数据隐私）、“用不起”（简单任务调用最贵模型）、局端“用不好”（模型能力层限）

- **三级隐私路由**：S3（私密）完全局端处理、S2（敖感）智能脱敏后上云、S1（安全）直接发往云端，“规则+模型”双检测引擎

- **性价比感知路由**：LLM-as-Judge 小模型评估任务复杂度，自动分发给最合适模型；PinchBench 测评：成本-58%、性能+6.3%

- **双轨记忆**：云端只看到脱敏后的 `MEMORY.md`，局端保留完整 `MEMORY-FULL.md`

- **可组合管线**：隐私路由器高权重先跑，安全通过后才启动性价比路由优化成本

## 提取的概念

- ClawXRouter

- EdgeClaw

## 原始文章信息

- **作者**：量子位

- **来源**：微信公众号

- **发布日期**：2026-04-01

- **链接**：[https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247879641&idx=2](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247879641&idx=2)

## 个人评注

直接关系 Tizer 的 OpenClaw 成本控制需求。双轨记忆架构和路由机制很具参考价值，尤其适合射涉企业数据的场景。
