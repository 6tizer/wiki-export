---
title: Codex 最佳配置实践：从 AGENTS.md 到插件生态与多 Agent 编排的工程化调优全景
type: synthesis
tags:
- 加密资产
- 多Agent协作
- MCP 协议
status: 已审核
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/5cd1796ad43542e6be0bc7035facd04b
notion_id: 5cd1796a-d435-42e6-be0b-c7035facd04b
---

## 研究问题

如何系统化地配置 Codex（OpenAI 的 AI 编程 Agent），使其从一个开箱即用的终端编码助手升级为具备策略化行为约束、插件化能力扩展、持久化记忆和多 Agent 协作能力的工程化开发平台？不同配置层级之间如何协作？模型选择、成本控制与安全沙箱之间如何取得平衡？

## 综合分析

### 一、三层配置架构：从用户偏好到项目约束

Codex 的配置体系以 `config.toml` 为核心，采用多级覆盖机制：

| **配置层级** | **位置** | **职责** | **优先级** | **信任要求** |

| --- | --- | --- | --- | --- |

| **系统级** | /etc/codex/config.toml | 全组织默认值 | 最低 | 无 |

| **用户级** | ~/.codex/config.toml | 个人偏好与模型默认 | 中 | 无 |

| **项目级** | .codex/config.toml | 项目特定规则与约束 | 高 | 需项目信任 |

| **Profile** | --profile <name> | 场景化配置切换 | 更高 | 无 |

| **CLI 标志** | -c key=value | 单次运行覆盖 | 最高 | 无 |

**关键原则**：

- 共享默认值放最顶层，差异化配置放 Profile

- 不信任的项目会跳过所有 `.codex/` 层级配置

- `openai_base_url` 可直接指向代理或数据驻留端点，无需额外定义 provider

### 二、[AGENTS.md](http://agents.md/)：行为策略的核心配置

