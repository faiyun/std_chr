from paddleocr import PaddleOCR, draw_ocr
from PIL import Image




class  img2text(object):
     # 初始化
    def __init__(self, IMGPath):
        self.IMGPath = IMGPath        
    
    def run(self):
        context_str = ""
        # Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
        # 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
        ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
        img_path = self.IMGPath
        result = ocr.ocr(img_path,cls=True)
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                print(line[1][0])
                context_str += line[1][0]
        print(context_str)
        return context_str

# if __name__ == "__main__":
    
#     img2text = img2text(IMGPath="imgrec_20240510142649.png")
    
#     img2text.run()

