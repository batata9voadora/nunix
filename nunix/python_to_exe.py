import os,shutil
on_cmd = input('on cmd (y/n)')
file = input('file\n')
file_path = file.split('/')
file_py = file.split('.')
path = []
py = ''
try:file_py[1]
except Exception:py = '.py'
for i in range(len(file_path)):
    if i != len(file_path)-1:
        if i != len(file_path)-2:path.append(file_path[i]+'/')
        else:path.append(file_path[i])
file_name = file_path[-1]
path_src = ''
for i in range(len(path)): path_src += path[i]
path_dst = path_src
path_src = path_src+"__pycache__/"+file_name+'.cpython-38.pyc'
if on_cmd == 'y':os.system('pyinstaller --onefile '+file+py)
elif on_cmd == 'n':os.system('pyinstaller --onefile -w '+file+py)
