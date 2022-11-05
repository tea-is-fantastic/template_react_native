import os

from scripts.tif_yaml import app_yaml
from .create_dirs import create_dirs


def pre():
    name = app_yaml.name
    cmd = f'npx --yes react-native init {name} --template react-native-template-typescript --skip-install'
    os.system(cmd)
    create_dirs()
