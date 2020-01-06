#! python3
# Organizes the downloads folder

import os
import shutil
import itertools

downloads_path = r'C:\Users\Username\Downloads'

for item in os.listdir(downloads_path):
    item_path = os.path.join(downloads_path, item)
    if os.path.isfile(item_path):
        f_name, f_ext = os.path.splitext(item)
        
        if f_ext != '':
            make_dir_path = os.path.join(downloads_path, f'{f_ext[1:].upper()} Files')

            # Create a new folder, if folder does not exist
            if not os.path.exists(make_dir_path):
                os.mkdir(make_dir_path)
            
            # Rename file, if filename exist
            if os.path.exists(os.path.join(make_dir_path, f'{item}')):
                for num in itertools.count(1):
                    file_path = os.path.join(make_dir_path, f'{f_name}({num}){f_ext}')
                    if not os.path.exists(file_path):
                        make_dir_path = file_path
                        break

            shutil.move(item_path, make_dir_path)
