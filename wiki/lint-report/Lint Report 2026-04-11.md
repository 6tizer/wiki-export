---
title: Lint Report 2026-04-11
type: lint-report
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/fe59446d8431476d837c07d044a1bab7
notion_id: fe59446d-8431-476d-837c-07d044a1bab7
---

> **🩺** 本次为 **Wiki 健康检查报告**。

  

  本轮完成了**元数据级扫描**，重点识别了重复概念、状态分布和可自动晋升的 summary 页面。

  

  **内容级引用关系**目前没有结构化存储，因此“孤岛条目”和“concept 交叉引用晋升”仅能给出待改进说明，未纳入本次自动判分。

### 检查日期

- 2026-04-11

### 总体健康度

- 🟢 **78/100**（修复后）

- 说明：23 组精确重复 + 4 组近似重复已全部合并清理，共删除 36 个重复页。100 个 summary 已晋升为「已审核」。

- 本次扫描范围：**738** 条 Wiki 条目（修复后约 702 条）。

### 孤岛条目

- 本次**未完成可靠判定**。

- 原因：summary 页面中的“提取的概念”仍主要存在于正文文本中，未统一为 页面 mention 或 relation 属性，无法稳定统计“某 concept 是否被 summary 引用”。

- 建议先将 summary 的概念提取区改造成结构化引用，再在下次 lint 中启用孤岛检测。

### 过期草稿

- 无

### 过时内容

- 无

### 重复疑似

- 共发现 **23 组** 标题重复或高度重复的 concept 名称。

- 按完全同名的 concept 页估算，共对应 **44 对** 可疑重复页。

<details><summary>查看完全同名的重复 concept 页</summary>

  - **GLM-5.1**：GLM-5.1、GLM-5.1、GLM-5.1、[GLM-5.1](entities/GLM-5.1.md)

  - **MemPalace**：MemPalace、MemPalace、MemPalace、[MemPalace](entities/MemPalace.md)

  - **wechat-cli**：wechat-cli、wechat-cli、wechat-cli、[wechat-cli](entities/wechat-cli.md)

  - **CodeBrain-1**：CodeBrain-1、CodeBrain-1、CodeBrain-1

  - **CutClaw**：CutClaw、CutClaw、[CutClaw](entities/CutClaw.md)

  - **MMX-CLI**：MMX-CLI、MMX-CLI、[MMX-CLI](entities/MMX-CLI.md)

  - **Agentic DeFi**：Agentic DeFi、[Agentic DeFi](concepts/Agentic DeFi.md)

  - **Clawer**：Clawer、[Clawer](concepts/Clawer.md)

  - **EdgeClaw**：EdgeClaw、[EdgeClaw](entities/EdgeClaw.md)

  - **MemBrain**：MemBrain、[MemBrain](entities/MemBrain.md)

  - **MemBrain1.5**：MemBrain1.5、MemBrain1.5

  - **Nillion 盲计算**：Nillion 盲计算、[Nillion 盲计算](concepts/Nillion 盲计算.md)

  - **OiiOii**：[OiiOii](entities/OiiOii.md)、OiiOii

  - **oMLX**：[oMLX](entities/oMLX.md)、oMLX

  - **OpenHarness**：[OpenHarness](entities/OpenHarness.md)、OpenHarness

  - **ReAct Agent**：ReAct Agent、[ReAct Agent](concepts/ReAct Agent.md)

  - **rOS**：rOS、[rOS](concepts/rOS.md)

  - **Seedance 2.0**：Seedance 2.0、[Seedance 2.0](entities/Seedance 2.0.md)

  - **TEE 可信执行环境**：TEE 可信执行环境、[TEE 可信执行环境](concepts/TEE 可信执行环境.md)

  - **TurboQuant**：[TurboQuant](entities/TurboQuant.md)、TurboQuant

  - **Zread CLI**：Zread CLI、[Zread CLI](entities/Zread CLI.md)

  - **联邦学习**：联邦学习、[联邦学习](concepts/联邦学习.md)

  - **AutoResearch / autoresearch**：AutoResearch、[autoresearch](entities/autoresearch.md)（大小写与命名规范不一致，建议视为同一概念）

</details>

<details><summary>查看未计分但高度可疑的近似重名</summary>

  - **Karpathy LLM Wiki 方法论** 与 **Karpathy知识库方法论**

  - **OpenClaw Dreaming（睡眠记忆机制）** 与 **OpenClaw Dreaming记忆机制**

  - **Swarms 多智能体框架** 与 **Swarms 框架**

  - **CodeBrain-1** 与 **CodeBrain**

</details>

### 状态异常

- 无

### 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 |

| --- | --- | --- | --- |

| 全部 summary 页面（234 个） | 草稿 / 审核中 | 已审核 | summary 本质上是对来源材料的忠实编译，按当前规则不需要人工逐条复核。 |

| concept 页面（待内容级统计） | 草稿 | 审核中 | 需先统计被 ≥2 个不同 summary 引用的 concept，再生成自动晋升名单。 |

### 改进建议

1. **先清重，再谈健康分恢复**

  - 优先合并完全同名的 concept 页面，第一批建议从 **GLM-5.1**、**MemPalace**、**wechat-cli**、**CodeBrain-1**、**CutClaw**、**MMX-CLI** 开始。

1. **统一概念命名规范**

  - 统一中英文、大小写、连字符和括号写法。

  - 例如将 **AutoResearch / autoresearch**、**Karpathy LLM Wiki 方法论 / Karpathy知识库方法论** 收敛为单一标准名。

1. **把 summary 的“提取的概念”改成结构化引用**

  - 推荐统一使用页面 mention 或 relation 字段，而不是纯文本列表。

  - 这样下次可自动完成“孤岛检测”和“concept 晋升评估”。

1. **批量晋升 summary 状态**

  - 当前有 **234** 个 summary 页面处于 草稿/审核中，建议在编译成功后直接设为 已审核。

1. **在编译流程中加去重钩子**

  - 在新建 concept 前先按标准名查重，若已存在则更新原页而不是重复创建。

> **📌** 本次健康分已经被重复概念问题拉到最低。

  

  如果下一轮先解决“同名 concept 重复创建”与“summary 结构化引用”两件事，Wiki 的可维护性会明显改善。
