import getpass
import audio_to_text as a2t
import summary


def main(input_audio, OPENAI_API_KEY):
    # 音訊轉文字
    output_filename = a2t.convert_audio_to_text(input_audio)

    # 生成摘要
    input_textfile = f'{output_filename}.txt'
    summary_result = summary.summarize_text(input_textfile, OPENAI_API_KEY)

    # 印出摘要結果
    print(summary_result['output_text'])

    # 儲存摘要結果
    with open(f'{output_filename}_summary.txt', 'w') as file:
        file.write(summary_result['output_text'])

if __name__ == "__main__":
    # 輸入音檔路徑和 API KEY
    input_audio = input('輸入音檔路徑:')
    OPENAI_API_KEY = getpass.getpass(prompt='open api key: ')
    
    main(input_audio, OPENAI_API_KEY)