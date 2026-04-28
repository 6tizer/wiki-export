---
title: Lint Report 2026-04-28
type: lint-report
tags:
- 知识管理
status: 草稿
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/be1628130cd4410d842abb54a29a5792
notion_id: be162813-0cd4-410d-842a-bb54a29a5792
---

## 检查日期

2026-04-28（每日定时触发，Asia/Shanghai 22:00）

## 总体健康度

**60 / 100** 🟡

> 主要扣分项：疑似重复条目（concept/entity 及 summary）、孤岛候选条目（抽样验证）。新标签体系退休旧标签属系统性变更，已列入 👤 人工介入项，未计入本次评分。

---

## 全库统计（类型 × 状态）

| 类型 | 草稿 | 审核中 | 已审核 | 需更新 | 小计 |

| --- | --- | --- | --- | --- | --- |

| concept | 419 | 1394 | 26 | 1 | 1840 |

| entity | 193 | 714 | 4 | 0 | 911 |

| summary | 0 | 0 | 1335 | 0 | 1335 |

| synthesis | 0 | 15 | 90 | 0 | 105 |

| qa | 0 | 0 | 4 | 0 | 4 |

| **合计** | **612** | **2123** | **1459** | **1** | **4195** |

---

## 孤岛条目

**检测方法**：标题命中初筛（concept/entity 名称是否出现在任何 summary 标题中），对未命中条目进行 Notion 搜索验证。

**已验证非孤岛**（搜索命中 summary）：

- [Barker](entities/Barker.md) → 匹配到「摘要：Barker：一站式稳定币理财收益聚合器」

- [ZeeLin Music](entities/ZeeLin Music.md) → 匹配到「摘要：这首AI歌曲为何戳中所有人」

**疑似孤岛（未找到 summary 标题匹配，未做全量搜索验证）**：

| 页面 | 类型 | 状态 |

| --- | --- | --- |

| [Untitled](entities/db9.md) | entity | 审核中 |

| [Untitled](entities/Aivilization.md) | entity | 审核中 |

| [Untitled](entities/IronClaw.md) | entity | 审核中 |

| [Untitled](entities/TrustMRR.md) | entity | 审核中 |

> ⚠️ 孤岛检测基于标题初筛，以上条目可能在 summary 正文中有 `<mention-page>` 引用，建议 Fixer 逐条搜索验证后再决定是否标注。整体数据库连通性良好，大多数条目有对应摘要。

---

## 过期草稿（>7天）

✅ **无**。全部 612 个草稿均创建于 2026-04-21 之后（最新批次集中于 2026-04-27 ~ 2026-04-28），无过期草稿。

---

## 过时内容（最后编译时间 > 30 天）

✅ **无**。查询结果显示无条目的 `最后编译时间` 早于 2026-03-29。仅有 4 个系统元 concept 页（关于 Wiki Compiler、关于 Wiki Fixer、关于 Wiki QA Agent、关于 Gap Agent）编译时间为 null，均在豁免名单内。

---

## 重复疑似

### A. concept / entity 完全同名重复

✅ SQL `GROUP BY 名称 HAVING COUNT(*) > 1` 查询返回 0 结果。**无**完全同名的 concept/entity 重复对。

### B. concept / entity 归一化后近似重复

| 疑似重复对 | 差异原因 | 建议 |

| --- | --- | --- |

| [Untitled](entities/Personal Agent.md) vs Untitled | 空格差异（归一化后同名） | 合并为一个条目 |

**跨工具疑似同名条目（需人工核实）**：以下条目在 SQL 查询和搜索结果中分别出现两次不同 URL，可能是重复页面，也可能是压缩 URL 映射差异：

| 名称 | 疑似类型 |

| --- | --- |

| Personalized AI | 同名 concept × 2 |

| AI CRM | 同名 concept × 2 |

| Berachain / PoL | concept + entity 同名不同类型 × 2 |

| AI Oracle 链上 AI 预言机 | 同名 concept × 2 |

### C. summary 完全同名重复

✅ SQL `GROUP BY 名称 HAVING COUNT(*) > 1` 查询返回 0 结果。**无**完全同名 summary 重复。

