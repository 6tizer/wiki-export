---
title: Agent-Skill-Script 三层架构
type: concept
tags:
- Agent 编排
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/b2cae6d86fc749af98ab944305eb434a
notion_id: b2cae6d8-6fc7-49af-98ab-944305eb434a
---

**定义**：AI 任务分配的金字塔模型，按"Script 优先 → Skill 次之 → Agent 最后"的阶段分配任务，使 Agent 专注于真正需要动态判断的创造性任务。

**三层定义**

| 层次 | 定义 | 适用场景 | 示例 |

| --- | --- | --- | --- |

| **Script** | 逻辑固定，输入输出确定 | 可预见的重复性任务 | 飞书自动化、定时投递 |

| **Skill** | 需要泛化能力，不需要自主决策 | 无法写死逻辑但规则相对确定 | 资讯打分、内容分类 |

| **Agent** | 需要动态规划，根据中间结果调整 | 不能提前规划所有步骤 | 开发新脚本、竞品分析报告 |

**核心思想**

- 错误地将所有任务交给 Agent = "慢、贵、不稳定"

- 最佳模式：Agent 创造工具，工具执行任务，已确定的逻辑不断下沉为 Skill 或脚本

- Skill 的价值：封装泛化能力，无法写死逻辑但又不需要多步骤规划

**相关概念**

- HITL 工作流：人类审批重要决策节点，Agent 只处理真正复杂的部分

**来源引用**

- [摘要：能用脚本就别用Agent。](summaries/摘要：能用脚本就别用Agent。.md)
