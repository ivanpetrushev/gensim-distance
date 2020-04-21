# import requests
import wikipedia
import os
import re
from time import sleep

wiki_titles = [
    # countries
    'Bulgaria', 'Germany', 'Greece', 'Romania', 'Serbia', 'Turkey', 'Albania', 'Andorra', 'Austria', 'Belarus',
    'Belgium', 'Croatia', 'Cyprus', 'Denmark', 'Estonia', 'Finland', 'France', 'Hungary', 'Iceland', 'Ireland',
    'Italy', 'Kosovo', 'Latvia', 'Malta', 'Moldova', 'Monaco', 'Norway', 'Poland', 'Portugal', 'Russia', 'Slovakia',
    'Slovenia', 'Spain', 'Sweden', 'Ukraine', 'China', 'Japan', 'Vietnam', 'Egypt', 'Brazil', 'Mexico',
    'Peru', 'Iran', 'Iraq', 'India',
    # cities - bg
    'Plovdiv', 'Sofia', 'Burgas', 'Varna', 'Pleven', 'Sliven', 'Pernik', 'Haskovo', 'Yambol', 'Vratsa',
    'Gabrovo', 'Asenovgrad', 'Vidin', 'Shumen', 'Sozopol', 'Albena', 'Bansko', 'Pamporovo', 'Borovets',
    'Nesebar', 'Preslav', 'Ohrid', 'Kazanlak', 'Stara_Zagora', 'Melnik', 'Karlovo', 'Kalofer',
    # cities - world
    'Tirana', 'Yerevan', 'Vienna', 'Baku', 'Sarajevo', 'Zagreb', 'Prague', 'Copenhagen', 'Helsinki', 'Paris',
    'Berlin', 'Athens', 'Kiev', 'Minsk', 'Moscow', 'Budapest', 'Dublin', 'Rome', 'Riga', 'Vaduz',
    'Oslo', 'Lisbon', 'Belgrade', 'Bratislava', 'Madrid', 'Bern', 'Ankara', 'London',
    # geography - bg
    'Thrace', 'Balkans', 'Danube', 'Rila', 'Pirin', 'Vitosha', 'Musala', 'Iskar', 'Kabile', 'Black_Sea',
    'Rhodopes', 'Verila', 'Vihren', 'Kutelo', 'Dospat', 'Maritsa', 'Mesta', 'Osam', 'Rezovo',
    'Ropotamo', 'Struma', 'Vacha', 'Veleka', 'Thracia',
    # geography - world
    'Europe', 'Africa', 'Asia', 'Australia', 'North America', 'South America',
    'Nile', 'Alps', 'Andes', 'Alaska', 'K2', 'Aconcagua',
    'Denali', 'Mont_Blanc', 'Amazon_River', 'Lena_River', 'Niger_River', 'Volga', 'Yukon_River',
    # misc
    'European Union', 'Agriculture', 'Christianity', 'Islam', 'Butterfly', 'Deer', 'Wild boar', 'Jackal', 'Fox',
    'Nuclear power',
    # history
    'Roman Empire'
]

for title in wiki_titles:
    filename = 'data/' + title + '.txt'
    if os.path.exists(filename):
        print('Exists: ' + title)
    else:
        print('Downloading: ' + title)
        ## requests-style page fetching
        # response = requests.get(
        #     'https://en.wikipedia.org/w/api.php',
        #     params={
        #         'action': 'query',
        #         'format': 'json',
        #         'titles': title,
        #         'prop': 'extracts',
        #         # 'exintro': True,
        #         # 'exsentences': 10,
        #         'explaintext': True,
        #         'exsectionformat': 'plain'
        #     }
        # )
        # response = response.json()
        # print('response', response)
        # page = next(iter(response['query']['pages'].values()))
        # content = page['extract']

        # module-style page fetching
        content = wikipedia.page(title).content
        content = re.sub(r'\n=.+?=\n', '', content)

        with open(filename, 'w') as fp:
            fp.write(content)
        sleep(1)
