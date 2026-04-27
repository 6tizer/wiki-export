---
title: Lint Report 2026-04-22
type: lint-report
tags:
- 知识管理
status: 草稿
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/97b23bce68744db3bf55c47fe925350c
notion_id: 97b23bce-6874-4db3-bf55-c47fe925350c
---

## 检查日期

2026-04-22（自动触发，UTC+8 14:00 定时任务）

## 总体健康度

**0 / 100** 🔴

> 主要拖分项：251 条过期草稿（-753 分）、5 对近似重复（-50 分）、引用结构化系统性问题（-48 分）、孤岛候选（-25 分）。最低封底为 0 分。

---

## 全库统计

| 类型 | 草稿 | 审核中 | 已审核 | 需更新 | 合计 |

| --- | --- | --- | --- | --- | --- |

| entity | 489 | 211 | 2 | 0 | 702 |

| synthesis | 4 | 59 | 0 | 0 | 63 |

| **合计** | **1576** | **618** | **1131** | **1** | **3326** |

---

## 孤岛条目

> 当前 summary 无 relation 字段指向 concept/entity，无法通过纯 SQL 精确检测。采用「标题命中初筛 + 推理层匹配」方案。

**候选孤岛（初筛未命中 summary 标题，待 Notion search 二次确认）：**

- [TAOR 循环](concepts/TAOR 循环.md)

- [R.E.S.T模型](concepts/R.E.S.T模型.md)

- [Agent八原语框架](concepts/Agent八原语框架.md)

- [Webhook 幂等性](concepts/Webhook 幂等性.md)

- [Agent 交易市场](concepts/Agent 交易市场.md)

- [GR4AD](concepts/GR4AD.md)

- [生成式推荐系统](concepts/生成式推荐系统.md)

- [PPAF循环](concepts/PPAF循环.md)

- [Ralph Loop](concepts/Ralph Loop.md)

- [Claw-Eval](entities/Claw-Eval.md)

*以上 10 条为保守估计，建议通过 Notion search 验证正文引用情况。*

---

## 过期草稿（>7 天）

SQL 查询确认：**共 251 条** concept/entity 草稿，创建于 2026-04-15 之前（距今 >7 天）。

部分示例：

| 页面 | 类型 | 标签 | 创建日期 | 已过天数 |

| --- | --- | --- | --- | --- |

| [Untitled](entities/pikiclaw.md) | entity | OpenClaw | 2026-04-11 | 11 天 |

| [Untitled](concepts/混合模型策略.md) | concept | OpenClaw/LLM | 2026-04-11 | 11 天 |

| Untitled | concept | 记忆系统 | 2026-04-12 | 10 天 |

*（共 251 条，以上仅为示例。2026-04-11 批次约 100+ 条，2026-04-12 批次约 60+ 条，2026-04-17 批次约 60+ 条，2026-04-20 批次约 30+ 条。）*

---

## 过时内容（>30 天）

**0 条**。所有条目均在近 30 天内完成编译。

7 个系统元 concept 页（「关于 Gap Agent」等，最后编译时间为 null）已按规则豁免。

---

## 重复疑似

### Concept/Entity 重复

**A. 完全同名重复：0 对**

**B. 归一化近似重复：5 对**

| 页面 A | 状态 A | 页面 B | 状态 B | 差异原因 | [Untitled](concepts/对抗性评审.md) | 审核中 | Untitled | 草稿 | 「性」vs「式」，语义相同 |

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| [Untitled](entities/Camoufox.md) | 草稿 | Untitled | 草稿 | 拼写变体，指同一工具 | [Untitled](concepts/提示注入.md) | 审核中 | Untitled | 草稿 | 中英文翻译，概念相同 |

| [Untitled](entities/CME FedWatch Tool.md) | 草稿 | [Untitled](entities/CME FedWatch.md) | 草稿 | 后缀「Tool」差异，指同一产品 | [Untitled](entities/Token Optimizer.md) | 草稿 | [Untitled](entities/Claude Token Optimizer.md) | 草稿 | 前缀「Claude」差异，疑似同一工具 |

### Summary 重复

**A. 完全同名重复：0 组**
**B. 近似同名重复：0 组**

