---
title: Wiki Schema（规则文件）
type: index
tags:
- 知识管理
- 笔记工具
- Agent 协作模式
---

## 📖 概述
这是知识 Wiki 系统的「宪法文件」，定义了 Wiki 的组织规则、页面模板、流程规范。
所有 Wiki 系统 Agent 和 Notion AI 都应遵循此文件。各 Agent 的详细职责分工见 系统工作流程图。
## 📂 条目类型定义
### concept（核心概念词条）
页面结构：
- 定义：一句话说明白这个概念是什么
- 关键要点：3-5 个核心要点
- 实例/应用：具体使用场景或案例
- 关联概念：与其他 concept 页面的 <mention-page> 链接
- 来源引用：引用的 summary 条目列表
### summary（单篇资料摘要）
页面结构：
- 一句话摘要：文章核心观点
- 关键洞察：3-5 个最重要的发现/观点
- 提取的概念：使用 <mention-page> 标签引用对应的 concept 页面（不是纯文本）
- 原始文章信息：作者、来源、发布时间、原文链接
- 个人评注：与 Tizer 现有工作流的关联点
### 🔗 引用链格式强约束（跨所有条目类型）
所有结构化引用必须使用 <mention-page> 标签，严禁纯文本引用。具体：
- summary 的「提取的概念」段 → <mention-page url="...">concept 名称</mention-page>
- concept/entity 的「来源引用」段 → <mention-page url="<summary-url>">摘要：<原文标题></mention-page>
- synthesis 的「来源列表」→ <mention-page> 引用所有 summary/concept
- qa 的「引用来源」 → <mention-page> 引用引用的 Wiki 页面
原因：结构化引用是知识图谱连通、孤岛检测、状态晋升的基础。Compiler 编译时必须遵守；历史纯文本存量由 Wiki 引用升级员 自动清理。
### synthesis（跨资料综合分析）
何时创建：
- 单标签：某个标签下积累了 ≥10 个 concept/entity，且没有已有 synthesis 覆盖该主题
- 双标签：两个标签的交集 ≥3 个共享 concept/entity（如「Agent 编排 × 记忆系统」）
- 三标签（高阶综合 / 面）：三个标签各自拥有 ≥5 个 concept/entity，且三个标签的两两交集各至少有 ≥2 个共享 concept/entity。三标签 synthesis 应引用已有的双标签 synthesis 作为输入，在其基础上提炼跨三边的涌现结构（闭环、矛盾、收敛模式等双标签视角无法呈现的洞察）
- 四标签（立体综合 / 体）：在一个已有的三标签三角形（A、B、C）基础上，引入第四个「远距离」标签 D，要求：
- 或者一轮系统性对话产出了重要的架构决策
产出配额：每次最多生成 1 篇单/双标签 + 1 篇三标签 + 1 篇四标签，深度优先。优先级：四标签（体）＞ 三标签（面）＞ 双标签（线）＞ 单标签（点）。
扫描逻辑：Synthesizer 每次运行时，先检查是否存在可产出的四标签组合（以已有的三标签 synthesis 为锚点，遍历剩余标签找远距离候选），再筛选三标签组合，最后扫描双标签和单标签候选。
页面结构：
- 研究问题：这篇 synthesis 要回答什么问题
- 综合分析：跨多篇资料的综合推理（鼓励使用对比表）
- 关键发现：3-5 个跨来源才能发现的洞察
- 来源列表：引用的所有 summary 和 concept
- 行动建议：基于分析的可执行建议
### qa（问答沉淀）
执行者：Wiki QA Agent
何时创建：当回答综合了 ≥3 个 Wiki 页面的内容，且问题不是一次性的操作请求（如「帮我合并这两个概念」）。
页面结构：
- 问题：原始提问
- 回答：综合回答正文
- 引用来源：使用 <mention-page> 引用的 Wiki 页面列表
### entity（实体档案 — 人物/产品/公司的持续跟踪页）
与 concept 的区别：
- concept = 技术概念、方法论、架构模式（如 Harness 工程、ReAct Agent、RAG）
- entity = 具体的产品、公司、人物（如 OpenClaw、Anthropic、Karpathy）
判断标准：如果这个概念有版本历史、融资信息、GitHub Stars、团队背景等「档案属性」，它就是 entity 而不是 concept。
页面结构：
- 简介：一句话介绍这个实体
- 关键数据：官网、GitHub、Stars、License、团队、融资等
- 版本/动态时间线：重要版本发布和事件记录（持续更新）
- 与我的关系：Tizer 如何使用/关注这个实体
- 相关 concept：与此实体相关的技术概念 <mention-page> 链接
- 所有引用的 summary：所有提到这个实体的摘要列表
### lint-report（健康报告）
页面结构：
- 检查日期、健康度评分、孤岛条目、过期草稿、重复疑似、状态异常、标签异常、标签分布统计、状态晋升建议、改进建议
## 📨 对话产出沉淀规则
当 Notion AI 与用户的对话产出了有价值的结果时，按以下规则判断是否需要沉淀到 Wiki：
## 🔄 Ingest 流程（资料编译）
执行者：Wiki Compiler Agent
触发条件：新文章入库（page.created，60s 防抖）或手动 @mention。定时批量触发已关闭（存量已清零）
执行步骤：
1. 读取新文章的完整内容和备注
1. 🔒 Summary 去重检查：先用源文章 URL 查询；若未命中且存在外部原文链接，再用「标题候选 + 原文链接核验」做第二层去重；对 Learn more in the official documentation 这类导航/占位标题或正文主要为目录跳转的页面直接跳过，不创建 summary
1. 创建一条 summary 页面（状态=已审核）
1. 从文章中提取核心概念（3-7 个）
1. 对每个概念：
1. 提取的概念用 <mention-page> 回填到 summary 的「提取的概念」段
1. 设置所有新页面的标签、置信度、最后编译时间
1. 标记源文章 已编译到Wiki = true
重要原则：
- 增量更新，不要全量重写已有页面
- concept 名称使用业界通用术语，遵循命名归一化规则
## 🔍 Query 流程（检索回答）
主要执行者：Wiki QA Agent（知识库专属问答窗口）、Notion AI（兑底 + 系统管理场景）
其他 Agent 也使用 SQL 查询来完成各自职责（Compiler 查重、Lint 统计、Fixer 定位目标等）。
查询策略（按优先级）：
1. SQL 直查：用 querySql 按名称、标签、类型等条件查询数据库，这是最快最准的方式
1. 读取具体页面：用 loadPage 读取 concept/summary/synthesis 的完整内容
1. 全局搜索：如果 SQL 查询结果不足，用 search 跨所有来源搜索
回答流程：
1. 根据问题类型选择查询策略，定位相关页面
1. 读取页面完整内容
1. 综合推理，标注来源引用。根据来源条目状态差异化处理：
1. 如果回答具有沉淀价值，按「对话产出沉淀规则」判断是否创建 qa 或 synthesis
常用 SQL 模板：
- 按标签找 concept：SELECT url, "名称" FROM wiki WHERE "类型" = 'concept' AND "标签" LIKE '%记忆系统%'
- 按名称模糊查找：SELECT url, "名称", "类型" FROM wiki WHERE "名称" LIKE '%MemBrain%'
- 查看最近更新：SELECT url, "名称", "类型" FROM wiki ORDER BY "最后编辑时间" DESC LIMIT 10
