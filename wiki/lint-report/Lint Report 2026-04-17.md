---
title: Lint Report 2026-04-17
type: lint-report
tags:
- 知识管理
status: 草稿
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/d55f9adb21cd49c6b0982874c2725dcf
notion_id: d55f9adb-21cd-49c6-b098-2874c2725dcf
---

## 检查日期

2026-04-17

---

## 总体健康度

🔴 **57 / 100**

> 主要问题：概念/实体 完全同名重复对（−20 分）+ 系统概念页 null 最后编译时间（−21 分）+ summary 近似重复积压（−2 分）。整体知识质量较好，草稿积压量大但均为新建（7 天内），无标签/状态异常。

---

## 全库统计

| 类型 | 草稿 | 审核中 | 已审核 | 需更新 | 合计 |

| --- | --- | --- | --- | --- | --- |

| concept | 1054 | 116 | 12 | 1 | **1183** |

| entity | 485 | 56 | 1 | 0 | **542** |

| summary | 0 | 0 | 968 | 0 | **968** |

| synthesis | 48 | 0 | 0 | 0 | **48** |

| qa | 1 | 0 | 4 | 0 | **5** |

| **合计** | **1588** | **172** | **985** | **1** | **2746** |

> **📊** **草稿积压提示**：concept 草稿 1054 条 + entity 草稿 485 条 = **1539 条**草稿，占总 concept/entity 的 89%。但所有草稿均在 7 天内创建（最早 2026-04-10 16:34 UTC），暂无过期草稿。synthesis 草稿 48 条无自动晋升规则，建议人工处理。

---

## 孤岛条目

> **⚠️** **Phase 1 初筛无法精确确定**：当前 summary 没有 relation 字段指向 concept/entity，且不允许动态 LIKE 拼接 SQL，无法通过纯 SQL 完成孤岛精确检测。已采用「标题关键词初筛 + 搜索二次验证」策略，但 1725 个 concept/entity 的全量验证需要进一步抽样搜索。

  **现状**：Phase 2 引用结构化检查（抽样 10 条）显示所有样本均有结构化 `<mention-page>` 引用，说明 Compiler 的引用写入基本正常。建议由 **Fixer** 在后续运行中通过 Notion search 逐批验证孤岛候选。

暂无已确认孤岛条目。

---

## 过期草稿

✅ **0 条**

当前时间 2026-04-17 22:01（北京时间），所有 concept/entity 草稿均在最近 7 天内创建（最早 2026-04-10 下午），尚未达到「创建超 7 天」阈值。

---

## 过时内容

**共 7 条** concept 页面的 `最后编译时间` 为 null（均为系统角色概念页，由人工维护，未经 Compiler 编译）：

1. [关于 Gap Agent](concepts/关于 Gap Agent.md) — 状态：需更新（已设置）

1. [关于 Wiki Lint Agent](concepts/关于 Wiki Lint Agent.md) — 状态：已审核，最后编译时间 null

1. [关于 Wiki Fixer](concepts/关于 Wiki Fixer.md) — 状态：已审核，最后编译时间 null

1. [关于 Wiki Compiler](concepts/关于 Wiki Compiler.md) — 状态：已审核，最后编译时间 null

1. [关于 Wiki QA Agent](concepts/关于 Wiki QA Agent.md) — 状态：已审核，最后编译时间 null

1. [关于 Wiki Synthesizer](concepts/关于 Wiki Synthesizer.md) — 状态：已审核，最后编译时间 null

1. [关于 Notion AI（Wiki 协调者）](concepts/关于 Notion AI（Wiki 协调者）.md) — 状态：已审核，最后编译时间 null

> **💡** 这 7 条均为 Agent 系统角色的概念条目，属人工维护，建议在 Wiki Schema 中为系统元概念增加「豁免时效性检查」规则，或统一在条目中注明维护方式，避免每次 Lint 报告重复标记。

---

## 重复疑似

### A. Concept / Entity 完全同名重复（2 对）

| 名称 | 页面 1 | 页面 2 | 处理建议 |

| --- | --- | --- | --- |

| Tree-sitter | Untitled | [Untitled](entities/Tree-sitter.md) | 加载两页，保留状态/内容更丰富者，合并后删除冗余页 |

