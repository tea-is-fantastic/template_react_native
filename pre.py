from scripts.tif_yaml import app_yaml
import os


def pre():
    os.system(f'npx --yes react-native init {app_yaml.name} --template react-native-template-typescript')