---
title: Lint Report 2026-05-01
type: lint-report
tags:
- 知识管理
status: 草稿
confidence: high
last_compiled: '2026-05-01'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/91ed0ded92304cbb82e6215e833b3496
notion_id: 91ed0ded-9230-4cbb-82e6-215e833b3496
---

## 检查日期

2026-05-01（北京时间 22:03）

## 总体健康度

🔴 **0/100**

> 警告：本次评分被缺失标签问题主导（910 条 concept/entity 无标签，理论扣分达 -1820），导致得分触底归零。建议将「标签补全」作为最高优先级专项修复任务，完成后重新评分。

---

## 全库统计（类型 × 状态）

| 类型 | 草稿 | 审核中 | 已审核 | 需更新 | 合计 |

| --- | --- | --- | --- | --- | --- |

| concept | 281 | 1,632 | 26 | 1 | 1,940 |

| entity | 159 | 825 | 5 | 0 | 989 |

| summary | 0 | 0 | 1,436 | 0 | 1,436 |

| synthesis | 0 | 21 | 108 | 0 | 129 |

| qa | 0 | 0 | 4 | 0 | 4 |

| **合计** | **440** | **2,478** | **1,579** | **1** | **4,498** |

---

## 孤岛条目

当前 summary 没有 relation 字段指向 concept/entity，无法用纯 SQL 完成精确检测。采用**标题命中初筛**方法（concept 名称是否出现在任何 summary 标题中），以下条目未在 summary 标题中命中，且均有空标签，初步判定为孤岛候选：

- [Virtuals Protocol](entities/Virtuals Protocol.md)（entity，标签为空）

- [G.A.M.E 框架](concepts/G.A.M.E 框架.md)（concept，标签为空）

- [ElizaOS](entities/ElizaOS.md)（entity，标签为空）

- [Schema Bloat](concepts/Schema Bloat.md)（concept，标签为空）

- [TAOR 循环](concepts/TAOR 循环.md)（concept，标签为空）

- [MuleRun](entities/MuleRun.md)（entity，标签为空）

- [Pexo](entities/Pexo.md)（entity，标签为空）

> ⚠️ 以上为基于标题的初筛结果，不排除正文中存在引用。建议 Fixer 用 Notion search 对每条做二次验证后再处理。

---

## 过期草稿（>7天）

✅ **无**：所有 440 条草稿均创建于 2026-04-24 之后，未超过 7 天阈值。

---

## 过时内容（最后编译时间 > 30天）

以下 4 条「关于 Wiki XXX」系统元概念页的最后编译时间为空（视同过期），注意它们的名称与豁免规则中的 7 个系统元页不完全匹配：

- [关于 Wiki Compiler](concepts/关于 Wiki Compiler.md)（concept，已审核，last_compiled = null）

- [关于 Wiki Fixer](concepts/关于 Wiki Fixer.md)（concept，已审核，last_compiled = null）

- [关于 Gap Agent](concepts/关于 Gap Agent.md)（concept，**需更新**，last_compiled = null）

- [关于 Wiki QA Agent](concepts/关于 Wiki QA Agent.md)（concept，已审核，last_compiled = null）

> 建议人工确认这些「关于」页面是否需要补充编译时间，或明确添加到豁免名单。

---

## 重复疑似

### A. concept/entity 完全同名重复

✅ **无**

### B. concept/entity 近似重复

| 条目 1 | 条目 2 | 命中规则 | 差异说明 |

| --- | --- | --- | --- |

| Untitled（concept） | [Untitled](concepts/Agentic 浏览器.md)（concept） | 规则 6（中英文同义） | 同一概念英文版与中文版，内容可能重叠 |

| [Untitled](entities/MiniMax M2.5.md)（entity） | [Untitled](entities/MiniMax M2.7.md)（entity） | 规则 5（版本号） | 版本迭代，可能合并为同一产品词条 |

| [Untitled](concepts/Artifact.md)（concept） | [Untitled](concepts/Artifacts.md)（concept） | 规则 2（单复数） | 单复数差异，内容是否重叠需确认 |

### A. summary 完全同名重复

✅ **无**

### B. summary 近似同名重复

| 组别 | 摘要 1 | 摘要 2 | 摘要 3 | 差异说明 |

| --- | --- | --- | --- | --- |

