---
title: Jujutsu
type: entity
tags:
- Harness 工程
- CLI 工具
status: 草稿
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/83364607c1e340d18e9eac32868fa802
notion_id: 83364607-c1e3-40d1-8e9e-ac32868fa802
---

## 定义

Jujutsu（命令行工具 `jj`）是由 Google 工程师 Martin von Zweigbergk 开发的**以变更为中心**的版本控制系统，目前已在 Google 内部大规模使用。它以 Git 仓库作为存储后端，完全兼容 Git 生态。

别名：jj

## 关键要点

- **工作区即提交**（working copy as a commit）：工作区始终是一个提交对象，任何文件改动实时反映，永远不会丢失未保存的工作

- **双标识符系统**：每个变更同时维护 Change ID（稳定字母标识，不随内容变化）和 Commit ID（内容哈希，等同 Git commit hash）

- **冲突是一等公民**：冲突存储在提交对象中而不阻塞操作，rebase 遇到冲突不会中止

- **操作日志**：每条命令都记录在操作日志中，`jj op undo` 可撤销任意操作

- **自动 rebase**：修改任意历史提交后，jj 自动 rebase 所有后代提交

- 核心命令：`jj split`（拆分提交）、`jj absorb`（自动归并改动到最合适的祖先）、`jj op undo`（撤销操作）

## 与 Agentic Coding 的关联

- 解决脏工作区问题：工作区始终已提交，agent 探索过程被自动记录

- 降低历史改写成本：自动 rebase 后代，agent 修改历史提交无需手动维护提交链

- `jj split` 和 `jj absorb` 让拆分巨型提交变得低成本

## 来源引用

- [摘要：万字干货｜AI 时代的 Git 版本管理，你用对了吗？](summaries/摘要：万字干货｜AI 时代的 Git 版本管理，你用对了吗？.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkxMTY4NTAyNQ%3D%3D&mid=2247510348&idx=1&sn=0eaed4bb608369011819fade6a28a188&chksm=c0583d219f4fda092c28dae7651cc941f4e0547dd5dedbffea47553e1c5866db75435efd9adc#rd)）
