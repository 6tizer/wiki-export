---
title: Lint Report 2026-05-02
type: lint-report
tags:
- 知识管理
status: 草稿
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a5ad13b9e3e54d16a78ad0932352774f
notion_id: a5ad13b9-e3e5-4d16-a78a-d0932352774f
---

## 检查日期

2026-05-02（定时触发，北京时间 10:00）

## 总体健康度

**65 / 100** 🟡

主要扣分项：草稿积压（4条，-12）、系统页时效过期（4条，-12）、孤岛条目（2条已确认，-10）、引用混合问题（-1）。

---

## 全库统计

| 类型 | 草稿 | 审核中 | 已审核 | 需更新 | 合计 |

| --- | --- | --- | --- | --- | --- |

| entity | 160 | 831 | 5 | 0 | 996 |

| synthesis | 0 | 36 | 108 | 0 | 144 |

| **合计** | **426** | **2516** | **1586** | **1** | **4529** |

> 注：index 和 lint-report 类型已从统计中排除。

---

## 孤岛条目

Phase 1 初筛（concept/entity 名称是否出现在 summary 标题）+ Phase 2 页面验证：

**已确认孤岛（来源引用为空）：**

- [画布式 Agent 编排](concepts/画布式 Agent 编排.md) — 来源引用区块完全为空，创建于 2026-04-24，无任何 summary 引用

- [Open Swarm](entities/Open Swarm.md) — 来源引用区块完全为空，创建于 2026-04-24，无任何 summary 引用

**说明：** 这两条均为 2026-04-24 批次创建的草稿，可能是 Compiler 在单次运行中生成了概念但未完成引用绑定。建议人工确认是否有对应摘要，若无则标记为待补充引用。

---

## 过期草稿（创建超过 7 天，状态仍为草稿）

> 截至检查日期 2026-05-02，超过 7 天的草稿（创建早于 2026-04-25）：

| 页面 | 类型 | 创建日期 | 已超时天数 | 是否内容完整 |

| --- | --- | --- | --- | --- |

| [Untitled](concepts/画布式 Agent 编排.md) | concept | 2026-04-24 | 8天 | ⚠️ 有定义+关键要点，但来源引用为空 |

| [Untitled](concepts/数字资产财库.md) | concept | 2026-04-24 | 8天 | ✅ 有定义+核心要点+1个mention-page引用 |

---

## 过时内容（最后编译时间 > 30 天或为空）

以下页面最后编译时间为 NULL（已豁免 7 个系统元 concept 页，但以下「关于」页不在豁免名单中）：

| 页面 | 类型 | 状态 | 最后编译时间 | 备注 |

| --- | --- | --- | --- | --- |

| [Untitled](concepts/关于 Wiki Fixer.md) | concept | 已审核 | NULL | 系统文档页，建议豁免或补填日期 |

| [Untitled](concepts/关于 Wiki QA Agent.md) | concept | 已审核 | NULL | 系统文档页，建议豁免或补填日期 |

> 💡 建议：将这 4 个「关于 ...」系统页加入豁免名单，或统一设置象征性的编译时间避免持续误报。

---

## 重复疑似

### A. 完全同名重复

**concept/entity：** SQL `GROUP BY 名称 HAVING COUNT(*) > 1` 结果 = 0 对，无完全同名重复。

**summary：** SQL `GROUP BY 名称 HAVING COUNT(*) > 1` 结果 = 0 对，无完全同名 summary 重复。

### B. 归一化后近似重复（concept/entity）

对已获取的 ~2000 条 concept/entity 名称进行推理层归一化匹配，发现以下疑似对：

| # | 条目A | 条目B | 差异原因 | 1 | [Untitled](entities/Vane.md)（entity） | — | 单一词，暂无匹配对 |

| --- | --- | --- | --- | --- | --- | --- | --- |

| 2 | 子 Agent 派生（concept） | 子智能体（concept） | 语义相近，但定义侧重不同（派生操作 vs 架构角色），建议人工确认是否合并 | 3 | 飞书 CLI（entity） | 钉钉 CLI（entity） | 不同产品，非重复 ✅ |

> 注：本次覆盖约 2000 条（全库 2938 条），剩余 ~938 条受 SQL 分页限制未覆盖，建议后续扩大扫描范围。实际重复对数量可能更多。

### C. Summary 近似重复

本次 summary 名称样本（按字母序抽取前 100 条）未发现近似重复，且 GROUP BY 精确匹配也未命中。Compiler 触发机制目前运行正常。

---

## 状态异常

全库所有 concept/entity/summary/synthesis 条目均已设置状态，状态为 NULL 的页面数 = **0**。✅

---

## 标签异常

### 缺失标签

SQL 查询 `标签 IS NULL OR 标签 = '[]'` WHERE 类型 IN (concept, entity) 返回 **0 条**。✅ 全库 concept/entity 均已设置标签。

