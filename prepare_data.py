import requests
import os
from time import sleep

wiki_titles = [
    # countries
    'Bulgaria', 'Germany', 'Greece', 'Romania', 'Serbia', 'Turkey', 'Albania', 'Andorra', 'Austria', 'Belarus',
    'Belgium', 'Croatia', 'Cyprus', 'Denmark', 'Estonia', 'Finland', 'France', 'Hungary', 'Iceland', 'Ireland',
    'Italy', 'Kosovo', 'Latvia', 'Malta', 'Moldova', 'Monaco', 'Norway', 'Poland', 'Portugal', 'Russia', 'Slovakia',
    'Slovenia', 'Spain', 'Sweden', 'Ukraine', 'China', 'Japan', 'Vietnam', 'Australia', 'Egypt', 'Brazil', 'Mexico',
    'Peru', 'Iran', 'Iraq', 'India',
    # cities
    'Plovdiv', 'Sofia', 'Burgas', 'Varna', 'Ruse', 'Pleven', 'Sliven', 'Pernik', 'Haskovo', 'Yambol', 'Vratsa',
    'Gabrovo', 'Asenovgrad', 'Vidin', 'Tarnovo', 'Shumen', 'Sozopol', 'Albena', 'Bansko', 'Pamporovo', 'Borovets',
    'Nesebar', 'Preslav', 'Ohrid', 'Kazanlak', 'Stara_Zagora', 'Melnik',
    # geography
    'Thrace', 'Balkans', 'Danube', 'Rila', 'Pirin', 'Vitosha', 'Musala', 'Iskar', 'Kabile', 'Europe', 'Black_Sea',
    'Rhodopes', 'Sakar', 'Verila', 'Vihren', 'Kutelo', 'Nile', 'Sahara',
    # misc
    'NATO',
]

for title in wiki_titles:
    filename = 'data/' + title + '.txt'
    if os.path.exists(filename):
        print('Exists: ' + title)
    else:
        print('Downloading: ' + title)
        response = requests.get(
            'https://en.wikipedia.org/w/api.php',
            params={
                'action': 'query',
                'format': 'json',
                'titles': title,
                'prop': 'extracts',
                'exintro': True,
                'explaintext': True,
            }
        )
        response = response.json()
        page = next(iter(response['query']['pages'].values()))
        with open(filename, 'w') as fp:
            fp.write(page['extract'])
        sleep(1)