| 爆炸半径分析 | [Untitled](concepts/爆炸半径分析.md) | Untitled | 加载两页，保留状态/内容更丰富者，合并后删除冗余页 |

### B. Concept / Entity 规范化后近似重复（1 对）

| 条目 A | 条目 B | 差异原因 | 处理建议 |

| --- | --- | --- | --- |

| [Untitled](entities/CME FedWatch.md)（entity） | [Untitled](entities/CME FedWatch Tool.md)（entity） | B 比 A 多"Tool"后缀（规则 B：产品后缀差异） | 确认是否为同一产品，如是则保留官方全名，合并内容后删除冗余页 |

---

### Summary 完全同名重复（2 组，A 类）

| 名称 | 重复页面 |

| --- | --- |

| 摘要：I Went Through Every AI Memory Tool I Could Find. There Are Two Camps. | Untitled · [Untitled](summaries/摘要：I Went Through Every AI Memory Tool I Could Find. There Are Two Camps.md) |

| 摘要：Learn more in the official documentation | [Untitled](summaries/摘要：Learn more in the official documentation.md) · Untitled |

### Summary 近似同名重复（约 18 组，B 类）

| 组别 | 代表条目 | 差异原因 |

| --- | --- | --- |

| Corporate Audit AI | [Untitled](summaries/摘要：Corporate Audit AI：用 AI Agent 扒上市公司年报，$AUDIT 市值冲破千万.md) · Untitled | 「扒」vs「扬」错字 + 「值」vs「値」繁简体 |

| Mac+oMLX+TurboQuant（4 变体） | Untitled · Untitled · [Untitled](summaries/摘要：Mac用户可以在oMLX中使用TurboQuant了，搭配Gemma-4-31B实测.md) · Untitled | 空格差异 + 内容略有扩展（谷歌全家桶） |

| OpenClaw 能接淘宝 | [Untitled](summaries/摘要：OpenClaw能接淘宝和腾讯会议了.md) · Untitled | 「淘宝」→「淡宝」错字 |

| Hermes Agent 实测 | [Untitled](summaries/摘要：Hermes Agent 实测，龙虾新对手是进化版爱马仕.md) · Untitled | 缺少「版」字 |

| 链上 AI Agent 全景图 | [Untitled](summaries/摘要：链上 AI Agent 全景图：2025 年最值得关注的资源整理.md) · Untitled | 「值」vs「値」繁简体 |

| OiiOii 正式上线 | [Untitled](summaries/摘要：OiiOii 正式上线！用 Seedance 2.0 做 AI 短剧的最优解法来了.md) · Untitled | 空格差异 |

| 对话 OiiOii 创始人（3 变体） | [Untitled](summaries/摘要：对话 OiiOii 创始人闹闹：做 AI 时代的皮克斯.md) · Untitled · Untitled | 「皁」vs「皮」错字 + 含/不含「光合说」后缀 |

| 谷歌语音 Agent | [Untitled](summaries/摘要：谷歌掀语音Agent新纪元！开口就是生产力.md) · Untitled | 「掀」vs「掼」错字 + 后缀差异 |

| 设计师天塌了 | [Untitled](summaries/摘要：设计师们的天塌了，谷歌 Stitch 太疯狂了.md) · Untitled | 「塌」vs「塔」错字 |

| Context Hub（3 变体） | Untitled · [Untitled](summaries/摘要：Context Hub：吴恩达为 AI 编程 Agent 打造的「Stack Overflow」.md) · [Untitled](summaries/摘要：Context Hub：吴恩达开源的 Coding Agent「文档新鲜度」解决方案.md) | 不同描述角度的同一源文章，Compiler 重复触发 |

| 实操指南+LLM+Wiki | Untitled · [Untitled](summaries/摘要：实操指南：如何用 Karpathy 的 LLM+Markdown+Wiki 搭建个人知识库.md) | 空格差异 |

| 给 AI 配张银行卡 | Untitled · [Untitled](summaries/摘要：给 AI 配张银行卡：Stripe 半年搭完的 Agent 支付全景.md) | 「銀」vs「银」繁简体 + 「搞」vs「搭」用词差异 |

