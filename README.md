<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Gradio-6.x-FF7C00?logo=gradio&logoColor=white" alt="Gradio">
  <img src="https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/ChromaDB-向量库-7B5EA7?logo=database&logoColor=white" alt="ChromaDB">
  <img src="https://img.shields.io/badge/LLM-DeepSeek-4D6BFE?logo=openai&logoColor=white" alt="DeepSeek">
  <img src="https://img.shields.io/badge/协议-MIT-green?logo=opensourceinitiative&logoColor=white" alt="License">
</p>

<h1 align="center">🗂️ MyKB</h1>
<h3 align="center">本地 AI 文件管家 — 拖拽、分类、搜索，全部在本机完成</h3>

<p align="center">
  <a href="#-功能特性">✨ 特性</a> •
  <a href="#-快速开始">🚀 快速开始</a> •
  <a href="#-使用教程">📖 教程</a> •
  <a href="#-api-接口">🔌 API</a> •
  <a href="#-常见问题">❓ FAQ</a> •
  <a href="#-开发计划">🗺️ 计划</a>
</p>

---

> 一套运行在 Windows 本机上的 AI 知识库管理系统。拖放文件即可自动分类，自然语言语义搜索，支持公网暴露与文件下载 —— 全部浓缩在一个 Python 脚本中。**不依赖 Docker、不需要数据库服务器、不对接第三方网盘，数据 100% 本地存储。**

---

## 📸 界面概览

```
┌─────────────────────────────────────────────────────────────────┐
│  👤 私人AI文件管家                                               │
│  🟢 API 运行中 | 🟢 模型就绪 | 🔒 本地模式                      │
├────────────────────────────────┬────────────────────────────────┤
│  📤 上传  📝 文本转文档  📂 文件管理  │  💬 对话查询              │
│                                │                                │
│  ┌──────────────────────────┐  │  ┌────────────────────────┐   │
│  │  拖拽文件到此处（多选）    │  │  │  用户：帮我找SSH密钥    │   │
│  │  支持 txt/md/docx/pdf…   │  │  │                        │   │
│  └──────────────────────────┘  │  │  AI：找到了 —           │   │
│  [🔄 自动分类]                  │  │  文件: ssh-config.md    │   │
│                                │  │  类型: 配置密钥          │   │
│  ┌──────────────────────────┐  │  │  路径: D:\MyKB\…        │   │
│  │ 文件名    │类型   │标签  │  │  │  📥 http://127.0.0.1…   │   │
│  │ ssh.md   │密钥   │配置  │  │  └────────────────────────┘   │
│  │ readme.md│笔记   │文档  │  │  [输入问题…]          [发送]  │
│  └──────────────────────────┘  │                                │
│  [✅ 确认全部入库]              │                                │
└────────────────────────────────┴────────────────────────────────┘
```

---

## ✨ 功能特性

