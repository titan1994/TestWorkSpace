try:
    import requests
except ModuleNotFoundError:
    import os
    os.system('pip install requests')

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print("Status code:", r.status_code)

# РЎРѕС…СЂР°РЅРµРЅРёРµ РѕС‚РІРµС‚Р° API РІ РїРµСЂРµРјРµРЅРЅРѕР№.
response_dict = r.json()
print(response_dict.keys())

# Get data
repo_dicts = response_dict['items']
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# РџРѕСЃС‚СЂРѕРµРЅРёРµ РІРёР·СѓР°Р»РёР·Р°С†РёРё.
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')
