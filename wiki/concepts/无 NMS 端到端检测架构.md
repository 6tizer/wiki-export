---
title: 无 NMS 端到端检测架构
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/b9b92ef957aa478bb5b8e1d0eac0c1c7
notion_id: b9b92ef9-57aa-478b-b5b8-e1d0eac0c1c7
---

## 定义

无 NMS 端到端检测架构 是一种在目标检测模型中尽量把后处理逻辑内化到模型本身、减少或去掉 NMS 步骤的设计路线。

## 核心要点

- 目标是简化推理链路并减少后处理开销

- 有利于提升端到端部署一致性和实时性能

- 是新一代目标检测模型追求更高效率的一条演进方向

## 来源引用

- [原文链接](https://x.com/berryxia/status/2042364832863961462)｜《YOLO26-MLX：Mac 上跑目标检测，彻底告别 PyTorch》｜来源页：YOLO26-MLX：Mac 上跑目标检测，彻底告别 PyTorch
