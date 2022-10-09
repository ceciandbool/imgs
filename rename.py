import os
from PIL import Image
class BatchRename():
 
    def rename(self):
        path = "/Users/mac/Documents/code/web/miniprogram/hjny1/miniprogram/images/product"
        dirlist = os.listdir(path)
        for dirf in dirlist:
            Olddir = os.path.join(path, dirf)    #原来的文件路径
            if os.path.isdir(Olddir):       #如果是文件夹则跳过
                filelist = os.listdir(Olddir)
                i =0
                for item in filelist:
                    src = os.path.join(os.path.abspath(Olddir), item)
                    dst = os.path.join(os.path.abspath(Olddir), ''+str(i)+'.jpg')
                    if item.endswith('.jpg') or item.endswith('.JPG'):
                        try:
                            os.rename(src, dst)
                            i += 1
                        except:
                            continue
                    elif item.endswith('.png'):
                        im = Image.open(src)
                        im = im.convert('RGB')
                        im.save(dst, quality=95)
                        os.remove(src)
                        i+=1



            print(dirf,'数量为',i)
if __name__=='__main__':
    demo = BatchRename()
    demo.rename()