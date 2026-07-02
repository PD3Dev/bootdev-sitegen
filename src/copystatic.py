import os
import shutil
def del_public():
    shutil.rmtree('public/')
    os.mkdir('public/')

def copy_static(src, dest):
    print('Hello')
    source_content = os.listdir('.')
    print (source_content)
