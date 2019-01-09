from selenium_agent import Agent

bot = Agent(visible=True,focus_page="https://coinmarketcap.com/")
print ("Bitcoin")
PRICE_BTC = bot.read_by_css_selector_txt('#id-bitcoin > td:nth-child(4)')
VOLUME_BTC = bot.read_by_css_selector_txt('#id-bitcoin > td:nth-child(5) > a')
print ("Price: {} Volume: {}".format(PRICE_BTC,VOLUME_BTC))
bot.end()