| 我把微信 cli 开源了 | [Untitled](summaries/摘要：我把微信 cli 开源了，群消息终于不用爬楼了.md) · Untitled | 句末感叹号差异 |

| GLM-5.1 直接上线 | [Untitled](summaries/摘要：智谱炸群了：GLM-5.1 直接上线，开源第一换人.md) · Untitled | 空格差异 |

| Karpathy 又双叒叕 | [Untitled](summaries/摘要：Karpathy 又双叒叕发新概念了，这次我替你找到了那个产品.md) · Untitled | 空格差异 |

| 太抽象了 Alice（4 变体） | Untitled · Untitled · [Untitled](summaries/摘要：太抽象了，Alice 都来了。MemPalace AI记忆系统.md) · Untitled | 标题长短/标点差异，同一源文章 4 次编译 |

| 终于明白为什么 Skill 不好用了 | [Untitled](summaries/摘要：终于明白为什么 Skill 不好用了.md) · Untitled | 句末句号差异 |

| 开源模型首超 Opus4.6 | Untitled · [Untitled](summaries/摘要：开源模型首超Opus4.6！智谱GLM-5.1登场，14小时后CUDA专家被冲了.md) | 缺少「后」字 |

| 闲鱼 OpenClaw | [Untitled](summaries/摘要：闲鱼，更适合中国宝宝的 OpenClaw.md) · Untitled | 空格差异 |

> **📌** Summary 近似重复约 20 组，主要原因：① Compiler 在同一源文章上多次触发；② 标题中的中文繁简体字符差异；③ 句末标点或空格差异。建议 Compiler 增加去重逻辑（基于标题归一化）。

---

## 状态异常

✅ **0 条**：所有非 index/lint-report 类型条目均已设置状态，无空状态异常。

---

## 标签异常

✅ **0 条**：所有 concept/entity 条目均有至少 1 个标签，无废弃标签（AI Agent / MCP / Notion）使用情况。

---

## 标签分布统计

> 注：以下统计为 SQL 按完整标签组合分组，单标签列为该组合的纯单标签条目数，不含多标签组合中的该标签出现次数。实际每个标签的覆盖范围更广。

| 标签（纯单标签组合） | concept+entity 条目数 | 备注 |

| --- | --- | --- |

| LLM | 97 | 最大单标签组，注意 LLM 概念与模型产品实体区分 |

| Agent 编排 | 90 | 第二大类，与 Agent 框架/工作流有重叠风险 |

| Coding Agent | 83 | 健康，与开发工具边界已较清晰 |

| Crypto/DeFi | 71 | 正常 |

| 开发工具 | 61 | 注意与 Agent 技能/Coding Agent 的边界 |

| 商业/生态 | 53 | 正常 |

| 记忆系统 | 46 | 正常 |

| Agent 技能 | 45 | 正常 |

| 知识管理 | 38 | 正常 |

| 内容创作 | 35 | 正常 |

| 安全/隐私 | 27 | 正常 |

| Agent 框架 | 21 | 正常 |

| OpenClaw | 20 | 正常 |

| 工作流 | 0（纯） | 工作流仅出现在多标签组合中，无纯工作流条目 |

---

## 类型启发式筛查结果

以下 concept 条目经推理层规则筛查，疑似应归类为 entity。**不自动判定，标注「建议人工确认」**。

| 条目 | 命中规则 | 说明 |

| --- | --- | --- |

| [Untitled](concepts/SearxNG.md)（concept） | 规则 C：英文专有名词 | 具体开源搜索引擎工具，有代码仓库和版本迭代 |

| [Untitled](concepts/pgvector.md)（concept） | 规则 C：英文专有名词 | PostgreSQL 向量扩展，具体软件组件 |

| [Untitled](concepts/LanceDB.md)（concept） | 规则 B/C：产品后缀 + 专有名词 | 具体向量数据库产品，有官网和版本 |

| [Untitled](concepts/Agent Reach.md)（concept） | 规则 C：英文专有名词 | 具体开源工具项目名，有 GitHub 仓库 |

