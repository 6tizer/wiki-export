---
title: OpenClaw
type: entity
tags:
- Agent 框架
- OpenClaw
status: 审核中
confidence: high
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/ee1b0c1ebfa3472fb5ed3259dc9c869a
notion_id: ee1b0c1e-bfa3-472f-b5ed-3259dc9c869a
---

## 定义

OpenClaw 是由奥地利开发者 **Peter Steinberger**（PSPDFKit / Nutrient 创始人）于 **2025 年 11 月**开源的本地自主 AI Agent 框架。核心理念：**"AI that actually does things"**——不只是对话，而是真正代替用户执行任务。

别名/前身：Clawdbt、Moltbot

## 核心能力

- 读写文件、执行 Shell 命令、浏览网页、调用 API

- 收发邮件、管理日历

- 通过 Telegram、iMessage、Discord、WhatsApp、Slack 等 20+ 平台接收指令

- 持久化跨会话记忆，支持 24/7 常驻运行

- 通过技能（Skill）扩展能力，生态由 ClawHub 集中管理

- 支持从对话中直接派生子 Agent 处理并行子任务

## 项目数据（截至 2026 年 4 月）

- GitHub Stars：344,000+（近年来增速最快的开源 AI 项目之一）

- 主要语言：TypeScript

- License：MIT（早期为 AGPL-3.0，后调整）

- 技能市场（ClawHub）：13,700+ 技能

- 创建时间：2025 年 11 月

## 架构特点

- **本地优先**：默认本地部署，数据不离开设备；不推荐 VPS 部署（功能损失约 80%）

- **System Prompt 九层架构**：框架层负责稳定性，用户层负责个性化