### 废弃标签使用

针对早期废弃标签（AI Agent、MCP、Notion）及新退休标签（LLM、Agent 框架、Agent 编排、Agent 技能、Coding Agent、开发工具、工作流、记忆系统、安全/隐私、Crypto/DeFi、内容创作）的 LIKE 检索返回 **0 条**。✅ 全库已完成标签迁移到新三维体系。

---

## 标签分布统计

以下为基于 ~2000 条 concept/entity 样本的标签频率估算（排序由高到低）：

| 标签 | 估算条目数 | 备注 |

| --- | --- | --- |

| 商业/生态 | ~170 | 高频，覆盖面广 |

| Harness 工程 | ~150 | 高频 |

| 推理优化 | ~140 | 高频 |

| 多Agent协作 | ~130 | 高频 |

| 长期记忆 | ~100 | 中频 |

| 链上协议 | ~80 | 中频 |

| Agent 安全 | ~75 | 中频 |

| CLI 工具 | ~70 | 中频 |

| 量化交易 | ~60 | 中频 |

| 模型评测 | ~55 | 中频 |

| 浏览器自动化 | ~50 | 中频 |

| AI 设计 | ~50 | 中频 |

| 社交媒体 | ~35 | 低频 |

| 多模态 | ~35 | 低频 |

| 视频/3D | ~25 | 低频 |

| 稳定币 | ~15 | 低频 |

| 身份准入 | ~15 | 低频 |

| 图像生成 | ~10 | 低频 |

| DevOps/运维 | ~5 | 极低 |

| 认知科学 | ~3 | 极低 |

| 嵌入式硬件 | ~2 | 极低 |

> 数据基于 ~2000/2938 条样本估算，供参考。

---

## 类型启发式筛查结果（疑似 concept→entity）

以下 concept 类型条目命中启发式规则，建议人工确认是否改为 entity：

| 条目 | 命中规则 | 说明 |

| --- | --- | --- |

| [Untitled](concepts/Knowledge Work Plugins.md) | Rule B（Plugins 后缀） | 插件集合产品 |

| [Untitled](concepts/Antigravity MCP.md) | Rule C（英文专有名词） | 疑似具体 MCP 产品 |

| [Untitled](concepts/QClaw.md) | Rule C（大写缩写+专名） | 疑似具体产品 |

| [Untitled](concepts/Claude Code Plugins.md) | Rule B（Plugins 后缀） | 插件体系，疑似实体 |

| [Untitled](concepts/OASIS.md) | Rule D（大写缩写） | 全大写缩写，疑似具体产品 |

> **注意**：以上为启发式建议，需人工确认。部分可能是架构范式（如 OASIS）而非具体产品。计分按 Phase 1 原则：每 3 个确认误分类 -3 分（当前未确认，不扣分）。

---

## 标签分类合理性检查（Phase 2 抽样）

抽样 12 个页面（含 4 个过期草稿 + 8 个审核中），均未发现明显标签误分类。所有页面标签均与内容吻合，使用的是新三维标签体系。

**特别观察：**

- [Single Source of Truth](concepts/Single Source of Truth.md) 仅标注「Agent 协作模式」，可考虑补充「知识管理」标签（该概念在知识库设计中同样重要）

---

## 引用结构化检查

### 抽样统计（共 12 个页面）

| 状态 | 抽样量 | 纯 mention-page | 混合引用 | 无引用 | 结构化率 |

| --- | --- | --- | --- | --- | --- |

| 审核中（April 10-17） | 8 | 5 | 3 | 0 | 63% 纯结构化，37% 混合 |

**总体 affected page rate（含混合引用）：** 5/12 = **42%** ⚠️（注：若仅计"纯文本、无 mention-page"则为 2/12 = 17%）

**系统性判定：**

- 若将「混合引用」（有 mention-page 但也有纯文本链接）计入，affected rate = 42% > 30% → 接近系统性问题阈值

- 若仅计「完全无 mention-page」的页面，affected rate = 17% < 30% → 未触发全局警报

- **本次判定：不触发【🚨 系统性问题】警报**，但混合引用现象普遍，建议逐步清理

**含混合引用的页面（需修复）：**

- [Single Source of Truth](concepts/Single Source of Truth.md) — 来源引用中混有 `[原文链接]` 纯文本，另有 1 个 mention-page

- [Claude Code Memory](concepts/Claude Code Memory.md) — 多条纯文本引用（@gerrox 账号引用、X 书签文章文本）与 mention-page 混用

- [Claude Cowork](entities/Claude Cowork.md) — 来源引用中混有纯文本日期+账号格式

**无引用的草稿（孤岛）：**

- [画布式 Agent 编排](concepts/画布式 Agent 编排.md)

- [Open Swarm](entities/Open Swarm.md)

---

## 计分明细

| 检查项 | 发现 | 扣分 | 孤岛条目 | 2 条已确认（画布式 Agent 编排、Open Swarm） | -10 |