<table>
  <tr>
    <td width="50%">
      <h4>🎯 多文件拖拽上传 + 智能分类</h4>
      <p>一次拖入多个文件，AI 逐个分析内容，自动识别<strong>文件类型</strong>（4种）、匹配<strong>标签</strong>（6类）、生成<strong>内容摘要</strong>。结果以<strong>可编辑表格</strong>呈现，双击单元格即可修改。</p>
    </td>
    <td width="50%">
      <h4>🔍 全文语义搜索对话</h4>
      <p>用自然语言提问，AI 检索向量库后读取<strong>文件完整内容</strong>（非仅标题）来回答。支持诸如"上周上传的API密钥在哪"、"AI短剧的流程是什么"这类口语化查询。</p>
    </td>
  </tr>
  <tr>
    <td>
      <h4>📝 文字一键转文档</h4>
      <p>粘贴任意文字（备忘、密钥说明、项目总结），AI 自动生成标题和摘要，保存为 <code>.md</code> 文件并同步入库。支持添加<strong>自定义标记</strong>方便分类，生成后的文档可在对话中搜索到。</p>
    </td>
    <td>
      <h4>📂 文件管理面板</h4>
      <p>集中浏览全部已索引文件，展示文件名、类型、标签、摘要、<strong>上传时间</strong>。支持<strong>在线编辑分类信息</strong>和<strong>删除索引记录</strong>，修改即时生效。</p>
    </td>
  </tr>
  <tr>
    <td>
      <h4>📥 文件下载 + 永久链接</h4>
      <p>每个入库文件分配唯一 UUID，通过 API 或对话回复中的<strong>完整下载链接</strong>即可获取原文件。支持中文文件名 RFC 5987 编码。</p>
    </td>
    <td>
      <h4>🌐 公网暴露（可选）</h4>
      <p>内置 ngrok 集成，一行命令 <code>--expose</code> 即可将 API 暴露到公网。搜索和下载链接自动切换为公网地址，方便其他设备远程访问。</p>
    </td>
  </tr>
  <tr>
    <td>
      <h4>💾 100% 本地存储</h4>
      <p>所有文件实体、向量数据、元数据全部存于本机磁盘。唯一的外部调用是 DeepSeek API（分类和对话），敏感文件可选择手动分类。</p>
    </td>
    <td>
      <h4>🔄 模型灵活切换</h4>
      <p>使用 OpenAI 兼容 SDK，只需改两行代码即可从 DeepSeek 切换到 Minimax 或任何兼容接口的大模型。</p>
    </td>
  </tr>
</table>

### 固定分类体系

AI 自动标注，用户可随时手动修改：

| 文件类型（4选1） | 可用标签（6选N） |
|:---:|:---|
| 文本笔记 | 文档 · 教程 · 项目说明 |
| 配置密钥 | API Key · 配置 |
| 项目文档 | 项目说明 · 文档 · 教程 |
| 项目截图 | 运行截图 |

---

## 🏗️ 系统架构

```
                         ┌──────────────────────────────┐
     浏览器 / 客户端 ───▶│  Gradio Web UI  :7860        │
                         │  ┌──────┬──────┬──────────┐  │
                         │  │上传  │文本转 │文件管理  │  │
                         │  └──────┴──────┴──────────┘  │
                         │  │       对话查询          │  │
                         └──────────────┬───────────────┘
                                        │
                         ┌──────────────▼───────────────┐
     外部客户端 ────────▶│  FastAPI REST  :8000         │
                         │  /upload /search /download   │
                         │  /files /text-to-doc        │
                         │  /docs (Swagger 交互文档)    │
                         └──────────────┬───────────────┘
                                        │
              ┌─────────────────────────┼─────────────────────────┐
              │                         │                         │
    ┌─────────▼──────┐    ┌─────────────▼──────────┐    ┌────────▼───────┐
    │   ChromaDB     │    │  Sentence-Transformer   │    │  DeepSeek API  │
    │   向量数据库    │    │  MiniLM-L12 (384维)     │    │  文件分类+问答  │
    │   (本地持久化)  │    │  (本机运行, 中英双语)    │    │  (云端调用)     │
    └────────┬───────┘    └─────────────────────────┘    └────────────────┘
             │
    ┌────────▼───────┐
    │   本地磁盘     │
    │   D:\MyKB\     │
    │   chroma_db/   │
    │   我的文件/     │
    └────────────────┘
```

### 技术选型说明

| 组件 | 选型 | 理由 |
|------|------|------|
| **Web 框架** | Gradio 6.x | 内置 Chatbot、Dataframe、File 等 ML 组件，无需写前端代码 |
| **API 服务** | FastAPI | 高性能异步框架，自动生成 Swagger 文档，适合作为对外接口 |
| **向量数据库** | ChromaDB | 零配置本地持久化，Python 原生 API，嵌入模型内嵌运行 |
| **嵌入模型** | MiniLM-L12 多语言版 | 384 维向量，中英双语，本机 CPU 推理即可，无需 GPU |
| **大语言模型** | DeepSeek (deepseek-chat) | 国产模型，中文理解优秀，API 价格低廉 |
| **文档解析** | python-docx | 轻量级，支持 Word 段落和表格文本提取 |

