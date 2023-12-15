import os
import whisper
from whisper.utils import get_writer # control output format


def convert_audio_to_text(input_audio):
    # 取出音檔名稱作為後續output名稱
    file_name_with_extension = os.path.basename(input_audio)
    filename, _ = os.path.splitext(file_name_with_extension)
    
    # 載入模型
    model = whisper.load_model('medium')
    
    # 轉錄音檔
    result = model.transcribe(input_audio, language='zh')
    
    ## 儲存 txt 檔
    txt_writer = get_writer('txt', './')
    txt_writer(result, filename)
    
    #儲存 srt 檔
    srt_writer = get_writer('srt', './')
    srt_writer(result, filename)

    return filename

if __name__ == "__main__":
    # 如果直接執行這個腳本，讓使用者輸入音檔路徑
    input_audio = input('輸入音檔路徑:')
    convert_audio_to_text(input_audio)
    


