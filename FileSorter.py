import os, shutil

path = r'C:\Users\maxim\OneDrive\Desktop'
files = os.listdir(path)


def get_date(file):
    file = file.split('-')
    file[0] = file[0].split('_')
    return [file[0][1], file[1]]


def create_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)
    return


def move_dir(file, destination):
    shutil.move(file, destination)


for file in files:
    if file.startswith('Snipaste_'):
        date = get_date(file)
        path = f'C:\\Users\\maxim\\OneDrive\\Desktop\\SnipasteFolder\\{date[0]}\\{date[1]}'
        create_dir(path)
        move_dir(f'C:\\Users\\maxim\\OneDrive\\Desktop\\{file}',
                 f'C:\\Users\\maxim\\OneDrive\\Desktop\\SnipasteFolder\\{date[0]}\\{date[1]}')