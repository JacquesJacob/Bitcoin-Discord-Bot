import requests
from datetime import datetime
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('BOT ONLINE!')
    print(client.user.name)
    print(client.user.id)
    print('-----PR------')

@client.event
async def on_message(message):
    if message.content.lower().startswith('!bitcoin'):

        bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
        litecoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/litecoin/'

        response = requests.get(bitcoin_api_url)
        response_json = response.json()
        response_ltc = requests.get(litecoin_api_url)
        response_json_ltc = response_ltc.json()

        moeda_btc = response_json[0]['name']
        valor_btc = int(float(response_json[0]['price_usd']))
        percent_change_1h = response_json[0]['percent_change_1h']
        percent_change_24h = response_json[0]['percent_change_24h']
        percent_change_7d = response_json[0]['percent_change_7d']

        moeda_ltc = response_json_ltc[0]['name']
        valor_ltc = int(float(response_json_ltc[0]['price_usd']))
        percent_change_1h_ltc = response_json_ltc[0]['percent_change_1h']
        percent_change_24h_ltc = response_json_ltc[0]['percent_change_24h']
        percent_change_7d_ltc = response_json_ltc[0]['percent_change_7d']

        data = int(response_json[0]['last_updated'])
        last_updated_btc = datetime.fromtimestamp(data).strftime('%d/%m/%Y %H:%M:%S')

        EmbedPu = discord.Embed(title="Mercado Criptomoedas em {} (CST)".format(last_updated_btc))

        EmbedPu.add_field(name="Bitcoin", value="Valor BTC: ${} (USD)\n"
                                           "Valorização 1h: {}%\n"
                                           "Valorização 24h: {}%\n"
                                           "Valorização 7d: {}%\n".format(valor_btc,
                                                                             percent_change_1h,
                                                                             percent_change_24h,
                                                                             percent_change_7d))

        EmbedPu.add_field(name="Litecoin", value="Valor LTC: ${} (USD)\n"
                                           "Valorização 1h: {}%\n"
                                           "Valorização 24h: {}%\n"
                                           "Valorização 7d: {}%\n".format(valor_ltc,
                                                                             percent_change_1h_ltc,
                                                                             percent_change_24h_ltc,
                                                                             percent_change_7d_ltc))

        EmbedPu.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        EmbedPu.set_footer(text="Developed by: Jacques Jacob | Integrado com API CoinMarketCap®")
        EmbedPu.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Bitcoin_logo.svg/450px-Bitcoin_logo.svg.png')
        await client.send_message(message.channel, embed=EmbedPu)

client.run('TOKEN_DISCORD')