- [**SOUL.md**](http://soul.md/)：用户自定义个人信息和偏好的核心配置文件

- **子 Agent 派生**：可在对话中动态创建并调度子 Agent 处理子任务

## 安全风险

- **ClawJacked 漏洞**（2026.2.26 修复）：允许任意网站静默劫持本地 Agent 实例

- **CVE-2026-25253**：本地代理框架一键远程代码执行漏洞，官方已修复

- **ClawHub 恶意插件**：Cisco 研究发现约 20% 插件存在恶意行为

- **提示注入攻击**：CrowdStrike 已发现针对 OpenClaw 的实际攻击案例

- 建议：不在运行设备登录敏感账户；不暴露于公共空间

## 创始人背景

Peter Steinberger：奥地利开发者，PSPDFKit（后更名 Nutrient）创始人，2021 年以约 1 亿欧元出售公司。2026 年 2 月宣布加入 OpenAI，OpenClaw 移交独立基金会继续维护。

## 同类工具对比

| 工具 | 定位 | 优势 | 劣势 |

| --- | --- | --- | --- |

| OpenClaw | 本地自主 Agent | 完全可控、多平台集成、开源 | 安装门槛高、安全配置复杂 |

| Manus | 云端自主 Agent | 开箱即用 | 数据不可控 |

| Claude Code | 终端 AI 编程助手 | 代码能力强 | 无自主持续运行能力 |

| AutoGPT | 开源 Agent 框架 | 历史悠久 | 工程成熟度低 |

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MjM5OTE0ODA2MQ%3D%3D&mid=2650996439&idx=1&sn=b0e8f9460d31651bdd374eae18db74f6&chksm=bdd2ba711515b068254cc8fae7b1d613c0f7602c73faca901e0862da74272e110b494db13b0f#rd)｜《汤道生：人工智能正式进入 Harness 时代》｜来源条目：[摘要：汤道生：人工智能正式进入 Harness 时代](summaries/摘要：汤道生：人工智能正式进入 Harness 时代.md)

- [摘要：Kiro CLI 2.0 升级指南：OpenClaw 加持下的 AI 编程提效新体验](summaries/摘要：Kiro CLI 2.0 升级指南：OpenClaw 加持下的 AI 编程提效新体验.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU0NDU3MTY1NQ%3D%3D&mid=2247483767&idx=1&sn=867d214d81d79ead13e6490529ea719a&chksm=fa6eece7aef6c4e6c2a54a44692f8dd8e6a97bc186516a2b2a664080568650441d5ac3218469#rd)）

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw%3D%3D&mid=2247523832&idx=1&sn=8a7013894ddc0668c0f1c9f935599450&chksm=c1b17f5bd2d0ca49ee848d1dc13c14fb122c8f551ba00b307b566dfa7edc4c20a52573051f79#rd)｜《字节最火的开源Agent项目，如何思考Agent的自我进化？》｜来源条目：[摘要：字节最火的开源Agent项目，如何思考Agent的自我进化？](summaries/摘要：字节最火的开源Agent项目，如何思考Agent的自我进化？.md)

- [原文链接](https://x.com/shmidtqq/status/2044027418541691041)｜《OpenClaw + GLM 5.1 = FREE AI AGENTS》｜来源条目：[摘要：OpenClaw + GLM 5.1 = FREE AI AGENTS](summaries/摘要：OpenClaw + GLM 5.1 = FREE AI AGENTS.md)

- 摘要：OpenClaw 入门指南：从压力点出发，逐步解锁 AI 自动化

- 摘要：OpenClaw 完全指南：把你的电脑变成一个 24/7 自主运转的 AI 员工

- 摘要：OpenClaw 2026.2.17：1M 上下文 + 子 Agent 催生的个人 AI 新范式

- 《OpenClaw + Obsidian：用 AI 智能体打造 7×24 小时内容工厂》（bggg_ai，2026-03-06）— 展示 OpenClaw 作为内容工厂执行层，与 Obsidian 形成记忆—执行闭环

- 《Gate MCP Skills：让 AI Agent 直接操盘加密交易的新基础设施》（NFTCPS，2026-03）— 展示 OpenClaw 作为加密 Agent 执行平台接入交易所能力

- 《飞书官方出手：OpenClaw 插件免费额度直升 100 万次，AI 助手终于能「亲自动手」了》（RocM301，2026-03）— 补充 OpenClaw 在飞书办公场景中的官方接入进展

- 《OpenClaw 多角色 Telegram 群聊：一个 Gateway 跑产品经理、工程师、QA 的实战指南》（[Berryxia.ai](http://berryxia.ai/)，2026-04-01）— 体现其多 Agent 群组路由与工作区隔离能力

- 《memory-lancedb-pro：给你的 OpenClaw Agent 装上真正会记忆的大脑》（axiaisacat，2026-03-07）— 补充 OpenClaw 生态中的长期记忆增强路径

- 《OpenClaw 的 9 层 System Prompt 架构：框架管稳定，你管个性化》（@yanhua1010，2026-03）— 补充其运行时 system prompt 分层设计

- 《OpenClaw 长期记忆终极方案：memory-lancedb-pro vs total-recall 深度对比》（akokoi1，2026-03-07）— 进一步说明其长期记忆生态分化

- 《6551-twitter-to-binance-square：用龙虾一句话同步推特到币安广场》（cryptoxiao，2026-03-07）— 展示 OpenClaw 在内容分发自动化中的 Skill 实战

- 摘要：OpenClaw 跑量化回测：看不懂，但大受震撼

- 摘要：OpenClaw + Obsidian：用 AI 智能体打造 7×24 小时内容工厂

- 摘要：Gate MCP Skills：让 AI Agent 直接操盘加密交易的新基础设施

- 摘要：飞书官方出手：OpenClaw 插件免费额度直升 100 万次，AI 助手终于能「亲自动手」了

- 摘要：OpenClaw 多角色 Telegram 群聊：一个 Gateway 跑产品经理、工程师、QA 的实战指南

- 摘要：memory-lancedb-pro：给你的 OpenClaw Agent 装上真正会记忆的大脑

- 摘要：OpenClaw 的 9 层 System Prompt 架构：框架管稳定，你管个性化

- 摘要：OpenClaw 长期记忆终极方案：memory-lancedb-pro vs total-recall 深度对比

- 摘要：6551-twitter-to-binance-square：用龙虾一句话同步推特到币安广场

- 《QClaw：腾讯把 AI Agent 装进微信，12 亿人的入口之争》（@joshesye，X书签）— 展示 OpenClaw 被大厂产品化封装并接入微信、QQ 的入口化路径

- 《用 Claude Code 搭一套 BTC 合约交易信号系统，每小时推送到 Telegram》（zeroxmin，X书签）— 将 OpenClaw 作为更智能的交易分析路线与脚本执行路线做对照

- 《OpenClaw 深度使用指南：10 个让 Agent 越用越顺手的实战技巧》（sitinme，X书签）— 补充记忆、身份、权限与多 Agent 协作的第一手实操经验

- 《OpenClaw 安全实践指南：SlowMist 给高权限 AI Agent 的「思想钢印」》（Cos / SlowMist_Team，X书签）— 补充高权限 Agent 的安全治理框架

- 《xiaohongshu-skills：让 AI Agent 真正「操控」小红书的 CDP 自动化方案》（Geek Lite，X书签）— 展示 OpenClaw 在社交平台自动化中的技能扩展路径

- 《OpenClaw 遇上 Polymarket：一个让你心动的套利故事，以及它经不起推敲的数学》（0x_Miko，X书签）— 补充其 Context Engine 在实时场景中的传播叙事与边界

- 《OpenClaw 养虾踩坑实录：如何用 CDP 把浏览器完全交给 AI Agent 控制》（未知，X书签）— 补充浏览器控制、CDP 会话复用与环境配置的实战坑点

- 《把 Agent 当新员工带：OpenClaw 深度使用心得》（@sitinme，X书签）— 补充记忆文件、权限分层与长期协作方法论

- 《OpenClaw 橙皮书：60天超越 React，这只「龙虾」究竟是什么来头？》（AlchainHust，X书签）— 补充项目背景、生态资源与竞品对照

- 《OpenClaw 版星露谷：让 Agent 帮你种菜偷菜，游戏的乐趣边界在哪里？》（0xAikoDai，X书签）— 展示 OpenClaw 在 Agent 游戏场景中的实验性应用

- 《DenchClaw：用 OpenClaw 搭一套本地 AI CRM，一行命令搞定客户管理》（Mark Rachapoom，X书签）— 展示 OpenClaw 生态向 CRM 垂直应用扩展

- 《OpenClaw 生态全景：Awesome Skills、ClawHub 与橙皮书，你需要的资源都在这》（zaprobest，X书签）— 补充生态学习资源、技能市场与精选仓库版图

- 《ClawPort：为 OpenClaw 多智能体团队打造的可视化指挥中心》（GitHub_Daily，X书签）— 补充 OpenClaw 在多 Agent 可观测性与团队运维界面的延展

- 《全球超 53 万台「肉虾」在线：OpenClaw 公网暴露的安全警示》（hzlzh，X书签）— 补充默认公网暴露、高权限执行与凭证泄露带来的系统性风险

- 《OpenClaw find-skills：让你的 AI 龙虾「不会就自动学」》（axiaisacat，X书签）— 补充 OpenClaw 技能生态中的元技能发现机制

- 《OpenClaw 飞轮启动指南：五个核心 Skill 让你的 AI Agent 自我进化》｜X书签文章｜原文链接：[https://x.com/aiwarts/status/2031750343621558380](https://x.com/aiwarts/status/2031750343621558380)

- 《OpenClaw 控制中心：把你的 AI Agent 集群从黑盒变成可视化驾驶舱》｜X书签文章｜原文链接：[https://x.com/ai_muzi/status/2032032878855348702](https://x.com/ai_muzi/status/2032032878855348702)

- 《Heartbeat-Like-A-Man：让你的 AI 龙虾像人一样「没事找事」》｜X书签文章｜原文链接：[https://x.com/loryoncloud/status/2032084837956501837](https://x.com/loryoncloud/status/2032084837956501837)

- 《用 YouMind Skill 追踪全球 AI 大佬动态：一键生成每日简报》｜X书签文章｜原文链接：[https://x.com/stark_nico99/status/2032098699665686682](https://x.com/stark_nico99/status/2032098699665686682)

- [原文链接](https://x.com/linyishan/status/2033129417376227537)｜《OpenClaw 内置命令完全指南：用好这只龙虾的 18 个斜杠命令》｜来源条目：[摘要：OpenClaw 内置命令完全指南：用好这只龙虾的 18 个斜杠命令](summaries/摘要：OpenClaw 内置命令完全指南：用好这只龙虾的 18 个斜杠命令.md)

- [原文链接](https://blog.chainbase.com/chainbase-newsletter-february-2026)｜《Chainbase 2026 年 2 月月报：AI Agent 的链上数据层正在成形》｜来源条目：[摘要：Chainbase 2026 年 2 月月报：AI Agent 的链上数据层正在成形](summaries/摘要：Chainbase 2026 年 2 月月报：AI Agent 的链上数据层正在成形.md)

- [原文链接](https://x.com/sitinme/status/2033171859144048745)｜《SwarmClaw：从管理一个 AI 助手到指挥一支 AI 团队》｜来源条目：[摘要：SwarmClaw：从管理一个 AI 助手到指挥一支 AI 团队](summaries/摘要：SwarmClaw：从管理一个 AI 助手到指挥一支 AI 团队.md)

- [原文链接](https://x.com/HiTw93/status/2033332424134795568)｜《MemOS：给 OpenClaw Agent 装上真正的长期记忆系统》｜来源条目：[摘要：MemOS：给 OpenClaw Agent 装上真正的长期记忆系统](summaries/摘要：MemOS：给 OpenClaw Agent 装上真正的长期记忆系统.md)

- [原文链接](https://x.com/akokoi1/status/2033335986214854911)｜《AgentCard：用国内 Visa 卡订阅 Claude，5 分钟搞定虚拟预付卡》｜来源条目：[摘要：AgentCard：用国内 Visa 卡订阅 Claude，5 分钟搞定虚拟预付卡](summaries/摘要：AgentCard：用国内 Visa 卡订阅 Claude，5 分钟搞定虚拟预付卡.md)

- [原文链接](http://x.com/i/article/2033336026006257664)｜《Happycapy：把 OpenClaw 和 Claude Code 装进浏览器，人人可用的 Agent 原生电脑》｜来源条目：[摘要：Happycapy：把 OpenClaw 和 Claude Code 装进浏览器，人人可用的 Agent 原生电脑](summaries/摘要：Happycapy：把 OpenClaw 和 Claude Code 装进浏览器，人人可用的 Agent 原生电脑.md)

- [原文链接](https://x.com/shangdu2005/status/2033360814355415061)｜《领哥量化机甲：用 OpenClaw + LLM 打造你的币安 AI 自动交易助手》｜来源条目：[摘要：领哥量化机甲：用 OpenClaw + LLM 打造你的币安 AI 自动交易助手](summaries/摘要：领哥量化机甲：用 OpenClaw + LLM 打造你的币安 AI 自动交易助手.md)

- [原文链接](https://x.com/oooooyoung/status/2033381962673766468)｜《AI 打狗时代来了？用 OKX OnchainOS + OpenClaw 让 Agent 替你链上自动交易》｜来源条目：[摘要：AI 打狗时代来了？用 OKX OnchainOS + OpenClaw 让 Agent 替你链上自动交易](summaries/摘要：AI 打狗时代来了？用 OKX OnchainOS + OpenClaw 让 Agent 替你链上自动交易.md)

- [原文链接](https://x.com/oran_ge/status/2033420708815208868)｜《GLM-5-Turbo：全球首个为 OpenClaw 龙虾训练的专属大模型》｜来源条目：[摘要：GLM-5-Turbo：全球首个为 OpenClaw 龙虾训练的专属大模型](summaries/摘要：GLM-5-Turbo：全球首个为 OpenClaw 龙虾训练的专属大模型.md)

- [原文链接](https://x.com/Chris_Defi/status/2033462650932523473)｜《200U 换来的 45 天实战：OpenClaw 高 ROI 部署最佳实践》｜来源条目：[摘要：200U 换来的 45 天实战：OpenClaw 高 ROI 部署最佳实践](summaries/摘要：200U 换来的 45 天实战：OpenClaw 高 ROI 部署最佳实践.md)

- [原文链接](https://x.com/shao__meng/status/2033497056460079453)｜《self-improving-agent：让 AI 编程助手从错误中真正学习的 OpenClaw Skills》｜来源条目：[摘要：self-improving-agent：让 AI 编程助手从错误中真正学习的 OpenClaw Skills](summaries/摘要：self-improving-agent：让 AI 编程助手从错误中真正学习的 OpenClaw Skills.md)

- 《一周暴涨 8.4k Star：GitHub Coding AI 开源项目周榜 Top 20 深度解析》— X书签，2026-03-16：将 OpenClaw 视为当周最强个人 AI 助手项目

- 《OpenClaw 生态七件套：那些大项目之外值得关注的小众开源神器》— X书签，2026-03：补充轻量化、数据接入、记忆增强与安全治理生态版图

- 《OpenClaw 提速指南：一个加密交易员写出的 AI Agent 优化手册》— X书签，2026-03-17：补充分层记忆、vault 路由与工作区瘦身实践

- 《用 GraphRAG 群体模拟「降维打击」Polymarket：一个 AI 交易机器人的技术拆解与冷思考》— X书签，2026-03-18：将 OpenClaw 作为预测市场交易 Agent 的执行层

- 《OpenClaw：Jensen Huang 口中「下一个 Linux」，Agent 时代的操作系统》｜X书签文章｜原文链接：[https://x.com/Voxyz_ai/status/2034334016711626766](https://x.com/Voxyz_ai/status/2034334016711626766)

- 《OpenClaw 的「睡醒失忆」问题：用 [MEMORY.md](http://memory.md/) 和 [AGENTS.md](http://agents.md/) 让龙虾记住你》｜X书签文章｜原文链接：[https://x.com/YuLin807/status/2034515832286708007](https://x.com/YuLin807/status/2034515832286708007)

- [原文链接](https://x.com/0xKingsKuan/status/2035029914844635315)｜《OpenClaw：AI 已经开始自己雇自己，这个「AI 代理经济」每月流水 260 万美元》｜来源条目：[摘要：OpenClaw：AI 已经开始自己雇自己，这个「AI 代理经济」每月流水 260 万美元](summaries/摘要：OpenClaw：AI 已经开始自己雇自己，这个「AI 代理经济」每月流水 260 万美元.md)

- [原文链接](https://x.com/0xKingsKuan/status/2035182295129461118)｜《ClawFlows：Alchemy CEO 把私人生活 OS 开源了，100+ 预置工作流让 AI Agent 真正跑起来》｜来源条目：[摘要：ClawFlows：Alchemy CEO 把私人生活 OS 开源了，100+ 预置工作流让 AI Agent 真正跑起来](summaries/摘要：ClawFlows：Alchemy CEO 把私人生活 OS 开源了，100+ 预置工作流让 AI Agent 真正跑起来.md)

- [原文链接](https://x.com/CryptoJHK/status/2035277242398540067)｜《OpenClaw 跑通小红书全自动矩阵：一句话发布，百号齐发》｜来源条目：[摘要：OpenClaw 跑通小红书全自动矩阵：一句话发布，百号齐发](summaries/摘要：OpenClaw 跑通小红书全自动矩阵：一句话发布，百号齐发.md)

- [原文链接](https://x.com/servasyy_ai/status/2035992223192654022)｜《XCrawl：3 行代码搞定网页采集，内置代理轮换让爬虫成功率稳定在 90%+》｜来源条目：[摘要：XCrawl：3 行代码搞定网页采集，内置代理轮换让爬虫成功率稳定在 90%+](summaries/摘要：XCrawl：3 行代码搞定网页采集，内置代理轮换让爬虫成功率稳定在 90%+.md)

- [原文链接](https://x.com/idoubicc/status/2036267766660079765)｜《ClawHost：用 Kubernetes 给每个人分配一只专属 OpenClaw》｜来源条目：[摘要：ClawHost：用 Kubernetes 给每个人分配一只专属 OpenClaw](summaries/摘要：ClawHost：用 Kubernetes 给每个人分配一只专属 OpenClaw.md)

- [原文链接](https://x.com/nexudotio/status/2036810399341740335)｜《Nexu：一键把 OpenClaw AI Agent 接入微信和飞书的开源桌面客户端》｜来源条目：摘要：Nexu：一键把 OpenClaw AI Agent 接入微信和飞书的开源桌面客户端

- [原文链接](https://x.com/tuturetom/status/2036823619339255970)｜《nexu：一键把 OpenClaw AI Agent 接入微信和飞书的开源桌面客户端》｜来源条目：摘要：nexu：一键把 OpenClaw AI Agent 接入微信和飞书的开源桌面客户端

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651027177&idx=1&sn=f3ece19977485e25725110b5dc3e1bb7&chksm=855a263b95874ae0288e165b327a35db0538c226bade72c984a4ff4f99ff14efe7e074c527ab#rd)｜《Openclaw 龙虾五天五连，24小时两更，火力全开！到底更新了些什么？》｜来源条目：[摘要：Openclaw 龙虾五天五连，24小时两更，火力全开！到底更新了些什么？](summaries/摘要：Openclaw 龙虾五天五连，24小时两更，火力全开！到底更新了些什么？.md)

- [原文链接](https://x.com/AYi_AInotes/status/2041021296377737696)｜《OpenClaw 2026.4.5：被 Anthropic 断供后，这只龙虾进化得更猛了》｜来源条目：[摘要：OpenClaw 2026.4.5：被 Anthropic 断供后，这只龙虾进化得更猛了](summaries/摘要：OpenClaw 2026.4.5：被 Anthropic 断供后，这只龙虾进化得更猛了.md)

- [原文链接](https://x.com/AlchainHust/status/2041144820098367592)｜《花叔用多个 OpenClaw Agent 联动，给自己的推文自动生成运营分析报告》｜来源条目：[摘要：花叔用多个 OpenClaw Agent 联动，给自己的推文自动生成运营分析报告](summaries/摘要：花叔用多个 OpenClaw Agent 联动，给自己的推文自动生成运营分析报告.md)

- [原文链接](https://x.com/YuLin807/status/2041667865477312551)｜《用 50 行 Python 跑通 Google A2A 协议：Hermes + OpenClaw 的多 Agent 互联实践》｜来源条目：[摘要：用 50 行 Python 跑通 Google A2A 协议：Hermes + OpenClaw 的多 Agent 互联实践](summaries/摘要：用 50 行 Python 跑通 Google A2A 协议：Hermes + OpenClaw 的多 Agent 互联实践.md)

- [原文链接](https://x.com/TheTuringPost/status/2040936147720048909)｜《Hermes WebUI：给 Hermes Agent 装上浏览器界面，CLI 党也能优雅用 AI》｜源文章：[摘要：Hermes WebUI：给 Hermes Agent 装上浏览器界面，CLI 党也能优雅用 AI](summaries/摘要：Hermes WebUI：给 Hermes Agent 装上浏览器界面，CLI 党也能优雅用 AI.md)

- [原文链接](https://x.com/AYi_AInotes/status/2041021296377737696)｜《OpenClaw 2026.4.5：被 Anthropic 断供后，这只龙虾进化得更猛了》｜源文章：[摘要：OpenClaw 2026.4.5：被 Anthropic 断供后，这只龙虾进化得更猛了](summaries/摘要：OpenClaw 2026.4.5：被 Anthropic 断供后，这只龙虾进化得更猛了.md)

- [原文链接](https://x.com/AlchainHust/status/2041144820098367592)｜《花叔用多个 OpenClaw Agent 联动，给自己的推文自动生成运营分析报告》｜源文章：[摘要：花叔用多个 OpenClaw Agent 联动，给自己的推文自动生成运营分析报告](summaries/摘要：花叔用多个 OpenClaw Agent 联动，给自己的推文自动生成运营分析报告.md)

- [原文链接](https://x.com/YuLin807/status/2041667865477312551)｜《用 50 行 Python 跑通 Google A2A 协议：Hermes + OpenClaw 的多 Agent 互联实践》｜源文章：[摘要：用 50 行 Python 跑通 Google A2A 协议：Hermes + OpenClaw 的多 Agent 互联实践](summaries/摘要：用 50 行 Python 跑通 Google A2A 协议：Hermes + OpenClaw 的多 Agent 互联实践.md)

- [原文链接](https://x.com/servasyy_ai/status/2042951017462169812)｜《同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比》｜来源条目：[摘要：同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比](summaries/摘要：同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzI0Mjc0MzA0Mg%3D%3D&mid=2247485445&idx=1&sn=76cc8a9f0947218acfbaeb3abaaf10cf&chksm=e87d5f08412f5b5a3cd9c4e9c75c6ba3c77347420e6699e8e54fe3e6be0b703447bf8d9c0065#rd)｜《OpenClaw 这次最骚的更新，不是 Molty 更辣了，而是 Agent 开始有灵魂了》｜来源条目：[摘要：OpenClaw 这次最骚的更新，不是 Molty 更辣了，而是 Agent 开始有灵魂了](summaries/摘要：OpenClaw 这次最骚的更新，不是 Molty 更辣了，而是 Agent 开始有灵魂了.md)

- [原文链接](https://x.com/0xJeff/status/2043656911044870203)｜《3 Things I learnt after 3 weeks of using Hermes as a personal analyst》｜来源条目：[摘要：3 Things I learnt after 3 weeks of using Hermes as a personal analyst](summaries/摘要：3 Things I learnt after 3 weeks of using Hermes as a personal analyst.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzE5ODM0MDIyNg%3D%3D&mid=2247484011&idx=1&sn=588c8c9f5f8a8e56cb1d32c5ba91947a&chksm=976d338b09e0fcd9565bdfc1728262bd18a93f1408aecb26a19ba94a31968423d172955f1a51#rd)｜《Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比》｜来源条目：[摘要：Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比](summaries/摘要：Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzA4MjUzNjc0Mw%3D%3D&mid=2247492969&idx=1&sn=718a0a8ae6e983d5a1c4664dddbeae7d&chksm=9e273fecd1442da8124bfb7b68978714369fca084bb9eca8e912c6e2322fc39fe43b2798f446#rd)｜《OpenClaw+爆款工厂：搭建一条10W+爆款内容自动化生产线》｜来源条目：[摘要：OpenClaw+爆款工厂：搭建一条10W+爆款内容自动化生产线](summaries/摘要：OpenClaw+爆款工厂：搭建一条10W+爆款内容自动化生产线.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzA5ODEzMjIyMA%3D%3D&mid=2247733292&idx=1&sn=e39369ea00846c222739652d5b47bcc8&chksm=913f8f245def967dec5b7fa87346d1d1fb0f05e5f0084f9bccfc6aeaf678203157c80fe2767b#rd)｜《「双线实测」Qwen 3.6-Plus，Agentic Coding 已经这么能“扛活儿”了？》｜来源条目：[摘要：「双线实测」Qwen 3.6-Plus，Agentic Coding 已经这么能“扛活儿”了？](summaries/摘要：「双线实测」Qwen 3.6-Plus，Agentic Coding 已经这么能“扛活儿”了？.md)

- [原文链接](https://x.com/witcheer/status/2044456778843238689)｜《I Went Through Every AI Memory Tool I Could Find. There Are Two Camps.》｜来源条目：摘要：I Went Through Every AI Memory Tool I Could Find. There Are Two Camps.

- 摘要：I Went Through Every AI Memory Tool I Could Find. There Are Two Camps.（[原文](https://x.com/witcheer/status/2044456778843238689)）

- [原文链接](https://x.com/chuhaiqu/status/2044701336554643793)｜《这可能是我在 X 上到目前为止看到的最详细最具实操性的 TikTok AI slideshow 手册了，是 Roman 月营收从 0 到 10 万刀的完整路径复盘。》｜来源条目：[摘要：这可能是我在 X 上到目前为止看到的最详细最具实操性的 TikTok AI slideshow 手册了，是 Roman 月营收从 0 到 10 万刀的完整路径复盘。](summaries/摘要：这可能是我在 X 上到目前为止看到的最详细最具实操性的 TikTok AI slideshow 手册了，是 Roman 月营收从 0 到 10 万刀的完整路径复盘。.md)

- [原文链接](https://x.com/tuturetom/status/2044745261679808644)｜《AI 初创必看：Nexu 上线 15 天被薅走 1000+ 账号免费额度的血泪复盘》｜来源条目：[摘要：AI 初创必看：Nexu 上线 15 天被薅走 1000+ 账号免费额度的血泪复盘](summaries/摘要：AI 初创必看：Nexu 上线 15 天被薅走 1000+ 账号免费额度的血泪复盘.md)

- 《OpenClaw 核心文档架构详尽分析与优化方案指南》｜X书签文章｜源文章：OpenClaw：用 Markdown 文件定义 AI Agent 大脑的「文件即代理」框架深度解析

- 源文章页面：[OpenClaw 与 Hermes Agent 官方核心文档架构对比](https://www.notion.so/344701074b6880dd995acb5fdc19fb2a)｜来源条目：[摘要：OpenClaw 与 Hermes Agent 官方核心文档架构对比](summaries/摘要：OpenClaw 与 Hermes Agent 官方核心文档架构对比.md)

- [原文链接](https://mp.weixin.qq.com/s/2k5S5UlZKqACLr8g1Mb2eQ)｜《真香！这可能是openclaw抓取任何网页的终极解决方案了》｜源文章：真香！这可能是openclaw抓取任何网页的终极解决方案了

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzAxMjUyNDQ5OA%3D%3D&mid=2653588165&idx=1&sn=0e0410e1d88cc5ad869c483fbd623864&chksm=8117dbc85ccbaa434bf29379eae62e8bcf7369e5d40eb167b51fe0d75aedc4c94a5c5efd5171#rd)｜《开发者的福音来了！ 京东ClawTip让你的Skill自动赚钱！》｜来源条目：[摘要：开发者的福音来了！ 京东ClawTip让你的Skill自动赚钱！](summaries/摘要：开发者的福音来了！ 京东ClawTip让你的Skill自动赚钱！.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkyMTczNjE3Nw%3D%3D&mid=2247489426&idx=1&sn=f03102462abd5114e7bb97fc03b2a85c&chksm=c0025f4ad0a3e2d4644ede93721e601809efe19f418a3a772f5407a2abd3118f0e0b4392598c#rd)｜《当500万个AI Agent涌入Telegram》｜来源条目：[摘要：当500万个AI Agent涌入Telegram](summaries/摘要：当500万个AI Agent涌入Telegram.md)

## 关联概念

- [AI爆款工厂](entities/AI爆款工厂.md)

- [Kiro CLI](entities/Kiro CLI.md)

- [Headless 模式](concepts/Headless 模式.md)

- [低粉爆款](concepts/低粉爆款.md)

- [异常值逻辑](concepts/异常值逻辑.md)

- [内容工厂工作流](concepts/内容工厂工作流.md)

- [Obsidian Skills](concepts/Obsidian Skills.md)

- OpenClaw 的 concept 版本已合并至本 entity 页

- [Gate MCP Skills](concepts/Gate MCP Skills.md)

- [飞书官方 OpenClaw 插件](concepts/飞书官方 OpenClaw 插件.md)

- [Telegram 群组路由](concepts/Telegram 群组路由.md)

- [memory-lancedb-pro](concepts/memory-lancedb-pro.md)

- [OpenClaw 九层 System Prompt 架构](concepts/OpenClaw 九层 System Prompt 架构.md)

- [6551-twitter-to-binance-square](concepts/6551-twitter-to-binance-square.md)

- [xiaohongshu-mcp](entities/xiaohongshu-mcp.md)

- CDP 直连

- [XCrawl](entities/XCrawl.md)

- [ClawHost](entities/ClawHost.md)

- [Active Memory 插件](entities/Active Memory 插件.md)

- [grounded REM backfill](concepts/grounded REM backfill.md)

- [Memory Wiki](concepts/Memory Wiki.md)

- [openclaw infer CLI](entities/openclaw infer CLI.md)

- [Seedance 2.0](entities/Seedance 2.0.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [delegate_task](concepts/delegate_task.md)

- [Subagents 并行](concepts/Subagents 并行.md)

- [Steer 机制](concepts/Steer 机制.md)

- [异步事件驱动编排](concepts/异步事件驱动编排.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Agent Skills](concepts/Agent Skills.md)

- [SkillHub](entities/SkillHub.md)

- [Context Engineering](concepts/Context Engineering.md)

- [上下文基底](concepts/上下文基底.md)

- [Molty SOUL](concepts/Molty SOUL.md)

- [Agent 人格层](concepts/Agent 人格层.md)

- [Push back 协作](concepts/Push back 协作.md)

- [Hindsight](entities/Hindsight.md)

- [Browser Use](entities/Browser Use.md)

- [OpenRouter](entities/OpenRouter.md)

- [GLM-5.1](entities/GLM-5.1.md)

- [MiniMax M2.7](entities/MiniMax M2.7.md)

- [MCP 协议](concepts/MCP 协议.md)

- [Honcho](entities/Honcho.md)

- [ClawShell](entities/ClawShell.md)

- [Qwen3.6-Plus](entities/Qwen3.6-Plus.md)

- [Agentic Coding](concepts/Agentic Coding.md)

- [OpenCode](entities/OpenCode.md)

- [Terminal-Bench 2.0](concepts/Terminal-Bench 2.0.md)

- [Claw-Eval](concepts/Claw-Eval.md)

- [Agent 持续学习三层框架](concepts/Agent 持续学习三层框架.md)

- [n8n](entities/n8n.md)

- [Nano Banana Pro](entities/Nano Banana Pro.md)

- [Faceless format](concepts/Faceless format.md)

- [Bot Detection](concepts/Bot Detection.md)

- [AI Post Verification](concepts/AI Post Verification.md)

- [静态住宅 IP](concepts/静态住宅 IP.md)

- [nexu](entities/nexu.md)

- [注册行为基线分析](concepts/注册行为基线分析.md)

- [一次性邮箱域名检测](concepts/一次性邮箱域名检测.md)

- [群体异常检测](concepts/群体异常检测.md)

- [文件即大脑](concepts/文件即大脑.md)

- [程序性记忆](concepts/程序性记忆.md)

- [STYLE.md](concepts/STYLE.md.md)

- [EVOLUTION.md](concepts/EVOLUTION.md.md)

- [受控自进化](concepts/受控自进化.md)

- [TOOLS.md](concepts/TOOLS.md.md)

- [Dokobot](entities/Dokobot.md)

- [ClawTip](entities/ClawTip.md)

- [Skill 变现](concepts/Skill 变现.md)

- [Agent 经济闭环](concepts/Agent 经济闭环.md)

- [Telegram](entities/Telegram.md)

- [Cocoon](entities/Cocoon.md)

- [TON Wallet](entities/TON Wallet.md)

- [IdentityHub](entities/IdentityHub.md)

- [TON MCP](concepts/TON MCP.md)

- [TON Pay SDK](entities/TON Pay SDK.md)
