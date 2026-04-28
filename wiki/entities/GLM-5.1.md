---
title: GLM-5.1
type: entity
tags:
- 代码生成
- 模型评测
- AI 产品
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c0ff002c86f541ab9acd0fcab3b4e679
notion_id: c0ff002c-86f5-41ab-9acd-0fcab3b4e679
---

## 定义

GLM-5.1是智谱发布的开源旗舰级代码生成模型，在SWE-bench Pro基准测试中刷新全球最佳成绩，超越Claude Opus 4.6、GPT-5.4等头部模型，并是全球首个在真实工程任务中验证了8小时持续工作能力的开源模型。

## 核心性能

### SWE-bench Pro 全球第一

- 超越Claude Opus 4.6、GPT-5.4、Gemini 3.1 Pro

- 中国开源模型首次在核心工程能力指标上与全球前沿并驾齐驱

- Design Arena全面包揽开源模型前四名

### Long Horizon Task 小时级主动工作

- **8小时任务**：构建包含窗口管理器的完整Linux桌面系统，执行1200+步骤

- **14小时CUDA内核优化**：加速比2.6×→ 35.7×，自主判断放弃高层框架转向底层C++

- **655轮向量数据库优化**：QPS从3108推到21472，提升到初始版本6.9倍

## 三个技术突破

1. **长程规划与目标保持**：复杂大目标拆解为多阶段计划，大量步骤后仍记得之前定的规则

1. **自适应纠错与持续执行**：自主查看错误日志、定位问题根源、修复bug，甚至自己写回归测试用例

1. **状态延续与上下文整合**：稳定追踪已完成的工作、当前阶段和下一步核心动作

## 成本性价比

- 与Claude Opus 4.6手感相同，用量3倍，成本1/3

- Coding Plan用户免费使用

- OpenRouter上调用量开源断档第一

## 开发背景

wechat-cli项目等实际项目均由GLM-5.1赞助开发，展示了其在长程任务上的稳定性。

## 来源引用

- [摘要：从0开始，在国内用上Claude Code的终极保姆教程来了。](summaries/摘要：从0开始，在国内用上Claude Code的终极保姆教程来了。.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA%3D%3D&mid=2647681650&idx=1&sn=ebe9c3f89ede3094c532f47dcd495081&chksm=f1848a70eb0ed8813b80a31c693a43c481d2e6a4d5180ff577c22c46d4146fd3e97b57ec5be4#rd)）

- [摘要：我给Claude Code 增加了多模型切换功能](summaries/摘要：我给Claude Code 增加了多模型切换功能.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIxNjM4MTMzOA%3D%3D&mid=2247484908&idx=1&sn=47c8fe19d582ad3d2a855cd0357a9078&chksm=96149bde764c82c85d8d9dca7aa660ae3913126cf6047a256cae541d3b55e91dadc9820ea101#rd)）

- 摘要：智谱炸群了：GLM-5.1直接上线，开源第一换人（开发者阿橙，2026-04-08）

- 摘要：开源模型首超Opus4.6！智谱GLM-5.1登场，14小时后CUDA专家被冲了（量子位，2026-04-08）

- 摘要：我把微信cli开源了，群消息终于不用爬楼了！（苍何，2026-04-08）

- [原文链接](https://x.com/0xJeff/status/2043656911044870203)｜《3 Things I learnt after 3 weeks of using Hermes as a personal analyst》｜来源条目：[摘要：3 Things I learnt after 3 weeks of using Hermes as a personal analyst](summaries/摘要：3 Things I learnt after 3 weeks of using Hermes as a personal analyst.md)

- [原文链接](https://x.com/shmidtqq/status/2044027418541691041)｜《OpenClaw + GLM 5.1 = FREE AI AGENTS》｜来源条目：[摘要：OpenClaw + GLM 5.1 = FREE AI AGENTS](summaries/摘要：OpenClaw + GLM 5.1 = FREE AI AGENTS.md)

- [原文链接](https://x.com/Zai_org/status/2044741938604093443)｜《GLM-5.1 的 Tool Calling 循环死锁：一个 Chat Template 引发的「幽灵 Bug」》｜来源条目：[摘要：GLM-5.1 的 Tool Calling 循环死锁：一个 Chat Template 引发的「幽灵 Bug」](summaries/摘要：GLM-5.1 的 Tool Calling 循环死锁：一个 Chat Template 引发的「幽灵 Bug」.md)

- [摘要：各家Coding Plan为啥不兼容Claude WebSearch格式](summaries/摘要：各家Coding Plan为啥不兼容Claude WebSearch格式.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkyOTY1NzMzNg%3D%3D&mid=2247489376&idx=1&sn=722c4f2ba5f82432e7abff79079f8bef&chksm=c3cb3b3b7b865b2b1cf89b3ea79ebe2a03d32fb1e8749f2f334e444c518356d58f2af2b2561f#rd)）

- [摘要：quantization](summaries/摘要：quantization.md)（[原文](https://x.com/leftcurvedev_/status/2044700338817564814)）

- [摘要：Okay this one is insane. A new 18B frankenstein model was just released on @huggingface — Beats the new Qwen3.6-35B-A3B on a 44-test suite despite requiring 12GB VRAM instead of 24GB 🤯](summaries/摘要：Okay this one is insane. A new 18B frankenstein model was just released on @huggingface — Beats the new Qwen3.6-35B-A3B on a 44-test suite despite requiring 12GB VRAM instead of 24GB 🤯.md)（[原文](https://x.com/leftcurvedev_/status/2045449352827580602)）

- [摘要：NVIDIA 免费开放 80+ AI 模型 API，直接接入 OpenCode / Cursor / Hermes](summaries/摘要：NVIDIA 免费开放 80+ AI 模型 API，直接接入 OpenCode - Cursor - Hermes.md)（[原文](https://x.com/dhruvtwt_/status/2047006444701274380)）

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [OpenRouter](entities/OpenRouter.md)

- [MiniMax M2.7](entities/MiniMax M2.7.md)

- [OpenClaw](entities/OpenClaw.md)

- [Ollama](entities/Ollama.md)

- [Tool Calling](concepts/Tool Calling.md)

- [vLLM](entities/vLLM.md)

- [SGLang](entities/SGLang.md)

- [Chat Template](concepts/Chat Template.md)

- [Claude Code](entities/Claude Code.md)

- [Anthropic API](entities/Anthropic API.md)

- [WebSearch](concepts/WebSearch.md)

- [WebFetch](concepts/WebFetch.md)

- [Qwen3.5](entities/Qwen3.5.md)

- [Qwen3.5-9B-GLM5.1-Distill-v1](entities/Qwen3.5-9B-GLM5.1-Distill-v1.md)

- [模型蒸馏](concepts/模型蒸馏.md)

- [模型量化](concepts/模型量化.md)

- [GGUF](concepts/GGUF.md)

- [MLX 框架](entities/MLX 框架.md)

- [Qwopus-GLM-18B-Merged-GGUF](entities/Qwopus-GLM-18B-Merged-GGUF.md)

- [模型合并](concepts/模型合并.md)

- [Agentic Reasoning](concepts/Agentic Reasoning.md)
