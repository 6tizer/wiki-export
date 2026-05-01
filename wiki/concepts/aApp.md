---
title: aApp
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/71b09e59e2e24091ad8a1175c2f96bca
notion_id: 71b09e59-e2e2-4091-ad8a-1175c2f96bca
---

**定义**

aApp（Agentic App）是运行在 rOS 上的 Agent 原生应用形态，以 Agent 为第一服务对象而非人，能后台持续运行、通过事件触发响应，并直接访问用户的完整工作上下文。

**与传统 Skill/插件的核心区别**

| 维度 | 传统 Skill | aApp |

| --- | --- | --- |

| 运行方式 | 用完即走，上下文清零 | 后台持续运行，主动响应 |

| 上下文获取 | 用户手动投喂 | 直接访问完整数字记忆 |

| 交互方式 | Prompt 指令 | 自然语言配置 |

| 版权保护 | 几乎无，易盗版 | 内置鉴权，付费才能运行 |

| 界面 | 有 GUI | 无需复杂 GUI，只需语义接口 |

**设计原则**

- 围绕业务模型设计，避免写死固定工作流

- 把步骤调度权交给 Agent，保持灵活性

- 不追求"大而全"，专注垂直场景做到行业最好

- 开箱即用，自然语言完成个性化配置

**典型案例**

- 智能待办 aApp：实时监听邮件和会议录音，自动提取待办事项；识别需要回复附件的邮件时，自动找文件、写内容、完成发送

**开发者价值**

- 行业专家无需代码基础，通过 AI Coding 生成可运行的 aApp

- 内置商业化体系（付费下载），解决了 Skill 无法变现的痛点

- 平台统一结算 Token 成本，开发者零运营成本

**来源引用**

- [摘要：从知识库到 Agent 原生 OS，汪源想为 Agent 造一个操作系统](summaries/摘要：从知识库到 Agent 原生 OS，汪源想为 Agent 造一个操作系统.md)（极客公园，2026-04-02）
