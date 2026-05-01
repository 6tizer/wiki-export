---
title: 摘要：Coxy ——将 GitHub Copilot 额度代理为 OpenAI 兼容 API
type: summary
tags:
- OpenClaw
- IDE 集成
- CLI 工具
- 商业/生态
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: LLM, Cursor
source_article_url: ''
notion_url: https://www.notion.so/Tizer/77a8aa5bb9314ddaaf31c3666c3ae6cc
notion_id: 77a8aa5b-b931-4dda-af31-c3666c3ae6cc
---

**一句话摘要**：Coxy 是本地代理服务，将 GitHub Copilot 的请求翻译成标准 OpenAI 兼容 API，让 OpenClaw 等工具可以利用 Copilot 订阅中几乎无限的 GPT-4o 等模型额度。

**关键洞察**

- **工作原理**：使用 VS Code 插件内置的同一语言服务器包，包了一层 OpenAI 兴容接口，在本地 8000/api 提供服务

- **安装极简**：一行 Docker 命令即可，浏览器登录 GitHub 账号生成 token

- **支持模型**：gpt-4.1、gpt-4o、GPT-5 mini（需要在 GitHub 设置开启）

- **多账号管理**：每个 GitHub 账号有独立免费额度，支持多 token 手动切换、本地 SQLite 存储

- **Copilot CLI 功能**：/fleet 命令实现并行 Subagent，作为第二层 API 选择对 GitHub 个人开发者几乎零迁移成本

**提取的概念**

- Coxy

**原始文章信息**

- 作者：字节笔记本

- 来源：微信公众号

- 发布时间：2026-04-06

- 链接：[https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw==&mid=2247515334](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw%3D%3D&mid=2247515334)

**个人评注**：在 Anthropic 封杀 OpenClaw 订阅后，Coxy + GitHub Copilot 是降低 AI 使用成本的另一选择。尤其对已有 GitHub Pro/Copilot 订阅的 Tizer，这是直接可用的额度币制工具。
