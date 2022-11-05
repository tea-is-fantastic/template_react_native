import os

from scripts.tif_yaml import app_yaml


def gen_icon():
    cmd = f'npx --yes react-native init {app_yaml.name} --template react-native-template-typescript --skip-install'
    os.system(cmd)


def gen_splash():
    cmd = f'npx react-native generate-bootsplash assets/bootsplash_logo_original.png \
  --background-color=F5FCFF \
  --logo-width=100 \
  --assets-path=assets \
  --flavor=main'
    os.system(cmd)


def gen_assets():
    gen_icon()
    gen_splash()