| [Untitled](entities/Agent Service Toolkit.md)（concept） | 规则 B：Toolkit 产品后缀 | LangGraph + FastAPI 的具体工具包，有 GitHub 仓库 |

| [Untitled](concepts/OpenSpec.md)（concept） | 规则 C：英文专有名词 | 具体编程规范工具，与 BMAD/Spec Kit 不同 |

| [Untitled](concepts/Spec Kit.md)（concept） | 规则 B：Kit 产品后缀 | 具体工具套件名称 |

| [Untitled](entities/Tool Calling 2.0.md)（concept） | 规则 A：含版本号 | Anthropic 发布的特定版本能力，但也可能视为概念迭代，边界模糊 |

---

## 标签分类合理性检查

**Phase 2 抽样结论**：抽查 10 个 草稿 concept/entity 页面，标签分类整体合理，未发现明显误分类。以下为边界模糊案例：

| 条目 | 当前标签 | 问题描述 | 建议 |

| --- | --- | --- | --- |

| [Untitled](concepts/Agent Reach.md) | 开发工具 | Agent Reach 是专为 AI Agent 联网而设计的技能工具，更贴近「Agent 技能」而非通用基础设施 | 建议改为 Agent 技能 |

其余抽查条目标签分类正常：

- SearxNG → Agent 技能 ✓（作为搜索接口为 Agent 服务）

- LM Studio / Ollama → 开发工具 ✓（本地部署工具）

- Claude Code / Codex / Trae → Coding Agent ✓

---

## 引用结构化检查

**抽样范围**：从草稿 concept/entity 中随机抽取 10 个页面（GDPVal、Fallback 模型、Agent 静默失败、Plugin Marketplace、Playwright Skill、Apify Agent Skills、Tool Calling 2.0、MANIFEST 分层管理、Playbook 驱动策略、模型蒸馏）

| 检查项 | 结果 |

| --- | --- |

| 抽样数量 | 10 个页面 |

| 有结构化 `<mention-page>` 引用 | 10 / 10（100%） |

| 纯文本引用（无 mention-page） | 0 / 10（0%） |

| 混合引用（mention-page + 原文 URL 文本） | 5 / 10（部分页面在 mention-page 之外还附原始链接文本，属可接受格式） |

✅ **引用结构化健康**：所有抽样页面均包含至少 1 条 `<mention-page>` 结构化引用，Compiler 写入逻辑正常运作。无需批量修复。

---

## 计分明细

| 检查项 | 发现 | 扣分 |

| --- | --- | --- |

| 孤岛条目 | 0 条已确认（待深度验证） | 0 |

| 过期草稿（>7 天） | 0 条 | 0 |

| 过时内容（null/> 30 天最后编译时间） | 7 条（系统 Agent 概念页，null 最后编译时间） | −21 |

| concept/entity 完全同名重复对 | 2 对（Tree-sitter × 2，爆炸半径分析 × 2） | −20 |

| concept/entity 近似重复对 | 1 对（CME FedWatch vs Tool，待确认） | 0（未确认） |

| summary 重复组（每 10 组 −1） | 约 20 组（2 完全同名 + 18 近似） | −2 |

| 状态异常 | 0 条 | 0 |

| 标签异常（空标签） | 0 条 | 0 |

| 废弃标签使用 | 0 条 | 0 |

| 类型误分类（每 3 个已确认 −3） | 8 个疑似（未确认，不扣分） | 0 |

| 纯文本引用（每 5 个 −1） | 0 个（抽样 10 页，100% 结构化） | 0 |

| **合计** |  | **−43** |

**最终得分：100 − 43 = 🔴 57 / 100**

---

## 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 |

| --- | --- | --- | --- |

| [Untitled](concepts/关于 Wiki Lint Agent.md) | 已审核 | 需更新 | 最后编译时间为 null，且内容已多次更新，建议重新编译或豁免 |

| [Untitled](concepts/关于 Wiki Fixer.md) | 已审核 | 需更新 | 同上 |

| [Untitled](concepts/关于 Wiki Compiler.md) | 已审核 | 需更新 | 同上 |

| [Untitled](concepts/关于 Wiki QA Agent.md) | 已审核 | 需更新 | 同上 |

