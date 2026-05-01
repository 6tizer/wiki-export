---
title: 摘要：We found 21 money-printers after backtesting 236 TradingView strategies
type: summary
tags:
- 量化交易
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b68814b88eed4ace23ea6bf
notion_url: https://www.notion.so/Tizer/3ffa01786bd94411b7a5c4b0ee83f2e6
notion_id: 3ffa0178-6bd9-4411-b7a5-c4b0ee83f2e6
---

### 一句话摘要

这篇文章系统展示了 Minara 如何把 236 个公开 TradingView 策略做逐笔复制、双费率回测与结构性修复，并得出一个核心结论：真正能穿越真实手续费环境的策略很少，而决定生死的首要变量是交易频率。

### 关键洞察

- 在 236 个公开策略中，只有 63 个通过了严格的逐笔复制验证，其中 36 个在真实费率下仍然盈利，最终只有 21 个年化收益超过 10%。

- 宽松的总收益容差会高估策略可复制性，逐笔对齐把“截图能看”和“执行能跑”清晰地区分开了。

- 真实手续费对高频策略杀伤极大，所有从零费率盈利转为真实费率亏损的策略，年交易次数都超过 200 次。

- 真正表现好的策略并不集中于某一种指标体系，而是共同满足“单笔 edge 足够厚”或“交易频率足够低”这两个条件之一。

- 文中 4 个修复案例说明，很多失败策略的问题不在信号本身，而在时间尺度、止损结构、出场机制和风险控制设计。

### 提取的概念

- [Strategy Studio](entities/Strategy Studio.md)

- [逐笔复制验证](concepts/逐笔复制验证.md)

- [双费率回测](concepts/双费率回测.md)

- [交易频率成本侵蚀](concepts/交易频率成本侵蚀.md)

- [ATR 追踪止损](concepts/ATR 追踪止损.md)

### 原始文章信息

- 作者：@minara

- 来源：X书签

- 发布时间：2026/04/15

- 原文链接：[https://x.com/minara/status/2044432012002635843](https://x.com/minara/status/2044432012002635843)

- 源文章：回测 236 个 TradingView 策略后，我们找到了 21 个真正能赚钱的

### 个人评注

这篇材料对 Tizer 的价值不只是“发现了哪些策略赚钱”，而是提供了一套更适合沉淀进研究工作流的验证框架：先做严格复制，再拆分零费率与真实费率，最后针对结构性缺陷做模块化修复。若后续要把 Crypto 研究内容持续编译进 Wiki，这类“验证框架”比单个策略结论更值得长期复用。
