import requests
from bs4 import BeautifulSoup as BS
import codecs
import time
import datetime
from random import randint

headers = [{'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
           'Accept':'text/html, application/xhtml+xml, application/xml;q=0.9,*/*;q=0.8'
},
{
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'    
},
{
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
},
{
'User-Agent':'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
}]

def tut_pars(start_url, city=None, language=None):
    session = requests.Session()
    if start_url:
        req = session.get(start_url, headers=headers[randint(0,3)])
        # print(req.status_code)
        if req.status_code == 200:
            bsObj = BS(req.content, "html.parser")
            jobs = []
            errors = []
            url = []
            base_url = 'https://jobs.tut.by'
            url.append(start_url)
            pagination = bsObj.find_all('a',attrs={'data-qa':'pager-page'})
            for link in pagination:
                link_pag = link.get('href')
                url.append(base_url + link_pag)
            time.sleep(2)
            for now_url in url:
                # print(now_url)
                req_div = bsObj.find_all('div',attrs={"class":"vacancy-serp-item"})
                if all_div:
                    for div in all_div:
                        title = div.find('a', attrs={"data-qa":"vacancy-serp__vacancy-title"}) # title #href
                        # print(title.text)
                        employer = div.find('a', attrs={"data-qa":"vacancy-serp__vacancy-employer"})
                        # print(employer.text)
                        descrp = div.find('div', attrs={"data-qa":"vacancy-serp__vacancy_snippet_responsibility"})
                        # print(descrp.text)
                        href = div.find('a', attrs={"data-qa":"vacancy-serp__vacancy-title"})
                        # print(href.get('href'))
                        logo = div.find('img', attrs={"class":"vacancy-serp-item__logo"})
                        # if logo:
                        #     print(logo.get('src'))
                        # else:
                        #     print('-')
                        # date = div.find('span', attrs={"class":"vacancy-serp-item__publication-date"}) # title #href
                        # print(date.text)
                        jobs.append({'url':href.get('href'),
                                    'title': title.text,
                                    'description':descrp.text,
                                    'company':employer.text,
                                    'city_id':city, 'language_id':language})
                else:
                    errors.append({'url': url, 'title': "Div does not exists"})
        else:
            errors.append({'url': url, 'title': "Page do not response"})
            # handle = codecs.open('div.html','w', 'utf-8')
            # handle.write(str(jobs))
            # handle.close  
    return jobs,errors

def bel_pars(start_url, city=None, language=None):
    session = requests.Session()
    if start_url:
        req = session.get(start_url, headers=headers[randint(0,3)])
        if req.status_code == 200:
            bsObj = BS(req.content, "html.parser")
            jobs = []
            errors = []
            pag_url = []
            base_url = 'https://belmeta.com'
            # url.append(start_url)
            pagination = bsObj.find_all('a',attrs={'class':'page'})
            for link in pagination:
                link = link.get('data-href')
                links = base_url + link
                # print(links)
                if links not in pag_url:
                    pag_url.append(links)
            # print(pag_url)

            time.sleep(2)
            for now_url in pag_url:
                # print(now_url)
                req = session.get(now_url, headers=headers[randint(0,3)])
                time.sleep(2)
                bsObj = BS(req.content, "html.parser")
                all_div = bsObj.find_all('article',attrs={"class":"job"})
                # print(all_div)
                if all_div:
                    for div in all_div:
                        title_div = div.find('h2', attrs={"class":"title"})
                        title = title_div.text # title #href
                        # print(title)
                        hrefs_divs = div.find('a',href=True)
                        hrefs_div = hrefs_divs.get('href')
                        href = base_url + hrefs_div
                        # print(href)
                        company_div = div.find('div', attrs={"class":"company"})
                        company = company_div.text # title #href
                        # print(company)
                        desc_div = div.find('div', attrs={"class":"desc"})
                        decript_with_spaces = desc_div.text # title #href
                        decript = decript_with_spaces.strip()
                        # print(decript)
                        # print(decript)
                        jobs.append({'url':href,
                                    'title': title,
                                    'description':decript,
                                    'company':company,
                                    'city_id':city, 'language_id':language})
                else:
                    errors.append({'url': url, 'title': "Div does not exists"})
        else:
            errors.append({'url': url, 'title': "Page do not response"})
                # handle = codecs.open('div.html','w', 'utf-8')
                # handle.write(str(jobs))
                # handle.close  
    return jobs,errors


