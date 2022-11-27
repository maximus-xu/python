import os, shutil

path = r'C:\Users\maxim\OneDrive\Desktop'
files = os.listdir(path)
file_types = {'.pdf':'pdf', '.png':'png', '.drawio':'drawio', '.html':'html', '.txt':'txt', '.wrpl':'wrpl', '.rbxl':'rbxl'}


def create_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)
    return


def move_dir(file, destination):
    shutil.move(file, destination)


for file in files:
    for file_type in file_types:
        if file.lower().endswith(file_type):
            create_dir(f'C:\\Users\\maxim\\OneDrive\\Desktop\\{file_types[file_type]}')
            move_dir(f'C:\\Users\\maxim\\OneDrive\\Desktop\\{file}', f'C:\\Users\\maxim\\OneDrive\\Desktop\\{file_types[file_type]}')