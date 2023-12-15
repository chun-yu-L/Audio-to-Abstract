# 音訊轉文字並生成摘要

這組程式可以將音訊檔案轉換成逐字稿與字幕檔，並且自動生成文字摘要。

## 使用說明

1. clone 此專案
2. 在命令列輸入: python audio_to_summary.py
3. 依提示輸入音訊檔案路徑以及 OpenAI API Key
4. 程式執行完成後,會生成逐字稿與重點摘要檔案

註：音訊轉文字與重點摘要可以獨立執行

## 檔案說明

- `audio_to_summary.py`: 主要的執行檔案
- `audio_to_text.py`: 將音訊轉換成逐字稿的模組
- `summary.py`: 生成文字摘要的模組

## 計畫中的新功能有:

- GUI 介面
    - 提供使用者介面，不需使用命令列
- 串接 whisper API 或 Gemini API
    - 使用 API 服務轉逐字稿，不需本地安裝 whisper 套件
- 客製化 prompt
    - 允許使用者自定義生成摘要的 prompt
- 針對 M 晶片優化
    - 優化效能，特別適用於 Mac 的 M 系列晶片

## 安裝需求

需要安裝以下套件:
- python==3.11
- openai-whisper
- openai
- langchain
- ffmpeg

## 授權

本專案使用 MIT 授權發佈。
