---
title: Polymarket
type: entity
tags:
- Crypto/DeFi
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a7d211b5113d4c0ea733b5fda816f582
notion_id: a7d211b5-113d-4c0e-a733-b5fda816f582
---

## 定义

Polymarket 是目前全球流动性最深的去中心化预测市场，建立在 Polygon 区块链上，月交易量已突破 **27 亿美元**。用户对政治、经济、体育、加密等事件结果下注，市场价格反映人群对概率的集体判断，常被媒体引用作为事件走势的风向标。

**总部**：纽约 | 2025 年估值 20 亿美元 | ICE（洲际交易所母公司）投资 20 亿美元

## 与 AI Agent 的结合

OpenClaw 等 AI Agent 框架已被社区用于 Polymarket 套利交易：

- **无风险套利**：监控 Yes + No 价格之和 < $1 的套利窗口，Agent 自动执行双边建仓

- **延迟套利**：利用 Polymarket 价格更新的几百毫秒滞后，在外部市场变动后快速下注

- 有真实案例：单个 Bot 账号历史合约超过 2 万笔，净利润超过 65 万美元

## 已知风险

- 约 25% 交易量是虚假的（刷量交易），峰值期间高达 60%

- 市场流动性有限，夸张收益宣称（「48 小时赚 $10 万」）数学上往往不成立

- 套利窗口随参与者增加而快速收窄

## 来源引用

- Jacob Posel 的「七天 700 万」：一场关于 OpenClaw 与 Polymarket 的反向炒作解析

- OpenClaw + Polymarket 的「躺赚神话」：一场你该保持警惕的造富叙事

- 当「OpenClaw」变成钓鱼钩：一个 Crypto 骗局的解剖

- 摘要：用两个 AI 代理把 $1000 变成 $2265：Rust 套利 vs Python 体育延迟优势实战

- 《planktonXD：用 1000 美元和自动化机器人在 Polymarket 赚到 10 万美元的人》（TGweb3）— 提供了高频小额自动化下注的典型案例

- 《PolyCop：用 AI 扫描钱包、一键跟单的 Polymarket「彭博终端」》（@qkl2058，X书签）— 补充预测市场工具向“信息终端 + 执行入口”一体化发展的案例

- 《OpenClaw 遇上 Polymarket：一个让你心动的套利故事，以及它经不起推敲的数学》（0x_Miko，X书签）— 从订单簿、时延与滑点角度补充跟单叙事的现实约束

- 《Polymarket 套利圣经：量化团队如何用数学基础设施提取 4000 万美元》（RohOnChain，X书签）— 补充组合套利、整数规划和做市优化的数学基础设施视角

- 《Polymarket 延迟套利机器人：200 毫秒的黄金窗口，还是精心包装的营销话术？》（@0x_Discover，X书签）— 补充低时延执行、数据源军备竞赛与营销化套利叙事的现实边界

- 《用 Claude 搭一套 Polymarket 交易 Agent：Skill 架构比临场判断更靠谱吗？》｜X书签文章｜原文链接：[https://x.com/Mikocrypto11/status/2031992492166693272](https://x.com/Mikocrypto11/status/2031992492166693272)

- [原文链接](https://x.com/waveking1314/status/2033414685069135897)｜《用 Claude 写个交易脚本，一晚赚 2300 美元？Polymarket 套利机器人的真相与幻象》｜来源条目：[摘要：用 Claude 写个交易脚本，一晚赚 2300 美元？Polymarket 套利机器人的真相与幻象](summaries/摘要：用 Claude 写个交易脚本，一晚赚 2300 美元？Polymarket 套利机器人的真相与幻象.md)

- [原文链接](https://x.com/MrRyanChi/status/2033466480067747844)｜《预测市场的 Black-Scholes 时刻：Polymarket 做市量化定价框架全解析》｜来源条目：[摘要：预测市场的 Black-Scholes 时刻：Polymarket 做市量化定价框架全解析](summaries/摘要：预测市场的 Black-Scholes 时刻：Polymarket 做市量化定价框架全解析.md)

- 《用 GraphRAG 群体模拟「降维打击」Polymarket：一个 AI 交易机器人的技术拆解与冷思考》— X书签，2026-03-18：补充多 Agent 群体推演与执行层叙事的典型案例

- [原文链接](https://x.com/qkl2058/status/2033888534587985936)｜《Polymarket 上的「印钞机」：一篇病毒式营销帖背后的套利真相》｜来源条目：[摘要：Polymarket 上的「印钞机」：一篇病毒式营销帖背后的套利真相](summaries/摘要：Polymarket 上的「印钞机」：一篇病毒式营销帖背后的套利真相.md)

- [摘要：Building a $1K/Day Wolf Hour System on Polymarket With Claude - Full Guide](summaries/摘要：Building a $1K-Day Wolf Hour System on Polymarket With Claude - Full Guide.md)（[原文](https://x.com/SolSt1ne/status/2043685450070831212)）

- [摘要：28 tools under the hood of bot that made $1M on Polymarket](summaries/摘要：28 tools under the hood of bot that made $1M on Polymarket.md)（[原文](https://x.com/antpalkin/status/2046654122892403188)）

- [摘要：最近看到一个 AI x 预测市场的项目，UniPat AI @UniPat_AI ，把预测做成了可对比、可验证的一套系统。](summaries/摘要：最近看到一个 AI x 预测市场的项目，UniPat AI @UniPat_AI ，把预测做成了可对比、可验证的一套系统。.md)（[原文](https://x.com/0xAA_Science/status/2046939173710676227)）

- [摘要：I asked PolyClaw Agent to find me best oil trader on Polymarket. He found an absolute monster.](summaries/摘要：I asked PolyClaw Agent to find me best oil trader on Polymarket. He found an absolute monster.md)（[原文](https://x.com/antpalkin/status/2047681583692333333)）

## 关联概念

- 跨交易所套利

- [体育延迟套利](concepts/体育延迟套利.md)

- [Wolf Hour](concepts/Wolf Hour.md)

- [逆向选择](concepts/逆向选择.md)

- 《用两个 AI 代理把 $1000 变成 $2265：Rust 套利 vs Python 体育延迟优势实战》（billtheinvestor，2026-03-08）— 补充 Polymarket 在 AI 自动化交易中的延迟优势案例

- 《Polymarket 与 Kalshi：两条路，一个终点——预测市场双雄的增长方法论》｜X书签文章｜原文链接：[https://x.com/Gans2049/status/2034552709786001789](https://x.com/Gans2049/status/2034552709786001789)

- 《AI Super Quant：把资金费率套利和 Polymarket 对冲做成人人可用的面板》｜X书签文章｜原文链接：[https://superquant.soo.network/](https://superquant.soo.network/)

- [原文链接](https://x.com/sol_jingou/status/2034979403193884992)｜《用 Claude 40 分钟写出 Polymarket 套利机器人：一次关于 AI 辅助量化交易的真实实验》｜来源条目：[摘要：用 Claude 40 分钟写出 Polymarket 套利机器人：一次关于 AI 辅助量化交易的真实实验](summaries/摘要：用 Claude 40 分钟写出 Polymarket 套利机器人：一次关于 AI 辅助量化交易的真实实验.md)
