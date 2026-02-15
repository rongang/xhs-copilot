# OOTD 穿搭风 (Outfit of the Day)

## 风格描述
适合展示服装搭配、街拍、探店。强调全身/七分身构图，自然光感，背景虚化适中。

## 推荐模型
*   **Checkpoint**: MajicMIX Realistic
*   **LoRA**: FilmGirl (权重 0.5)

## 通用 Prompt (正向提示词)
```
(best quality, masterpiece, highres, 8k:1.2), (photorealistic:1.4), raw photo,
1girl, solo, beautiful asian woman, 
(full body shot:1.2), (walking on the street:1.1),
wearing trendy korean fashion, oversized blazer, mini skirt, boots,
natural makeup, happy smile, looking at viewer,
soft lighting, depth of field, city street background, bokeh,
(film grain:0.5), (soft focus:0.8)
```

## Negative Prompt (反向提示词)
```
(worst quality, low quality:1.4), (zombie, sketch, interlocked fingers, comic),
monochrome, grayscale, bad anatomy, bad hands, text, watermark,
missing fingers, extra digit, fewer digits, cropped, worst quality, low quality,
normal quality, jpeg artifacts, signature, watermark, username, blurry,
artist name, bad feet
```

## 参数设置
*   **Sampler**: DPM++ 2M Karras
*   **Steps**: 30
*   **CFG**: 7
*   **Size**: 768x1024 (3:4)