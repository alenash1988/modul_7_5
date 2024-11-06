import os
import time
directory = "."

for root, dirs, files in os.walk(directory):
    # print(type(root), type(dirs), type(files))
    for file in files:
        filepath = os.path.join(root,file)
        # print(filepath)
        filetime = os.path.getatime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'''Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},
             Родительская директория: {parent_dir}''')