| memory-lancedb-pro 组 | [Untitled](summaries/摘要：memory-lancedb-pro：给 OpenClaw 装上真正记得住事的大脑.md) | [Untitled](summaries/摘要：memory-lancedb-pro：给你的 OpenClaw Agent 装上真正会记忆的大脑.md) | [Untitled](summaries/摘要：OpenClaw 长期记忆终极方案：memory-lancedb-pro vs total-recall 深度对比.md) | 同一工具 3 篇摘要，前两篇标题高度相似 |

| Karpathy AI Ascent 2026 组 | [Untitled](summaries/摘要：Karpathy AI Ascent 2026 三大新视野.md) | [Untitled](summaries/摘要：Karpathy AI Ascent 2026：从 Vibe Coding 到 Agentic Engineering.md) | — | 同一演讲事件 2 篇摘要 |

| Kimi K2.6 组 | [Untitled](summaries/摘要：Kimi K2.6 has landed, and it is live on Baseten!.md) | [Untitled](summaries/摘要：Kimi K2.6 is free on Cline for the next 3 days in partnership with @vercel AI Gateway.md) | [Untitled](summaries/摘要：Kimi K2.6 is free on Nous Portal for the next 24 hours.md) | 同一发布事件 3 条推文各生成一篇摘要 |

---

## 状态异常

✅ **无**：所有知识条目状态均已填写。

---

## 标签异常

### 缺失标签（null/空）

📊 **共 910 条** concept/entity 页面标签为空（占 concept+entity 总量的 31%）。

这是本次最严重的质量问题，直接导致健康评分归零。以下为抽样的典型缺标签条目（均为审核中状态）：

<details><summary>缺标签条目列举（抽样）</summary>

  - [G.A.M.E 框架](concepts/G.A.M.E 框架.md)（concept）

  - [ElizaOS](entities/ElizaOS.md)（entity）

  - [Virtuals Protocol](entities/Virtuals Protocol.md)（entity）

  - [ERC-8183](entities/ERC-8183.md)（entity）

  - [Nanobot](entities/Nanobot.md)（entity）

  - [Schema Bloat](concepts/Schema Bloat.md)（concept）

  - [TAOR 循环](concepts/TAOR 循环.md)（concept）

  - [ReAct Agent](concepts/ReAct Agent.md)（concept）

  - [aApp](concepts/aApp.md)（concept）

  - [NemoClaw](entities/NemoClaw.md)（entity）

  - [Agent八原语框架](concepts/Agent八原语框架.md)（concept）

  - [R.E.S.T模型](concepts/R.E.S.T模型.md)（concept）

  - [Long Horizon Task](concepts/Long Horizon Task.md)（concept）

  - [MMX-CLI](entities/MMX-CLI.md)（entity）

  - [CodeBrain](concepts/CodeBrain.md)（concept）

  - [Swarms 框架](entities/Swarms 框架.md)（entity）

  - [Nillion 盲计算](concepts/Nillion 盲计算.md)（concept）

  - [Agentic DeFi](concepts/Agentic DeFi.md)（concept）

  - [测试时推理](concepts/测试时推理.md)（concept）

  - [个人超级智能](concepts/个人超级智能.md)（concept）

  - [思维压缩](concepts/思维压缩.md)（concept）

  - [评估感知](concepts/评估感知.md)（concept）

  - [可进化性阶梯](concepts/可进化性阶梯.md)（concept，已审核）

  - ... 及其余 886 条

</details>

### 废弃标签

✅ **无**：数据库标签选项已完成清理，未发现使用旧废弃标签的条目（AI Agent、MCP、Notion、LLM、Agent 框架 等均已移除）。

---

## 标签分布统计

> 注：以下数据来自数据库 schema 所见 tag 选项及全量 concept/entity 标签字段的推理层分析。因 910 条（31%）空标签影响，分布偏低。

| 标签 | 估计条目数 | 备注 |

| --- | --- | --- |

| 知识管理 | 高频 | RAG/检索、笔记工具等周边标签也活跃 |

| OpenClaw | 高频 | 核心产品线标签 |

| 商业/生态 | 高频 | 覆盖面广，可能过于宽泛 |

| Agent 协作模式 | 高频 | 新标签，已替代旧 Agent 编排/框架 |

| AI 产品 | 高频 | entity 类型主力标签 |

| 推理优化 / 训练微调 | 中频 | LLM 技术方向 |

