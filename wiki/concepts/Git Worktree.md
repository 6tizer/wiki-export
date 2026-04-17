---
title: Git Worktree
type: concept
tags:
- 开发工具
- 工作流
status: 审核中
confidence: medium
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/698addfbefd54f35a35cac9e790bd847
notion_id: 698addfb-efd5-4f35-a35c-ac9e790bd847
---

## 定义

Git Worktree 是 Git 的内置功能，允许同一个仓库同时检出到多个工作目录，每个工作目录可以处于不同的分支，共享底层的 `.git` 对象存储。

## 在 Agentic Engineering 中的应用

在多 Agent 并行开发场景下，Git Worktree 被用作 Agent 任务隔离的核心机制：

- 每个 Agent 任务分配一个独立的 worktree

- Agent 在自己的工作目录中自由修改文件，不影响其他 Agent 的工作

- 任务完成后，通过 diff 审查决定是否合并到主分支

代表性工具：SuperConductor 明确以 git worktree 作为 Agent 并行隔离方案。

## 基本命令

```bash
git worktree add ../feature-branch feature-branch   # 新增 worktree
git worktree list                                    # 列出所有 worktree
git worktree remove ../feature-branch               # 删除 worktree
```

## 来源引用

- [原文链接](https://x.com/runes_leo/status/2042243228678693244)｜《用半年 Claude Code 踩坑，我验证了 OpenAI/Cursor/Anthropic 三篇 Harness Engineering 的每一条》｜来源条目：[摘要：用半年 Claude Code 踩坑，我验证了 OpenAI/Cursor/Anthropic 三篇 Harness Engineering 的每一条](summaries/摘要：用半年 Claude Code 踩坑，我验证了 OpenAI-Cursor-Anthropic 三篇 Harness Engineering 的每一条.md)

- SuperConductor 官网 [https://super.engineering/](https://super.engineering/) 功能介绍（2026-04-10）

- 《obra/superpowers：让 AI 写代码真正靠谱的方法论》｜X书签文章｜原文链接：[https://x.com/sitinme/status/2031976481933414457](https://x.com/sitinme/status/2031976481933414457)

- [原文链接](https://x.com/vikingmute/status/2036043855594975485)｜《Superpowers：给你的 AI 编码代理装上一套严格的开发方法论》｜来源条目：[摘要：Superpowers：给你的 AI 编码代理装上一套严格的开发方法论](summaries/摘要：Superpowers：给你的 AI 编码代理装上一套严格的开发方法论.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkyOTY1NzMzNg%3D%3D&mid=2247489341&idx=1&sn=daacfde9379ca04f72db432ff7d3a506&chksm=c3c92ed089e6aa78d4d6b3470f7a3c3ef68c1ce53308052413796c8de473c962f7b365246a83#rd)｜《git worktree在AI编程智能体时代为啥火了》｜来源条目：[摘要：git worktree在AI编程智能体时代为啥火了](summaries/摘要：git worktree在AI编程智能体时代为啥火了.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw%3D%3D&mid=2247515443&idx=1&sn=83324258b9f56b464f858f0deb0962a1&chksm=e99cecb1a90cbe4df1285e9b663144d03d9aa6cf67951e02148b275d61446970490fc395284c#rd)｜《全新重构版Claude Code Desktop上线！把Codex APP抄了个遍》｜源页面：全新重构版Claude Code Desktop上线！把Codex APP抄了个遍

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw%3D%3D&mid=2247515443&idx=1&sn=83324258b9f56b464f858f0deb0962a1&chksm=e99cecb1a90cbe4df1285e9b663144d03d9aa6cf67951e02148b275d61446970490fc395284c#rd)｜源页面：全新重构版Claude Code Desktop上线！把Codex APP抄了个遍

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw%3D%3D&mid=2247515443&idx=1&sn=83324258b9f56b464f858f0deb0962a1&chksm=e99cecb1a90cbe4df1285e9b663144d03d9aa6cf67951e02148b275d61446970490fc395284c#rd)｜《全新重构版Claude Code Desktop上线！把Codex APP抄了个遍》｜来源条目：摘要：全新重构版Claude Code Desktop上线！把Codex APP抄了个遍

## 关联概念

- [superpowers 框架](concepts/superpowers 框架.md)

- [测试驱动开发](concepts/测试驱动开发.md)

- [Claude Code](entities/Claude Code.md)

- [Claude Code Desktop](entities/Claude Code Desktop.md)

- [目录级会话绑定](concepts/目录级会话绑定.md)

- [Claude Code Desktop](entities/Claude Code Desktop.md)

- [Routines](concepts/Routines.md)

- Claude Code Desktop

- [Claude Code Routines](concepts/Claude Code Routines.md)
