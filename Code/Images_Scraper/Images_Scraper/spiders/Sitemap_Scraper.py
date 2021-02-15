# from bs4 import BeautifulSoup as bs
# import requests
# import pandas as pd

# Sitemap_Urls = []
# Webpage_Urls = []


# def sitemap_scrape(sitemap):

#     req = requests.get(sitemap)

#     soup = bs(req.text, 'lxml')

#     sub_sitemap = soup.find_all('loc')
#     for link in sub_sitemap:
#         href = link.text
#         Sitemap_Urls.append(href)
#     for url in Sitemap_Urls:
#         r = requests.get(url[:48])

#         xml_soup = bs(r.text, 'lxml')

#         web_pages = xml_soup.find_all('loc')
#         for webpage in web_pages:
#             li = webpage.text
#             Webpage_Urls.append(li)

    
# if __name__ == '__main__':

#     try:
#         sitemap_scrape('https://www.famousbirthdays.com/fb-sitemap.xml')
#     finally:
#         data = Webpage_Urls[3:]
        
#     df = pd.DataFrame(data)
#     df.to_csv('URLs.csv', index=False)
