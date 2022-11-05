import os

from scripts.tif_yaml import app_yaml


def create_dirs():
    cmd = f'npx --yes react-native init {app_yaml.name} --template react-native-template-typescript --skip-install'
    os.system(cmd)
