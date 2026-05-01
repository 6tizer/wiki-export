---
title: 摘要：Claude Code + Source-Verifier-skill 信源可靠性验证实践
type: summary
tags:
- 知识管理
- 内容自动化
- RAG/检索
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化, skills
source_article_url: ''
notion_url: https://www.notion.so/Tizer/9ce5f9981ebf4114b2b36f42f88950f9
notion_id: 9ce5f998-1ebf-4114-b2b3-6f42f88950f9
---

**一句话摘要**：将 last30days-skill（采集近 30 天社区讨论）与 Source-Verifier-skill（NATO Admiralty Code 双维度验证）组合使用，构建从信息采集到可信度评估的完整信息处理链路。

**关键洞察**

- **last30days 的差异化**：搜索 Reddit/X/HN/Polymarket 的社区真实讨论，而非媒体文章；三维评分 = 相关度 45% + 时效性 25% + 热度 30%

- **适用场景**：工具对比、技术争议、行业事件类话题效果好；泛泛概念类话题数据稀疏

- **Source-Verifier 工作原理**：自动提取可验证声明，按 NATO Admiralty Code 双维度（来源可靠性 + 信息准确性）逐条评估

- **实测发现**：Claude Code 5.5 倍 token 效率的声明仅有 1 个信源（一次 X 帖子），验证结果 D-4（存疑）

- **安装方式**：`claude plugin marketplace add Luxuzhou/source-verifier-skill`，无需 API key

**提取的概念**

- Source-Verifier-skill

- last30days-skill

- NATO Admiralty Code（信息评估体系）

**原始文章信息**

- 作者：硅基鹿鸣（陆徐洲）

- 来源：微信公众号

- 发布时间：2026-03-30

- 链接：[https://mp.weixin.qq.com/s?__biz=MzU0MDcyMDQ0Nw==&mid=2247484431](https://mp.weixin.qq.com/s?__biz=MzU0MDcyMDQ0Nw%3D%3D&mid=2247484431)

**个人评注**：与 Tizer 的知识管理工作流直接相关，Source-Verifier + last30days 组合可以集成进 HITL 内容 pipeline，为信息采集和验证提供自动化支撑。值得在 Wiki Compiler 中参考这种分层验证思路。
