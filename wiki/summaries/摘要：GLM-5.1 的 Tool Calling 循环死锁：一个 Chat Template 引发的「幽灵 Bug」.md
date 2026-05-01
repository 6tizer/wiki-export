---
title: 摘要：GLM-5.1 的 Tool Calling 循环死锁：一个 Chat Template 引发的「幽灵 Bug」
type: summary
tags:
- Harness 工程
- 模型部署
- 推理优化
status: 已审核
confidence: medium
last_compiled: '2026-04-16'
source_tags: LLM, Agent, 开发者工具
source_article_url: https://www.notion.so/344701074b688122b769d875cbfa7bf4
notion_url: https://www.notion.so/Tizer/1faa7a74e28a44c6ad0563fddf001db1
notion_id: 1faa7a74-e28a-44c6-ad05-63fddf001db1
---

## 一句话摘要

GLM-5.1 在 vLLM 与 SGLang 的工具调用场景中，会因旧版 Chat Template 无法正确渲染 array parts 形式的 tool message，导致工具结果被吞掉并反复触发同一工具调用。

## 关键洞察

- 问题根因不在模型能力本身，而在 chat template 对工具消息格式的假设过窄

- vLLM 会把工具返回的 string 自动转换成结构化数组，这一步与 GLM-5.1 旧模板发生了协议错位

- 工具结果被渲染为空后，模型会误判工具未成功执行，从而进入重复调用同一工具的死循环

- 修复方式很直接，替换 Hugging Face 仓库中的新版 `chat_template.jinja` 即可，临时也可用 `--chat-template-content-format string` 规避

- 这件事说明 Tool Calling 的稳定性不仅取决于模型，还取决于推理框架、消息格式与模板层之间的隐形契约

## 提取的概念

- [GLM-5.1](entities/GLM-5.1.md)

- [Tool Calling](concepts/Tool Calling.md)

- [vLLM](entities/vLLM.md)

- [SGLang](entities/SGLang.md)

- [Chat Template](concepts/Chat Template.md)

## 原始文章信息

- 作者：@Zai_org

- 来源：X书签

- 发布时间：2026-04-16

- 原文链接：[https://x.com/Zai_org/status/2044741938604093443](https://x.com/Zai_org/status/2044741938604093443)

## 个人评注

这条材料对 Tizer 当前的 Agent 工作流很有参考价值。它提醒我们在 OpenClaw、HITL 和内容编译链路里，不要只盯着模型能力本身，还要把消息格式、模板渲染和工具返回结构当成一等公民来验证。对于后续自建 Agent pipeline，这也是一个很典型的“接口契约层故障”案例。
