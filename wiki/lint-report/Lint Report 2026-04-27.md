---
title: Lint Report 2026-04-27
type: lint-report
tags:
- 知识管理
status: 草稿
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/b51cac06b1f141a399cc4b8c5b6222a7
notion_id: b51cac06-b1f1-41a3-99cc-4b8c5b6222a7
---

## 检查日期

2026-04-27（北京时间 10:00，定时触发）

---

## 总体健康度

🔴 **0 / 100**

> 注：分数受 242 条过期草稿（-726分）压制至 0。数据库创建仅 17 天，草稿积压属历史首轮批量编译的正常现象，建议结合上下文参考分数细节。

---

## 全库统计（类型 × 状态交叉表）

| 类型 | 草稿 | 审核中 | 已审核 | 需更新 | 合计 |

| --- | --- | --- | --- | --- | --- |

| concept | 677 | 1055 | 26 | 1 | **1759** |

| entity | 301 | 541 | 4 | 0 | **846** |

| summary | 0 | 0 | 1264+ | 0 | **1264+** |

| synthesis | 0 | 6 | 90 | 0 | **96** |

| qa | 0 | 0 | 4 | 0 | **4** |

| **合计** | **978** | **1602** | **1388+** | **1** | **~3969+** |

> summary 总数因分页查询截断，实际可能超过 1264。

---

## 孤岛条目

**检测方法**：SQL 分步查询（concept/entity 名称 + summary 标题），在推理层做名称命中匹配。当前 summary 无 relation 字段指向 concept，精确检测依赖 loadPage 全量扫描，以下为初筛结果（标题未命中 summary 且 Notion 搜索无返回的条目）。

**说明**：数据库建立仅 17 天，Compiler 编译时通常同步创建 concept/entity 和 summary，孤岛率预计较低。以下为通过名称特殊性判断的疑似孤岛：

- [planktonXD](entities/planktonXD.md) — 专有名词，在 summary 标题中未见命中

- [存在姿态三角形](concepts/存在姿态三角形.md) — 抽象概念，来源不明

- [预测市场交易 Agent](concepts/预测市场交易 Agent.md) — 通用描述性概念，可能被孤立

- [角色 Prompt](concepts/角色 Prompt.md) — 通用概念，可能无专属 summary

- [Weibull 遗忘曲线](concepts/Weibull 遗忘曲线.md) — 专业术语，summary 标题未见

- [公司即 Agent](concepts/公司即 Agent.md) — 状态为草稿，summary 关联需验证

**建议**：由 Wiki Fixer 或 Gap Agent 执行 Notion search 二轮验证，确认真实孤岛数量后更新分数。

---

## 过期草稿（>7天，状态=草稿）

**总计：242 条**（创建于 2026-04-20 之前，均超过 7 天）

**背景说明**：首批编译于 2026-04-10 至 2026-04-12，距今 15~17 天，属批量创建的历史积压，并非渐进式劣化。建议 Fixer 分批执行状态晋升，而非全部标记为问题。

部分代表性条目（完整列表见数据库草稿视图）：

- [SuperConductor](entities/SuperConductor.md)（entity，2026-04-11，内容完整，含 mention-page）

- [Pal](entities/Pal.md)（entity，2026-04-11，内容完整，纯文本引用）

- [automation-workflows](entities/automation-workflows.md)（entity，2026-04-11，内容完整，纯文本引用）

- [OpenSandbox](entities/OpenSandbox.md)（entity，2026-04-11，内容完整，纯文本引用）

- [模型自我进化](concepts/模型自我进化.md)（concept，2026-04-11，内容完整，纯文本引用）

- [yoyo](entities/yoyo.md)（entity，2026-04-15）

- [Claude Opus](entities/Claude Opus.md)（entity，2026-04-16）

- [Devin](entities/Devin.md)（entity，2026-04-16）

- [flow matching](concepts/flow matching.md)（concept，2026-04-17，**标签为空**）

- [Gemini Robotics-ER](entities/Gemini Robotics-ER.md)（entity，2026-04-15）

---

## 过时内容（>30天未编译）

✅ **无过时内容**

数据库建立仅 17 天，所有非系统页均在 30 天内编译。7 个系统 concept 页（关于 Wiki Compiler、关于 Wiki Lint Agent 等）compile_time 为 null，按规则豁免。

