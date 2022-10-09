import os
from PIL import Image

def compress():
        path = "/Users/mac/Documents/code/web/miniprogram/hjny1/miniprogram/images/product"
        dirlist = os.listdir(path)
        j = 0
        for dirf in dirlist:
            
            Olddir = os.path.join(path, dirf)    #原来的文件路径
            if os.path.isdir(Olddir):       #如果是文件夹则跳过
                filelist = os.listdir(Olddir)
                i =0

                for item in filelist:

                    src = os.path.join(os.path.abspath(Olddir), item)
                    if item.endswith('.jpg'):
                        img = Image.open(src)
                        w,h = img.size
                        
                        fsize = os.path.getsize(src)/1024
                        if fsize < 100:
                            print(fsize)
                            scale = 1.5
                            w,h = round(w * scale),round(h * scale)
                            img = img.resize((w,h),Image.Resampling.LANCZOS )

                        if fsize >150:
                            scale = 1-(fsize/(10*1024))
                            w,h = round(w * scale),round(h * scale)
                            img = img.resize((w,h), Image.Resampling.LANCZOS )
                        img.save(src, quality=95)
                    i+=1
            if(os.path.isdir(Olddir)):

                print(j,dirf,'数量为',i)
                j+=1
if __name__=='__main__':
    compress()