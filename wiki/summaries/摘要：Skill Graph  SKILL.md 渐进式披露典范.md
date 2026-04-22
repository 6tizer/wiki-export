---
title: 摘要：Skill Graph > SKILL.md 渐进式披露典范
type: summary
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Skill 开发, Agent, Prompt Engineering
source_article_url: ''
notion_url: https://www.notion.so/6fe0d94ed87a425ba745496db9aca3e5
notion_id: 6fe0d94e-d87a-425b-a745-496db9aca3e5
---

**一句话摘要**：Skill Graph 将知识拆分为多个 markdown 文件并用 wikilinks 连成网络，让 Agent 可像专家一样按需导航知识体系，实现渐进式披露。

**关键洞察**

- 单个 [SKILL.md](http://skill.md/) 无法装下复杂领域知识，而 Skill Graph 把知识拆成多个 markdown 文件，用 wikilinks 建立关联

- 三个核心要素：wikilinks（嵌入正文告知何时深入）、YAML frontmatter（扫一眼描述判断是否读全文）、MOC（导航索引）

- 渐进式披露：Agent 先读 index 了解全局，再扫描 YAML 筛选，再沿 wikilinks 跳转—— 10 万字知识库可能只需读 3000 字

- arscontexta 是该理念的具体实现（249 个文件的 Claude Code 插件）

- 本质：Agent 从"背课文"进化到"理解领域"，从静态注入到动态导航

**提取的概念**

- Skill Graph（基于 wikilinks 的分布式知识框架）

- 渐进式披露（已有词条 [https://www.notion.so/23b110f4b1af40c5a252c04882bac4ed）](https://www.notion.so/23b110f4b1af40c5a252c04882bac4ed）)

**原始文章信息**

- 作者：向量空性 | 来源：微信公众号 | 发布时间：2026-03-20

- 链接：[https://mp.weixin.qq.com/s?__biz=Mzg5NjgzMTE5MQ==&mid=2247484194](https://mp.weixin.qq.com/s?__biz=Mzg5NjgzMTE5MQ%3D%3D&mid=2247484194)

**个人评注**

与 Tizer 的知识管理工作流密切相关，尤其适合将 OpenClaw 的复杂领域知识（如量化策略、内容制作过程）拆分为 Skill Graph，显著提升 Agent 处理复杂任务的能力。