---

## 重复疑似

### A. Concept/Entity 完全同名重复

✅ **未发现完全同名重复**

### B. Concept/Entity 近似重复（归一化后命中）

| 条目 A | 条目 B | 差异原因 |

| --- | --- | --- |

| [Untitled](entities/llm-wiki.md)（entity） | [Untitled](entities/llm-wikid.md)（entity） | 仅末尾多一个字母 'd'，高度疑似重复 |

| [Untitled](concepts/LLM+Markdown+Wiki 知识库.md)（concept） | [Untitled](concepts/Karpathy LLM Wiki 方法论.md)（concept） | 主题高度重叠，前者偏产品形态，后者偏方法论，建议人工确认是否合并 |

| [Untitled](concepts/Memory Folder.md)（concept） | [Untitled](concepts/Smart Extraction.md)（concept） | 同属 Claude Code 记忆模块，功能有重叠，建议确认区分 |

### C. Summary 完全同名重复

✅ **SQL 查询未发现完全同名 summary**

### D. Summary 近似同名重复（归一化后命中）

共发现 **11 组** 近似重复（每 10 组扣 1 分）：

| 组别 | 条目 | 差异原因 |

| --- | --- | --- |

| Alice/MemPalace（4条） | Untitled
Untitled
[Untitled](summaries/摘要：太抽象了，Alice 都来了。MemPalace AI记忆系统.md)
Untitled | 标题变体、截断差异 |

| Hermes 又来了（4条） | Untitled
[Untitled](summaries/摘要：不是，咋又来了一个 Hermes？OpenClaw vs Hermes Agent 对比.md)
Untitled | 标题变体、副标题差异 |

| Hermes 实测（2条） | [Untitled](summaries/摘要：Hermes Agent 实测，龙虾新对手是进化版爱马仕.md)
Untitled | 空格差异 + 省略「版」字 |

| oMLX TurboQuant（4条） | Untitled
Untitled
Untitled
[Untitled](summaries/摘要：Mac用户可以在oMLX中使用TurboQuant了，搭配Gemma-4-31B实测.md) | 标题截断 + 空格差异 |

| OiiOii 对话（3条） | [Untitled](summaries/摘要：对话 OiiOii 创始人闹闹：做 AI 时代的皮克斯.md)
Untitled
Untitled | 空格 + 错字（皂→皮）+ 来源后缀差异 |

| Karpathy LLM+Wiki 实操（2条） | [Untitled](summaries/摘要：实操指南：如何用 Karpathy 的 LLM+Markdown+Wiki 搭建个人知识库.md)
Untitled | 加号空格差异 |

| AI 漫剧（2条） | [Untitled](summaries/摘要：一键搞定全流程！AI 漫剧一站式生成工具分享.md)
Untitled | 空格 + 末尾感叹号差异 |

| Corporate Audit AI（2条） | [Untitled](summaries/摘要：Corporate Audit AI：用 AI Agent 扒上市公司年报，$AUDIT 市值冲破千万.md)
Untitled | 错字（扬→扒、値→值） |

| OpenAI 超级智能新政（2条） | Untitled
[Untitled](summaries/摘要：刚刚，OpenAI 发了一份 13 页的「超级智能新政」.md) | 前缀「刚刚，」差异 |

| Agency Agents（2条） | [Untitled](summaries/摘要：Agency Agents：用 147 个 AI 专家角色，把 Claude Code 变成一整家公司.md)
[Untitled](summaries/摘要：agency-agents：用 147 个 Markdown 文件，搭建你的零成本 AI 专业团队.md) | 来源/角度差异，可能是不同文章 |

| Anthropic 封杀 OpenClaw（2条） | [Untitled](summaries/摘要：突发！Anthropic 封杀 OpenClaw，龙虾之父：说服失败.md)
[Untitled](summaries/摘要：Claude封杀OpenClaw！龙虾之父回应.md) | 标题视角不同，可能是不同文章/转发 |

---

## 状态异常

✅ **未发现状态为空/null 的条目**

---

## 标签异常

### 1. 缺失标签（null/空）

- [flow matching](concepts/flow matching.md)（concept，草稿，2026-04-17）— 标签为空，需补充

