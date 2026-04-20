---
title: claude-mem
type: entity
tags:
- 记忆系统
- OpenClaw
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/9ddf247fa2e844d88f548604a97180f7
notion_id: 9ddf247f-a2e8-44d8-8f54-8604a97180f7
---

## 定义

claude-mem 是一套基于 RAG + Hook 的开源长期记忆系统，通过生命周期 Hook 收集 OpenClaw 和 Claude Code 的对话与工具调用，存入本地向量库，在新会话中注入相关记忆。

GitHub: [https://github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

## 技术实现

- **存储**：SQLite FTS5 + Chroma 向量库

- **检索**：embedding 语义检索

- **注入**：在新会话开始时，把「相关记忆」以压缩形式注入上下文

## 与 mem9 的对比

| 特性 | claude-mem | mem9 |

| --- | --- | --- |

| 存储 | 本地 | 云端（TiDB Cloud） |

| 提取 | Hook 收集 | 两段式提取+调和 |

| 搜索 | 语义检索 | 混合搜索（向量+全文） |

| 安装 | 一行 curl | 发指令给 Agent |

| 来源 | 开源社区 | TiDB 团队 |

## 已知问题

- 记忆库越大，检索容易错抓相似但不相关内容

- 可能出现幻觉

- 无法从根本上解决上下文漂移

## 安装

```bash
curl -fsSL https://install.cmem.ai/openclaw.sh | bash
```

## 关联概念

- [andrej-karpathy-skills](concepts/andrej-karpathy-skills.md)

- [Evolver](entities/Evolver.md)

- [GenericAgent](entities/GenericAgent.md)

- [CLAUDE.md](concepts/CLAUDE.md.md)

- [Agent Skills](concepts/Agent Skills.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [Multica](entities/Multica.md)

## 来源引用

- [摘要：Claude-Mem：让AI编程助手拥有跨会话持久记忆](summaries/摘要：Claude-Mem：让AI编程助手拥有跨会话持久记忆.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2MjIwODc3Mw%3D%3D&mid=2247518172&idx=1&sn=867250666fc5c9f4a7ca9c84f243b970&chksm=cf5ea8e68aca9ab2d4c501de00f8682baffb9866b120a678223699ba9024ea0b302de2a35158#rd)）

- [摘要：TOP FIVE GITHUB REPOSITORIES THIS WEEK](summaries/摘要：TOP FIVE GITHUB REPOSITORIES THIS WEEK.md)（[原文](https://x.com/RoundtableSpace/status/2045906520672461309)）

- [摘要：本周增长最快的 GitHub 仓库：](summaries/摘要：本周增长最快的 GitHub 仓库：.md)（[原文](https://x.com/pritipatelfgoo/status/2045105855662809267)）

- [摘要：脑子是个好东西：为龙虾和 CC 加装外脑之后，这俩货要上天了](summaries/摘要：脑子是个好东西：为龙虾和 CC 加装外脑之后，这俩货要上天了.md)
