
import re

BASE_URL = ('https://www.cia.gov/library/publications/the-world-factbook'
            '/graphics/flags/large/')

re_flag = re.compile(r'src="\.\./graphics/flags/large/([^"]+)"')

with open('flagsoftheworld.html') as arq_html:
    html = arq_html.read()

res = re_flag.findall(html)
for nome in res:
    print nome
