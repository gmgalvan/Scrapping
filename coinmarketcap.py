from scrapper_page import Scrapper

page = Scrapper(visible=True,focus_page="https://coinmarketcap.com/")
print ("Bitcoin")
PRICE_BTC = page.read_by_css_selector_txt('#id-bitcoin > td:nth-child(4)')
VOLUME_BTC = page.read_by_css_selector_txt('#id-bitcoin > td:nth-child(5) > a')
print ("Price: {} Volume: {}".format(PRICE_BTC,VOLUME_BTC))
page.end()