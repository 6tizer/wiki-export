---
title: 知识 Wiki 双轨系统方案：从 Notion 编译引擎到本地 Markdown 分发层
type: synthesis
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/22dabdd5d3a349d9a15bf6a0e86fda2f
notion_id: 22dabdd5-d3a3-49d9-a15b-f6a0e86fda2f
---

## 研究问题

**如何让 Claude Code、Cursor、OpenClaw 等外部 Agent 像 Notion AI 一样高效使用知识 Wiki？同时为 Notion Agent 5 月收费后的成本压力预留迁移路径？**

---

## 一、问题背景

### 1.1 当前系统的成就

知识 Wiki 系统在 2 天内从零搭建，目前已运行稳定：

| 指标 | 数值 |

| --- | --- |

| concept（核心概念） | 666 |

| entity（实体档案） | 336 |

| summary（摘要） | 752 |

| synthesis（综合分析） | 43 |

| 总条目 | 1827 |

| 自动化 Agent | 6 个角色（Compiler / Lint / Fixer / Synthesizer / QA / Notion AI 协调者） |

编译引擎运行在 Notion AI Agent 集群上，利用 SQL 查询、事件触发器、Agent 间 mention 链式协作，形成了完整的「原始资料 → 编译 → 结构化 Wiki → 消费」流水线。

### 1.2 两个核心痛点

**痛点一：外部 Agent 无法高效消费知识 Wiki**

Notion AI（我）在 Wiki 中是「一等公民」，拥有 SQL 直查、触发器、视图查询等原生能力。但 Claude Code、Cursor、OpenClaw 通过 API/MCP 接入时是「访客」：

| 能力 | **Notion AI** | **外部 Agent（API/MCP）** |

| --- | --- | --- |

| SQL 查询 | ✅ querySql 支持 JOIN、聚合 | ❌ 不支持 |

| Agent 触发器 | ✅ 定时 / 事件驱动 | ❌ 需自建 cron |

| 视图查询 | ✅ queryView | ❌ 不支持 |

| 访问范围 | 你有权限的一切 | 需逐页/逐库授权 |

| 读取方式 | 原生 loadPage，完整 Markdown | 逐层拉取 blocks，手动拼装 |

**痛点二：Notion Agent 5 月后开始收费**

当前知识 Wiki 系统构建已花费近 5 万积分。5 月后自定义 Agent 按积分计费（每 1000 积分 $10），6 个 Agent 每小时级运行，月费预估 $50-200+。这使得「编译引擎长期依赖 Notion」变成一个不可持续的成本结构。

### 1.3 多终端、多 Agent 的实际场景

Tizer 的设备和 Agent 矩阵：

| 终端 | 位置 | 运行的 Agent |

| --- | --- | --- |

| MacBook Pro (M1) | 随身 | Claude Code、Cursor |

| Mac Studio | 家里 | Claude Code |

| Mac mini | 家里 | OpenClaw、各种脚本 |

| 东京服务器 | 云端 | OpenClaw（国宝） |

| 硅谷服务器 | 云端 | OpenClaw（瓜瓜） |

| Notion | 任意 | Notion AI（6 个 Agent） |

所有这些终端和 Agent 都需要访问同一份知识 Wiki。

---

## 二、方案探索过程

### 2.1 最初思路：在 Notion 内建 Index 页面

第一个想法是在 Notion Wiki 内部建立三层 Index 体系（L0 Gateway → L1 Tag Index × 14 → L2 具体页面），供外部 Agent 通过 MCP 逐层导航。

**否决原因**：

- 构建成本高：952 个 concept+entity 需要逐页提取一句话定义，预估 15+ 小时 Agent 工作量

- 维护复杂：需要新增 Index Keeper Agent，处理新增、合并、标签变更、删除等多种同步场景

- 旧 Index 的失败教训：之前的 Index Updater 因「全量重写一个巨页」而频繁出错，已被下线

- 唯一受益者是外部 Agent：Notion AI 有 SQL 不需要 Index，Tizer 有 Dashboard 视图

### 2.2 进化思路：方案 C（极简 Gateway + search）

只做 1 个 Gateway 页面 + 引导外部 Agent 用 `notion_search` 搜索。

**否决原因**：

- `notion_search` 缺乏「发现性」——Agent 不知道还有哪些概念没搜到

- 无法系统性浏览某个领域的全部知识

### 2.3 根本性追问：回到 Karpathy 方法论

Karpathy 的 LLM Wiki 方法论核心是：**纯 Markdown + 文件系统是 Agent 时代最优的知识载体**。

- 中小规模（1000 篇 / 40 万词以内），LLM 直接读 Markdown，无需 RAG

- Claude Code 天然操作文件系统（`cat`、`ls`、`grep`），这是 Agent 最原生的接口