### 2. 已废弃标签使用情况

**⚠️ 系统性问题：废弃标签系统与现行 3-维度标签体系不一致**

根据最新 Wiki Schema 规则，以下标签已退休：

- **早期废弃**：AI Agent、MCP、Notion

- **新退休（2026-04 批次）**：LLM、Agent 框架、Agent 编排、Agent 技能、Coding Agent、开发工具、工作流、记忆系统、安全/隐私、Crypto/DeFi、内容创作

从已查阅的约 300 条 concept/entity 记录中，**绝大多数（估计 90%+）**至少使用了一个新退休标签。估算受影响条目：**约 2000~2300 条**（占 concept+entity 总量的 ~85%）。

这属于全局性 Schema 迁移问题，不适合逐条修复，需要人工决策（见改进建议 👤 人工介入项）。

---

## 标签分布统计

> 注：当前 SQL 不支持 multi-select 展开计数，以下为从抽样数据中观察到的高频标签估算。完整统计需由 Autofill Agent 或批量脚本执行。

| 标签 | 状态 | 估算频率 |

| --- | --- | --- |

| OpenClaw | ✅ 活跃 | 极高（>150条） |

| 知识管理 | ✅ 活跃 | 极高（>120条） |

| 商业/生态 | ✅ 活跃 | 高（>80条） |

| Agent 协作模式 | ✅ 活跃 | 高（>70条） |

| 多Agent协作 | ✅ 活跃 | 高（>60条） |

| 上下文管理 | ✅ 活跃 | 高（>50条） |

| RAG/检索 | ✅ 活跃 | 高（>50条） |

| AI 产品 | ✅ 活跃 | 高（>60条） |

| Agent 编排 | ⚠️ 新退休 | 极高（>200条） |

| Crypto/DeFi | ⚠️ 新退休 | 极高（>180条） |

| LLM | ⚠️ 新退休 | 极高（>150条） |

| Agent 框架 | ⚠️ 新退休 | 高（>100条） |

| 工作流 | ⚠️ 新退休 | 高（>100条） |

| 记忆系统 | ⚠️ 新退休 | 高（>80条） |

| Coding Agent | ⚠️ 新退休 | 高（>70条） |

| Agent 技能 | ⚠️ 新退休 | 高（>100条） |

| 内容创作 | ⚠️ 新退休 | 中（>50条） |

| 安全/隐私 | ⚠️ 新退休 | 中（>30条） |

| 开发工具 | ⚠️ 新退休 | 中（>30条） |

---

## 类型启发式筛查结果（疑似 concept → entity）

以下为规则匹配结果，**建议人工确认**，未自动判定。

| 条目 | 当前类型 | 命中规则 | 理由 |

| --- | --- | --- | --- |

| [Untitled](concepts/CodeBrain.md) | concept | 规则 C | 英文专有名词，具体 Coding Agent 产品 |

| [Untitled](concepts/GraphRAG.md) | concept | 规则 C | 微软特定命名检索系统 |

| [Untitled](concepts/Smallville.md) | concept | 规则 C | 斯坦福具体命名的多 Agent 模拟平台 |

| [Untitled](concepts/Darwin Gödel Machine.md) | concept | 规则 C | 特定命名的自进化 AI 系统（论文成果） |

| [Untitled](concepts/G.A.M.E 框架.md) | concept | 规则 C | Virtuals Protocol 旗下具体框架产品 |

| [Untitled](concepts/OASIS.md) | concept | 规则 C+D | 大写缩写，具体命名的多 Agent 模拟系统 |

| [Untitled](concepts/GR4AD.md) | concept | 规则 C+D | 大写+数字组合，具体命名架构 |

| [Untitled](concepts/obsidian-cli.md) | concept | 规则 B | 含 cli 后缀，疑似具体工具产品 |

| [Untitled](concepts/CLI Harness.md) | concept | 规则 B | 含 CLI 前缀，疑似方法论或具体工具 |

| [Untitled](concepts/MTProto.md) | concept | 规则 B | Telegram 具体通信协议，应归为 entity |

| [Untitled](entities/memory-lancedb-pro.md) | concept | 规则 B+C | 具体工具命名，含 pro 版本暗示 |

