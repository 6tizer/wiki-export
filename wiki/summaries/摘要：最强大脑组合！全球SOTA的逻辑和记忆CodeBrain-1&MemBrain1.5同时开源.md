---
title: 摘要：最强大脑组合！全球SOTA的逻辑和记忆CodeBrain-1&MemBrain1.5同时开源
type: summary
tags:
- 长期记忆
- MCP 协议
- Harness 工程
status: 已审核
confidence: high
last_compiled: '2026-04-28'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/715659112e52406ebccc2cb9de3f908c
notion_id: 71565911-2e52-406e-bccc-2cb9de3f908c
---

**一句话摘要**：Feeling AI开源CodeBrain-1（Terminal-Bench 2.0全球前列，成本降低63.9%）和MemBrain1.5（自适应实体树算法，论文内容管理基准测试SOTA），将Agent从工程师助手变为可信赖的交付专家。

**关键洞察**：

- CodeBrain-1：5层架构（核心层/引擎层/工具层/技能层/MCP服务器），将LSP语言服务器和tree-sitter语法封装为11个面向意图的工具，任何Agent均可调用

- CodeBrain-1.5：81.3%成绩领跑全球，在Claude Opus 4.6上节省63.9% Token成本（$313.0降至$112.9）

- MemBrain vs 纯文本方案（OpenClaw式）vs 图结构方案（Graphiti）：尝试同时保留语义保真和显式关联

- 自适应实体树算法：实体为根节点，Agent自动按主题聚类为中间层，原子事实为叶节点；每条原子事实含带别名指向实体，内容完整不拆分，可动态替换为实体最新描述（「可渲染模板」）

- 分层检索：80%由先验结构处理，20%由Agent判断——查询扩展和Agentic模式

**提取的概念**：CodeBrain、MemBrain、自适应实体树算法

**原始文章信息**：

- 作者：机器之心

- 来源：微信公众号

- 发布时间：2026-04-08

- GitHub：[https://github.com/feelingai-team/CodeBrain](https://github.com/feelingai-team/CodeBrain), [https://github.com/feelingai-team/MemBrain](https://github.com/feelingai-team/MemBrain)

**个人评注**：MemBrain的自适应实体树算法是构建Agent记忆系统的重要参考实现。CodeBrain的成本削减方法对Wiki Compiler这类大量调用工具的Agent有直接借鉴价值。
