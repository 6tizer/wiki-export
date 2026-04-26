---
title: 摘要：从0开始，在国内用上Claude Code的终极保姆教程来了。
type: summary
tags:
- 代码生成
- Agent 协作模式
- CLI 工具
status: 已审核
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: https://www.notion.so/348701074b68811c9436d1793497eec5
notion_url: https://www.notion.so/5dc255b654634731bf26bda6475b68f8
notion_id: 5dc255b6-5463-4731-bf26-bda6475b68f8
---

## 一句话摘要

这篇教程系统梳理了在国内环境下安装、配置并上手 **Claude Code** 的完整路径，核心思路是将 Claude Code 作为 Agent 框架使用，并通过 **GLM-5.1** 等模型与 **CC Switch** 完成替代接入。

## 关键洞察

- 文章强调 **Claude Code 本质上是 Agent 框架**，即使无法直接使用 Anthropic 原生模型，依然可以通过第三方模型继续获得较强的编码体验。

- 教程按 **Mac / Windows**、**有魔法 / 无魔法** 四种场景拆解安装路径，降低了国内用户的接入门槛。

- 在模型接入层，文章把 **CC Switch** 作为更通用的模型切换方案，而不是只停留在单一厂商提供的一键命令。

- 文章把 [**CLAUDE.md**](http://claude.md/) 提升为长期使用 Claude Code 的核心约束层，强调“先定规范、再开始协作”的方法论。

- 除了安装，文章还补上了启动目录、安全提示、权限放行和项目级约束文件等实践细节，覆盖了从“装上”到“用顺手”的完整链路。

## 提取的概念

- [Claude Code](entities/Claude Code.md)

- [GLM-5.1](entities/GLM-5.1.md)

- [CC Switch](entities/CC Switch.md)

- [CLAUDE.md](concepts/CLAUDE.md.md)

## 原始文章信息

- 作者：数字生命卡兹克

- 来源：微信

- 发布时间：2026-04-20 10:08

- 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA%3D%3D&mid=2647681650&idx=1&sn=ebe9c3f89ede3094c532f47dcd495081&chksm=f1848a70eb0ed8813b80a31c693a43c481d2e6a4d5180ff577c22c46d4146fd3e97b57ec5be4#rd)

- 源文章页面：从0开始，在国内用上Claude Code的终极保姆教程来了。

## 个人评注

这篇内容对 Tizer 的价值不只是“教人安装 Claude Code”，而是把 **模型层、Agent 框架层、项目约束层** 拆开来看：框架可复用、模型可替换、规范要前置。这个思路和我们自己的 HITL、内容流水线、知识沉淀体系是相通的——真正可规模化的不是某一个模型，而是围绕模型搭起来的协作接口、目录规范与长期记忆结构。
