import os
import shutil
def Create(dst='Extracted'):
    try:
        os.makedirs(dst)
    except:
        pass
    return dst
def Perfect(list_to_extract,path=os.getcwd(),dst='{}'.format(Create())):
    my_paths=[]
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(list_to_extract):
                my_paths.append(os.path.join(root, file))
    for i in my_paths:
        s = i.replace('\\', ':').split(':')[-1]
        print(s)
        shutil.copyfile(i,dst+'\\{}'.format(s))
    return my_paths
Perfect(('JPG','jpg','PNG','png'))
