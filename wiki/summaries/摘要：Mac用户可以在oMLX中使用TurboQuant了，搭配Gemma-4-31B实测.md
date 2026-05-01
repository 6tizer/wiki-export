---
title: 摘要：Mac用户可以在oMLX中使用TurboQuant了，搭配Gemma-4-31B实测
type: summary
tags:
- 推理优化
- 上下文管理
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1700f5a80a434959b44dffe38ec1e43d
notion_id: 1700f5a8-0a43-4959-b44d-ffe38ec1e43d
---

**一句话摘要**：TurboQuant KV缓存量化算法在oMLX v0.3.4中正式优化落地，在128K-256K极限上下文下可将KV缓存压缩70%以上，让Mac用户实现「长文档自由」。

**关键洞察**

- TurboQuant不是模型量化，而是专针对运行时KV缓存的压缩；3-bit可实现4-5倍极端压缩，PPL增幅仅约1%

- **关键版本**：必须使用oMLX v0.3.4+，早期v0.3.2有混合注意力Bug导致模型输出失焦

- **效果依赖上下文长度**：<16K基本没收益（反而略慢）；32K-64K内存骤降73-75%；128K+化不可能为可能

- Mac M5 Max实测：128K上下文的KV缓存从8.14GB压至1.70GB（降幅79%）

- RTX 5090 32GB实测：成功跑满262K极限上下文，显存27.7GB，生成速度约61 tokens/s

- 对OpenClaw/Claude Code用户的误区：开TurboQuant不能解决超长Prefill的超时问题

**提取的概念**：TurboQuant（已有）、oMLX（已有）

**原始文章信息**

- 作者：AI修猫Prompt | 来源：微信 | 发布：2026-04-08

**个人评注**：对于Tizer的本地部署大模型工作流，TurboQuant+oMLX是处理长文档（如大量文章编译）时的重要参考。直接影响长上下文推理的可行性。
