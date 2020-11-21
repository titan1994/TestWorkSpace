"""
Р—Р°РїСѓСЃРє СЃРєСЂРёРїС‚РѕРІ Рё СѓСЃС‚Р°РЅРѕРІРєР° Р±РёР±Р»РёРѕС‚РµРє
"""

from os import system as system
from pathlib import Path


def packege_install(name_pack, name_install=''):
    """РЎРїР°СЃРµРЅРёРµ РѕС‚ РІСЃРµС… Р±РµРґ. РЎС‚Р°РІРёРј РїР°РєРµС‚, РµСЃР»Рё
    РµРіРѕ РЅРµС‚ - РІ РІРёСЂСѓС‚Р°Р»СЊРЅРѕРµ РѕРєСЂСѓР¶РµРЅРёРµ

    Args:
        name_pack: РёРјСЏ Р±РёР±Р»РёРѕС‚РµРєРё РїСЂРё РёРјРїРѕСЂС‚Рµ
        name_install: РёРјСЏ Р±РёР±Р»РёРѕС‚РµРєРё РїСЂРё СѓСЃС‚Р°РЅРѕРІРєРµ
    """
    try:
        exec('import {}'.format(name_pack))
    except ModuleNotFoundError:
        path_pack = Path.cwd() / 'venv' / 'Lib' / 'site-packages'
        name_install = name_install if len(name_install) > 0 else name_pack
        inst_cmd = 'pip install --upgrade --ignore-installed --target={} {}'.format(path_pack, name_install)
        system(inst_cmd)


def get_python_pass():
    """РџРѕР»СѓС‡Р°РµС‚ РїСѓС‚СЊ Рє РїРёС‚РѕРЅСѓ РІ РІРёСЂС‚СѓР°Р»СЊРЅРѕРј
    РѕРєСЂСѓР¶РµРЅРёРё РџР°Р№С‡Р°СЂРј :return: РїСѓС‚СЊ Рє РїРёС‚РѕРЅСѓ
    """

    if Path('venv').exists():
        python_pass = Path.cwd() / 'venv' / 'Scripts' / 'python.exe'
        return python_pass
    return None


def run_python_file_in_env(python_file, params=''):
    """Р·Р°РїСѓСЃРєР°РµС‚ РєР°РєРѕР№-Р»РёР±Рѕ СЃРєСЂРёРїС‚ РїРёС‚РѕРЅР°,
    РёСЃРїРѕР»СЊР·СѓСЏ РїРёС‚РѕРЅ РёР· РІРёСЂС‚СѓР°Р»СЊРЅРѕРіРѕ
    РѕРєСЂСѓР¶РµРЅРёСЏ :param python_file: РїСѓС‚СЊ Рє СЃРєСЂРёРїС‚Сѓ :param
    params: РїР°СЂР°РјРµС‚СЂС‹ Р·Р°РїСѓСЃРєР° :return:

    Args:
        python_file:
        params:
    """
    python_pass = get_python_pass()
    if python_pass is None:
        print('РЅРµ СѓСЃС‚Р°РЅРѕРІР»РµРЅРѕ РІРёСЂС‚СѓР°Р»СЊРЅРѕРµ РѕРєСЂСѓР¶РµРЅРёРµ!')
        return None

    file_run_pass = '{} {} {}'.format(Path(python_pass), Path(python_file), params)
    try:
        result_run = system(file_run_pass)
        print(file_run_pass)
        return result_run
    except Exception as info:
        print(info)
        return None
