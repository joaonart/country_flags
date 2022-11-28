# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
import shutil
import pandas as pd

def adjust_name(name):
    name = name.replace('austallia','australia')
    return name.capitalize()

def mkdirs(directory, mode=0o777):
    try:
        os.makedirs(directory, mode)
    except OSError as err:
        return err


data = []

path = "assets/flags"

for folder in os.listdir(path):
    if folder != ".DS_Store":
        for item in os.listdir(f"{path}/{folder}"):
            new_item = item.split("-", 1)
            new_item = adjust_name(new_item[0])
            mkdirs(f"assets/flags_new/{folder}")
            original = f"{path}/{folder}/{item}"
            target = f"assets/flags_new/{folder}/{new_item}.png"
            shutil.copyfile(original, target)
            data.append([new_item,f"{new_item}.png",target,folder,f"https://github.com/joaonart/country_flags/raw/master/assets/flags_new/{folder}/{new_item}.png"])

df = pd.DataFrame(data, columns=['Country','Flag','Path','Folder','WebPath'])

df.to_csv("assets/flags_new/country_flags_dataset.csv")

print(df)
