---
title: 摘要：UPenn提出Graph of Skills：把海量Skill连成技能图 ｜CC可用、支持Minimax2.7
type: summary
tags: []
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b68817f808ccb52a147a99f
notion_url: https://www.notion.so/Tizer/26170ed28bf243bf86ac0193fe476fae
notion_id: 26170ed2-8bf2-43bf-86ac-0193fe476fae
---

### 一句话摘要

Graph of Skills 通过把海量 Skill 库组织成带依赖关系的技能图，并结合混合检索与逆向扩散，在有限上下文预算内找出真正可执行的技能组合，从而显著优于全量上下文加载和单纯向量检索。

### 关键洞察

- 文章指出，Skill 库一旦扩张到数千甚至数万个，Agent 的核心瓶颈不再只是推理，而是能否一次找齐可执行链路所需的完整 Skill 组合。

- 传统的全量加载方案会造成 Token 成本爆炸与注意力稀释，而纯向量检索又容易遗漏解析器、预处理器、环境设置器等关键依赖。

- GoS 的核心创新在于离线构建带类型技能图，并在在线检索阶段允许相关性沿依赖边反向传播，从高层技能回溯到底层依赖。

- 在 SkillsBench 与 ALFWorld 等基准中，GoS 同时取得更高任务奖励和更低上下文成本，说明“结构化检索”优于“语义相似度优先”的简单召回。

- GoS 的效果高度依赖离线图谱质量。如果图中缺少关键边或局部邻域不完整，依然可能在长依赖任务中失效。

### 提取的概念

- [Graph of Skills](concepts/Graph of Skills.md)

- [混合种子检索](concepts/混合种子检索.md)

- [逆向感知图谱扩散](concepts/逆向感知图谱扩散.md)

- [先决条件鸿沟](concepts/先决条件鸿沟.md)

- [带类型关系归纳](concepts/带类型关系归纳.md)

### 原始文章信息

- 作者：AI修猫Prompt

- 来源：微信

- 发布时间：2026-04-16 20:01

- 链接：[https://mp.weixin.qq.com/s?__biz=Mzg4MzYxODkzMg==&mid=2247508030&idx=1&sn=572b29895c21b52d527d16bb96fda6e3&chksm=ce5a1e823375cc2ef34695e8938d278b705a3b1ec50ca3d068e6d45f7c52a5428589e76d6478#rd](https://mp.weixin.qq.com/s?__biz=Mzg4MzYxODkzMg%3D%3D&mid=2247508030&idx=1&sn=572b29895c21b52d527d16bb96fda6e3&chksm=ce5a1e823375cc2ef34695e8938d278b705a3b1ec50ca3d068e6d45f7c52a5428589e76d6478#rd)

### 个人评注

这篇文章对 Tizer 当前的 Agent 工作流很有启发，尤其适合用于思考 OpenClaw 或多 Skill 系统在大规模工具库下的检索层设计。相比把全部工具描述直接塞进上下文，先做结构化建图，再在运行时按依赖感知检索，更适合内容流水线、HITL 协作和复杂 Skill 编排场景。
