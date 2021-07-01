from PIL import Image

codeLib = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.''' #生成字元畫所需的字符集
count = len(codeLib)

# def transform1(image_file):
#     image_file = image_file.convert("L")#轉換為黑白圖片，引數"L"表示黑白模式
#     codePic = ''
#     for h in range(0,image_file.size[1]):  #size屬性表示圖片的解析度，'0'為橫向大小，'1'為縱向
#         for w in range(0,image_file.size[0]):
#             gray = image_file.getpixel((w,h)) #返回指定位置的畫素，如果所開啟的影象是多層次的圖片，那這個方法就返回一個元組
#             codePic = codePic + codeLib[int(((count-1)*gray)/256)]#建立灰度與字符集的對映
#         codePic = codePic+'\r\n'
#     return codePic

def transform2(image_file):
    codePic = ''
    for h in range(0,image_file.size[1]):
        for w in range(0,image_file.size[0]):
            g,r,b = image_file.getpixel((w,h))
            gray = int(r* 0.299+g* 0.587+b* 0.114)
            codePic = codePic + codeLib[int(((count-1)*gray)/256)]
        codePic = codePic+'\n'
    return codePic


fp = open('test2.jpg','rb')
image_file = Image.open(fp)
image_file=image_file.resize((int(image_file.size[0]*0.09), int(image_file.size[1]*0.09)))#調整圖片大小
print('Info:',image_file.size[0],' ',image_file.size[1],' ',count)

tmp = open('tmp.txt','w')
tmp.write(transform2(image_file))
tmp.close()