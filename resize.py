# coding=utf-8
import os
from os import listdir
from os.path import isfile, join
from shutil import copyfile

__author__ = 'matheusjardimb'

mypath = '.'

retina_sufix_2x = '@2x'
retina_sufix_1x = '@1x'

allowed_extensions = ['.png']

res = 'res'
res_ldpi = 'res\\drawable-ldpi'
res_mdpi = 'res\\drawable-mdpi'
res_hdpi = 'res\\drawable-hdpi'
res_xhdpi = 'res\\drawable-xhdpi'
res_xxhdpi = 'res\\drawable-xxhdpi'
res_dirs = [res, res_ldpi, res_mdpi, res_hdpi, res_xhdpi, res_xxhdpi]


def sanitize_filename(name):
    new_filename = name.replace(retina_sufix_1x, '')
    new_filename = new_filename.replace(retina_sufix_2x, '')
    new_filename = new_filename.replace('-', '_')
    new_filename = new_filename.lower()
    return new_filename


def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


for directory in res_dirs:
    create_dir(directory)

for filename in listdir(mypath):
    if isfile(join(mypath, filename)) and [ext for ext in allowed_extensions if ext in filename]:
        path = res_ldpi
        if retina_sufix_2x in filename:
            path = res_hdpi

        new_name = sanitize_filename(filename)
        copyfile(filename, os.path.join(path, new_name))
