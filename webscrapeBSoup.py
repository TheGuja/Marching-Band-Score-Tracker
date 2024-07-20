import requests
from bs4 import BeautifulSoup
import pandas as pd

# 2023 PIW
# r = requests.get('https://wgi.org/wp-content/uploads/wgi_events/static_scores/2023/scores_PIW_Finals.html?_gl=1*hhs161*_ga*MTk1NzM4OTU2MS4xNzA2NDgxMjkz*_ga_EQM3XDN44E*MTcwNjU1NjMwNi4yLjEuMTcwNjU1NjMyOC4wLjAuMA..*_gcl_au*MTA0MTY0MTU1Ny4xNzA2NDgxMjkz')

# 2024 PSW
r = requests.get('https://www.wgi.org/scores/')

soup = BeautifulSoup(r.text, 'html.parser')

content = soup.find('div', class_= 'inner-content').find_all('td')

ranking = [line.text for line in content[7::3]]
scores = [line.text for line in content[9::3]]
schools = [line.text for line in content[8::3]]
division = (content[0].text)[:-11]
date = (content[1].text)[11:20]

dict = {
    'school': schools,
    'rank': ranking,
    'score': scores,
    'division': division,
    'date': date
}

df = pd.DataFrame(dict)

# Data for 2023 PIW
# df.to_csv('piw_data.csv', index=False)

# Data for 2024 PSW
df.to_csv('psw_data.csv', index=False)