[AGENTS.md](concepts/AGENTS.md.md) 是 Codex 的行为策略配置文件，与 Claude Code 的 [CLAUDE.md](http://claude.md/) 角色类似，但 Codex 的设计更强调「手动维护策略而非细节」。

**最佳实践**：

- **写策略，不写步骤**：聚焦优先级、约束和决策框架，而非逐步操作指南

- **避免过度定制**：规则越多，副作用越多；保持最小干预原则

- **分层放置**：全局行为规范放用户级 [AGENTS.md](http://agents.md/)，项目约束放项目级

- **持续迭代**：在使用过程中观察 Agent 行为，逐步完善而非一次性写满

**OpenAI 官方实践**：OpenAI 用 Codex 维护 [OpenAI Agents SDK](entities/OpenAI Agents SDK.md) 时，展示了四层架构——[AGENTS.md](http://agents.md/) 负责写明何时触发什么规则（行为入口层），Skills 负责拆分具体工作流，[Codex GitHub Action](concepts/Codex GitHub Action.md) 让本地验证的规则进入 CI 形成一致执行环境。

**⚠️ 常见错误**：把 [AGENTS.md](http://agents.md/) 写成百科全书式的详细操作手册，导致上下文膨胀、Agent 遵循度下降。

### 三、模型选择与推理策略

Codex 的模型配置是成本与效果平衡的关键杠杆。

**三维选择公式**：

- **高难度推理**：用最强推理模型（如 GPT-5.2-Codex xhigh），适合复杂架构决策

- **机械性执行**：用高性价比模型（medium/low），适合批量重构、格式化

- **长上下文**：用大窗口模型，配合 Compaction 支持多小时连续推理

**推理等级配置**：

| **等级** | **适用场景** | **速度** | **成本** |

| --- | --- | --- | --- |

| **Low** | 快速、边界清晰的小任务 | 快 | 低 |

| **Medium** | 日常交互式编码（推荐默认） | 中 | 中 |

| **High** | 复杂变更或调试 | 慢 | 高 |

| **Extra High** | 长程自主推理、最难任务 | 最慢 | 最高 |

**分阶段锁定模型**：

- **设计阶段**：用强模型做架构决策

- **实现阶段**：锁定中等模型保持一致性

- **验证阶段**：用弱模型跑测试，确保可复现

### 四、插件生态配置：三层能力扩展

[Codex 插件系统](concepts/Codex 插件系统.md) 是 Codex 从编程助手走向 Agent 平台的关键接口，分三层：

**Skills（技能包）**：

- 把平台知识、操作规范和执行脚本封装为可复用能力

- 例如 [Build macOS Apps 插件](entities/Build macOS Apps 插件.md)：注入 Xcode 规范、运行脚本和日志闭环

- 安装方式：`codex marketplace add <skill>`

**App Integrations（应用集成）**：

- 连接外部服务与数据源

- 包括应用内浏览器（评论模式）、图像生成等

**MCP Servers（模型上下文协议）**：

- 基于 [MCP 协议](concepts/MCP 协议.md) 接入任意外部工具

- 在 config.toml 中配置 MCP server 列表

**Skills Pipeline 设计哲学**：Wiki 中的分析指出，Codex 官方插件命名强调的是「待解决的问题与能力边界」而非岗位身份。这说明 **skills pipeline（能力管线）而非角色型 Agent，才是可持续的系统组织方式**——先拆 Skill，再拼 Pipeline，比直接定义「架构师 Agent」「测试 Agent」更稳定。

### 五、记忆系统配置

Codex 的记忆体系正在快速演进，目前包含两大机制：

**持久化跨会话记忆**：

- Codex 内置记忆功能，自动捕获用户偏好、工作模式和项目上下文

- 自动化任务可沿用既有线程继续执行，让长期任务运营成为现实

**Chronicle（屏幕上下文记忆）**：

- [Chronicle](concepts/Chronicle.md) 把近期屏幕上下文纳入记忆增强流程

- 从「每次重新 briefing」推进到「能延续上下文的持续型伙伴」

- ⚠️ 隐私与合规考量：屏幕级记忆把权限边界和地区合规问题推到台前

**oh-my-codex 的持久化方案**：

- [oh-my-codex](entities/oh-my-codex.md) 在 `.omx/` 目录维护项目状态和记忆

- 关闭终端也能无缝续接，提供接近跨会话记忆的工程体验

**配置建议**：

- 对于连续多轮编码任务，优先启用 Chronicle 降低重述成本

- 对于团队共享项目，审慎配置记忆范围以避免隐私泄露

- 配合 Compaction（上下文压缩）支持多小时不间断推理

### 六、安全沙箱与审批策略

Codex 的安全配置直接影响自动化程度与风险边界：

**三种审批模式**：

- **untrusted**：所有操作需审批（最安全）

- **on-request**：仅被标记的操作需审批（平衡模式）

- **yolo**（--dangerously-bypass-approvals-and-sandbox）：跳过所有审批和沙箱（仅限外部已加固环境）

**沙箱配置**：

- [bubblewrap](concepts/bubblewrap.md) 提供本地沙箱隔离

- `sandbox_workspace_write` 控制写入范围

- 受保护路径白名单防止关键文件被误改

**Harness 工程**：

- OpenAI 把 Codex 沉淀的 Harness 实践产品化进 [OpenAI Agents SDK](entities/OpenAI Agents SDK.md)

- [Sandbox 抽象](concepts/Sandbox 抽象.md) 统一 E2B、Modal、Cloudflare 等多家沙盒供应商

- 快照恢复与[多沙盒并行](concepts/多沙盒并行.md)让 Agent 具备长跑容错能力

### 七、多 Agent 编排配置

Codex 的多 Agent 配置已形成多条实践路径：

**路径一：Claude Code + Codex SubAgent 模式**

- Claude Code 负责规划与调度，Codex 做被调度的执行者

- 核心收益来自成本分层——贵模型做决策，便宜模型做执行

- 通过 [tmux](entities/tmux.md) 提供最小可用的多 Agent 运行面板

**路径二：oh-my-codex 多智能体套件**

- `$deep-interview`：结构化需求澄清

- `$ralplan`：AI 先出完整方案文档，审批后再执行

- `$team`：通过 tmux 会话启动多个 Agent 并行工作

- `$ralph`：持久化项目状态，关闭终端也能续接

**路径三：codex-plugin-cc 跨 Agent 嵌入**

- [codex-plugin-cc](entities/codex-plugin-cc.md) 让 Codex 以插件形式嵌入 Claude Code 工作流

- 提供 `review`（代码审查）、`adversarial review`（对抗审查）、`rescue`（救场修复）等命令

- 体现从「抢用户」到「嵌入对方工作流」的策略变化

**路径四：GitHub Action CI 集成**

- [Codex GitHub Action](concepts/Codex GitHub Action.md) 把本地验证的 Codex 规则搬进 CI 流水线

- 从本地开发→CI 自动化→生产部署的完整闭环

### 八、成本优化配置矩阵

| **策略** | **原理** | **适用场景** | **配置方式** |

| --- | --- | --- | --- |

| **强弱模型分阶段** | 决策用强模型，执行用弱模型 | 全流程 | 按阶段切换 reasoning_effort |

| **Token 精准管理** | rg 定位代码，分段读取不超 250 行 | 代码审查/重构 | 在 [AGENTS.md](http://agents.md/) 中注明策略 |

| **Compaction** | 上下文压缩，支持多小时不间断 | 长会话 | compact_prompt 配置 |

| **SubAgent 分工** | 拆分上下文避免窗口膨胀 | 大型任务 | Claude Code + Codex 编排 |

| **Plan Mode** | 先规划后执行，减少返工 | 复杂/模糊任务 | /plan 或 Shift+Tab |

| **本地代理** | openai_base_url 指向代理 | 数据驻留/成本控制 | config.toml 中设置 |

### 九、从编程助手到 Agent 平台的配置演进

Codex 的产品路线正从单点编程助手向全周期开发平台演化：

**能力扩展时间线**：

1. **CLI 编码助手** → 终端内代码生成与编辑

1. **+插件生态** → Skills/MCP/App Integrations 三层扩展

1. **+Computer Use** → 桌面级跨应用操作

1. **+记忆系统** → Chronicle + 持久化偏好

1. **+自动化线程** → 长程任务延续执行

1. **+应用内浏览器** → 评论模式 + DOM 上下文注入

1. **+Harness 开放** → Agents SDK 产品化，sandbox 标准化

### 十、与 Claude Code / Hermes 配置体系的对比

| **维度** | **Codex** | **Claude Code** | **Hermes Agent** |

| --- | --- | --- | --- |

| **配置哲学** | config.toml 多级覆盖 + [AGENTS.md](http://agents.md/) 策略 | 四层架构（Rules→Skills→Hooks→Agents） | 文件即大脑，五层分层加载 |

| **行为约束** | [AGENTS.md](http://agents.md/)（策略优先） | [CLAUDE.md](http://claude.md/)  • Hooks（语义+物理） | [SOUL.md](http://soul.md/)  • [AGENTS.md](http://agents.md/)（人格+上下文） |

| **能力扩展** | Plugin Marketplace + MCP | Skills 目录 + Hooks | Skills 自动沉淀 + 手动安装 |

| **安全机制** | bubblewrap 沙箱 + 审批策略 | Hooks 事件驱动守卫 | Gateway + Policy Gate |

| **记忆** | Chronicle + 持久化偏好 | Dreaming 后台整理 + [MEMORY.md](http://memory.md/) | 三层记忆 + Frozen Snapshot |

| **多 Agent** | oh-my-codex $team + codex-plugin-cc | SubAgent 并行 | Profile 隔离 + delegate_task |

| **执行环境** | 本地沙箱 + Harness + 多沙盒并行 | 终端为主 | 18+ 消息平台原生适配 |

| **CI/CD 集成** | Codex GitHub Action 原生支持 | 需自行配置 | Cron + Gateway |

| **开源程度** | codex-cli 完全开源可 fork | 核心闭源 | hermes-rs 开源 |

## 关键发现

1. [**AGENTS.md**](http://agents.md/)** 的核心原则是「最小干预」**：写策略/优先级/约束，不写逐步操作。过度定制引入副作用，保持精简让 Agent 有空间做出合理判断。这与 Claude Code 的 [CLAUDE.md](http://claude.md/) 和 Hermes 的 [SOUL.md](http://soul.md/) 形成有趣的三角——三者都强调「少即是多」，但侧重点不同：[AGENTS.md](http://agents.md/) 偏策略，[CLAUDE.md](http://claude.md/) 偏规范，[SOUL.md](http://soul.md/) 偏人格。

1. **Skills Pipeline 比角色型 Agent 更适合长期系统**：Codex 官方插件生态的组织方式证明，围绕可复用能力节点（Skill）构建执行管线，比围绕岗位化角色设定构建 Agent 更稳定、更可持续。这一洞察对所有 Agent 框架的配置策略都有指导意义。

1. **Codex 的开源特性使其成为最佳配置实验场**：codex-cli 完全开源可 fork，意味着用户可以在 [AGENTS.md](http://agents.md/)、config.toml、Skills 之外，直接修改 Agent 内核逻辑。这是 Claude Code（闭源）和大多数竞品不具备的优势，使得社区能快速涌现 oh-my-codex 等增强层。

1. **Codex 正从编程工具向 Personal Agent 平台演化**：Computer Use、应用内浏览器、Chronicle 记忆、插件市场、自动化线程——这些能力叠加后，Codex 的定位已超越单纯的 Coding Agent，向 OpenAI 的个人代理 Super App 入口靠拢。配置策略也应随之调整，从「怎么让它写好代码」转向「怎么让它稳定接管工作流」。

1. **多 Agent 编排的成本分层是核心收益**：Claude Code + Codex SubAgent 实践证明，多 Agent 的直接价值不在于「更聪明」，而在于把昂贵的推理预算分配给决策层，把执行预算分配给便宜模型。这种成本架构适用于所有 Agent 编排场景。

## 来源列表

### Entity/Concept 页面

- [Codex](entities/Codex.md)

- [Codex 插件系统](concepts/Codex 插件系统.md)

- [codex-plugin-cc](entities/codex-plugin-cc.md)

- [oh-my-codex](entities/oh-my-codex.md)

- [AGENTS.md](concepts/AGENTS.md.md)

- [Codex GitHub Action](concepts/Codex GitHub Action.md)

- [Codex Spark](entities/Codex Spark.md)

- [OpenAI Agents SDK](entities/OpenAI Agents SDK.md)

- [bubblewrap](concepts/bubblewrap.md)

- [Chronicle](concepts/Chronicle.md)

- [Skills Pipeline](concepts/Skills Pipeline.md)

- [Orchestrator 模式](concepts/Orchestrator 模式.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Sandbox 抽象](concepts/Sandbox 抽象.md)

### Summary 页面

- [摘要：OpenAI Codex CLI 实用最佳实践](summaries/摘要：OpenAI Codex CLI 实用最佳实践.md)

- [摘要：Codex 重大更新，全面解读](summaries/摘要：Codex 重大更新，全面解读.md)

- [摘要：Codex Plugins：OpenAI 为 AI 编程 Agent 补上「工具连接层」](summaries/摘要：Codex Plugins：OpenAI 为 AI 编程 Agent 补上「工具连接层」.md)

- [摘要：OpenAI 用 Codex 维护 Agents SDK 的四层架构：把工程规范变成 Agent 的行为约束](summaries/摘要：OpenAI 用 Codex 维护 Agents SDK 的四层架构：把工程规范变成 Agent 的行为约束.md)

- [摘要：OpenAI祭出GPT-5.4神装！Codex同款Harness全面开放](summaries/摘要：OpenAI祭出GPT-5.4神装！Codex同款Harness全面开放.md)

- [摘要：我翻了 Codex App的插件后，开始相信 skills pipeline 才是 AI 系统的主线](summaries/摘要：我翻了 Codex App的插件后，开始相信 skills pipeline 才是 AI 系统的主线.md)

- [摘要：oh-my-codex — Codex CLI 的多智能体增强套件](summaries/摘要：oh-my-codex — Codex CLI 的多智能体增强套件.md)

- [摘要：Last week, we released a preview of memories in Codex.](summaries/摘要：Last week, we released a preview of memories in Codex.md)

- [摘要：Codex for (almost) everything.](summaries/摘要：Codex for (almost) everything.md)

- [摘要：Codex macOS 插件：让 AI 真正理解 Mac 原生开发](summaries/摘要：Codex macOS 插件：让 AI 真正理解 Mac 原生开发.md)

- [摘要：Codex 刚刚上线了一个重磅新功能——自带“评论模式”的应用内浏览器](summaries/摘要：Codex 刚刚上线了一个重磅新功能——自带“评论模式”的应用内浏览器.md)

- [摘要：【黑武器】让Codex从单打独斗到AI团队作战，这个开源项目一周暴涨1.1万星！](summaries/摘要：【黑武器】让Codex从单打独斗到AI团队作战，这个开源项目一周暴涨1.1万星！.md)

- [摘要：用 Claude Code 调度 Codex 当 SubAgent：省 Token 的多 Agent 编排实践](summaries/摘要：用 Claude Code 调度 Codex 当 SubAgent：省 Token 的多 Agent 编排实践.md)

- [摘要：codex-plugin-cc：OpenAI 官方出手，把 Codex 塞进了 Claude Code](summaries/摘要：codex-plugin-cc：OpenAI 官方出手，把 Codex 塞进了 Claude Code.md)

- [摘要：Codex不打算让Claude Code好过](summaries/摘要：Codex不打算让Claude Code好过.md)

- [摘要：前端 Gemini、后端 Codex：用 Claude Code 调度多 Agent 的分工哲学](summaries/摘要：前端 Gemini、后端 Codex：用 Claude Code 调度多 Agent 的分工哲学.md)

- [摘要：用 tmux 搭建 Agent Team 的终端舞台：Claude Code + Codex 多窗口协作入门](summaries/摘要：用 tmux 搭建 Agent Team 的终端舞台：Claude Code + Codex 多窗口协作入门.md)

- [摘要：CCG Workflow：让 Claude、Codex、Gemini 组团写代码，Token 省了一半](summaries/摘要：CCG Workflow：让 Claude、Codex、Gemini 组团写代码，Token 省了一半.md)

- [摘要：Codex能够控制电脑了：](summaries/摘要：Codex能够控制电脑了：.md)

- [摘要：没等来 Image 模型，等来了 Codex 大升级。](summaries/摘要：没等来 Image 模型，等来了 Codex 大升级。.md)

## 行动建议

1. **为知识编译流水线编写 Codex 版 **[**AGENTS.md**](http://agents.md/)** 模板**：在 `.codex/` 项目目录中配置专属 [AGENTS.md](http://agents.md/)，只写策略层（「遇到 Wiki 数据源先查重」「引用优先于推测」「中文输出」），不写执行步骤。配合 `config.toml` 设定默认 medium reasoning 和 compact_prompt，确保日常编译任务的成本可控。

1. **部署 Claude Code + Codex SubAgent 编排架构**：用 Claude Code 做知识编译的规划与审查层（高成本精准决策），把批量内容生成、格式化、链接修复等执行型任务分发给 Codex（低成本高吞吐）。通过 tmux 或 oh-my-codex 的 $team 模式实现并行，预计可降低 50%+ 的 token 成本。

1. **关注 Codex Plugin Marketplace 的领域插件**：随着 Skills Pipeline 生态扩张，适合内容生产和知识管理的插件（如文档解析、知识图谱构建、格式化输出）可能出现。定期扫描 marketplace 并评估是否可以替代当前手工维护的工作流节点，把重复性能力沉淀为可复用的 Skill 资产。
