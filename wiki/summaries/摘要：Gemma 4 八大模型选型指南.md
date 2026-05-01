---
title: 摘要：Gemma 4 八大模型选型指南
type: summary
tags: []
status: 已审核
confidence: medium
last_compiled: '2026-04-26'
source_tags: LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/341c72f459ef450e9c4d314920a67212
notion_id: 341c72f4-59ef-450e-9c4d-314920a67212
---

**一句话摘要**：Gemma 4 发布八个型号，选型关键看后缀（Base/IT）和尺寸：E2B/E4B 适合端侧，26B a4b（MoE）适合 Agent 自动化，31B Dense 适合重度推理任务。

**关键洞察**

- **Base vs IT**：Base 是预训练原始版本，适合二次微调；IT（Instruction Tuned）是对齐后版本，日常使用认准 IT

- **E2B/E4B**：Effective 系列，PLE 技术让极小模型智商出众，原生音频/视觉，适合手机端

- **26B a4b（MoE）**：260 亿参数但每次只激活 40 亿，响应速度达 4B 级别，代码/文案精通，适合延迟敏感的 Agent 自动化

- **31B Dense**：310 亿全量参数，256K 超长上下文，逻辑推理天花板，适合科研和重度代码

- **内存选型**：24GB 对应 26B a4b IT；64GB 可运行 31B Dense

**提取的概念**

- Gemma 4

**原始文章信息**

- 作者：程序员wang哥

- 来源：微信公众号

- 发布时间：2026-04-04

- 链接：[https://mp.weixin.qq.com/s?__biz=MzU2MDYyMTIyMg==&mid=2247483746](https://mp.weixin.qq.com/s?__biz=MzU2MDYyMTIyMg%3D%3D&mid=2247483746)

**个人评注**：实用选型指南，直接可用于判断哪个 Gemma 4 型号最适合本地部署，与 OpenClaw 成本优化策略配套使用。
