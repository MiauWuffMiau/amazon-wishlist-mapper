# -*- coding: iso-8859-15 -*-

from bs4 import BeautifulSoup
import array
import requests

global header
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0',
}

def getting_links_from_wishlist(wishlist_url):
    wishlist = []
    i = 1
    if "http://" not in wishlist_url:
        wishlist_url = "http://" + str(wishlist_url)
    if "gp" in wishlist_url:
        wishlist_id = str(wishlist_url).split("/")[6]
    else:
        wishlist_id = str(wishlist_url).split("/")[5]

    while 1:
        page = "http://www.amazon.de/gp/registry/wishlist/" + str(wishlist_id) + "/ref=cm_wl_sortbar_o_page_" + str(i) + "?ie=UTF8&page=" + str(i)
        answer = requests.get(page, headers=header).text
        output = BeautifulSoup(answer)
        last_page = output.find_all('li', {'class':'a-disabled a-last'})
        wishlist_links = output.find_all('a', {'class':'a-link-normal'})
        for link in wishlist_links:
            href_link = link.get('href')
            if "/dp/" in href_link:
                if href_link not in wishlist and "_ttl/" in href_link:
                    wishlist.append("http://www.amazon.de" + str(href_link))
        if len(last_page) > 0:
            break
        i = i + 1
    return wishlist