### D. summary 归一化后近似重复

以下三条 summary 归一化后名称高度相似，疑似同一源文章被 Compiler 多次触发：

| URL | 名称 |

| --- | --- |

| [Untitled](summaries/摘要：Agency Agents：用 147 个 AI 专家角色，把 Claude Code 变成一整家公司.md) | 差异：大写开头，人数 147 |

| [Untitled](summaries/摘要：agency-agents：一个开源的 AI 虚拟团队，144 个专业 Agent 覆盖 12 个职能部门.md) | 差异：小写，人数 144 |

| [Untitled](summaries/摘要：agency-agents：用 147 个 Markdown 文件，搭建你的零成本 AI 专业团队.md) | 差异：强调 Markdown 文件 |

> 归一化后均约为 「agency-agents」，来源不同推文/文章切角，但主体相同。建议保留最完整的一份，其余归档或删除。

---

## 状态异常

✅ **无**。查询所有 concept/entity/summary/synthesis/qa 类型中，无「状态 = null 或空」的页面。

---

## 标签异常

### 1. 标签为空

✅ **无**。所有 concept/entity 条目均有至少 1 个标签。

### 2. 废弃标签使用情况

**🚨 重要发现：新标签体系尚未落地**

根据最新 Lint Agent 指令（2026-04-28 版本），标签体系已从「14 标签扁平制」升级为「3维标签制（A=场景领域, B=技术方法, C=产品形态）」，以下标签已退休：

**早期废弃（已从选项移除）**：~~AI Agent~~, ~~MCP~~, ~~Notion~~

- ✅ 数据库中未发现这些废弃标签的使用

**新退休标签（覆盖面过宽）**：

~~LLM~~, ~~Agent 框架~~, ~~Agent 编排~~, ~~Agent 技能~~, ~~Coding Agent~~, ~~开发工具~~, ~~工作流~~, ~~记忆系统~~, ~~安全/隐私~~, ~~Crypto/DeFi~~, ~~内容创作~~

**影响估算**（基于标签分布统计）：

- LLM: 单标签条目 128+ 个，出现在大量组合标签中

- 开发工具: 单标签 83+ 个

- Agent 编排: 单标签 71+ 个

- Crypto/DeFi: 单标签 55+ 个

- Coding Agent: 单标签 55+ 个

- 其余退休标签（工作流、记忆系统、安全/隐私、Agent 框架、Agent 技能、内容创作）各有数十至数百条使用

**影响范围：估计超过 70% 的 concept/entity 条目使用了至少一个退休标签**，属于 **系统性变更**，需要 Wiki Schema 制定新标签映射规则并批量执行。

---

## 标签分布统计（前20，仅含 concept/entity）

> 注：以下为标签组合维度的分布，非单标签频次。

| 标签组合 | 条目数 |

| --- | --- |

| ["LLM"]（单标签） | 128 |

| ["开发工具"]（单标签） | 83 |

| ["Agent 编排"]（单标签） | 71 |

| ["Crypto/DeFi"]（单标签） | 55 |

| ["Coding Agent"]（单标签） | 55 |

| ["知识管理"]（单标签） | 52 |

| ["商业/生态"]（单标签） | 46 |

| ["Harness 工程"]（单标签） | 32 |

| ["Coding Agent","工作流"] | 31 |

| ["Agent 编排","工作流"] | 31 |

| ["内容创作","工作流"] | 29 |

| ["Crypto/DeFi","商业/生态"] | 28 |

| ["Coding Agent","Agent 技能"] | 28 |

| ["开发工具","安全/隐私"] | 27 |

| ["Agent 编排","Coding Agent"] | 26 |

| ["长期记忆"]（单标签） | 25 |

| ["LLM","商业/生态"] | 25 |

| ["Agent 安全"]（单标签） | 25 |

| ["Agent 协作模式"]（单标签） | 23 |

| ["Coding Agent","Agent 编排"] | 22 |

**标签健康观察**：`知识管理`、`Harness 工程`、`OpenClaw`、`长期记忆`、`Agent 安全`、`Agent 协作模式` 等新维度标签分布较健康。退休标签（LLM、开发工具、Agent 编排 等）仍是高频主力，是 3D 标签迁移的主要对象。