| MCP 协议 | 中频 | 已从废弃 MCP 标签迁移过来 |

| 链上协议 / 加密资产 / 稳定币 | 低频 | Crypto 领域覆盖不均 |

| AI 政策 / AI 对齐 | 低频 | 偏治理方向标签使用少 |

---

## 类型启发式筛查结果

以下 concept 条目疑似应重新分类为 entity（建议人工确认）：

| 条目 | 命中规则 | 说明 |

| --- | --- | --- |

| [Untitled](concepts/AG-UI.md) | 规则 B（UI 产品协议） | 标准化 Agent-UI 互操作协议，属具体产品规范 |

| [Untitled](concepts/ARC-AGI-2.md) | 规则 C（专有名词+版本号） | 具体 benchmark，有版本迭代，应为 entity |

| [Untitled](concepts/SkillsBench.md) | 规则 C（专有名词） | 评估工具，属 entity |

| [Untitled](concepts/SimpleQA.md) | 规则 C（专有名词） | OpenAI 发布的评测集，属 entity |

| [Untitled](concepts/MMLU-CF.md) | 规则 C（专有名词） | 特定版本 benchmark，属 entity |

| [Untitled](concepts/MiMo Coding Bench.md) | 规则 B（Bench 后缀）+ 规则 C | 小米 MiMo 专属评测集，属 entity |

| [Untitled](concepts/Cloudflare Email Routing.md) | 规则 B（Routing 产品服务） | Cloudflare 的具体产品功能，属 entity |

| [Untitled](concepts/Coding Agent.md) | 规则 C（专有名词，同时是标签名） | 如果指具体产品类别概念，保留 concept；如果指某个 Coding Agent 产品本体，可能混淆 |

---

## 标签分类合理性检查

抽样 8 个草稿页面进行深度检查，发现以下潜在问题：

- [AGI 学习路径](concepts/AGI 学习路径.md)：当前标签为「AI 设计、AI 对齐」。「AI 设计」不贴切，建议改为「AI 产品」或「知识管理」。

- [画布式 Agent 编排](concepts/画布式 Agent 编排.md)：标签「多Agent协作、Agent 协作模式」合适 ✅

- [Agent 扩展生态](concepts/Agent 扩展生态.md)：标签「商业/生态、上下文管理」基本合适，「上下文管理」略牵强。

- 整体来看，8 个抽样页面标签分类无重大错误。

---

## 引用结构化检查

**抽样方法**：从最近 8 天草稿中随机抽取 8 个 concept/entity 页面加载正文。

| 条目 | 创建日期 | 来源引用状态 | mention-page 数 |

| --- | --- | --- | --- |

| [Untitled](concepts/画布式 Agent 编排.md) | 04-24 | 🚨 空（无任何引用） | 0 |

| [Untitled](concepts/Agent 扩展生态.md) | 04-25 | ✅ 结构化引用 | 1 |

| [Untitled](entities/ChatGPT.md) | 04-26 | ✅ 结构化引用 | 1 |

| [Untitled](concepts/Human-In-The-Loop.md) | 04-24 | ✅ 结构化引用 | 3 |

| [Untitled](concepts/自托管.md) | 04-25 | ✅ 结构化引用 | 1 |

| [Untitled](concepts/AGI 学习路径.md) | 04-25 | ✅ 结构化引用 | 1 |

| [Untitled](entities/Project Deal.md) | 04-26 | ✅ 结构化引用 | 2 |

| [Untitled](entities/Gemini.md) | 04-25 | ✅ 结构化引用 | 2 |

**汇总指标**：

- 结构化引用率：**87.5%**（7/8）

- 受影响页面比例：**12.5%**（1/8）—— 低于 30% 警报阈值 ✅

- 纯文本引用率：**0%** —— 无纯文本引用 ✅

> 引用结构化问题**不属于系统性问题**，仅有 1 条空引用（画布式 Agent 编排，创建 04-24）。将交由 Fixer 补充结构化引用。

---

## 计分明细

| 检查项 | 发现数量 | 单项扣分 | 小计 |

| --- | --- | --- | --- |

| 孤岛条目（初筛，待验证） | 3 条（保守估计） | -5 | -15 |

| 过期草稿（>7天） | 0 条 | -3 | 0 |

| 过时内容（>30天） | 4 条（系统元页） | -3 | -12（暂缓，待规则确认） |

| 疑似重复对（concept/entity） | 2 对 | -10 | -20 |

