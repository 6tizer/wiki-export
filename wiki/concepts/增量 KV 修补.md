---
title: 增量 KV 修补
type: concept
tags:
- 推理优化
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e0447e77bafe405a923e192c8fe6da54
notion_id: e0447e77-bafe-405a-923e-192c8fe6da54
---

## 定义

增量 KV 修补，是一种在模型持续推理期间同步 KV 缓存状态的机制：系统持续追踪新写入的 KV 数据，并将增量补丁异步传输到目标设备，直到两端状态收敛后再进行最终切换。

## 关键要点

- 设计灵感来自虚拟机热迁移中的脏页同步思路。

- 它避免了“停止服务后整体复制”带来的长暂停问题。

- 通过脏位图与周期性补丁发送，源端与目标端 KV 状态可以逐步逼近一致。

- 当残余差距足够小时，再执行极短同步点与原子切换，从而将服务中断压到毫秒级。

## 关联概念

- [摘要：大模型服务新范式：PipeLive突破在线流水线并行重构难题，自适应异构GPU环境，性能提升超30%](summaries/摘要：大模型服务新范式：PipeLive突破在线流水线并行重构难题，自适应异构GPU环境，性能提升超30%.md)

## 来源引用

- [摘要：大模型服务新范式：PipeLive突破在线流水线并行重构难题，自适应异构GPU环境，性能提升超30%](summaries/摘要：大模型服务新范式：PipeLive突破在线流水线并行重构难题，自适应异构GPU环境，性能提升超30%.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDgzMA%3D%3D&mid=2247557871&idx=1&sn=93ad2f6963d089262651c0d240c0e4f8&chksm=cf61645b6cd81036051aff2da5c3faf13afa936640bf4670322c43996fa2c291fc30415885df#rd)）