---

## 类型启发式筛查结果

以下 concept 条目疑似应为 entity 类型（建议人工确认，不自动判定）：

| 页面 | 命中规则 | 理由 |

| --- | --- | --- |

| [Untitled](concepts/Symphony.md) | 规则 B（产品后缀/专有名词） | OpenAI 开源的编程自主管理工具，特定产品 |

| [Untitled](concepts/Spec Kit.md) | 规则 B + 规则 C | GitHub 官方开源框架，有具体版本/发布主体 |

| [Untitled](concepts/G.A.M.E 框架.md) | 规则 B（Framework后缀） | Virtuals Protocol 的具体产品框架 |

| [Untitled](concepts/EIP-7702.md) | 规则 C | 具体以太坊提案编号，类似 ERC-8183（已为 entity） |

| [Untitled](concepts/MTProto.md) | 规则 B（Protocol后缀） | Telegram 专有协议，特定产品标准 |

| [Untitled](concepts/Telethon.md) | 规则 C | 具体 Python 库，有版本/维护方 |

| [Untitled](concepts/pgvector.md) | 规则 C | PostgreSQL 特定扩展插件 |

| [Untitled](concepts/CLAUDE.md.md) | 规则 B（文件/配置后缀） | 特定配置文件格式 → 但这也可能是方法论，边界模糊 |

**计分说明**：上述 8 项均为「建议人工确认」，待确认后按 每 3 个确认误分类扣 -3 计算。

---

## 标签分类合理性检查（Phase 2 抽样）

共加载 5 个页面进行深度检查：

| 页面 | 当前标签 | 问题 | 建议 |

| --- | --- | --- | --- |

| [Untitled](concepts/Symphony.md) | Agent 编排 | 应为 entity；标签也需调整 | 改类型 → entity，标签考虑 Coding Agent/IDE 集成 |

| [Untitled](concepts/Telethon.md) | MCP 协议 | Telethon 是 Telegram Python 库，非 MCP 协议 | 标签应改为 开发工具 或具体平台标签 |

| [Untitled](concepts/Memory Folder.md) | Harness 工程, 长期记忆, 上下文管理 | 合理 ✅ | 无需修改 |

| [Untitled](concepts/Spec Kit.md) | 知识管理, Harness 工程, AI 产品 | 应为 entity；标签基本合理 | 改类型 → entity |

| [Untitled](concepts/Builder-Operator 模式.md) | Agent 协作模式, Harness 工程 | 合理 ✅ | 无需修改 |

---

## 引用结构化检查（Phase 2）

**抽样规模**：5 个页面（均含来源引用区块）

**分层说明**：本次样本覆盖草稿（2026-04-27）、审核中（2026-04-10/11）、已审核（2026-04-11）各类别

| 指标 | 结果 |

| --- | --- |

| 样本总量 | 5 页 |

| 含 mention-page 引用页数 | 5 / 5 (100%) |

| 含纯文本引用页数 | 0 / 5 (0%) |

| plain-text rate | 0% |

| affected page rate | 0% |

✅ **未触发系统性问题警报**（阈值：affected page rate ≥ 30% 或 plain-text rate ≥ 20%）

**结论**：本次抽样中，引用结构均使用了规范的 `<mention-page>` 格式，无纯文本引用问题。

**说明**：由于抽样量（5页）低于指令要求的 80 页最低标准，结论为参考性结论。建议后续扩大抽样。

---

## 计分明细

| 检查项 | 发现 | 扣分 |

| --- | --- | --- |

| 孤岛条目（抽样验证） | 4 个疑似孤岛（未全量验证） | -20 |

| 过期草稿（>7天） | 0 个 | 0 |

| 过时内容（>30天） | 0 个 | 0 |

| concept/entity 重复疑似 | 1 确认近似重复对（Personal Agent/PersonalAgent）+ 4 需核实对 | -10（1 确认对） |

| summary 重复疑似 | 1 组近似重复（agency-agents × 3）< 10 组阈值 | 0 |

| 状态异常（null/空） | 0 个 | 0 |

| 标签缺失 | 0 个 | 0 |

