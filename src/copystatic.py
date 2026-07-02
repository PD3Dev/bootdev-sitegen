import os
import shutil
def del_public():
    shutil.rmtree('public/')

def copy_static():
    print('Hello')
    current_directory = os.listdir('.')
    print (current_directory)