全部 1108 条 summary 名称唯一。

---

## 状态异常

**0 条**。全库所有条目均已设置状态字段。

---

## 标签异常

**标签缺失：0 条**。

**废弃标签使用：0 条**（~~AI Agent~~、~~MCP~~、~~Notion~~ 标签均未使用）。

---

## 标签分布统计

> 以下为基于抽样数据的估算；精确数值可通过 Dashboard「📊 concept+entity 标签分布」图表查看。

| 标签 | 估计条目数 | 备注 |

| --- | --- | --- |

| Agent 编排 | ~400 | 体量最大 |

| 开发工具 | ~250 | 需关注 AI Coding Agent 类是否误入 |

| 记忆系统 | ~250 | 正常 |

| OpenClaw | ~200 | 正常 |

| Crypto/DeFi | ~180 | 正常 |

| 内容创作 | ~150 | 正常 |

| 知识管理 | ~120 | 正常 |

---

## 类型启发式筛查结果

以下 concept 条目经推理层规则筛查，**疑似应为 entity 类型**，建议人工确认：

| 条目名称 | 命中规则 | 建议 | [Untitled](entities/Step 3.5 Flash.md) | Rule A（版本号 3.5）+ Rule C（英文专有名） | 建议改为 entity，当前类型 concept 不准确 |

| --- | --- | --- | --- | --- | --- |

| [Untitled](entities/superpowers 框架.md) | Rule B（"superpowers" 产品名） | 建议人工确认是否为具体产品 | [Untitled](concepts/G.A.M.E 框架.md) | Rule D（大写缩写+产品名） | 建议改为 entity（Virtuals Protocol 旗下具体框架） |

| [Untitled](concepts/CodeBrain.md) | Rule C（英文专有名词，驼峰命名） | 建议人工确认是否为具体产品 | [Untitled](concepts/OpenSpec.md) | Rule B（"Spec" 工具/产品名） | 建议人工确认 |

| [Untitled](concepts/Spec Kit.md) | Rule B（"Kit" 产品后缀） | 建议人工确认 | [Untitled](concepts/QClaw.md) | Rule C（英文专有名词） | 建议人工确认 |

*（共 7 条候选，均标注「建议人工确认」，不自动判定。）*

---

## 标签分类合理性检查

Phase 2 抽样 8 条页面，发现以下问题：

| 条目 | 当前类型/标签 | 问题 | 建议修正 | [Untitled](entities/Step 3.5 Flash.md) | concept / LLM | 特定版本模型产品，应为 entity | 类型改 entity，标签改 商业/生态 或 LLM |

| --- | --- | --- | --- | --- | --- | --- | --- |

其余抽样条目标签与分类均合理。

---

## 引用结构化检查 🚨 系统性问题

**抽样 8 条草稿页（分层覆盖 2026-04-11 至 2026-04-20）：**

| 页面 | 创建日期 | 来源引用类型 | 详情 |

| --- | --- | --- | --- |

| [Untitled](concepts/混合模型策略.md) | 2026-04-11 | 纯文本 ❌ | 摘要名文本但无 mention-page 标签 |

| [Untitled](concepts/多租户托管.md) | 2026-04-12 | 纯文本 ❌ | 《...》书名号 + URL 格式 |

| [Untitled](concepts/Refusal Direction.md) | 2026-04-17 | 混合 ⚠️ | mention-page + [原文链接] 纯文本混用 |

| [Untitled](concepts/Minions.md) | 2026-04-20 | 结构化 ✅ | 完整 mention-page + 关联概念 |

**汇总统计：**

- **Affected page rate：6/8 = 75%** ⚠️（阈值 30%）

- **Plain-text rate：约 50%** ⚠️（阈值 20%）

- 推测受影响总量：≈ 188 条（251 × 75%）

**【🚨 系统性问题判定】** 两项指标均远超阈值。仅靠 Wiki Fixer 逐条修复不现实（估计 ≥150 条需修复，每条耗时 3-5 次工具调用）。**强烈建议建立独立的 Autofill Agent（引用升级员）批量处理。**

---

## 计分明细

| 检查项 | 发现 | 扣分 |

