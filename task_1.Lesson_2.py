import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint
import json

url = 'https://hh.ru'

name_vacancy = input()

params = {"search_field":"name",
          "text": name_vacancy,
          "page": 0}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

response = requests.get(url+'/search/vacancy', params=params, headers=headers)

dom = BeautifulSoup(response.text, 'html.parser')

vacancy_list = dom.find_all('div', {'class': 'vacancy-serp-item__row vacancy-serp-item__row_header'})

vacancy_jobs = []

for vacancy in vacancy_list:
    vacancy_data = {}

    info = vacancy.find('a', {'class': 'bloko-link'}).getText()
    info_2 = vacancy.find('a')
    link = info_2['href']
    salary = vacancy.find('div', {'class': 'vacancy-serp-item__compensation'})
    if not salary:
        salary_min = None
        salary_max = None
    else:
        salary = salary.getText().replace(u'\xa0', u'')
        salaries = salary.split('-')
        salaries[0] = re.sub(r'[^0-9]', '', salaries[0])
        salary_min = int(salaries[0])
        if len(salaries) > 1:
            salaries[1] = re.sub(r'[^0-9]', '', salaries[1])
            salary_max = int(salaries[1])
        else:
            salary_max = None
    vacancy_data['name'] = info
    vacancy_data['link'] = link
    vacancy_data['salary_max'] = salary_max
    vacancy_data['salary_min'] = salary_min
    vacancy_data['source'] = "hh.ru"

    vacancy_jobs.append(vacancy_data)

pprint(vacancy_jobs)


with open("job_search.json", "w", encoding="utf-8") as f:
    json.dump(vacancy_jobs, f)

