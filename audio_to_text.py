# %%
### install packages
#pip install -U openai-whisper
#brew install ffmpeg

import os
import whisper
from whisper.utils import get_writer # control output format

# %%
audiofile = input('輸入音檔路徑:')

# %%
## 取出音檔名稱作為後續output名稱
file_name_with_extension = os.path.basename(audiofile)
filename, extension = os.path.splitext(file_name_with_extension)

# %%
model = whisper.load_model('medium')

# %%
result = model.transcribe(audiofile, language='zh')

# %%
## Save text file
txt_writer = get_writer('txt', './')
txt_writer(result, filename)

## Save srt file
srt_writer = get_writer('srt', './')
srt_writer(result, filename)


