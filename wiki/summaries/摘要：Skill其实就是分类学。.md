---
title: 摘要：Skill其实就是分类学。
type: summary
tags:
- Harness 工程
- 上下文管理
status: 已审核
confidence: medium
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b6881d48281c5d7e3ddcc46
notion_url: https://www.notion.so/Tizer/00cb245e8301468692d51fd50bbf55e0
notion_id: 00cb245e-8301-4686-92d5-1fd50bbf55e0
---

## 一句话摘要

作者认为 Skill 的本质不是不断堆数量，而是先做好分类体系与触发设计，用合适的颗粒度把相近场景收敛进少量高质量 Skill。

## 关键洞察

- Skill 的核心是**分类**和**触发**，能否正确命中比堆积更多 Skill 更重要

- 当 Skills 数量从 20 个以下增长到数十甚至数百时，准确率、速度和 Token 成本都会明显恶化

- 相近需求不应机械拆成多个 Skill，而应先归入同一类 Skill，再在内部按上下文分流

- 判断一个 Skill 是否值得存在，可以看场景边界是否明确、是否高频复现、能否并入已有 Skill

- `CLAUDE.md` 与 Skill 应该各司其职，前者处理全局规则，后者处理具体能力与触发逻辑

## 提取的概念

- [Skill 分类学](concepts/Skill 分类学.md)

- [Skill 触发条件](concepts/Skill 触发条件.md)

- [Skill 颗粒度设计](concepts/Skill 颗粒度设计.md)

- [NanoBanana](entities/NanoBanana.md)

- [CLAUDE.md](concepts/CLAUDE.md.md)

- [Thin Harness, Fat Skills](concepts/Thin Harness, Fat Skills.md)

## 原始文章信息

- 作者：数字生命卡兹克

- 来源：微信

- 发布时间：2026-04-16 10:58

- 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA%3D%3D&mid=2647681530&idx=1&sn=d5c714699089e31276c667cda1edefdb&chksm=f153676ae06e0dadad8df80becf797662c0126d74a5c1a314ecac659ebf41da34625aac44a6b#rd)

## 个人评注

这篇文章对 Tizer 的内容管线和 Agent 设计都有直接启发：与其持续增加零散 Skill，不如先设计清晰的分类层级、触发边界和总 Skill 内部分流逻辑。对现有工作流来说，更适合把稳定规则沉淀在 `CLAUDE.md`，把高频可复用能力沉淀为少量高质量 Skill，避免技能库膨胀后带来命中率下降和维护负担。