---

## 标签分类合理性检查

**抽样覆盖**：通过加载 6 个草稿页面进行分析。

**发现**：当前条目使用的大量「新退休」标签（LLM、Agent 框架、记忆系统等）本身在新 3-维度体系中已无对应位置，导致分类合理性检查无法按新体系评估。核心问题是标签体系本身需要先迁移，再评估合理性。

暂无明显个体误分类发现（需在标签体系迁移后重新扫描）。

---

## 引用结构化检查

### 🚨 系统性问题

**抽样方法**：从最早创建的草稿批次（2026-04-11）中随机抽取 6 条 concept/entity 页面。

**结果统计**：

| 页面 | 来源引用格式 | 结论 |

| --- | --- | --- |

| [Untitled](entities/SuperConductor.md) | 含 `&lt;mention-page&gt;` | ✅ 结构化 |

| [Untitled](entities/Pal.md) | 纯文本（「摘要：...（X书签）」） | ❌ 纯文本 |

| [Untitled](entities/automation-workflows.md) | 纯文本（「摘要：OpenClaw 飞轮启动指南（X书签）」） | ❌ 纯文本 |

| [Untitled](concepts/Tool Registry.md) | 纯文本（《...》｜X书签文章｜原文链接） | ❌ 纯文本 |

| [Untitled](entities/OpenSandbox.md) | 纯文本（[原文链接](...)｜《...》） | ❌ 纯文本 |

| [Untitled](concepts/模型自我进化.md) | 纯文本（[原文链接](...)｜《...》） | ❌ 纯文本 |

- **Affected page rate**：5/6 = **83%** ≥ 30% 阈值 → 🚨 系统性问题触发

- **Plain-text rate**：5/6 = **83%**

- **估算受影响条目数**：978 条草稿 concept/entity × 83% ≈ **约 812 条**需要引用升级

**影响**：纯文本引用会导致：孤岛检测失准（无法通过 mention-page 发现引用关系）；状态晋升无法执行（completeness check 要求至少 1 个 mention-page）；知识图谱断链。

**建议**：Wiki Fixer 逐条修复不现实（812+ 条），需建立独立的「引用升级员」Autofill Agent 批量处理（见 👤 人工介入项）。

---

## 计分明细

| 检查项 | 发现数量 | 单项扣分 | 小计 |

| --- | --- | --- | --- |

| 起始分 | — | — | +100 |

| 孤岛条目（估算） | ~5 条 | -5/条 | -25 |

| 过期草稿（>7天） | 242 条 | -3/条 | -726 |

| 过时内容（>30天） | 0 条 | -3/条 | 0 |

| 疑似重复对（concept/entity） | 2 对 | -10/对 | -20 |

| Summary 重复（11组） | 11 组 | -1/10组 | -1 |

| 状态异常 | 0 | -2/条 | 0 |

| 缺失标签 | 1 条 | -2/条 | -2 |

| 废弃标签（系统性） | ~2000 条 | 按系统性处理 | 见 👤 介入项 |

| 纯文本引用（5条样本） | 5/6 = 83% | -1/5条 | -1 |

| 引用问题系统性额外扣分 | 1 次 | -10 | -10 |

| **合计** | — | — | **MAX(0, 100-765) = 0** |

> 💡 实际健康度说明：如去除「首批编译积压」这一历史因素（242 条草稿均来自 2026-04-10 至 2026-04-12 的初始化批次），扣除草稿分后剩余扣分约 -39，调整后分数 ~61/100（🟡）。

---

## 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 |

| --- | --- | --- | --- |

| [Untitled](entities/SuperConductor.md) | 草稿 | 审核中 | 创建 >7天，含定义+核心特点+结构化 mention-page 引用，内容完整 |

| 242 条过期草稿中含 mention-page 的条目 | 草稿 | 审核中 | 需 Fixer 逐条确认内容完整性（定义+关键要点+mention-page 引用），批量晋升 |

| 所有 summary（当前已全部为已审核） | 已审核 | 无需变更 | ✅ summary 全部已审核，符合预期 |

| Synthesis 审核中（6条） | 审核中 | 待人工确认 | 综合分析类，需人工评估是否符合已审核标准 |

---

## 改进建议

