---
title: 摘要：这才是AI做ppt的正确姿势 ！
type: summary
tags:
- AI 设计
- AI 产品
- 图像生成
status: 已审核
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: https://www.notion.so/348701074b68810abfaffdb1dfc520f1
notion_url: https://www.notion.so/919d257d10b84a5cb80f64c0936433ee
notion_id: 919d257d-10b8-4a5c-b80f-64c0936433ee
---

## 一句话摘要

PPT Master 通过把 AI 生成的 SVG 逐元素转换为 PowerPoint 原生 DrawingML，解决了 AI 做 PPT 常见的“导出后不可编辑、格式易错乱、隐私依赖云端”的问题。

## 关键洞察

- 它的核心差异不在于“也能生成幻灯片”，而在于导出的 `.pptx` 仍然是可编辑的原生形状，而不是截图或贴图。

- 项目把 SVG 到 DrawingML 的转换做成默认导出路径，因此文本框、渐变、阴影、箭头、裁剪等细节都能在 PowerPoint 中继续修改。

- 整体流程尽量本地运行，除模型调用外不必把 PDF、DOCX 上传到第三方 SaaS，对金融、咨询、政务等隐私敏感场景更友好。

- 它采用 Strategist、Executor、Image Generator、后处理导出等分工式流水线，并强调按页顺序生成，以换取跨页面视觉一致性。

- 相比订阅制 AI PPT SaaS，PPT Master 走开源 + 多模型/多编辑器适配路线，更强调可控性、低锁定和二次开发空间。

## 提取的概念

- [PPT Master](entities/PPT Master.md)

- [DrawingML](concepts/DrawingML.md)

- [本地优先处理](concepts/本地优先处理.md)

- [多 Agent 协作工作流](concepts/多 Agent 协作工作流.md)

- [串行页面生成](concepts/串行页面生成.md)

## 原始文章信息

- 作者：开源日记

- 来源：微信

- 发布时间：2026-04-19 15:09（Asia/Shanghai）

- 原文链接：[https://mp.weixin.qq.com/s?__biz=Mzg3NzU0NzIxMA==&mid=2247511533&idx=1&sn=92a0da3abdf30964dfee5cad8e3d4a37&chksm=cef35009229a433f9fb8123e47f9426a2e6858f506f7d551ce5ad710f6f0545513c6c2a2d595#rd](https://mp.weixin.qq.com/s?__biz=Mzg3NzU0NzIxMA%3D%3D&mid=2247511533&idx=1&sn=92a0da3abdf30964dfee5cad8e3d4a37&chksm=cef35009229a433f9fb8123e47f9426a2e6858f506f7d551ce5ad710f6f0545513c6c2a2d595#rd)

## 个人评注

这类“生成结果可继续编辑”的路线，对 Tizer 的内容流水线很有参考价值：它不是把 AI 产物当成终稿，而是把 AI 变成高质量初稿生成器，先保证结构和视觉起点，再把后续人工精修保留在熟悉的软件里。同时，本地优先 + 开放导出的思路，也符合 HITL 场景里对可控性、可审阅性和低平台锁定的偏好。
