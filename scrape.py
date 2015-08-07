# -*- coding: utf-8 -*-

# scrape Murakami Haruki's blog
# 村上さんのところ
# http://www.welluneednt.com
# book version
# http://www.shinchosha.co.jp/murakamisannotokoro/books/

import requests
from bs4 import BeautifulSoup
from urlparse import urlparse

# get from wayback machine
BASE_URL = u'https://web.archive.org/web/20150430111855/http://www.welluneednt.com/archive/category/読者↔村上春樹'

def main(base_url=BASE_URL):

    def get_entries_on_page():
        # find all links to entries
        entries = soup.find_all(attrs='entry-title-link')
        for ind, entry in enumerate(entries):
            href = entry.attrs['href']
            hop_url = scheme + u'://' + netloc + href
            hop_r = requests.get(hop_url)
            hop_soup = BeautifulSoup(hop_r.content)
            try:
                question, answer = hop_soup.find_all('blockquote')
            except ValueError:
                continue
            for paragraph in answer.find_all('p'): # write each paragraph of Murakami's answer on a line
                f.write(paragraph.text.encode('utf8'))
                f.write('\n')
            print 'entry', ind

    next_page_exists = True
    page = 1

    with open('input.txt', 'w') as f:
        while(next_page_exists):
            # get the page HTML and parse by BeautifulSoup
            if page > 1:
                url = base_url + '?page=' + str(page)
            else:
                url = base_url
            r = requests.get(url)
            if not r.ok:
                print 'invalid request'
                break
            soup = BeautifulSoup(r.content)
            scheme, netloc, path, _, _, _ = urlparse(url)

            get_entries_on_page()

            print 'page', page
            page += 1
            if page > 100: # hard stop
                next_page_exists = False
            if not soup.find(attrs='pager-next'): # does next page link exist
                next_page_exists = False


if __name__ == '__main__':
    main()