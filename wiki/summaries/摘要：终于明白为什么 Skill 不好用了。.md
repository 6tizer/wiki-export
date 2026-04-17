---
title: 摘要：终于明白为什么 Skill 不好用了。
type: summary
tags:
- OpenClaw
- 工作流
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: OpenClaw, Skill 开发, 经验分享
source_article_url: ''
notion_url: https://www.notion.so/f61f2bb3934d440f942d7a563fa69844
notion_id: f61f2bb3-934d-440f-942d-7a563fa69844
---

**一句话摘衑**：OpenClaw Skill 的两大痛点（耗 Token + 不够准确）局源于用 MD 文档描述规则，而 AiPy 的 Python-Use 思路将所有环节 Python 化，用确定性的代码替代概率性的 LLM 执行。

**关键洞察**

- OpenClaw Skill 痛点：Skill MD 文档中的规则依赖 LLM 理解，产生幻觉或遗漏；执行全程消耗大量 Token

- Python-Use 思路：LLM 做规划，写 Python 代码，由 Python 执行——代码跑起来几乎不耗 Token、结果也稳定

- AiPy 循环：Task → Plan → Code → Execute → Feedback，执行出错则自动修改代码直到成功

- Code is Agent：不需要 MCP、Workflow、Tools注册——Python 就是全能接口，直接 import 就能用

- Python 生态极其丰富：pandas/beautifulsoup/matplotlib 外加各 AI SDK，几乎能想到的场景全有现成库

**提取的概念**

- AiPy / Python-Use（模型写代码、Python 执行的 AI Agent 架构模式）

**原始文章信息**

- 作者：AI产品阿颖 | 来源：微信公众号 | 发布时间：2026-03-23

- 链接：[https://mp.weixin.qq.com/s?__biz=Mzg5Mjc3MjIyMA==&mid=2247581171](https://mp.weixin.qq.com/s?__biz=Mzg5Mjc3MjIyMA%3D%3D&mid=2247581171)

**个人评注**

这个思路直接导向了 Tizer OpenClaw Skill 的下一步迭代方向：将已验证的逻辑 Python 化，显著降低 Token 消耗并提高执行准确性。