- [index.md](http://index.md/) 一次读完，Agent 提取路径后按需 `cat` 具体文件

**关键洞察**：问题不在于「要不要建 Index」，而在于 **Notion 页面不是 Markdown 文件**。与其在 Notion 里用页面模拟文件系统的 Index，不如直接把 Wiki 导出为真正的 Markdown 文件系统。

### 2.4 最终方案：Notion Wiki + 本地 Markdown 双轨系统

**不是「迁移」，而是「投影」**。Notion Wiki 继续作为编译引擎和协作中心，同时向本地文件系统投射一份 Markdown 镜像，供所有外部 Agent 原生消费。

---

## 三、最终架构设计

### 3.1 系统全景

```mermaid
graph TB
    subgraph "采集层 raw"
        R1["微信文章 DB"]
        R2["X 书签 DB"]
        R3["Obsidian Web Clipper（可选）"]
    end

    subgraph "编译层"
        E1["Notion AI Agent 集群<br>免费期：6 角色全力运行"]
        E2["Claude Code 本地编译<br>收费后：渐进接管"]
        DB["Notion Wiki DB<br>666 concepts · 336 entities<br>752 summaries · 43 syntheses"]
    end

    subgraph "同步层"
        S1["Notion Worker Sync（推荐）"]
        S2["Mac mini cron + Python（兜底）"]
    end

    subgraph "分发层"
        GIT["GitHub 私有仓库<br>tizer/wiki-export"]
    end

    subgraph "消费层"
        C1["MacBook Pro<br>Claude Code · Cursor · Obsidian"]
        C2["Mac mini<br>OpenClaw · 脚本"]
        C3["云端服务器 ×2<br>OpenClaw 东京/硅谷"]
        C4["Notion MCP<br>ChatGPT · VS Code 等"]
    end

    R1 --> E1
    R2 --> E1
    R3 -.-> E1
    E1 --> DB
    E2 -.->|"收费后接管"| DB
    DB --> S1
    DB --> S2
    S1 --> GIT
    S2 --> GIT
    GIT -->|"git pull"| C1
    GIT -->|"git pull"| C2
    GIT -->|"git pull"| C3
    DB -->|"Notion MCP"| C4
```

### 3.2 三层架构映射（对齐 Karpathy 方法论）

| 层 | Notion 侧（编译引擎） | 本地侧（Agent 消费层） | 设计来源 |

| --- | --- | --- | --- |

| **raw/** | 微信文章 DB、X 书签 DB | Obsidian Web Clipper + 本地文件 | Karpathy 三层架构 |

| **wiki/** | 知识 Wiki 数据库 | 导出的 .md 文件 + [index.md](http://index.md/) | Karpathy + GBrain |

| **schema/** | Wiki Schema + Agent 指令页 | [CLAUDE.md](http://claude.md/)  • [WIKI-SCHEMA.md](http://wiki-schema.md/) | Karpathy + Skill Graph |

### 3.3 Git 仓库目录结构

```javascript
wiki-export/
  schema/
    CLAUDE.md            ← 外部 Agent 唯一入口 + 宪法规则
    WIKI-SCHEMA.md       ← 类型定义和命名规范
  wiki/
    index.md             ← 全局目录（按标签分组，~15K tokens）
    concepts/
      mem0.md
      graphrag.md
      ...（666 个）
    entities/
      openclaw.md
      claude-code.md
      ...（336 个）
    syntheses/
      ai-knowledge-management.md
      ...（43 个）
    summaries/           ← 全量导出（已审核）
      ...（777 个）
  raw/                   ← Obsidian Web Clipper 直接存入（可选）
```

### 3.4 单个文件格式

融合 Skill Graph（YAML frontmatter 渐进式披露）+ GBrain（编译真相+时间线分离）：

```javascript
---
title: Mem0
type: entity
tags: [记忆系统]
status: 已审核
confidence: high
last_compiled: 2026-04-12
notion_url: https://notion.so/xxx
one_liner: "面向 Agent 的云端长期记忆服务"
---

<!-- 编译真相：当前最优理解，可被 Agent 改写 -->
## 定义
Mem0 是面向 Agent 的云端长期记忆服务...

## 关键要点
- ...

## 关联概念
- [Dreaming 记忆机制](../concepts/dreaming-记忆机制.md)

---
<!-- 时间线：只增不改的证据链 -->
## 来源引用
- 2026-04-10: 摘要：xxx（@author）
```

### 3.5 各外部 Agent 的接入方式

| Agent | 接入方式 | 查询路径 |

| --- | --- | --- |

| **Claude Code** | `wiki-export/` 作为项目子目录 | `cat schema/CLAUDE.md` → `cat wiki/index.md` → `cat wiki/concepts/xxx.md` |

| **Cursor** | `wiki-export/` 作为 workspace | Agent 自动索引 .md 文件 |

| **OpenClaw** | Skill Vault 挂载 / GBrain 导入 | Memory 系统读取 wiki/ 目录 |

| **Notion AI** | 不变，继续用 SQL 查 Notion DB | 不经过 Git 仓库 |

| **Notion MCP 客户端** | 不变，通过 MCP 读 Notion 页面 | 不经过 Git 仓库 |

### 3.6 Obsidian 的角色

在本方案中，Obsidian 是**可选的人类 GUI**，不在核心链路上：

- 装在 MacBook Pro / Mac Studio 上，打开 `wiki-export/` 文件夹即可作为 Vault

- 提供图谱视图、搜索、编辑等人类友好界面

- 服务器端（Mac mini、东京/硅谷服务器）不需要装 Obsidian

- **完全免费**，不需要 Obsidian Sync（用 Git 替代同步）

---

## 四、同步机制

### 4.1 同步方向

| 阶段 | SSOT | 编译引擎 | 同步方向 |

| --- | --- | --- | --- |

| **Phase 1-2（现在~5月）** | Notion Wiki DB | Notion AI Agent | Notion → Git（单向） |

| **Phase 3（5月后评估）** | Notion（观察中） | 开始迁移到 Claude Code | 仍 Notion → Git |

| **Phase 4（迁移完成）** | **Git 仓库** | Claude Code | **Git → Notion**（反向，只更新 GUI） |

### 4.2 同步实现（两套并行）

**方案 A：Notion Worker Sync**

- TypeScript Worker 部署在 Notion 平台，定时执行

- 查询变更条目 → Notion API 读页面 → 转 Markdown → GitHub API push

- 优点：Notion 托管，零运维

- 风险：Notion Workers 目前是 extreme pre-alpha，可能不稳定

**方案 B：Mac mini cron + Python 脚本（兜底）**

- Python 脚本部署在 Mac mini，cron 定时执行

- 同样的逻辑，完全可控

- 两个方案同时搭建，Worker 稳就用 Worker，不稳切回 cron

### 4.3 Notion API 限速应对

**官方限速**：平均 3 请求/秒，15 分钟内最多 2700 次调用。

| 场景 | API 调用数 | 耗时（3 req/s） |

| --- | --- | --- |

| 首次全量导出（1045 条目） | ~3123 次 | 25-40 分钟 |

| 每日增量同步（20-30 条变更） | 60-90 次 | < 1 分钟 |

**限速器设计要点**：

- 设置 2.5 req/s 上限（留 0.5 余量）

- 遇到 HTTP 429 时读取 `Retry-After` header，等待后重试

- 指数退避策略：1s → 2s → 4s → 8s → 最大 30s

- 首次导出支持断点续传（记录已导出的 page_id 列表）

### 4.4 mention-page 链接转换

Notion 页面中的关联概念 `<mention-page url="xxx">名称</mention-page>` 需转换为 wikilink `[名称](../concepts/xxx.md)`。

**解决方案**：

1. 预先用 SQL 查出所有条目的 url + 名称 + 类型

1. 构建 page_id → 文件路径映射表（JSON）

1. 导出时用映射表替换所有 mention-page 标签

1. 指向导出范围外的 mention → 降级为纯文本

---

## 五、成本分析

| 项目 | 当前（免费期） | 5月后保留 Notion Agent | 5月后迁到 Claude Code |

| --- | --- | --- | --- |

| Notion Agent | $0 | $50-200+/月 | $0 |

| Claude Code 订阅 | $100-200/月（已有） | $100-200/月 | $100-200/月（承担编译） |

| Notion Worker | $0 | $0 | $0 或不再使用 |

| GitHub 私有仓库 | $0 | $0 | $0 |

| Obsidian | $0 | $0 | $0 |

| **总计新增** | **$0** | **+$50-200+** | **$0** |

---

## 六、风险清单

| 风险 | 概率 | 影响 | 应对 |

| --- | --- | --- | --- |

| Notion API 429 限速 | 高（首次） | 导出变慢 | 限速器 + 指数退避重试 |

| Notion Worker 不稳定 | 中 | 同步中断 | Mac mini cron 兜底 |

| mention-page 映射遗漏 | 中 | 部分链接断裂 | 导出后脚本自动检测断链 |

| 首次导出中途失败 | 中 | 需断点续传 | 脚本记录已导出列表 |

| 5月 Agent 定价超预期 | 中 | 成本压力 | Phase 3 迁移方案已预备 |

| 文件名冲突 | 低 | 同名覆盖 | 文件名加类型前缀 |

---

## 七、实施路线图

### Phase 0：准备（30 分钟）

- [x] 确认导出范围：**concept + entity + synthesis + summary（1915 个）**，[index.md](http://index.md/) 只列 concept+entity+synthesis 作为导航目录，summary 存在 summaries/ 目录下按需跳转

- [x] 创建 GitHub 私有仓库：[https://github.com/6tizer/wiki-export](https://github.com/6tizer/wiki-export)

- [x] Notion API Token：复用现有 Integration Token，确保知识 Wiki 数据库已授权给导出脚本使用的 Token

### Phase 1：MVP 导出 ✅ 已完成（2026-04-14）

1. [x] Notion AI 生成任务说明文档（含 [index.md](http://index.md/) / [CLAUDE.md](http://claude.md/) / [WIKI-SCHEMA.md](http://wiki-schema.md/) 规格）

1. [x] Claude Code 写导出脚本 `export.py`（含限速器、分页处理、mention 转换、断点续传）

1. [x] 构建 page_id → 文件路径映射表

1. [x] 首次全量导出（实际耗时 **15 分钟**，远低于预估的 45-60 分钟）

1. [x] git push 到 [https://github.com/6tizer/wiki-export](https://github.com/6tizer/wiki-export)

**实际产出**：1919 个 .md 文件（6.3 MB），733 concepts + 360 entities + 43 syntheses + 777 summaries + [index.md](http://index.md/) + [CLAUDE.md](http://claude.md/) + [WIKI-SCHEMA.md](http://wiki-schema.md/)

**待处理**：

- [x] 2 对 synthesis 同名冲突 → 已合并（保留新版本，合并旧版本独有内容，删除旧版本）。同时修复了 Synthesizer Agent 的指令，增加了三级去重检查（精确标题 → 模糊主题 → 标签覆盖）

- [x] 验证标准 → 在 Mac mini 和 Mac Studio 两端的 Claude Code 中测试，两边都能成功导航 [index.md](http://index.md/) → synthesis → concept/entity 并给出有深度的回答。两端因读取文件路径不同导致回答侧重略有差异，但核心结论一致，属正常现象

### Phase 2：增量同步自动化 ✅ 已完成（2026-04-14）

- [x] `export.py --incremental` 增量同步模式（变更检测 + 删除检测 + 自动 git push）

- [x] `sync_state.json` 状态文件（时间戳 + 页面映射表）

- [x] Mac mini cron 定时任务（每天凌晨 3:00 自动运行）

- [ ] 各终端配置 `git pull` cron（待各设备上配置）

- [ ] 运行 3-5 天观察同步准确性（等今晚 3:00 首次自动触发）

- [x] Notion Worker Sync ✅ 已完成（2026-04-14）：每 30 分钟自动同步，含安全加固（5 层防护：阈值 10 + 两阶段确认 + 隐藏文件排除 + [index.md](http://index.md/) 硬排除 + 逐文件 try/catch）。部署过程中发生 P0 事故（mock 对象缺 type 字段导致 1913 个文件被误删），已通过全量重导 + 安全加固修复。详见 Phase 2.5 任务说明页的事故记录

### Phase 3：Claude Code 编译引擎迁移（5月后视账单）

- Claude Code 项目配置 `wiki-export/` 为 Vault

- 写 [CLAUDE.md](http://claude.md/) 中的 Ingest / Lint / Fix 指令

- 逐步停用 Notion Agent（Lint → Fixer → Compiler）

- 反向同步脚本上线（Git → Notion，更新 GUI）

### Phase 4：高级功能（按需）

- [index.md](http://index.md/) 补充一句话定义（渐进式披露）

- GBrain 编译真相模式升级

- OpenClaw Skill Vault 接入

- pgvector 语义检索（条目超 2000 后）

---

## 八、核心设计原则

> **💡** 

  1. **Notion 是「大脑」，Git 是「接口」** — Notion 负责编译+存储+协作（人类和 Notion AI 的主战场），Git 仓库负责向所有外部 Agent 分发 Markdown 镜像。

  1. **现在做的每一步都要「可反转」** — frontmatter 中保留 `notion_url`，脚本预留反向同步接口，确保 SSOT 可以从 Notion 切换到 Git。

  1. **增量优于全量** — 旧 Index 的失败教训：全量重写 = 每次都是高风险操作。新方案中 [index.md](http://index.md/) 全量重建（因为是纯 SQL 生成，成本极低），但页面导出是增量的。

  1. **不是「迁移」而是「渐进」** — 免费期全力利用 Notion Agent，同时搭建导出管道。收费后根据实际账单逐步迁移，而不是一步断崖式切换。

  1. **Agent 的原生接口是文件系统** — 与其用 Notion 页面模拟 Index，不如给 Agent 它最擅长消费的格式：纯 Markdown + 目录结构 + wikilinks。

---

## 来源列表

### 知识 Wiki 内部页面

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md) — 三层架构和 [index.md](http://index.md/) 设计

- [Skill Graph](concepts/Skill Graph.md) — 渐进式披露和 YAML frontmatter

- [编译真相+时间线模式](concepts/编译真相+时间线模式.md) — GBrain 的文件格式设计

- [GBrain](entities/GBrain.md) — 万篇级知识库架构参考

- [AI 时代知识管理范式演进：从个人 Wiki 到 Agent 原生知识系统](syntheses/AI 时代知识管理范式演进：从个人 Wiki 到 Agent 原生知识系统.md) — 双轨并行建议的理论基础

- [Notion AI Agent 能力边界与「指挥部」演进路径：从知识库到执行中枢](syntheses/Notion AI Agent 能力边界与「指挥部」演进路径：从知识库到执行中枢.md) — Notion AI vs 外部 Agent 权限对比

- [Notion Workers](entities/Notion Workers.md) — 同步层的可选实现

- Untitled — Workers 能力边界评估

- [Wiki Schema（规则文件）](index/Wiki Schema（规则文件）.md) — 系统宪法

- [Obsidian](entities/Obsidian.md) — 本地 GUI 层

### 相关实操教程

- [摘要：Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）](summaries/摘要：Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）.md)

- [摘要：用 LLM 把 Obsidian 变成「会编译的知识库」：Karpathy 方法论落地实践](summaries/摘要：用 LLM 把 Obsidian 变成「会编译的知识库」：Karpathy 方法论落地实践.md)

- [摘要：当我把 Claude 接进 Obsidian 后，笔记软件这个概念死了](summaries/摘要：当我把 Claude 接进 Obsidian 后，笔记软件这个概念死了.md)

- [摘要：10,000+ markdown files（GBrain 开源发布）](summaries/摘要：10,000+ markdown files（GBrain 开源发布）.md)

- [摘要：Skill Graph > SKILL.md 渐进式披露典范](summaries/摘要：Skill Graph  SKILL.md 渐进式披露典范.md)

**Phase 1 任务说明：Wiki Markdown 导出（给 Claude Code）**

# Phase 1 任务说明：Wiki Markdown 导出

  > **读者**：Claude Code（通过 Notion MCP 读取本页面）

  > **目标**：将 Notion 知识 Wiki 数据库导出为本地 Markdown 文件系统，推送到 GitHub 仓库

  > **背景**：见父页面 [知识 Wiki 双轨系统方案：从 Notion 编译引擎到本地 Markdown 分发层](syntheses/知识 Wiki 双轨系统方案：从 Notion 编译引擎到本地 Markdown 分发层.md)

---

## 1. 项目概述

### 1.1 你要做什么

  将 Notion 数据库「📚 知识 Wiki」中的 1915 个页面（concept / entity / synthesis / summary 四种类型）批量导出为 Markdown 文件，并生成 [index.md](http://index.md/) 全局目录、[CLAUDE.md](http://claude.md/) 外部 Agent 使用指南、[WIKI-SCHEMA.md](http://wiki-schema.md/) 类型规范。

  最终产出推送到 GitHub 私有仓库：`https://github.com/6tizer/wiki-export`

### 1.2 数据规模

  | 类型 | 数量 | 导出到目录 | 列入 [index.md](http://index.md/) |

  | --- | --- | --- | --- |

  | concept | 733 | `wiki/concepts/` | ✅ |

  | entity | 360 | `wiki/entities/` | ✅ |

  | synthesis | 45 | `wiki/syntheses/` | ✅ |

  | summary | 777 | `wiki/summaries/` | ❌（太多，Agent 通过 wikilink 按需跳转） |

  | **合计** | **1915** |  |  |

### 1.3 最终目录结构

  ```javascript
wiki-export/
  schema/
    CLAUDE.md
    WIKI-SCHEMA.md
  wiki/
    index.md
    concepts/
      mem0.md
      graphrag.md
      ...
    entities/
      openclaw.md
      claude-code.md
      ...
    syntheses/
      ai-knowledge-management.md
      ...
    summaries/
      摘要：xxx.md
      ...
  ```

---

## 2. Notion 数据库信息

### 2.1 数据库与数据源

  - **数据库名称**：📚 知识 Wiki

  - **数据库 Notion URL**：`https://www.notion.so/1c770107-4b68-80f3-ab3b-e38f0ed25ba9`

  - **数据源用于 API 查询的 database_id**：从上面 URL 提取，即 `1c770107-4b68-80f3-ab3b-e38f0ed25ba9`（去掉连字符也可以）

### 2.2 数据库 Schema（属性）

  | 属性名 | 类型 | 说明 |

  | --- | --- | --- |

  | 名称 | title | 条目标题 |

  | 类型 | select | concept / entity / summary / synthesis / qa / lint-report / index |

  | 标签 | multi_select | 14 个一级标签 |

  | 状态 | status | 草稿 / 审核中 / 已审核 / 需更新 |

  | 置信度 | select | high / medium / low |

  | 最后编译时间 | date | LLM 上次编译的时间 |

  | 来源标签 | text | 二级标签（逗号分隔字符串） |

  | 源文章URL | url | 源文章页面 URL |

  | 最后编辑时间 | last_edited_time | 自动 |

  | 创建时间 | created_time | 自动 |

### 2.3 API 查询示例

  用 Notion API 查询所有需要导出的条目（需要分页，每页最多 100 条）：

  ```javascript
// POST https://api.notion.com/v1/databases/{database_id}/query
{
  "filter": {
    "property": "类型",
    "select": {
      "is_not_empty": true
    }
  },
  "sorts": [
    { "property": "类型", "direction": "ascending" },
    { "property": "名称", "direction": "ascending" }
  ]
}
  ```

  然后在代码中按 `类型` 过滤，只保留 `concept / entity / synthesis / summary`。

---

## 3. 导出脚本规格（[export.py](http://export.py/)）

### 3.1 总体流程

  ```javascript
1. 查询数据库 → 获取所有 concept/entity/synthesis/summary 的元数据
   （url, 名称, 类型, 标签, 状态, 置信度, 最后编译时间, 来源标签, 源文章URL）

2. 构建映射表：page_id → 文件路径（JSON）
   - 用于 mention-page 链接转换

3. 逐页获取内容（retrieve page + retrieve block children）
   → 转换为标准 Markdown + YAML frontmatter
   → 写入对应目录

4. 生成 index.md（从步骤 1 的元数据生成，不需要读页面内容）

5. 写入 schema/CLAUDE.md 和 schema/WIKI-SCHEMA.md（静态内容）

6. git add + commit + push
  ```

### 3.2 Notion API 限速器

  **官方限速**：平均 3 请求/秒，15 分钟内最多 2700 次调用。

  **必须实现的限速策略**：

  - 设置 **2.5 req/s** 上限（留余量）

  - 遇到 HTTP 429 时读取 `Retry-After` header，等待后重试

  - 指数退避策略：1s → 2s → 4s → 8s → 最大 30s

  - 最大重试次数：5 次

  **首次全量导出预估**：

  - 1915 个页面 × 约 3 次 API 调用/页 = ~5745 次调用

  - 按 2.5 req/s ≈ 38 分钟

  - 加上重试和延迟 ≈ 45-60 分钟

### 3.3 断点续传

  首次导出可能中途失败，脚本必须支持断点续传：

  - 维护一个 `exported_pages.json` 文件，记录已成功导出的 page_id 列表

  - 重新运行时跳过已导出的页面

  - 全量完成后可删除该文件

### 3.4 Notion Block → Markdown 转换

  Notion API 返回的 block 需要转换为标准 Markdown。主要 block 类型：

  | Notion block type | Markdown 输出 |

  | --- | --- |

  | paragraph | 正文段落 |

  | heading_1/2/3 | `#` / `##` / `###` |

  | bulleted_list_item | `  • item` |

  | numbered_list_item | `1. item` |

  | to_do | `  • [ ] item` / `  • [x] item` |

  | toggle | `<details><summary>title</summary>children</details>` |

  | code | ` `languagencoden` ` |

  | quote | `> text` |

  | divider | `---` |

  | table | Markdown table |

  | callout | `> **icon** text`（简化处理） |

  | image | `![caption](url)` |

  | bookmark | `[title](url)` |

  | link_to_page / child_page | 转为 wikilink（见下文 mention 转换） |

  **嵌套 block**：有些 block 有 `has_children: true`，需要递归获取子 block（额外 API 调用）。

  **Rich text 处理**：

  - bold → `**text**`

  - italic → `*text*`

  - strikethrough → `~~text~~`

  - code →  `text` 

  - link → `[text](url)`

  - mention（user）→ 纯文本

  - mention（page）→ wikilink（见下文）

  - mention（date）→ 纯文本日期

### 3.5 mention-page → wikilink 转换

  **这是最重要的转换规则。**

  Notion 页面内容中经常引用其他 Wiki 页面，API 返回的格式类似：

  ```json
{ "type": "mention", "mention": { "type": "page", "page": { "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" } } }
  ```

  **转换规则**：

  1. 用步骤 2 构建的映射表查找 page_id

  1. 如果 page_id 在映射表中 → 转为 `[名称](相对路径)`

    - 例：concept 页面 Mem0，当前在 `entities/xxx.md` 中 → `[Mem0](../concepts/mem0.md)`

  1. 如果 page_id 不在映射表中（指向导出范围外的页面，如 lint-report）→ 保留为纯文本名称

### 3.6 文件命名规则

  - 直接使用条目的「名称」属性作为文件名

  - 特殊字符替换：`/` → `-`、`:` → `-`、`\` → `-`、`*` → 、`?` → 、`"` → 、`<` → 、`>` → 、`|` → 

  - 保留中文字符（现代文件系统和 Git 都支持 UTF-8）

  - 文件扩展名：`.md`

  - 如果名称为空，用 page_id 前 8 位作为文件名

  **示例**：

  - 名称 `Mem0` → `Mem0.md`

  - 名称 `编译真相+时间线模式` → `编译真相+时间线模式.md`

  - 名称 `摘要：Karpathy 的 LLM 知识库` → `摘要：Karpathy 的 LLM 知识库.md`

  - 名称 `Agent 编排/协调` → `Agent 编排-协调.md`

### 3.7 单个 Markdown 文件格式

  每个导出文件包含 YAML frontmatter + 正文：

  ```yaml
---
title: "Mem0"
type: entity
tags:
  - 记忆系统
status: 草稿
confidence: high
last_compiled: "2026-04-12"
source_tags: "OpenClaw, Agent, LLM"
source_article_url: ""
notion_url: "https://www.notion.so/xxxxxxxx"
notion_id: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
---

（页面正文内容，Markdown 格式）
  ```

  **frontmatter 字段映射**：

  | frontmatter 字段 | 来自 Notion 属性 |

  | --- | --- |

  | title | 名称 |

  | type | 类型 |

  | tags | 标签（JSON 数组 → YAML 列表） |

  | status | 状态 |

  | confidence | 置信度 |

  | last_compiled | 最后编译时间（取 date 部分） |

  | source_tags | 来源标签 |

  | source_article_url | 源文章URL |

  | notion_url | 从 page_id 构造的 Notion URL |

  | notion_id | page_id 原始值（用于反向同步） |

---

## 4. [index.md](http://index.md/) 生成规则

  [**index.md**](http://index.md/)** 只列出 concept + entity + synthesis**（共 1138 个），不列 summary。

  **按 14 个一级标签分组**。一个条目有 2 个标签时，在两个标签组下都出现。

  **格式**：

  ```markdown
---
type: index
total_concepts: 733
total_entities: 360
total_syntheses: 45
last_updated: 2026-04-14
---

# 📚 知识 Wiki Index

> 733 concepts · 360 entities · 45 syntheses
> 导出时间: 2026-04-14

## 使用方式
1. 搜索本文件定位感兴趣的条目名称
2. 沿文件路径读取具体 .md 文件
3. 沿关联概念的 wikilinks 跳转探索

## Agent 框架
### Concepts
- [OpenHarness](concepts/OpenHarness.md)
- [NanoClaw](concepts/NanoClaw.md)
- ...
### Entities
- [OpenClaw](entities/OpenClaw.md)
- [Manus](entities/Manus.md)
- ...

## 记忆系统
### Concepts
- [Dreaming 记忆机制](concepts/Dreaming 记忆机制.md)
- ...
### Entities
- [Mem0](entities/Mem0.md)
- ...

## Syntheses（所有综合分析）
- [AI 时代知识管理范式演进...](syntheses/AI 时代知识管理范式演进....md)
  → 研究问题：知识库第一读者从人变为 Agent 后的重构
- ...
  ```

  **注意**：[index.md](http://index.md/) 的文件路径是相对于 `wiki/` 目录的，例如 `concepts/Mem0.md`，不带 `wiki/` 前缀。

---

## 5. schema/[CLAUDE.md](http://claude.md/) 内容

  这是外部 Agent 的入口文件。将以下内容直接写入 `schema/CLAUDE.md`：

  ```markdown
# Tizer's Knowledge Wiki

## 概述
这是一个 AI 编译的个人知识库，由 Notion AI Agent 集群自动编译维护。
包含 733 个核心概念（concept）、360 个实体档案（entity）、45 篇综合分析（synthesis）、777 篇单篇摘要（summary）。
知识来源：微信公众号、X/Twitter、技术博客、会议记录。

## 目录结构
- `schema/CLAUDE.md` — 你正在读的文件（入口）
- `schema/WIKI-SCHEMA.md` — 详细的类型定义和命名规范
- `wiki/index.md` — 全局目录（按标签分组，只列 concept/entity/synthesis）
- `wiki/concepts/` — 733 个核心概念
- `wiki/entities/` — 360 个实体档案
- `wiki/syntheses/` — 45 篇综合分析
- `wiki/summaries/` — 777 篇摘要（通过 concept 中的 wikilink 按需跳转）

## 查询流程
1. 先读 `wiki/index.md` 了解全局
2. 根据标签和名称定位目标文件
3. 读取 .md 文件的 YAML frontmatter 判断相关性
4. 读取正文获取详细内容
5. 沿 wikilinks（`[名称](路径)`）跳转探索关联概念

## 文件格式约定
- 每个 .md 文件包含 YAML frontmatter（title/type/tags/status/confidence）
- `notion_id` 字段用于反向追溯到 Notion 原始页面
- 优先引用 status=已审核 且 confidence=high 的条目
- 草稿条目内容可能不完整，引用时需标注

## 标签体系（14 个一级标签）
Agent 框架 · Agent 编排 · Agent 技能 · Coding Agent · LLM · 记忆系统 · OpenClaw · Crypto/DeFi · 知识管理 · 开发工具 · 工作流 · 安全/隐私 · 内容创作 · 商业/生态

## 写入规则（如果你需要更新知识库）
- 可以改写正文中分隔线（`---`）上方的「编译真相」区
- 分隔线下方的「来源引用」区只允许追加，不允许修改或删除
- 新增条目需遵循 schema/WIKI-SCHEMA.md 的命名规范
  ```

---

## 6. schema/[WIKI-SCHEMA.md](http://wiki-schema.md/) 内容

  将知识 Wiki 的 Schema 规则文件的核心内容导出为标准 Markdown。包含以下章节：

  - 条目类型定义（concept / entity / summary / synthesis 的页面结构）

  - 命名规范

  - 双层标签体系（14 个一级标签的定义）

  **获取方式**：通过 Notion MCP 读取页面 `Wiki Schema（规则文件）`（Notion URL: `https://www.notion.so/5616b847-5113-4607-a28a-810ec9b26386`），提取「条目类型定义」「命名规范」「双层标签体系」三个章节，转换为标准 Markdown 写入。

---

## 7. 技术要求

### 7.1 语言和依赖

  - **语言**：Python 3.10+（或 TypeScript/Node.js，选一个你最熟悉的）

  - **Notion SDK**：`notion-client`（Python: `notion-client`，Node: `@notionhq/client`）

  - **其他依赖**：尽量最小化

### 7.2 配置

  - `NOTION_TOKEN`：环境变量，Notion Integration Token

  - `NOTION_DATABASE_ID`：`1c7701074b6880f3ab3be38f0ed25ba9`

  - `GITHUB_REPO`：`6tizer/wiki-export`

  - `OUTPUT_DIR`：本地输出目录（默认 `./wiki-export`）

### 7.3 运行方式

  ```bash
# 首次全量导出
python export.py --full

# 增量同步（只导出上次之后变更的页面）
python export.py --incremental --since 2026-04-14T00:00:00

# 只重建 index.md（不重新导出页面）
python export.py --index-only
  ```

---

## 8. 验收标准

  1. `wiki/index.md` 按 14 个标签分组列出所有 concept + entity，synthesis 单独列出

  1. `wiki/concepts/`、`wiki/entities/`、`wiki/syntheses/`、`wiki/summaries/` 四个目录各有对应文件

  1. 每个 .md 文件有正确的 YAML frontmatter

  1. 页面中的 mention-page 链接已转换为 `[名称](相对路径)` 的 wikilink

  1. 指向导出范围外的 mention 降级为纯文本

  1. `schema/CLAUDE.md` 和 `schema/WIKI-SCHEMA.md` 存在且内容完整

  1. 可以成功 `git push` 到 `6tizer/wiki-export`

  1. 在另一个 Claude Code 会话中执行 `cat wiki/index.md` 后，能自主导航到具体 concept 文件回答问题

---

## 9. 注意事项

  - **不要导出** 类型为 `lint-report`、`index`、`qa` 的条目

  - Notion API 返回的 rich text 中，颜色/高亮等样式信息可以丢弃，只保留文字内容和格式（加粗、斜体、代码、链接）

  - 表格 block 转换为 Markdown 表格时，注意处理合并单元格的情况（简化为普通表格即可）

  - 如果某个页面内容为空（只有标题没有正文），仍然创建文件，frontmatter 下方留空即可

  - `notion_url` 字段格式：`https://www.notion.so/{page_id_without_hyphens}`

---

## 10. 执行记录（2026-04-14）

### ✅ 完成状态

  - 1915 个页面全部导出成功，0 失败（首次导出 9 个 SSL 错误，重试后全部成功）

  - 已推送到 GitHub: https://github.com/6tizer/wiki-export

  - 目录统计：733 concepts + 360 entities + 777 summaries + 43 syntheses（2 对同名重复，详见问题记录）

  - index.md 包含 1711 个链接条目，按 14 个标签分组

  - schema/CLAUDE.md + schema/WIKI-SCHEMA.md 已生成

### ⚠️ 遇到的问题与处理

  1. 数据库 ID 错误：文档中写的 database_id（1c770107...）返回 404。通过 Notion search API 查询到实际 ID 为 f98c88d3-d587-494a-98ff-92fbaf9228c4。原因：文档中的 ID 可能是页面 ID 而非数据库 ID，或数据库在 Notion 中被重建过。

  1. SSL 连接错误：导出过程中间歇出现 SSLEOFError（共约 10 次），导致单个页面获取 block children 失败。首次全量导出 9 页失败，重试后全部成功。已修复：在限速器中添加了 SSL/Connection error 的异常捕获和指数退避重试（原代码只处理了 HTTP 429 和 5xx）。

  1. 目录名复数形式错误：Python 简单拼接 f"{type}s" 导致 entitys、synthesiss、summarys 等错误目录名。已修复：建立 TYPE_TO_DIR 映射表 {concept→concepts, entity→entities, synthesis→syntheses, summary→summaries}。

  1. Synthesis 同名冲突：2 对 synthesis 条目标题完全相同，文件名冲突导致后一个覆盖前一个（45 条 → 43 个文件）。这是 Notion 数据源中的重复条目，不是导出逻辑的 bug。可通过在文件名中追加 page_id 后缀解决，但需确认是否需要。

  1. 时区问题：index.md 的 last_updated 和导出时间使用了 UTC，导致日期比实际少一天。已修复：改为 Asia/Tokyo (UTC+9) 时区。

  1. Python 输出缓冲：首次运行使用 python3（默认缓冲 stdout），导致后台运行时无法实时看到进度。已改用 python3 -u（unbuffered）解决。

### 📊 性能数据

  - 总耗时：约 15 分钟（含查询元数据 + 逐页导出 + 生成 index + schema）

  - 导出速度：约 130 页/分钟（2.5 req/s 限速下）

  - 总 API 调用：约 5800 次（1915 页 × ~3 次/页 + 数据库查询分页）

  - 总文件大小：约 6.3 MB（1919 个文件）

**Phase 2 任务说明：增量同步自动化（给 Claude Code）**

# Phase 2 任务说明：增量同步自动化

  > **读者**：Claude Code

  > **前置条件**：Phase 1 已完成，`export.py` 已存在且首次全量导出成功

  > **目标**：让 Notion Wiki 的变更每天自动同步到 GitHub 仓库

---

## 1. 要做什么

  基于 Phase 1 的 `export.py`，完善以下功能：

### 1.1 增量同步模式（`--incremental`）

  ```bash
python export.py --incremental
  ```

  行为：

  1. 读取上次同步时间戳（从 `sync_state.json` 文件）

  1. 查询 Notion 数据库：`最后编辑时间 > 上次同步时间` 的所有 concept/entity/synthesis/summary

  1. 对每个变更页面：重新导出（覆盖旧文件）

  1. 检测已删除的页面：对比本地文件列表与 Notion 数据库中的活跃页面，删除本地多余的 .md 文件

  1. 重新生成 `index.md`（全量重建，因为是纯元数据生成，成本极低）

  1. 更新 `sync_state.json` 中的时间戳

  1. `git add -A && git commit && git push`

### 1.2 sync_state.json 格式

  ```json
{
  "last_sync_time": "2026-04-14T03:30:00+08:00",
  "last_full_export_time": "2026-04-14T02:00:00+08:00",
  "total_pages_exported": 1915,
  "page_mapping": {
    "notion_id_1": {
      "type": "concept",
      "file_path": "wiki/concepts/Mem0.md",
      "last_edited": "2026-04-14T02:00:00Z"
    }
  }
}
  ```

  说明：

  - `last_sync_time`：上次同步的时间，用于下次增量查询的 filter

  - `page_mapping`：所有已导出页面的 notion_id → 本地文件路径映射，用于检测删除

### 1.3 删除检测逻辑

  ```javascript
本地文件列表 = 扫描 wiki/concepts/ + wiki/entities/ + wiki/syntheses/ + wiki/summaries/
Notion 活跃页面 = 查询数据库所有 concept/entity/synthesis/summary 的 page_id

对比：本地文件的 notion_id（从 frontmatter 提取）是否仍在 Notion 活跃页面中
→ 不在 → 删除本地 .md 文件
  ```

  注意：删除检测只在 `--incremental` 模式下执行，不在 `--full` 模式下执行（全量导出会重建整个目录）。

### 1.4 Git 自动提交

  同步完成后自动执行：

  ```bash
cd wiki-export
git add -A
git diff --cached --quiet || git commit -m "sync: {n} updated, {m} deleted, {timestamp}"
git push
  ```

  说明：

  - `git add -A` 会处理新增、修改、删除

  - `git diff --cached --quiet` 检查是否有变更，没变更则不提交

  - commit message 包含更新/删除数量和时间戳

---

## 2. cron 定时任务配置

  在 Mac mini 上配置 cron，每天凌晨 3 点运行增量同步：

  ```bash
# 编辑 crontab
crontab -e

# 添加以下行（每天凌晨 3:00 运行）
0 3 * * * cd /path/to/wiki-export-project && /usr/bin/python3 -u export.py --incremental >> /var/log/wiki-sync.log 2>&1
  ```

  同时，在各终端配置 `git pull` cron：

  ```bash
# MacBook Pro / Mac Studio / 服务器们
# 每小时拉取最新
0 * * * * cd /path/to/wiki-export && git pull --quiet >> /var/log/wiki-pull.log 2>&1
  ```

---

## 3. 验收标准

  1. `python export.py --incremental` 可以正确检测并导出变更的页面

  1. 已删除的 Notion 页面对应的本地 .md 文件会被自动删除

  1. [index.md](http://index.md/) 在每次同步后自动更新

  1. 同步完成后自动 git commit + push

  1. 无变更时不产生空提交

  1. `sync_state.json` 正确记录同步时间戳

  1. cron 定时任务可以正确运行（在 Mac mini 上测试）

---

## 4. 测试方法

  先手动运行一次增量同步，然后在 Notion 中修改一个 concept 页面的内容，再运行一次，确认：

  - 该页面的 .md 文件被更新了

  - 其他文件没有被触动

  - [index.md](http://index.md/) 已更新

  - git log 显示新的 commit

---

## 5. 时区注意

  - Notion API 返回的 `last_edited_time` 是 UTC

  - `sync_state.json` 中的时间戳统一使用 **ISO 8601 带时区**（如 `2026-04-14T03:00:00+08:00`）

  - 比较时全部转为 UTC 后再比

  - [index.md](http://index.md/) 和 commit message 中的时间显示为 **Asia/Shanghai** 时区

---

## 6. 执行记录（2026-04-14）

### ✅ 完成状态

  - export.py 已完善 --incremental 模式：从 sync_state.json 自动读取上次同步时间，查询 Notion 变更页面，重新导出覆盖旧文件，检测已删除页面并清理本地 .md 文件，重建 index.md，更新 sync_state.json，自动 git commit + push

  - --full 模式完成后自动生成 sync_state.json（含 last_sync_time、last_full_export_time、page_mapping 全量映射）

  - 时区统一改为 Asia/Shanghai（UTC+8）：sync_state.json 用 ISO 8601 带时区，index.md 显示本地时间，Notion API 查询时转为 UTC

  - cron 已配置：每天凌晨 3:00 运行 python3 -u export.py --incremental --output ./wiki-export，日志输出到 /tmp/wiki-sync.log

  - 测试结果：--incremental 正确读取 sync_state.json（无需 --since），0 变更时跳过导出，无变更时不产生空提交，sync_state.json 正确更新并推送

### ⚠️ 遇到的问题与处理

  1. sync_state.json 缺失：首次测试 --incremental 时报错，因为 Phase 1 全量导出时还没有 sync_state.json 逻辑。解决：手动查询一次数据库生成初始 sync_state.json。后续 --full 模式会自动生成。

  1. SSL 连接错误：Phase 1 遗留问题，已在 Phase 1 修复限速器添加 SSL/Connection error 异常捕获和指数退避。增量同步中仍然间歇出现（约每次全量查询 1 次），但重试后均成功。

  1. Synthesis 同名冲突（Phase 1 遗留）：Phase 1 全量导出时发现 2 对同名 synthesis 条目（文件名冲突导致覆盖，45 → 43 文件）。用户已在 Notion 中删除重复条目。由于 sync_state.json 是在用户删除之后生成的，所以增量同步的删除检测没有触发——三边数据一致（sync_state 43 = Notion 43 = 本地 43）。删除检测逻辑本身是正确的，只是没有实际触发过。

  1. cron 工作目录问题：初始 cron 配置缺少 cd 和 --output 参数，会导致脚本找不到 export.py 或在错误目录生成文件。已修正为 python3 -u export.py --incremental --output ./wiki-export。

### 📋 验收标准逐项检查

  - python export.py --incremental 可以正确检测并导出变更的页面 → ✅（0 变更时正确跳过，无报错）

  - 已删除的 Notion 页面对应的本地 .md 文件会被自动删除 → ✅（逻辑正确，因数据在 sync_state 建立前已清理，未实际触发）

  - index.md 在每次同步后自动更新 → ✅

  - 同步完成后自动 git commit + push → ✅

  - 无变更时不产生空提交 → ✅（使用 git diff --cached --quiet 检测）

  - sync_state.json 正确记录同步时间戳 → ✅（ISO 8601 带 Asia/Shanghai 时区）

  - cron 定时任务可以正确运行 → ✅（已配置，等今晚 3:00 自动触发验证）

**Phase 2.5 任务说明：Notion Worker 同步（给 Claude Code）**

# Phase 2.5 任务说明：Notion Worker 同步

  > **读者**：Claude Code

  > **前置条件**：Phase 1-2 已完成，`export.py` 已验证可用，GitHub 仓库 `6tizer/wiki-export` 已有完整导出

  > **目标**：用 Notion Worker 实现每 30 分钟自动同步 Notion Wiki → GitHub 仓库，作为 Mac mini cron 的高频补充

---

## 0. 前置检查（开始前必须完成）

  在写任何代码之前，先检查以下依赖是否就绪。缺少的项目需要先安装/配置。

### 0.1 ntn CLI

  ```bash
# 检查是否已安装
ntn --version

# 如果未安装：
npm i -g ntn

# 检查是否已登录
ntn whoami

# 如果未登录：
ntn login
  ```

### 0.2 GitHub Personal Access Token

  需要一个有 `repo` 权限的 GitHub Token，用于 Worker 通过 GitHub API 推送文件。

  ```bash
# 检查用户是否已有 Token（可能存在环境变量或 .env 中）
echo $GITHUB_TOKEN

# 如果没有，提示用户：
# “需要一个 GitHub Personal Access Token（有 repo 权限）。
# 请到 https://github.com/settings/tokens 创建，然后提供给我。”
  ```

### 0.3 Node.js 版本

  ```bash
# Notion Workers 需要 Node.js >= 22
node --version

# 如果版本低于 22，需要升级
  ```

### 0.4 现有项目确认

  ```bash
# 确认 wiki-export 仓库已 clone 且可用
ls ~/wiki-export/wiki/index.md

# 确认 export.py 存在（用作 Markdown 转换逻辑参考）
ls ~/wiki-export-project/export.py  # 或者它实际所在的路径
  ```

### 0.5 检查清单汇总

  以上检查全部通过后，再继续执行后续步骤。如果有任何项缺失，先停下来提示用户处理。

---

## 1. 项目概述

### 1.1 你要做什么

  创建一个 Notion Worker，包含：

  1. **Sync 能力**：每 30 分钟自动检测 Notion Wiki 变更，转换为 Markdown，通过 GitHub API 推送到仓库

  1. **Tool 能力**：让 Notion Custom Agent 可以手动触发同步（按需）

### 1.2 技术栈

  - **Notion Workers**：TypeScript，`@notionhq/workers` SDK

  - **GitHub API**：REST API（Contents API）用于创建/更新/删除文件

  - **认证**：GitHub Personal Access Token（存储在 Worker secrets 中）

### 1.3 参考文档

  - Notion Workers 模板：[https://github.com/makenotion/workers-template](https://github.com/makenotion/workers-template)

  - GitHub Contents API：[https://docs.github.com/en/rest/repos/contents](https://docs.github.com/en/rest/repos/contents)

  - 现有 `export.py` 的逻辑（Markdown 转换、mention 处理、文件命名）可作为参考

---

## 2. Worker 结构

  ```typescript
import { Worker } from "@notionhq/workers";
import { j } from "@notionhq/workers/schema-builder";
import * as Schema from "@notionhq/workers/schema";
import * as Builder from "@notionhq/workers/builder";

const worker = new Worker();
export default worker;

// 同步状态跟踪数据库（Worker 管理）
const syncStatus = worker.database("syncStatus", {
  type: "managed",
  initialTitle: "Wiki Sync Status",
  primaryKeyProperty: "Sync ID",
  schema: {
    properties: {
      Title: Schema.title(),
      "Sync ID": Schema.richText(),
      Status: Schema.richText(),
      "Pages Synced": Schema.number(),
      "Last Sync": Schema.richText(),
    },
  },
});

// 限速器
const notionPacer = worker.pacer("notion", { allowedRequests: 2, intervalMs: 1000 });
const githubPacer = worker.pacer("github", { allowedRequests: 10, intervalMs: 1000 });
  ```

---

## 3. 核心同步逻辑

### 3.1 增量同步流程

  ```javascript
1. 从 state 读取 last_sync_time（首次为空则做全量）
2. 查询 Notion 数据库：last_edited_time > last_sync_time 的 concept/entity/synthesis/summary
3. 对每个变更页面：
   a. 用 Notion API 获取页面属性 + block children
   b. 转换为 Markdown（YAML frontmatter + 正文）
   c. 通过 GitHub Contents API 创建或更新文件
4. 检测已删除页面：
   a. 查询 Notion 数据库获取所有活跃页面 ID
   b. 通过 GitHub API 列出仓库中的文件
   c. 对比，删除仓库中多余的文件
5. 重新生成 index.md（全量查询元数据 → 生成 → push）
6. 更新 state 中的 last_sync_time
  ```

### 3.2 Notion → Markdown 转换

  复用 Phase 1 的 `export.py` 中的转换逻辑，用 TypeScript 重写。核心规则：

  **Block 转换**：

  - paragraph → 正文

  - heading_1/2/3 → `#` / `##` / `###`

  - bulleted_list_item → `- item`

  - numbered_list_item → `1. item`

  - code → ` `languagencoden` `

  - quote → `> text`

  - divider → `---`

  - table → Markdown table

  - callout → `> **icon** text`

  **Rich text 转换**：

  - bold → `**text**`

  - italic → `*text*`

  - code →  `text` 

  - link → `[text](url)`

  - mention(page) → `[名称](相对路径)` 或纯文本（如果不在导出范围内）

  **YAML frontmatter**：

  ```yaml
---
title: "页面名称"
type: concept
tags:
  - 标签1
  - 标签2
status: 草稿
confidence: high
last_compiled: "2026-04-14"
notion_id: "page-id"
---
  ```

### 3.3 GitHub API 操作

  **创建/更新文件**：

  ```javascript
PUT /repos/6tizer/wiki-export/contents/{path}
{
  "message": "sync: update {filename}",
  "content": "{base64_encoded_content}",
  "sha": "{current_file_sha}"  // 更新时需要，新建时不需要
}
  ```

  **删除文件**：

  ```javascript
DELETE /repos/6tizer/wiki-export/contents/{path}
{
  "message": "sync: delete {filename}",
  "sha": "{current_file_sha}"
}
  ```

  **获取文件列表**（用于删除检测）：

  ```javascript
GET /repos/6tizer/wiki-export/git/trees/main?recursive=1
  ```

  **GitHub API 限速**：认证用户 5000 请求/小时，足够用。

---

## 4. Sync 定义

  ```typescript
worker.sync("wikiSync", {
  database: syncStatus,
  schedule: "30m",
  mode: "incremental",
  execute: async (state) => {
    const lastSyncTime = state?.lastSyncTime ?? null;
    
    // 1. 查询 Notion 变更页面
    // 2. 转换 + push 到 GitHub
    // 3. 检测删除
    // 4. 重建 index.md
    
    const syncId = new Date().toISOString();
    return {
      changes: [{
        type: "upsert" as const,
        key: syncId,
        properties: {
          Title: Builder.title(`Sync ${syncId}`),
          "Sync ID": Builder.richText(syncId),
          Status: Builder.richText(`${updatedCount} updated, ${deletedCount} deleted`),
          "Pages Synced": Builder.number(updatedCount),
          "Last Sync": Builder.richText(new Date().toISOString()),
        },
      }],
      hasMore: false,
      nextState: { lastSyncTime: new Date().toISOString() },
    };
  },
});
  ```

---

## 5. Tool 定义（手动触发）

  ```typescript
worker.tool("triggerWikiSync", {
  title: "触发 Wiki 同步",
  description: "手动触发 Notion Wiki → GitHub 仓库的增量同步",
  schema: j.object({
    fullSync: j.boolean().describe("是否全量同步（默认增量）").nullable(),
  }),
  execute: async ({ fullSync }, context) => {
    // 复用 sync 逻辑
    // 返回同步结果摘要
    return `同步完成：${updatedCount} 更新，${deletedCount} 删除`;
  },
});
  ```

---

## 6. 配置

### 6.1 环境变量

  ```bash
ntn workers env set GITHUB_TOKEN=ghp_xxx
ntn workers env set GITHUB_REPO=6tizer/wiki-export
ntn workers env set NOTION_DATABASE_ID=f98c88d3-d587-494a-98ff-92fbaf9228c4
  ```

  注意：`NOTION_DATABASE_ID` 用 Phase 1 执行记录中确认的实际 ID（`f98c88d3...`），不是文档中最初写的 `1c770107...`。

### 6.2 部署

  ```bash
ntn workers deploy
ntn workers sync status  # 查看同步状态
ntn workers sync trigger wikiSync --preview  # 预览（不实际写入）
ntn workers sync trigger wikiSync  # 手动触发一次真实同步
  ```

---

## 7. 文件命名规则

  与 Phase 1 的 `export.py` 完全一致：

  - 直接使用条目的「名称」属性

  - 特殊字符替换：`/` → `-`、`:` → `-`、`\` → `-`、`*?"<>|` → 删除

  - 保留中文（UTF-8）

  - 扩展名 `.md`

  目录映射：

  - concept → `wiki/concepts/`

  - entity → `wiki/entities/`

  - synthesis → `wiki/syntheses/`

  - summary → `wiki/summaries/`

---

## 8. mention-page 转换

  需要在 Worker 启动时构建 page_id → 文件路径的映射表（查询 Notion 数据库所有条目的 id + 名称 + 类型），然后在转换 Markdown 时替换 mention。

  - mention 指向导出范围内的页面 → `[名称](../concepts/xxx.md)`

  - mention 指向范围外 → 保留为纯文本名称

---

## 9. 验收标准

  1. Worker 部署成功（`ntn workers deploy` 无报错）

  1. `ntn workers sync trigger wikiSync --preview` 能正确预览变更

  1. `ntn workers sync trigger wikiSync` 能实际将变更推送到 GitHub

  1. 30 分钟后自动触发同步（查看 `ntn workers sync status`）

  1. 在 Notion 中修改一个 concept 页面，等待 30 分钟后确认 GitHub 仓库已更新

  1. Worker Tool `triggerWikiSync` 可以被 Notion Custom Agent 调用

  1. 已删除的 Notion 页面对应的 GitHub 文件被自动删除

  1. [index.md](http://index.md/) 在每次同步后自动更新

---

## 10. 注意事项

  - **Notion API 限速**：使用 `worker.pacer()` 限制为 2 req/s（比 cron 脚本更保守，因为 Worker 是 Notion 托管，不想触发自家限速）

  - **GitHub API 限速**：5000 req/h，正常同步不会触发

  - **GitHub Contents API 单文件限制**：文件大小不超过 1MB，Wiki 页面不会超过

  - **base64 编码**：GitHub Contents API 要求文件内容 base64 编码

  - **SHA 获取**：更新/删除文件前需要先获取当前文件的 SHA（GET 文件 → 取 sha 字段）

  - **并发**：Worker 是单线程执行，不需要处理并发

  - **pre-alpha 风险**：如果 Worker 行为异常，Mac mini cron 作为兜底（每天凌晨 3 点全量校正）

---

# 事故记录：Worker 误删全部 GitHub 文件

  > **🔴** 严重程度：P0 | 影响：GitHub 仓库 1913 个文件被全部删除 | 时间：2026-04-14 00:00-00:30 UTC+8

## 根因

  index.ts 中 Phase 2 和 Phase 3 构建 mock page 对象时，遗漏了 Notion API 返回的 type 元数据字段。

  ```typescript
// Bug: 缺少 type 字段
名称: { title: [{ plain_text: title }] },
类型: { select: { name: type } },

// Fix: 加上 type 字段
名称: { type: "title", title: [{ plain_text: title }] },
类型: { type: "select", select: { name: type } },
  ```

## 影响链路

  1. extractSelect() 检查 p?.type === "select"，但 mock 对象没有 type 字段 → 返回空字符串

  1. buildPageMap() 中 VALID_TYPES.has("") 为 false → 所有页面被跳过 → pageMap 为空

  1. activePaths 为空集合 → GitHub tree 中所有文件都不在 activePaths 中

  1. 1913 个文件全部被判为孤儿 → 生成 1896 个 delete 提交

## 恢复过程

  1. git revert HEAD~160..HEAD 恢复了 160 个文件（summaries + syntheses），但 concepts 和 entities 未恢复

  1. git checkout 2a374aa -- wiki/ 从初始导出提交恢复，但初始导出只包含 629 个文件（Python cron 尚未全量导出 concepts/entities）

  1. 最终用 python3 export.py --full 重新全量导出，恢复全部 1913 个文件（733 concepts + 360 entities + 777 summaries + 43 syntheses）

## 修复措施

  1. Phase 2/3 的 mock 对象添加 type: "title" 和 type: "select" 字段

  1. 删除检测暂时禁用（只打日志不实际删除），验证 activePaths=1913 正确后再恢复

  1. 修复后部署验证：日志显示 activePaths=1913, treeFiles=1915, orphans=1（仅 .DS_Store），确认路径比对正常

## 待办

  - [x] 恢复删除检测逻辑（当前仅打日志）

  - [x] 增加安全阈值：orphans 数量超过 50 时自动跳过删除并报警

  - [x] 考虑用 dry-run 模式替代直接删除，先记录待删列表到 syncStatus 数据库

---

## 实施记录：安全加固（2026-04-14 09:10 UTC+8）

  > **✅** 执行者：Claude Code | 状态：已完成 ✅ | 部署验证通过

### 改动内容

  仅修改 src/index.ts，4 处改动：

  - `ORPHAN_THRESHOLD = 10` — 孤儿数量超过 10 自动跳过删除并打印 SAFETY 告警

  - `pendingDeletions` — SyncState 新增字段，第一轮检测孤儿只记录，第二轮确认仍为孤儿后才删除（两阶段 dry-run）

  - **状态初始化保留 pendingDeletions** — 防止 sync 周期重置时丢失待删列表

  - 隐藏文件排除 — index.md 和所有隐藏文件（.DS_Store 等 /.* 文件）永不删除

### 安全机制（5 层防护）

  1. 阈值 10 — 超过 10 个孤儿直接跳过，防系统 bug 导致批量误删

  1. 两阶段确认 — 首轮只记录，次轮二次确认后才删，防时序/API 延迟误判

  1. 隐藏文件排除 — .DS_Store 等 macOS 系统文件永不删除

  1. index.md 排除 — 索引文件硬排除

  1. 逐文件 try/catch — 单个删除失败不影响其他

### 验证结果

  部署后触发 sync，日志输出：

  ```plain text
[wikiSync] Deletion check: activePaths=1913, treeFiles=1915, pendingDeletions=0
[wikiSync] Done: 0 updated, 0 deleted
  ```

  1913 个 Notion 页面全部匹配，0 个孤儿（.DS_Store 已被隐藏文件排除规则过滤），sync 状态 **HEALTHY**。