### 🤖 自动修复项（Fixer 可直接执行）

1. **补充缺失标签**

  - 修复类型：属性更新

  - 目标：[flow matching](concepts/flow matching.md)

  - 操作：添加合适标签（建议：训练/微调）

1. **删除 Summary 重复条目**

  - 修复类型：页面删除

  - Alice/MemPalace 组：保留 [https://www.notion.so/7e12d84239d445c19dc02966032f57e7（最完整标题），删除](https://www.notion.so/7e12d84239d445c19dc02966032f57e7（最完整标题），删除) [https://www.notion.so/0f9d6a3bc1ec458faed2cf6678446df1、https://www.notion.so/4d8ee340a337481dba94b753ae1a0a02、https://www.notion.so/5c479478715d4e1ba1868bfdfc4b2168](https://www.notion.so/0f9d6a3bc1ec458faed2cf6678446df1、https://www.notion.so/4d8ee340a337481dba94b753ae1a0a02、https://www.notion.so/5c479478715d4e1ba1868bfdfc4b2168)

  - Hermes 又来了组：保留 [https://www.notion.so/a1e49e306b514720a81441764aa0b635（最完整），删除](https://www.notion.so/a1e49e306b514720a81441764aa0b635（最完整），删除) [https://www.notion.so/a5f5724349484c15b3af4a94247e1656、https://www.notion.so/9f3e8f8138e14b3a81ab324191cfe6ea](https://www.notion.so/a5f5724349484c15b3af4a94247e1656、https://www.notion.so/9f3e8f8138e14b3a81ab324191cfe6ea)

  - Hermes 实测组：保留 [https://www.notion.so/0cc24936b20e4007a2df2a294012aedb，删除](https://www.notion.so/0cc24936b20e4007a2df2a294012aedb，删除) 摘要：Hermes Agent实测，龙虾新对手是进化爱马仕

  - oMLX TurboQuant 组：保留 [https://www.notion.so/84942898e02642a68e6aa7cf9e702945（空格规范），删除](https://www.notion.so/84942898e02642a68e6aa7cf9e702945（空格规范），删除) [https://www.notion.so/5744e1cff69440758ac3dea9d12f3b12、https://www.notion.so/7f4baca9d5e046cdbe33a886b63fb201、https://www.notion.so/1700f5a80a434959b44dffe38ec1e43d](https://www.notion.so/5744e1cff69440758ac3dea9d12f3b12、https://www.notion.so/7f4baca9d5e046cdbe33a886b63fb201、https://www.notion.so/1700f5a80a434959b44dffe38ec1e43d)

  - OiiOii 对话组：保留 [https://www.notion.so/e5022ab129704c63b4a4373281b38a06，删除](https://www.notion.so/e5022ab129704c63b4a4373281b38a06，删除) [https://www.notion.so/6451023912594e598b23cf2d80db0c94、https://www.notion.so/09270b2a613c44a9b612e20a8098a0d7](https://www.notion.so/6451023912594e598b23cf2d80db0c94、https://www.notion.so/09270b2a613c44a9b612e20a8098a0d7)

  - Karpathy LLM+Wiki 组：保留 [https://www.notion.so/2e2506b1c37940539a1e8c0264c559a2（空格规范），删除](https://www.notion.so/2e2506b1c37940539a1e8c0264c559a2（空格规范），删除) [摘要：实操指南：如何用 Karpathy 的 LLM+Markdown+Wiki 搭建个人知识库](summaries/摘要：实操指南：如何用 Karpathy 的 LLM+Markdown+Wiki 搭建个人知识库.md)

  - AI 漫剧组：保留 [https://www.notion.so/1f12afbbd7344886b7b0a4375e46b2c2，删除](https://www.notion.so/1f12afbbd7344886b7b0a4375e46b2c2，删除) 摘要：一键搞定全流程！AI漫剧一站式生成工具分享！

  - Corporate Audit AI 组：保留 [https://www.notion.so/c6ff284406d44dc1ac7ee7efa1910cf9（无错字），删除](https://www.notion.so/c6ff284406d44dc1ac7ee7efa1910cf9（无错字），删除) 摘要：Corporate Audit AI：用 AI Agent 扬上市公司年报，$AUDIT 市値冲破千万

  - OpenAI 新政组：保留 [https://www.notion.so/7170b74d15384ea2927ce1b88f7c2cda，删除](https://www.notion.so/7170b74d15384ea2927ce1b88f7c2cda，删除) [摘要：刚刚，OpenAI 发了一份 13 页的「超级智能新政」](summaries/摘要：刚刚，OpenAI 发了一份 13 页的「超级智能新政」.md)

1. **近似重复 concept/entity 合并**

  - [llm-wiki](entities/llm-wiki.md) 与 [llm-wikid](entities/llm-wikid.md)：确认后保留内容更完整的，合并另一个内容并删除

1. **SuperConductor 状态晋升**

  - 目标：[SuperConductor](entities/SuperConductor.md)

  - 操作：状态从「草稿」更新为「审核中」

1. **草稿批量晋升筛查**

  - 操作：对 242 条过期草稿，逐条加载检查是否含 `<mention-page>` 引用，符合条件者更新状态为「审核中」

  - 优先顺序：按创建时间从最旧开始处理

---

### 👤 人工介入项

1. **🚨 引用结构化系统性问题：建立「引用升级员」Autofill Agent**

  - **问题规模**：样本 83% 的草稿页面使用纯文本引用（估算 ~812 条受影响）

  - **Wiki Fixer 无法胜任**：逐条修复需要 800+ 次 loadPage + updatePage，超出单次修复能力

  - **建议行动**：建立独立 Autofill Agent（引用升级员），专门执行以下循环：

    1. 读取 concept/entity 页面的「来源引用」区块

    1. 从纯文本引用中提取摘要标题关键词

    1. 用 Notion search 找到对应 summary 页面 URL

    1. 将纯文本替换为 `<mention-page>` 结构化引用

    1. 循环直到全库完成

  - **等效手动指令模板**（供 Fixer 小批量测试）：

    > Wiki Fixer，对以下页面执行引用升级：

    > 1. 加载页面，找到「来源引用」区块

    > 2. 搜索对应 summary 页面

    > 3. 将纯文本引用替换为 `<mention-page url="xxx">摘要标题</mention-page>`

    > 目标页面：[https://www.notion.so/e9b6274a9b8742d399378a759f0b3f66、https://www.notion.so/3264e3fa96a341cbaedf1563df82316f、https://www.notion.so/d980660047594c17b8aa54e03bdda907、https://www.notion.so/050fbeec038e4c6da9dc615ac5c65d1b、https://www.notion.so/3aa4e698c7be40a385fe1ef13b9ee66e](https://www.notion.so/e9b6274a9b8742d399378a759f0b3f66、https://www.notion.so/3264e3fa96a341cbaedf1563df82316f、https://www.notion.so/d980660047594c17b8aa54e03bdda907、https://www.notion.so/050fbeec038e4c6da9dc615ac5c65d1b、https://www.notion.so/3aa4e698c7be40a385fe1ef13b9ee66e)

1. **标签体系迁移（Schema 变更）**

  - **问题**：现有 11 个「新退休」标签仍在 Schema 中存在，且约 85% 条目使用这些标签

  - **需要人工决策**：

    - 确认新 3-维度标签体系的完整 active 标签列表

    - 制定旧标签 → 新标签的映射规则（如：「记忆系统」→「长期记忆」+「上下文管理」）

    - 授权 Fixer 执行批量重新打标

    - 完成后从 Schema 中删除废弃标签选项

  - **规模估算**：~2000 条条目需重新打标

1. **类型误分类人工确认**

  - 对「类型启发式筛查」中的 11 条疑似 concept→entity 条目，逐条人工确认是否改为 entity 类型

  - 优先确认：CodeBrain、GraphRAG、MTProto、Darwin Gödel Machine

1. **孤岛二轮验证**

  - 对「孤岛条目」中列出的 6 个疑似孤岛，由 Gap Agent 执行 Notion search 验证

  - 如确认为孤岛，决定是删除还是补充来源引用

1. **LLM+Markdown+Wiki 知识库 vs Karpathy LLM Wiki 方法论合并**

  - 两条 concept 主题重叠，需人工判断是否保留两条独立词条或合并

---

>  请根据以上报告执行自动修复。