---

## 🚀 快速开始

### 环境要求

| 项目 | 最低要求 |
|------|----------|
| 操作系统 | Windows 11 / Windows 10 |
| Python | 3.11 及以上 |
| 内存 | ≥ 8 GB（嵌入模型运行占用约 2GB） |
| 磁盘 | D 盘空闲 ≥ 5 GB（程序 + 模型 + 文件） |
| 网络 | 需访问 `api.deepseek.com`（模型调用） |
| 其他 | DeepSeek API Key（[免费注册获取](https://platform.deepseek.com/)） |

### 一分钟上手

```bash
# 1. 克隆仓库
git clone https://github.com/ysking-0-0/-ai-Local-AI-File-Assistant-.git
cd -ai-Local-AI-File-Assistant-

# 2. 创建虚拟环境
python -m venv venv
venv\Scripts\activate

# 3. 安装依赖（国内用户用清华镜像加速）
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple chromadb fastapi uvicorn gradio openai sentence-transformers python-docx

# 4. 编辑 app.py 第 17 行，填入你的 DeepSeek API Key
#    DEEPSEEK_API_KEY = "sk-your-key-here"

# 5. 启动
python app.py
```

首次启动自动下载嵌入模型（约 470MB），等待 2-3 分钟后：

> 🌐 浏览器打开 **http://127.0.0.1:7860**  
> 📡 API 文档访问 **http://127.0.0.1:8000/docs**

### 可选：公网暴露

```bash
# 安装 ngrok SDK
pip install pyngrok

# 注册 ngrok.com 获取 authtoken，设置环境变量
set NGROK_TOKEN=你的ngrok_token

# 启动（加 --expose 参数）
python app.py --expose
```

启动后将显示公网地址，其他设备可通过该地址搜索和下载文件。

---

## 📖 使用教程

<details open>
<summary><b>📤 文件上传与自动分类</b></summary>

1. 打开「📤 文件上传」标签页
2. 拖拽一个或多个文件到上传区域，或点击选择文件
3. 点击「🔄 自动分类」—— AI 逐个分析并建议类型、标签、摘要
4. 在下方表格中核对结果（**双击任意单元格**可直接修改）
5. 确认无误后，点击「✅ 确认全部入库」

**支持格式：** `.txt` · `.md` · `.py` · `.json` · `.yaml` · `.yml` · `.ini` · `.cfg` · `.log` · `.docx` · `.pdf` · `.png` · `.jpg` · `.jpeg` · `.gif` · `.bmp` · `.zip` · `.rar`

> ⚠️ 超过 **10MB** 的大文件不提取全文内容，仅记录路径和元数据，节省 AI Token 消耗。

</details>

<details open>
<summary><b>💬 对话式语义搜索</b></summary>

在右侧对话面板中，用自然语言提问：

| 问题示例 | AI 会做什么 |
|----------|------------|
| "帮我找一下 SSH 密钥配置的文档" | 搜索向量库 → 读取匹配文件全文 → 返回具体路径和下载链接 |
| "AI 短剧的制作流程有几个步骤" | 检索相关 SOP 文档 → 提取并总结步骤 → 附带来源文件 |
| "昨天上传了哪些文本笔记" | 匹配时间条件 → 列出符合的文件名、类型和摘要 |
| "傲世九重天第一章讲了什么" | 找到对应小说文件 → 基于原文内容回答情节 |

</details>

<details>
<summary><b>📝 文字转文档</b></summary>

1. 打开「📝 文本转文档」标签页
2. 在文本框中粘贴内容（备忘、配置说明、会议记录等）
3. 可选：在「标记」栏填写注释，方便后续识别（如 `SSH配置`、`项目总结`）
4. 点击「🔄 生成文档并入库」
5. AI 生成标题和摘要 → 保存为 `.md` 文件 → 自动入库

**适用场景：** 随手记录零散信息、保存密钥用途说明、整理项目笔记。

</details>

<details>
<summary><b>📂 文件管理与编辑</b></summary>

1. 打开「📂 文件管理」标签页
2. 点击「🔄 刷新列表」加载全部已索引文件
3. 点击表格中的某一行，选中该文件
4. 在下方编辑区域修改类型、标签、摘要
5. 点击「💾 保存修改」即时更新
6. 点击「🗑️ 删除记录」从知识库移除（原文件保留在磁盘）

</details>

---

## 🔌 API 接口

完整的交互式文档：**http://localhost:8000/docs**（自动生成的 Swagger UI）。

### 端点一览

| 方法 | 路径 | 功能 |
|:---:|------|------|
| `GET` | `/` | 系统信息、版本、端点列表 |
| `POST` | `/upload` | 上传文件 → 自动分类 → 直接入库 |
| `POST` | `/upload-preview` | 上传 + 分类预览（不入库，供外部程序确认）|
| `POST` | `/confirm-upload` | 确认预览结果 → 正式入库 |
| `GET` | `/search?q=关键词` | 语义搜索，返回 AI 答案 + 匹配文件列表 |
| `GET` | `/download/{文件ID}` | 按 ID 下载原文件 |
| `GET` | `/files` | 列出所有已索引文件及元数据 |
| `PUT` | `/files/{文件ID}` | 更新文件类型、标签、摘要 |
| `DELETE` | `/files/{文件ID}` | 删除索引记录 |
| `POST` | `/text-to-doc` | 文字 → `.md` 文档，自动入库 |

### 调用示例

```bash
# ── 搜索 ──
curl "http://localhost:8000/search?q=SSH密钥"

# ── 下载文件 ──
curl -O "http://localhost:8000/download/b19f32ae-8f44-4ebd-876d-2d845a400ee6"

# ── 列出全部文件 ──
curl "http://localhost:8000/files"

# ── 上传文件 ──
curl -X POST -F "files=@报告.docx" -F "files=@笔记.txt" http://localhost:8000/upload

# ── 文字转文档 ──
curl -X POST \
  -F "text=ssh-keygen -t ed25519 生成密钥对" \
  -F "label=SSH配置" \
  http://localhost:8000/text-to-doc

# ── 更新文件元数据 ──
curl -X PUT \
  -F "file_type=配置密钥" \
  -F "tags=API Key, 配置" \
  -F "summary=SSH密钥生成配置说明" \
  http://localhost:8000/files/b19f32ae-8f44-4ebd-876d-2d845a400ee6

# ── 删除文件记录 ──
curl -X DELETE http://localhost:8000/files/b19f32ae-8f44-4ebd-876d-2d845a400ee6
```

### 响应格式示例

搜索接口返回：

```json
{
  "answer": "SSH 密钥配置文件位于：D:\\MyKB\\我的文件\\ssh_config.md...",
  "files": [
    {
      "file_id": "b19f32ae-8f44-4ebd-876d-2d845a400ee6",
      "filename": "ssh_config.md",
      "type": "配置密钥",
      "tags": "API Key, 配置",
      "summary": "SSH密钥生成与配置说明",
      "upload_time": "2026-05-25T23:29:05",
      "file_path": "D:\\MyKB\\我的文件\\ssh_config.md",
      "download_url": "http://127.0.0.1:8000/download/b19f32ae-..."
    }
  ]
}
```

---

## 📁 项目结构

```
📦 MyKB/
├── 📄 app.py                 # 主程序 (~1100行，FastAPI + Gradio + ChromaDB)
├── 📄 check.py               # 数据库诊断工具
├── 📄 README.md              # 本文档
├── 📄 LICENSE                # MIT 协议
├── 📄 .gitignore             # Git 忽略规则
├── 📁 chroma_db/             # ChromaDB 向量库存储（自动生成）
│   └── chroma.sqlite3
├── 📁 我的文件/               # 文件实体存储（上传文件存放处）
├── 📁 temp_uploads/          # 上传临时目录（确认后自动清理）
└── 📁 venv/                  # Python 虚拟环境
```

---

## ⚙️ 配置项

`app.py` 顶部集中管理所有可配置项：

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `DEEPSEEK_API_KEY` | `"sk-your-key-here"` | DeepSeek API 密钥（**必填**）|
| `FILE_THRESHOLD` | `10 * 1024 * 1024` | 大文件阈值（字节），超过不提取全文 |
| `CATEGORY_RULES` | 4 类型 + 6 标签 | 分类规则字典 |
| `FILE_TYPES` / `FILE_TAGS` | 见代码 | UI 中下拉框和多选的选项列表 |
| `_DOWNLOAD_BASE` | `http://127.0.0.1:8000` | 下载链接基础地址（由 `--port` 自动设定）|

### 启动参数

```
python app.py [选项]

选项:
  --port PORT           FastAPI 端口 (默认: 8000)
  --gradio-port PORT    Gradio UI 端口 (默认: 7860)
  --expose              通过 ngrok 暴露 API 到公网
```

### 切换大模型

本项目使用 OpenAI 兼容 SDK，切换模型只需修改两处：

```python
# app.py 约第 62 行 — 修改 API 地址和密钥
openai_client = OpenAI(
    api_key="你的密钥",
    base_url="https://api.minimax.chat/v1"   # 替换为目标 API 地址
)

# classify_file() 和 gradio_chat() 中 — 修改模型名
model="deepseek-chat"   # 替换为目标模型
```

### HuggingFace 镜像

国内用户如果模型下载失败，设置环境变量后重试：

```bash
set HF_ENDPOINT=https://hf-mirror.com
python app.py
```

---

## 🔧 常见问题

<details>
<summary><b>启动报 ModuleNotFoundError</b></summary>

虚拟环境未激活或依赖未安装。先执行 `venv\Scripts\activate`，然后 `pip install` 缺失的包。

</details>

<details>
<summary><b>嵌入模型下载失败或卡住</b></summary>

HuggingFace 在国内访问可能不稳定。设置镜像：
```bash
set HF_ENDPOINT=https://hf-mirror.com
```
然后重新启动程序。

</details>

<details>
<summary><b>端口 7860 已被占用</b></summary>

改用其他端口：
```bash
python app.py --gradio-port 7861
```

</details>

<details>
<summary><b>分类结果不准确怎么办？</b></summary>

- **上传时**：在预览表格中双击单元格直接修改，再确认入库
- **入库后**：去「文件管理」标签页随时修改类型、标签和摘要

</details>

<details>
<summary><b>对话回答不理想</b></summary>

知识库中可能缺少相关文件。先上传更多资料再提问。提问越具体，答案越精准。

</details>

<details>
<summary><b>如何查看数据库中有哪些文件？</b></summary>

```bash
python check.py
```
或通过 API：`curl http://localhost:8000/files`

</details>

---

## 🛣️ 开发计划

- [x] 多文件拖拽上传 + 可编辑分类预览
- [x] 全文语义搜索对话
- [x] 文字转文档自动总结入库
- [x] ngrok 一键公网暴露
- [x] 文件下载（中文文件名 RFC 5987 编码）
- [x] 文件管理面板（查看 / 编辑 / 删除）
- [x] API 接口完整文档（Swagger 自动生成）
- [ ] PDF 全文解析（PyMuPDF）
- [ ] 图片 OCR 文字识别
- [ ] Docker 部署支持
- [ ] 多用户认证与独立知识库空间
- [ ] Webhook 通知（文件入库时触发外部操作）
- [ ] 简历素材智能提取

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建功能分支：`git checkout -b feat/amazing-feature`
3. 提交更改：`git commit -m "feat: add amazing feature"`
4. 推送到分支：`git push origin feat/amazing-feature`
5. 提交 Pull Request

---

## 📄 开源协议

本项目基于 **MIT License** 开源。详见 [LICENSE](LICENSE) 文件。

---

## ⭐ Star History

如果这个项目对你有帮助，请给个 Star ⭐ 支持一下！

---

<p align="center">
  <sub>Built with ❤️ for personal productivity | 数据主权，本机掌控</sub>
</p>