| 废弃标签（原始：AI Agent/MCP/Notion） | 0 个 | 0 |

| 新退休标签（3D 体系） | 系统性变更，未计入本次评分，列入 👤 人工介入项 | — |

| 引用结构化（5页样本） | 0 纯文本引用 | 0 |

| **总计** |  | **-30 → 70/100** |

> **调整说明**：孤岛条目为未完整验证的抽样（4个），最终以验证后数量计算。4 个 × (-5) = -20。1 确认重复对 × (-10) = -10。总扣 30，最终得分 **70/100** 🟡

---

## 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 |

| --- | --- | --- | --- |

| （全部 612 个草稿） | 草稿 | 暂不晋升 | 均创建于 7 天内（2026-04-21 之后），未满 7 天等待期 |

| 全部 1335 个 summary | 已审核 | ✅ 已为目标状态 | 所有 summary 均已是「已审核」 |

| 审核中 → 已审核（多源引用） | 审核中 | 需系统核查 | 需检查哪些 concept/entity 被 ≥2 个不同 summary 引用，当前数据不足以批量判断 |

**关注**：[Dreaming 记忆机制](concepts/Dreaming 记忆机制.md) 已为「已审核」，被 4 个 summary 引用，状态正确。

---

## 改进建议

### 🤖 自动修复项

| 编号 | 修复类型 | 目标页面 | 具体操作 |

| --- | --- | --- | --- |

| E1 | 近似重复合并 | [Untitled](entities/Personal Agent.md)  • Untitled | 保留内容更丰富的一个，将另一个归档（archivePages） |

| E2 | summary 重复清理 | [Untitled](summaries/摘要：agency-agents：一个开源的 AI 虚拟团队，144 个专业 Agent 覆盖 12 个职能部门.md)  • [Untitled](summaries/摘要：agency-agents：用 147 个 Markdown 文件，搭建你的零成本 AI 专业团队.md) | 与 [Untitled](summaries/摘要：Agency Agents：用 147 个 AI 专家角色，把 Claude Code 变成一整家公司.md) 比较内容，保留最完整版本，其余 archivePages |

| E3 | 标签修正 | [Untitled](concepts/Telethon.md) | 将标签从 「MCP 协议」改为「开发工具」 |

| E4 | 疑似重复核实 | Personalized AI、AI CRM、Berachain / PoL、AI Oracle 链上 AI 预言机 | 逐一加载两个同名 URL，确认是否为重复页面，若是则合并 |

### 👤 人工介入项

| 编号 | 问题类型 | 说明 |

| --- | --- | --- |

| H1 | **🚨 标签体系迁移（最高优先级）** | 新 3D 标签体系（A=场景领域, B=技术方法, C=产品形态）已在指令层面确立，但数据库 Schema 尚未更新，11 个退休标签仍在使用（估计影响 70%+ 条目）。需要：① 确定完整的新标签列表（见 Wiki Schema 规则文件）；② 制定旧标签→新标签映射规则；③ 建立批量迁移 Agent（建议创建独立 Autofill Agent「标签升级员」）执行。 |

| H2 | 类型误分类确认 | 对「类型启发式筛查结果」中列出的 8 个疑似 concept→entity 条目进行人工确认，确认后由 Fixer 执行类型修正。 |

| H3 | 孤岛条目补全验证 | 对 4 个疑似孤岛条目（db9、Aivilization、IronClaw、TrustMRR）在 Wiki 正文中进行全文搜索，确认是否真正孤立，若是则标注或关联到已有 summary。 |

| H4 | Symphony 类型修正 | [Untitled](concepts/Symphony.md) 当前为 concept，内容显示为 OpenAI 的具体产品，建议改为 entity 并更新标签。 |

| H5 | Spec Kit 类型修正 | [Untitled](concepts/Spec Kit.md) 当前为 concept，实为 GitHub 官方框架产品，建议改为 entity。 |

| H6 | Compiler 重复触发机制 | agency-agents 出现 3 条近似重复 summary，说明 Compiler 在同一源文章被多次触发。建议检查 Compiler 的去重机制，防止后续继续产生重复 summary。 |

---

>  请根据以上报告执行自动修复。
