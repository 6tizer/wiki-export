---
title: Conway
type: entity
tags:
- 浏览器自动化
- 长期记忆
- AI 产品
status: 审核中
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/9feabbf4f7dd4231b6ad6420d4553f01
notion_id: 9feabbf4-f7dd-4231-b6ad-6420d4553f01
---

**定义**

Conway（也常被称作 Conway Agent）是 Anthropic 内部测试的"永久在线"（Always-On）AI 智能体环境，通过 Webhook 外部唤醒机制实现事件驱动的自主决策，标志着 AI 从会话式工具向持续运行数字分身的演进。

> ⚠️ 注意：Conway 目前为内部测试阶段，信息来自泄露的内部资料，非官方正式发布。

**核心特性**

- **独立 UI**：专属侧边栏，不寄生于聊天窗口，持久存在于系统中

- **Webhook 唤醒**：外部事件（邮件到达、股价波动、服务器预警等）可直接激活 Agent，无需用户主动发起对话

- **深度浏览器集成**：直接接管 Chrome 权限，能访问和操作网页内容

- **.**[**cnw.zip**](http://cnw.zip/)** 扩展协议**：定义 Agent 的"基因标准"，绕过聊天界面直接通过浏览器和本地工具进行深层操作

- **持久记忆**：无 Session 概念，跨次操作保持完整工作记忆

**Conway vs Cowork 区别**

| 维度 | Cowork | Conway |

| --- | --- | --- |

| 触发方式 | 用户发指令 | Webhook 自动触发 |

| 在线状态 | 用户在线时 | 7×24 永久在线 |

| 能力定位 | 完成任务 | 自主决定何时做事 |

| 目标用户 | 95% 非技术职场人 | 所有需要持续监控/执行的场景 |

**战略意义**

- Anthropic 路线图：Claude Code（工程师）→ Cowork（95% 职场人）→ Conway（AI 操作系统底座）

- 代表 AI 从"高级工具"到"数字生命"的范式跃迁

**来源引用**

- [摘要：Anthropic一夜震撼升级：Claude获得「永久在线」！全球打工人变天](summaries/摘要：Anthropic一夜震撼升级：Claude获得「永久在线」！全球打工人变天.md)（新智元，2026-04-02）

- [摘要：凌晨3点，硅谷炸锅！Anthropic源码意外泄露，51万行代码揭露Claude惊天野心](summaries/摘要：凌晨3点，硅谷炸锅！Anthropic源码意外泄露，51万行代码揭露Claude惊天野心.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652695027&idx=2&sn=95c7c69c2170bdfcc5acec870d14cd59&chksm=f0e3f5d6d7d4b599e156421a54e77bfae306b7fb7b21299b37c7ddcf43d8de24ef5723b0a15c#rd)）