| --- | --- | --- | --- | --- | --- |

| 过期草稿（>7天） | 4 条（比特币增益、画布式 Agent 编排、Open Swarm、数字资产财库） | -12 | 过时内容（>30天/null） | 4 条系统文档页（关于 Wiki Compiler/Fixer/Gap Agent/QA Agent） | -12（建议豁免） |

| 重复疑似 | 0 对确认重复（子 Agent 派生 vs 子智能体 待确认） | 0 | 状态异常 | 0 条 | 0 |

| 缺失/空标签 | 0 条 | 0 | 废弃标签使用 | 0 条 | 0 |

| 引用混合/纯文本 | ~5 处纯文本引用（3 个页面） | -1 | **合计** |  | **-35（其中 -12 为建议豁免项）** |

**最终得分：100 - 10 - 12 - 12 - 1 = 65 / 100** 🟡

（若豁免 4 条系统文档页：**77 / 100** 🟡）

---

## 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 | [Untitled](concepts/比特币增益.md) | 草稿 | 审核中 | 内容完整（定义+核心要点+1个mention-page来源），创建 >7 天 |

| --- | --- | --- | --- | --- | --- | --- | --- |

| [Untitled](concepts/数字资产财库.md) | 草稿 | 审核中 | 内容完整（定义+核心要点+1个mention-page来源），创建 >7 天 | [Untitled](concepts/Agent八原语框架.md) | 审核中 | 已审核 | 被 ≥2 个 summary 引用（摘要：循环即实验室 两个版本） |

| [Untitled](concepts/DESIGN.md.md) | 审核中 | 已审核 | 被 ≥6 个不同 summary 引用，多源交叉验证高置信度 | [Untitled](concepts/MoE 架构.md) | 审核中 | 已审核 | 被 ≥12 个不同 summary 引用，置信度 high，多源高度验证 |

---

## 改进建议

### 🤖 自动修复项

1. **状态晋升 E1（草稿→审核中）**

  - 修复类型：状态更新

  - 目标：[比特币增益](concepts/比特币增益.md) → 状态改为「审核中」

  - 目标：[数字资产财库](concepts/数字资产财库.md) → 状态改为「审核中」

1. **状态晋升 E2（审核中→已审核）**

  - 修复类型：状态更新

  - 目标：[Agent八原语框架](concepts/Agent八原语框架.md) → 状态改为「已审核」

  - 目标：[DESIGN.md](concepts/DESIGN.md.md) → 状态改为「已审核」

  - 目标：[MoE 架构](concepts/MoE 架构.md) → 状态改为「已审核」

1. **引用修复（混合→纯 mention-page）**

  - 修复类型：引用结构化升级

  - 目标：[Single Source of Truth](concepts/Single Source of Truth.md) — 将「[原文链接](...)｜来源条目：<mention-page>」格式精简为纯 `<mention-page>` 引用

  - 目标：[Claude Code Memory](concepts/Claude Code Memory.md) — 将 @gerrox、《Claude Code七层记忆架构》等纯文本条目替换为对应 summary 的 `<mention-page>` 引用

  - 目标：[Claude Cowork](entities/Claude Cowork.md) — 将 `2026-04-09｜@claudeai｜...｜源页：` 格式统一为纯 `<mention-page>` 格式

1. **标签补充**

  - 修复类型：标签更新

  - 目标：[Single Source of Truth](concepts/Single Source of Truth.md) — 建议增加「知识管理」标签

### 👤 人工介入项

1. **孤岛草稿处置**

  - [画布式 Agent 编排](concepts/画布式 Agent 编排.md) 和 [Open Swarm](entities/Open Swarm.md)：来源引用为空，无 summary 与其关联。请确认：①是否有对应 summary 尚未绑定？②还是源文章已在书签库中但 Compiler 未能提取来源引用？若确认无源，建议手动添加对应 summary 的 mention-page 引用，或保留为「待补充」草稿。

1. **系统文档页豁免规则**

  - 「关于 Wiki Compiler / Fixer / Gap Agent / QA Agent」4 个页面持续触发时效性误报。建议：将其加入豁免名单（与「Wiki Lint Agent」等 7 个系统元 concept 同等处理），或统一设置固定编译时间（如 2026-04-10）。

1. **类型误分类确认**

  - 以下 concept 页面可能应为 entity，请人工确认：

  - obsidian-cli、Knowledge Work Plugins、OpenClaw Expert Suite、Antigravity MCP、NanoClaw、QClaw、ClawBio、Claude Code Plugins、MCP-Atlas、OASIS

  - 确认后由 Fixer 批量修改类型字段。

1. **「子 Agent 派生」vs「子智能体」重复判断**

  - 两者语义相近，但定义侧重不同。请确认是否需要合并，或保留为独立词条并在内容中互相引用。

---

>  请根据以上报告执行自动修复。