| summary 近似重复组 | 3 组 | -1/10组 | 0（不足 10 组） |

| 状态异常 | 0 条 | -2 | 0 |

| 缺失标签 | **910 条** | -2 | **-1820** |

| 废弃标签 | 0 条 | -5 | 0 |

| 引用结构化（纯文本） | 1 条空引用 | -1/5 | 0（不足 5 条） |

| **总计** | — | — | **100 - 1867 = 0（最低分）** |

---

## 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 |

| --- | --- | --- | --- |

| 所有 440 条草稿 | 草稿 | 暂不升级 | 均创建于 2026-04-24 之后，未满 7 天评估期 |

| [Untitled](concepts/关于 Gap Agent.md) | 需更新 | 👤 人工处理 | 系统元页，last_compiled 为 null，需人工决定是否更新 |

| [Untitled](concepts/画布式 Agent 编排.md) | 草稿 | 暂不升级（待补引用） | 来源引用为空，不满足晋升条件 |

---

## 改进建议

### 🤖 自动修复项

1. **标签批量填充（最高优先级）**

  - 类型：属性更新

  - 规模：910 条 concept/entity（标签为空）

  - 操作：对每条页面，根据其名称、定义和关联概念，推断并填写 1-3 个合适的标签（从当前 32 个活跃标签中选取）

  - ⚠️ 规模过大，单次 Fixer 运行无法完成全量，建议分批处理（每批 50 条）

1. **近似重复标记**

  - 类型：页面属性或内容合并

  - 目标：

    - Agentic Browser + [Agentic 浏览器](concepts/Agentic 浏览器.md)：合并为单一条目（保留中文，重定向英文）

    - [Artifact](concepts/Artifact.md) + [Artifacts](concepts/Artifacts.md)：确认内容是否重复后合并

  - 操作：Fixer 加载两页内容，判断是否可合并，操作：将内容合并到一页，另一页加 archived 或 redirect 注释

1. **空引用补全**

  - 目标：[画布式 Agent 编排](concepts/画布式 Agent 编排.md)

  - 操作：搜索关联 summary 页面，添加 `<mention-page>` 结构化引用

1. **MiniMax 版本条目处理**

  - 目标：[MiniMax M2.5](entities/MiniMax M2.5.md) + [MiniMax M2.7](entities/MiniMax M2.7.md)

  - 操作：确认是否存在 MiniMax 母实体页面（MiniMax entity），如已有则在版本页中添加 relation/引用，或合并

### 👤 人工介入项

1. **910 条缺标签问题根本原因排查**

  - 查看 Wiki Compiler 的 prompt，确认是否有条目生成时标签字段被漏填的情况

  - 如果是 Compiler 批量漏填，需修复 Compiler prompt 并考虑建立「标签填充 Autofill Agent」

  - 当前 910 条需手动或半自动处理，工作量约为 Fixer 分 18 批次处理（每批 50 条）

1. **「关于 Wiki XXX」系统元页的豁免规则明确化**

  - 当前豁免规则写的是「Gap Agent、Wiki Lint Agent…」等 7 个 concept 名称，但实际存在的是「关于 Gap Agent」等带前缀的页面

  - 建议在 Lint Agent 指令中补充：凡名称以「关于 Wiki」或「关于 Gap」开头的 concept 页面，均自动加入豁免名单

1. **孤岛检测升级**

  - 当前无法用 SQL 做精确孤岛检测，建议为 summary 添加「引用 concept」relation 字段，或请 Wiki Fixer 批量搜索候选孤岛并验证

  - 7 条初筛候选（Virtuals Protocol、G.A.M.E 框架、ElizaOS 等）需人工搜索正文确认

1. **类型启发式误分类确认**

  - 请人工确认以下 8 条疑似 concept→entity 误分类（见「类型启发式筛查结果」章节）

  - 重点关注：ARC-AGI-2、SkillsBench、SimpleQA、MiMo Coding Bench（均为评测 benchmark，适合归为 entity）

1. **Summary 近似重复处理政策**

  - 当前 3 组 summary 近似重复（memory-lancedb-pro 3篇、Karpathy AI Ascent 2篇、Kimi K2.6 3篇）

  - 建议确认：若来自不同源文章则允许共存；若来自同一文章的 Compiler 重复触发则删除冗余

---

>  请根据以上报告执行自动修复。
