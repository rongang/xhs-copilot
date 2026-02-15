# xhs-copilot (小红书智能运营助手)

## 简介
这是一个专为 **MacBook M4 芯片** 优化的本地化小红书运营工具。它利用 **Stable Diffusion** 生成高质量、具“网感”的图片素材，结合自动化脚本辅助文案生成与发布，帮助个人博主高效运营账号。

## 核心功能
*   **AI 绘图 (Stable Diffusion)**: 本地生成小红书爆款风格图片（穿搭、探店、美妆）。
*   **Prompt 管理**: 内置针对小红书优化的提示词库。
*   **自动化工作流**: 集成 ComfyUI 配置，一键生成多尺寸素材。
*   **文案辅助**: 提供 GPT/Claude 提示词模板，生成Emoji丰富的种草文案。

## 硬件与环境要求
*   **硬件**: MacBook Pro (M4 / M3 / M2 / M1 Pro/Max 芯片)
*   **内存**: 推荐 16GB 及以上 Unified Memory
*   **软件**: 
    *   [Draw Things](https://apps.apple.com/us/app/draw-things-ai-generation/id1642835916) (推荐新手)
    *   [ComfyUI](https://github.com/comfyanonymous/ComfyUI) (进阶自动化)

## 模型推荐 (Model Checklist)

| 类型 | 模型名称 | 风格/用途 | 下载地址 (Civitai) |
| :--- | :--- | :--- | :--- |
| **底模** | **MajicMIX Realistic** | 亚洲人���写实、美妆、穿搭 | [Link](https://civitai.com/models/43331/majicmix-realistic) |
| **底模** | **ChilloutMix** | 经典亚洲女性人像 | [Link](https://civitai.com/models/6424/chilloutmix) |
| **LoRA** | **FilmGirl / Polaroid** | 胶片感、拍立得风格 | [Link](https://civitai.com/models/23250/film-girl-film-grain-lo-ra) |
| **LoRA** | **Asian Cutie** | 东亚面孔优化 | [Link](https://civitai.com/models/12694/asian-cutie) |
| **LoRA** | **Blindbox** | 盲盒公仔风格 (IP打���) | [Link](https://civitai.com/models/25995/blindbox) |

## 快速开始

### 1. 安装运行环境
推荐使用 **Draw Things** (App Store 直接下载)，它针对 Apple Silicon 进行了极致优化。

### 2. 导入 Prompt
在 `prompts/` 目录下（即将上传）找到对应的风格文件，复制到绘画软件中。

### 3. 生成图片
*   设置尺寸: 3:4 (1024x1366 或 768x1024)
*   Sampling Steps: 25-30
*   CFG Scale: 7.0

## 项目结构
```
├── prompts/          # 提示词库 (分类：穿搭、美妆、风景)
├── workflows/        # ComfyUI 工作流 JSON 文件
├── scripts/          # 自动化 Python 脚本
└── assets/           # 示例图片
```

## 贡献
欢迎提交 PR 分享你的 Prompt 或工作流！