| --- | --- | --- |

| 过期草稿（>7 天） | 251 条 | -753 |

| 疑似重复对 | 5 对 | -50 |

| 标签缺失/废弃 | 0 条 | 0 |

| 引用系统性问题（额外惩罚） | Affected rate 75% > 30% | -10 |

| **最终健康分（封底 0）** |  | **0 / 100 🔴** |

---

## 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 | [Untitled](concepts/AI小程序成长计划.md) | 草稿 | 审核中 | 创建 >7 天，定义完整，内容完整，来源引用含 ≥2 个 mention-page ✓ |

| --- | --- | --- | --- | --- | --- | --- | --- |

> ⚠️ 其余 250 条过期草稿因来源引用为纯文本或缺 mention-page，暂不符合晋升条件，需先完成引用结构化修复。

---

## 改进建议

### 🤖 自动修复项

1. **[E1] 状态晋升 — AI小程序成长计划**

  - 修复类型：状态更新

  - 目标页面：[AI小程序成长计划](concepts/AI小程序成长计划.md)（[https://www.notion.so/fce3a27f94504ba28165c55dfaafb546）](https://www.notion.so/fce3a27f94504ba28165c55dfaafb546）)

  - 操作：`updatePage(url, propertyUpdates: { 状态: "审核中" })`

1. **[E2] 重复合并（4 对已可执行）**

  - 对抗式评审（草稿）→ 删除，保留 [对抗性评审](concepts/对抗性评审.md)（审核中）

  - CamoFox（草稿）→ 删除，保留 [Camoufox](entities/Camoufox.md)（草稿，主流拼写）

  - Prompt Injection（草稿）→ 删除，保留 [提示注入](concepts/提示注入.md)（审核中）

  - [CME FedWatch Tool](entities/CME FedWatch Tool.md) 与 [CME FedWatch](entities/CME FedWatch.md)：人工确认后合并（见 👤 项）

1. **[E3] 类型修正**

  - [Step 3.5 Flash](entities/Step 3.5 Flash.md)（[https://www.notion.so/5eea43dcf716477db20930ea6ebfe708）：](https://www.notion.so/5eea43dcf716477db20930ea6ebfe708）：)`updatePage(url, propertyUpdates: { 类型: "entity" })`

1. **[E4] 引用结构化（小批量 Fixer 可处理的已知纯文本页）**

  - [SuperHQ](entities/SuperHQ.md)：将「未匹配」文本替换为搜索匹配的 summary mention-page

  - [多租户托管](concepts/多租户托管.md)：将《ClawHost: 用 Kubernetes...》纯文本替换为对应 summary mention-page

  - Dreaming 记忆整合：将《Claude Code 的七层记忆架构...》纯文本替换为对应 summary mention-page

  - [混合模型策略](concepts/混合模型策略.md)：将「摘要：OpenClaw + 本地模型...」文本替换为对应 summary mention-page

  - 注意：以上 4 条为示例，实际受影响页面 ≈ 188 条，**建议仅处理以上 4 条作为验证，大批量交给 Autofill Agent（见 👤 项）**

### 👤 人工介入项

1. **🚨 建立独立 Autofill Agent（引用升级员）**

  - 背景：Affected page rate 75%，估计 ≥150 条需修复引用结构化，Fixer 逐条处理效率不足

  - 建议：新建专属 Agent，功能：

    1. 扫描所有草稿 concept/entity 的来源引用

    1. 识别纯文本引用行（无 mention-page 的行）

    1. 通过 summary 名称匹配找到对应 summary 页面 URL

    1. 将纯文本替换为 `<mention-page url="...">摘要标题</mention-page>`

  - 批处理指令模板（供 Fixer 手动执行少量时参考）：

    ```javascript
1. loadPage(页面 URL)
2. 定位「来源引用」区块中的纯文本行
3. search(摘要标题关键词) → 获得 summary URL
4. updatePage(URL, contentUpdates: [{oldStr: "纯文本引用行", newStr: "<mention-page url='summary-url'>标题</mention-page>"}])
    ```

1. **CME FedWatch 重复对人工确认后合并**

  - [CME FedWatch Tool](entities/CME FedWatch Tool.md) vs [CME FedWatch](entities/CME FedWatch.md)

  - Token Optimizer vs Claude Token Optimizer：确认是否同一工具

1. **类型启发式筛查人工确认**

  - 7 条疑似 concept→entity 条目（见「类型启发式筛查结果」）

  - 需人工审查内容后确认分类

1. **孤岛候选 Notion Search 验证**

  - 对「孤岛条目」节列出的 10 条候选，通过 Notion 搜索验证是否在 summary 正文中被提及

1. **草稿积压策略讨论**

  - 251 条过期草稿是当前最大扣分项（-753 分）

  - 建议评估：引用结构化修复完成后，批量晋升内容完整的草稿至「审核中」

  - 或讨论是否适当调整晋升标准，以应对大批量积压情况

1. **concept/entity → summary relation 字段**

  - 当前孤岛检测依赖 summary 标题匹配，精度有限

  - 如增加 relation 字段指向 summary，将显著提升孤岛检测与状态晋升的准确性

---

>  请根据以上报告执行自动修复。

---

## 📋 引用结构化待处理完整列表（251 条草稿 concept/entity）

> 以下为所有过期草稿 concept/entity（创建 ≥7 天），Lint 抽样显示约 75%（≈188 条）存在纯文本引用需升级为 `<mention-page>` 结构化链接。✅ = Wiki Fixer 已修复。引用升级员逐条 loadPage 检查「来源引用」段，纯文本行升级为 mention-page。

[SuperHQ](entities/SuperHQ.md)、[SuperConductor](entities/SuperConductor.md)、[Nezha](entities/Nezha.md)、[pikiclaw](entities/pikiclaw.md)、[Dageno](entities/Dageno.md)、[SafePal](entities/SafePal.md)、[ARC/Rig 框架](entities/ARC-Rig 框架.md)、[Fiat24](entities/Fiat24.md)、[Qdrant](entities/Qdrant.md)、[x-tweet-fetcher](entities/x-tweet-fetcher.md)、[MiniMax M2.5](entities/MiniMax M2.5.md)、✅ [混合模型策略](concepts/混合模型策略.md)、[Cursor Skills 生态](concepts/Cursor Skills 生态.md)、[阿里百炼 Coding Plan](concepts/阿里百炼 Coding Plan.md)、[superpowers 框架](entities/superpowers 框架.md)、[Binance Skills Hub](entities/Binance Skills Hub.md)、[账号风控](concepts/账号风控.md)、[X 列表](concepts/X 列表.md)、[跨交易所套利](concepts/跨交易所套利.md)、[CME FedWatch](entities/CME FedWatch.md)、[双向链接](concepts/双向链接.md)、[逆向分析](concepts/逆向分析.md)、[传播飞轮](concepts/传播飞轮.md)、[FRED](entities/FRED.md)、[AI 工具逆向分析](concepts/AI 工具逆向分析.md)、[OpenClaw 九层 System Prompt 架构](concepts/OpenClaw 九层 System Prompt 架构.md)、[多模型交叉验证筛选](concepts/多模型交叉验证筛选.md)、[飞书官方 OpenClaw 插件](concepts/飞书官方 OpenClaw 插件.md)、[X 信息源矩阵](concepts/X 信息源矩阵.md)、[OpenClaw Context Engine](entities/OpenClaw Context Engine.md)、[Context Hub](entities/Context Hub.md)、[SESSION.md](concepts/SESSION.md.md)、[四层 Fallback 链](concepts/四层 Fallback 链.md)、[Agent 人设](concepts/Agent 人设.md)、[三层防御矩阵](concepts/三层防御矩阵.md)、[潜规则挖掘提示法](concepts/潜规则挖掘提示法.md)、[AI Wallet Matcher](concepts/AI Wallet Matcher.md)、[交易信号自动化](concepts/交易信号自动化.md)、[思想钢印](concepts/思想钢印.md)、[投资人压力测试](concepts/投资人压力测试.md)、[鲸鱼跟单](concepts/鲸鱼跟单.md)、[XHS Bridge](concepts/XHS Bridge.md)、[xiaohongshu-skills](entities/xiaohongshu-skills.md)、[ERC-8004](concepts/ERC-8004.md)、[三层追问链](concepts/三层追问链.md)、[OmniRoute](entities/OmniRoute.md)、[本地 LLM 网关](concepts/本地 LLM 网关.md)、[Volume Profile](concepts/Volume Profile.md)、[QClaw](concepts/QClaw.md)、[CVD 背离](concepts/CVD 背离.md)、[Agent Drift](concepts/Agent Drift.md)、[Barker](entities/Barker.md)、[db9](entities/db9.md)、[Aivilization](entities/Aivilization.md)、[skill-security-auditor](concepts/skill-security-auditor.md)、[IronClaw](entities/IronClaw.md)、[稳定币收益聚合](concepts/稳定币收益聚合.md)、[program.md](concepts/program.md.md)、[Agent 游戏](concepts/Agent 游戏.md)、[Social CLI](entities/Social CLI.md)、[DenchClaw](entities/DenchClaw.md)、[Awesome OpenClaw Skills](entities/Awesome OpenClaw Skills.md)、[MTProto](concepts/MTProto.md)、[OpenClaw101](entities/OpenClaw101.md)、[Cloudflare 全家桶](concepts/Cloudflare 全家桶.md)、[OpenInsider](entities/OpenInsider.md)、[BettaFish](entities/BettaFish.md)、[LLM 投研工作流](concepts/LLM 投研工作流.md)、[内部人士买入筛查](concepts/内部人士买入筛查.md)、[Siftly](entities/Siftly.md)、[CLI-Hub](entities/CLI-Hub.md)、[CLI Harness](concepts/CLI Harness.md)、[一人公司](concepts/一人公司.md)、[TrustMRR](entities/TrustMRR.md)、[AEO Engine](entities/AEO Engine.md)、[Bregman 投影](concepts/Bregman 投影.md)、[整数规划](concepts/整数规划.md)、[OpenClaw Exposure Watchboard](entities/OpenClaw Exposure Watchboard.md)、[find-skills](concepts/find-skills.md)、[Kelly 准则](concepts/Kelly 准则.md)、[书签 AI 管道](concepts/书签 AI 管道.md)、[多模态 K 线形态匹配](concepts/多模态 K 线形态匹配.md)、[Context Agent](concepts/Context Agent.md)、[原生多模态 Embedding](concepts/原生多模态 Embedding.md)、[Agentic Navigation](concepts/Agentic Navigation.md)、[C++ 级指纹伪造](concepts/C++ 级指纹伪造.md)、[记忆热插拔](concepts/记忆热插拔.md)、[Cloudflare /crawl](entities/Cloudflare -crawl.md)、[Ralph Loop](concepts/Ralph Loop.md)、[camoufox-cli](entities/camoufox-cli.md)、[Moltbook](entities/Moltbook.md)、[统一语义空间](concepts/统一语义空间.md)、[Browser Rendering](concepts/Browser Rendering.md)、[模型路由](concepts/模型路由.md)、[InsForge](entities/InsForge.md)、[Next-State Signal](concepts/Next-State Signal.md)、[AI Crawl Control](concepts/AI Crawl Control.md)、[语义层](concepts/语义层.md)、[设计词汇](concepts/设计词汇.md)、[OKX Agent Trade Kit](entities/OKX Agent Trade Kit.md)、[Agent Tool Interface](concepts/Agent Tool Interface.md)、[Claude Code Handoff](concepts/Claude Code Handoff.md)、[LLM 重排序](concepts/LLM 重排序.md)、web fetch、[Pal](entities/Pal.md)、[Gemini Embedding 2](entities/Gemini Embedding 2.md)、[AI 公司操作系统](concepts/AI 公司操作系统.md)、[Twitter Buddy](entities/Twitter Buddy.md)、[IP 纯净度检测](concepts/IP 纯净度检测.md)、[时间线监控 Agent](concepts/时间线监控 Agent.md)、[Skill-Based Agent 架构](concepts/Skill-Based Agent 架构.md)、[历史人物人格唤醒](concepts/历史人物人格唤醒.md)、[跨次账号评分](concepts/跨次账号评分.md)、[链式代理](concepts/链式代理.md)、[automation-workflows](entities/automation-workflows.md)、[自生长人格](concepts/自生长人格.md)、[链上交易 Skill](concepts/链上交易 Skill.md)、[skills-vetter](entities/skills-vetter.md)、[Persona Pattern](concepts/Persona Pattern.md)、[读写分离控制面板](concepts/读写分离控制面板.md)、[Tool Registry](concepts/Tool Registry.md)、[Heartbeat-Like-A-Man](entities/Heartbeat-Like-A-Man.md)、[随机心跳机制](concepts/随机心跳机制.md)、[AI 情报员工作流](concepts/AI 情报员工作流.md)、[存在姿态三角形](concepts/存在姿态三角形.md)、[预测市场交易 Agent](concepts/预测市场交易 Agent.md)、[YouMind](entities/YouMind.md)、[自主探索](concepts/自主探索.md)、[验证闭环](concepts/验证闭环.md)、[ultrathink](concepts/ultrathink.md)、[Manus](entities/Manus.md)、[Agent 共享学习](concepts/Agent 共享学习.md)、[思维预算](concepts/思维预算.md)、[ZeroClaw](entities/ZeroClaw.md)、[PicoClaw](entities/PicoClaw.md)、[My Computer](concepts/My Computer.md)、[graph-memory](entities/graph-memory.md)、[角色分工式 Agent 工作流](concepts/角色分工式 Agent 工作流.md)、[图推理](concepts/图推理.md)、[AstrBot](entities/AstrBot.md)、[Agent-native Application](concepts/Agent-native Application.md)、[桌面 Agent](concepts/桌面 Agent.md)、[领域状态](concepts/领域状态.md)、[注意力带宽](concepts/注意力带宽.md)、[运行时文档获取](concepts/运行时文档获取.md)、[提示词驱动量化研究](concepts/提示词驱动量化研究.md)、[Vibe Advertising](concepts/Vibe Advertising.md)、[Arcads](entities/Arcads.md)、[UGC 广告流水线](concepts/UGC 广告流水线.md)、[自动科研](concepts/自动科研.md)、[AutoDarwin](entities/AutoDarwin.md)、[出站网络控制](concepts/出站网络控制.md)、[MetaClaw](entities/MetaClaw.md)、[Slash 命令工作流](concepts/Slash 命令工作流.md)、[策略自我进化](concepts/策略自我进化.md)、[链上选币](concepts/链上选币.md)、[虚拟工程团队](concepts/虚拟工程团队.md)、[AutoResearchClaw](entities/AutoResearchClaw.md)、[OpenSandbox](entities/OpenSandbox.md)、[ClawTeam](entities/ClawTeam.md)、[Reviewer 模式](concepts/Reviewer 模式.md)、[CrewClaw](entities/CrewClaw.md)、[Pipeline 模式](concepts/Pipeline 模式.md)、[技能注入](concepts/技能注入.md)、[Awesome OpenClaw Agents](entities/Awesome OpenClaw Agents.md)、[Generator 模式](concepts/Generator 模式.md)、[Tool Wrapper 模式](concepts/Tool Wrapper 模式.md)、[Inversion 模式](concepts/Inversion 模式.md)、[Agent 模板库](concepts/Agent 模板库.md)、[TaskBoard](concepts/TaskBoard.md)、[InboxSystem](concepts/InboxSystem.md)、[多角色决策](concepts/多角色决策.md)、[模型自我进化](concepts/模型自我进化.md)、[1M 上下文](concepts/1M 上下文.md)、[虚拟董事会](concepts/虚拟董事会.md)、[Agent Swarm Intelligence](concepts/Agent Swarm Intelligence.md)、[GoBot](entities/GoBot.md)、✅ [多租户托管](concepts/多租户托管.md)、[浏览器指纹模拟](concepts/浏览器指纹模拟.md)、[ClawHost](entities/ClawHost.md)、[OpenCLI 插件系统](entities/OpenCLI 插件系统.md)、[住宅代理轮换](concepts/住宅代理轮换.md)、[Gemini 3 Pro](entities/Gemini 3 Pro.md)、[测试驱动开发](concepts/测试驱动开发.md)、[Kubernetes](entities/Kubernetes.md)、[feedgrab](entities/feedgrab.md)、[Daytona 沙箱](entities/Daytona 沙箱.md)、[Open-SWE](entities/Open-SWE.md)、[Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2](entities/Qwen3.5-27B-Claude-4.6-Opus-Reasoning-Distilled-v2.md)、[六层兜底抓取机制](concepts/六层兜底抓取机制.md)、[投委会模拟](concepts/投委会模拟.md)、[tmux](entities/tmux.md)、[角色 Prompt](concepts/角色 Prompt.md)、[多智能体社会仿真](concepts/多智能体社会仿真.md)、[xiaohongshu-mcp](entities/xiaohongshu-mcp.md)、[prompts.chat](entities/prompts.chat.md)、[异步编程 Agent](concepts/异步编程 Agent.md)、[Railway 一键部署](concepts/Railway 一键部署.md)、[IM 集成 Agent](concepts/IM 集成 Agent.md)、对抗性代码审查、[Exit Node](concepts/Exit Node.md)、[WireGuard](entities/WireGuard.md)、[OmniCoder](entities/OmniCoder.md)、[V8 Isolate](concepts/V8 Isolate.md)、[OpenSpace](entities/OpenSpace.md)、[TypeScript RPC](concepts/TypeScript RPC.md)、[Read-before-write](concepts/Read-before-write.md)、[群体智能技能共享](concepts/群体智能技能共享.md)、[Cloudflare Dynamic Workers](entities/Cloudflare Dynamic Workers.md)、[代码执行沙箱](concepts/代码执行沙箱.md)、[Agentic 编程轨迹蒸馏](concepts/Agentic 编程轨迹蒸馏.md)、[MoneyPrinterTurbo](entities/MoneyPrinterTurbo.md)、[微压缩](concepts/微压缩.md)、[social-auto-upload](entities/social-auto-upload.md)、[OSWorld-Verified](entities/OSWorld-Verified.md)、[Holo3](entities/Holo3.md)、[短视频自动化工作流](concepts/短视频自动化工作流.md)、[FunClip](entities/FunClip.md)、[Agentic Learning Flywheel](concepts/Agentic Learning Flywheel.md)、[KrillinAI](entities/KrillinAI.md)、[浏览器 Session 复用](concepts/浏览器 Session 复用.md)、[姚金刚](entities/姚金刚.md)、[会话记忆](concepts/会话记忆.md)、[Claude Code Dreaming](concepts/Claude Code Dreaming.md)、[promptsref](entities/promptsref.md)、[JSON Prompt](concepts/JSON Prompt.md)、[网站 CLI 化](concepts/网站 CLI 化.md)、[GEO 提示词](concepts/GEO 提示词.md)、✅ Dreaming 记忆整合、[Pika AI Self](entities/Pika AI Self.md)、[数字同事](concepts/数字同事.md)、[会议代理](concepts/会议代理.md)、[云浏览器自动化](concepts/云浏览器自动化.md)、[回测引擎](concepts/回测引擎.md)、[STRC](entities/STRC.md)、[反身性风险](concepts/反身性风险.md)、[ATM 融资](concepts/ATM 融资.md)、[内容发布自动化](concepts/内容发布自动化.md)、[DailyNews](entities/DailyNews.md)、[群体模拟](concepts/群体模拟.md)、[PANews Skills](entities/PANews Skills.md)、[统计套利](concepts/统计套利.md)、[Kronos](entities/Kronos.md)、[Notion AI 上下文注入架构](concepts/Notion AI 上下文注入架构.md)、[Mano-CUA Skill](concepts/Mano-CUA Skill.md)、[React Flow](entities/React Flow.md)、[Agent 人格层](concepts/Agent 人格层.md)、[Molty SOUL](concepts/Molty SOUL.md)

[https://www.notion.so/agent/fbef0474915d4aed910e0cf80ad30a73](https://www.notion.so/agent/fbef0474915d4aed910e0cf80ad30a73) 请按以上列表批量处理来源引用段的纯文本引用升级。每批 30 条，按 createdTime 升序扫描，将纯文本引用行升级为 mention-page 结构化链接。
