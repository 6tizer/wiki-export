---
title: 摘要：智谱炸群了：GLM-5.1直接上线，开源第一换人
type: summary
tags:
- LLM
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, OpenClaw, 自动化
source_article_url: ''
notion_url: https://www.notion.so/a43dba01a194499b91269e8f0116f369
notion_id: a43dba01-a194-499b-9126-9e8f0116f369
---

**一句话摘要**：GLM-5.1在SWE-bench Pro中刷新全球最佳成绩超越Claude Opus 4.6，展示了8小时长程任务自主工作能力，并在三个不同领域的实测任务中全部零介入完成。

**关键洞察**：

- SWE-bench Pro全球第一，超过Claude Opus 4.6、GPT-5.4、Gemini 3.1 Pro

- 实测案例（1）量化回测系统：10分钟自主构建包含DataLoader/FactorEngine/BacktestEngine等六个类的完整框架

- 实测案例（2）电商数据仪表板：自主生成模拟数据+搭建含5个KPI卡片和7个可视化图表的Plotly交互页面

- 实测案例（3）全栈博客系统：Next.js+Supabase，主动集成代码高亮和实时预览（需求中未提过）

- OpenRouter上调用量开源断档第一，成本只有Claude Code的1/3

- 整体体现了长程任务（Long Horizon Task）的交付单位转变：从「一个回答」到「一个项目」

**提取的概念**：GLM-5.1、Long Horizon Task、SWE-bench

**原始文章信息**：

- 作者：开发者阿橙

- 来源：微信公众号

- 发布时间：2026-04-08

**个人评注**：GLM-5.1的高性价比对OpenClaw工作流有直接价值——作为Claude的替代选项，尤其是Anthropic封杀事件后。其高SWE-bench成绩也证明了这就是一个适合代码密集型Agent工作的模型。
