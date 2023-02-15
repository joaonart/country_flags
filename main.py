import os
import uuid
import shutil
import pandas as pd
from os.path import exists


def adjust_name(name):
    name = name.replace('austallia', 'australia')
    return name.capitalize()


def mkdirs(directory, mode=0o777):
    try:
        os.makedirs(directory, mode)
    except OSError as err:
        return err


def file_exists(file_path, file_name):
    if exists(file_path):
        file_name_new = f"{file_name}-{str(uuid.uuid4().fields[-1])[:5]}"
        file_path = file_path.replace(file_name, file_name_new)
        return file_path, file_name_new
    return file_path, file_name


data = []

path = "assets/flags"

remote_path_base = "https://raw.githubusercontent.com/joaonart/country_flags/master/assets/flags_new"

try:

    for folder in os.listdir(path):
        if folder != ".DS_Store":
            for item in os.listdir(f"{path}/{folder}"):
                new_item = item.split("-", 1)
                new_item = adjust_name(new_item[0])
                mkdirs(f"assets/flags_new/{folder}")
                original = f"{path}/{folder}/{item}"
                target = f"assets/flags_new/{folder}/{new_item}.png"
                target, new_item = file_exists(target, new_item)
                shutil.copyfile(original, target)
                data.append([new_item, f"{new_item}.png", target, folder,
                             f"{remote_path_base}/{folder}/{new_item}.png"])

    df = pd.DataFrame(data, columns=['Country', 'Flag', 'Path', 'Folder', 'WebPath'])

    df.to_csv("datasets/country_flags_dataset.csv")

    print("Finished process!!!")

except OSError as error:
    print(error)