| [Untitled](concepts/关于 Wiki Synthesizer.md) | 已审核 | 需更新 | 同上 |

| [Untitled](concepts/关于 Notion AI（Wiki 协调者）.md) | 已审核 | 需更新 | 同上 |

> **ℹ️** **说明**：

  - **草稿 → 审核中**（≥7 天且内容完整）：当前所有草稿均在 7 天内创建，0 条符合晋升条件。

  - **草稿/审核中 → 已审核**（≥2 summary 引用）：需加载各条目正文验证引用数，已超出本次 Phase 2 抽样范围，建议 Fixer 在下轮运行中逐批验证。

  - **summary 全部已审核**：无需操作。

  - **synthesis 草稿 48 条**：无自动晋升规则，建议人工处理。

---

## 改进建议

### 🤖 自动修复项（Fixer 可直接执行）

1. **合并完全同名 concept/entity 重复对**（修复类型：同名合并）

  - 目标：Tree-sitter + [Tree-sitter](entities/Tree-sitter.md) → 加载两页，保留状态更高/内容更丰富者，删除冗余页

  - 目标：[爆炸半径分析](concepts/爆炸半径分析.md) + 爆炸半径分析 → 同上

1. **合并完全同名 summary 重复组**（修复类型：同名合并）

  - 目标：摘要：I Went Through Every AI Memory Tool I Could Find. There Are Two Camps. + [摘要：I Went Through Every AI Memory Tool I Could Find. There Are Two Camps.](summaries/摘要：I Went Through Every AI Memory Tool I Could Find. There Are Two Camps.md) → 保留内容更完整者，删除另一页

  - 目标：[摘要：Learn more in the official documentation](summaries/摘要：Learn more in the official documentation.md) + 摘要：Learn more in the official documentation → 同上

1. **合并近似重复 summary**（修复类型：近似合并，约 18 组）

  - 按上方「Summary 近似同名重复」表格所列各组，每组保留内容更完整/创建时间更早的版本，删除冗余页。注意修复其他页面中指向删除页的引用。

1. **Agent Reach 标签修正**（修复类型：标签修正）

  - 目标：[Agent Reach](concepts/Agent Reach.md) 当前标签「开发工具」→ 改为「Agent 技能」

### 👤 人工介入项（需人类确认）

1. **孤岛检测深度验证**：当前 SQL 无法全量确认孤岛条目，建议通过 Notion search 对若干低知名度 concept/entity 名称做二次验证（每次 Lint 运行后由 Fixer 抽样验证 30 条）

1. **系统概念页 null 最后编译时间 豁免规则**：Wiki Lint Agent、Wiki Fixer、Wiki Compiler、Wiki QA Agent、Wiki Synthesizer、Notion AI（Wiki 协调者）等 6 条系统角色概念页无最后编译时间，建议在 Wiki Schema 中增加「系统元概念豁免」规则，或改为「index」类型以便 Lint 跳过

1. **CME FedWatch 重复确认**：[CME FedWatch](entities/CME FedWatch.md) 和 [CME FedWatch Tool](entities/CME FedWatch Tool.md) 是否为同一产品，如是则合并；如是不同版本/功能请保留两者

1. **类型启发式筛查确认**：以下 8 个 concept 疑似应为 entity，需人工逐一确认后由 Fixer 执行类型迁移：SearxNG、pgvector、LanceDB、Agent Reach、Agent Service Toolkit、OpenSpec、Spec Kit、Tool Calling 2.0

1. **草稿积压处理策略**：1539 条草稿（concept+entity），均为近 7 天新建。建议制定批量晋升策略（例如：由 Fixer 每日抽样 50 条，验证引用数后批量晋升）

1. **synthesis 草稿积压**：48 条 synthesis 均为草稿，无自动晋升规则。建议 Synthesizer 或 Notion AI 协调者统一审阅处理

1. **Compiler 去重逻辑**：summary 出现约 20 组近似重复，主要原因是 Compiler 在同一源文章上多次触发，建议 Compiler 在写入前对标题归一化去重（lowercase + 去标点 + 比较前 N 字符）

---

>  请根据以上报告执行自动修复。
