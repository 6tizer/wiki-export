---
title: Anthropic API
type: entity
tags:
- AI 产品
- Agent 协作模式
status: 审核中
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/765984c29947459ca549f1a3ac4166f2
notion_id: 765984c2-9947-459c-a549-f1a3ac4166f2
---

## 定义

Anthropic API 是 Anthropic 提供的模型与工具调用接口层，除了文本生成，还支持内置工具与标准 Tools 模式。

## 关键要点

- 它既支持普通自定义工具，也支持像 `web_search` 这样的内置工具类型

- 内置工具与自定义工具的请求结构并不完全相同，不能简单混用

- 当第三方服务只做“表面兼容”时，Claude Code 这类原生客户端的工具调用就可能失配

## 来源引用

- [摘要：我给Claude Code 增加了多模型切换功能](summaries/摘要：我给Claude Code 增加了多模型切换功能.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIxNjM4MTMzOA%3D%3D&mid=2247484908&idx=1&sn=47c8fe19d582ad3d2a855cd0357a9078&chksm=96149bde764c82c85d8d9dca7aa660ae3913126cf6047a256cae541d3b55e91dadc9820ea101#rd)）

- [摘要：各家Coding Plan为啥不兼容Claude WebSearch格式](summaries/摘要：各家Coding Plan为啥不兼容Claude WebSearch格式.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkyOTY1NzMzNg%3D%3D&mid=2247489376&idx=1&sn=722c4f2ba5f82432e7abff79079f8bef&chksm=c3cb3b3b7b865b2b1cf89b3ea79ebe2a03d32fb1e8749f2f334e444c518356d58f2af2b2561f#rd)）

- [摘要：9秒，公司没了！Claude「删库跑路」，Anthropic封杀110人公司，却还在扣钱](summaries/摘要：9秒，公司没了！Claude「删库跑路」，Anthropic封杀110人公司，却还在扣钱.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652695870&idx=1&sn=90f71bfc3f6091269c543b91368b22ee&chksm=f0e8f6e20c4403138c01e736a3c07cd72c780fe55c94401be3d215aa64fd7e8e3adce1d273e2#rd)）

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [自定义模型接入](concepts/自定义模型接入.md)

- [MiniMax M2.7](entities/MiniMax M2.7.md)

- [WebSearch](concepts/WebSearch.md)

- [WebFetch](concepts/WebFetch.md)

- [GLM-5.1](entities/GLM-5.1.md)

- [OpenClaw](entities/OpenClaw.md)
