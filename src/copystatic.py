import os
import shutil
def del_docs():
    shutil.rmtree('docs/')
    os.mkdir('docs/')

def copy_static(src, dest):
    source_content = os.listdir(src)
#    print(f'Current source folder content: {source_content}')

    for item in source_content:
        if os.path.isfile(f'{src}{item}'):
#            print(f'Copying: {src}{item}')
            shutil.copy(f'{src}{item}', dest)
        else:
            new_src = f'{src}{item}/'
            new_dest= f'{dest}{item}/'
#            print(f'Creating: {new_dest}')
            os.mkdir(new_dest)
            copy_static(new_src, new_dest)
