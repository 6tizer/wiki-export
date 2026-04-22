---
title: 关于 Gap Agent
type: concept
tags:
- 知识管理
- Agent 技能
status: 需更新
confidence: medium
last_compiled: ''
source_tags: ''
source_article_url: https://www.notion.so/1249bdf6ad334e11ad3d44fde9cb241f
notion_url: https://www.notion.so/71f059d5e85c4426bdaeee1517c8c849
notion_id: 71f059d5-e85c-4426-bdae-ee1517c8c849
---

## 核心定位

**反向 Lint**——现有 Lint Agent 审查 Wiki 内部质量问题（冗余、矛盾、格式），Gap Agent 则检测 Wiki 与外部世界之间的认知缺口，让 Wiki 从「被动接收」转变为「主动感知边界」。

---

## 两层检测机制

### 第一层：领域覆盖缺口（Coverage Gap）

定期抓取关注领域的前沿信号源，与 Wiki 现有概念页对比，识别"外部频繁提及但 Wiki 中无对应页面"的盲点。

**信号源示例：**

- OpenRouter 新上线模型

- HuggingFace 热门新 repo

- arXiv 近期高引论文

- GitHub Trending

- 行业 Newsletter / RSS 聚合

**输出：** 待摄取清单（ingestion backlog），推送给用户或直接触发 Compiler 流水线。

### 第二层：知识老化检测（Staleness Detection）

标记「页面上次更新时间 vs 该领域此后重大进展」的时间差，提醒 Compiler 重新摄取和更新。

**判定逻辑：**

- 页面最后编译时间距今超过阈值（如 90 天）

- 该页面所属领域在此期间有高信号事件（新论文、新版本发布、架构变更等）

- 优先级 = 领域变化速度 × 页面重要性 × 过期时长

**输出：** 需更新清单，可将对应页面状态标记为「需更新」。

---

## 与现有 Agent 的协作关系

| Agent | 视角 | 检查方向 |

| --- | --- | --- |

| Lint Agent | 内审 | Wiki 内部质量（格式、冗余、矛盾） |

| **Gap Agent** | 外审 | Wiki 与外部世界的覆盖差距 + 知识老化 |

| Compiler | 执行 | 根据 Gap Agent 输出执行摄取与更新 |

| Synthesizer | 整合 | 新摄取内容跨页面综合分析 |

---

## 实现路径思考

- **Phase 1（手动触发）：** 用户提供关键词列表 → Gap Agent 搜索 Web + 对比 Wiki → 输出缺口报告页（类型 = lint-report）

- **Phase 2（定期自动）：** 通过定时触发器周期运行，自动生成 gap-report，推送通知

- **Phase 3（闭环）：** Gap Agent 输出直接进入 Compiler 的摄取队列，形成"感知 → 摄取 → 编译 → 审核"全自动闭环
