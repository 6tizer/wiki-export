---
title: Graph of Skills
type: concept
tags:
- Agent 编排
- Agent 技能
status: 审核中
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/a218b4a94a9c4192885b4f49f78f1093
notion_id: a218b4a9-4a9c-4192-885b-4f49f78f1093
---

**定义**

Graph of Skills，简称 GoS，是一种面向大规模 Skill 库的结构化检索框架。它不再把 Skill 看作孤立文本，而是把 Skill 组织为带依赖关系的有向图，在有限上下文预算内检索出可直接执行的技能组合。

### 关键要点

- 先离线构建技能图，再在线做结构化检索。

- 图中的核心价值不只是“找相似 Skill”，而是补齐执行所需的依赖链。

- 相比全量塞入上下文或单纯向量检索，GoS 在任务成功率、Token 成本和可执行性之间取得了更优平衡。

- GoS 的前提是离线图谱质量足够高，否则局部邻域缺边时仍可能检索失败。

### 别名

- GoS

### 来源引用

- [UPenn提出Graph of Skills：把海量Skill连成技能图 ｜CC可用、支持Minimax2.7](https://mp.weixin.qq.com/s?__biz=Mzg4MzYxODkzMg%3D%3D&mid=2247508030&idx=1&sn=572b29895c21b52d527d16bb96fda6e3&chksm=ce5a1e823375cc2ef34695e8938d278b705a3b1ec50ca3d068e6d45f7c52a5428589e76d6478#rd)｜来源：微信｜作者：AI修猫Prompt｜发布日期：2026-04-16｜源页面：UPenn提出Graph of Skills：把海量Skill连成技能图 ｜CC可用、支持Minimax2.7
