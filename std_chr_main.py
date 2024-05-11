import text2sound
import img2text as i2t
import websocket
import ssl
import time
import cv2
import sys
  
# 测试时候在此处正确填写相关信息即可运行

APPID='8d8e7214'
APISecret='MDdjMTM0MjEwMjdhYzFlYjE2MDJlOWY4'
APIKey='ae20d56fbcaf9a1116f1b898ead78282'

RATE = 16000 #语音速率

output_pcm = './demo.pcm'
output_wav = './demo.wav'

TEXT = "没有看到文字"

if __name__ == "__main__":

    try:
        TEXT = i2t.img2text("11.png").run()
    except Exception as e:
            print("读取文字失败", e)

    # ffplay -ar 16000 -channels 2 -f s16le -i demo.pcm
    wsParam = text2sound.Ws_Param(APPID=APPID, APISecret=APISecret,APIKey=APIKey,Text=f"请读：{TEXT}[p500]",Rate=RATE)
    websocket.enableTrace(False)

    # 调用Make_Sound，传参进行初始化
    ms = text2sound.Make_Sound(output_pcm,output_wav,wsParam,RATE)

    # 播放wav文件
    ms.sound_out()
    print('播放完毕')