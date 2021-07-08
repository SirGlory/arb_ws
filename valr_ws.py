import asyncio
from typing import Dict
from pprint import pprint
from valr_python import WebSocketClient
from valr_python.enum import TradeEvent
from valr_python.enum import WebSocketType

API_KEY, API_SECRET = '4094b901923609064d5a5e1c9b7463aeab0df17ecaf6dcd5bcf449d9ae43e277', '7d497cb12394d007cbacefa12f2bd1e3417d1aee228f1bd2d022e2fdb9a61d80'

pair = ['BTCZAR']

vol_cond = 1.0      #  <--------- Set minimum volume condition
depth = 20          #  <--------- Also adjust depth, higher for greater volume condition above
                    #             Recommended depth=20 for volume=1.0

class Valrws:

    def run(self):

        def pretty_hook(data: Dict):
        # Bid Calculations
            cum_value=0
            vol =0
            index_loc=0
            for i in range(0,depth):
                vol += float(data['data']['Bids'][i]['quantity'])
                cum_value += float(data['data']['Bids'][i]['quantity'])*float(data['data']['Bids'][i]['price'])
                index_loc = i
                #print(f"Current Volume= {vol}")
                if vol > vol_cond:
                    break
            w_avg_price=cum_value/vol

        # Ask Calculations
            acum_value=0
            avol =0
            aindex_loc=0
            for x in range(0,depth):
                avol += float(data['data']['Asks'][x]['quantity'])
                acum_value += float(data['data']['Asks'][x]['quantity'])*float(data['data']['Asks'][x]['price'])
                aindex_loc = x
                #print(f"Current Volume= {vol}")
                if avol > vol_cond:
                    break
            aw_avg_price=acum_value/avol

            spread = float(data['data']['Asks'][0]['price']) - float(data['data']['Bids'][0]['price'])

        # Text Output
            print("* VALR BID ORDER BOOK *")
            print(f"Order Position= {index_loc}")
            print(f"Cumulative Value= {int(cum_value)}")
            print(f"Volume > 1 BTC= {vol.__round__(3)}")
            print(f"Weighted Average Price = {int(w_avg_price)}")
            print("*   *   *   *   *   * ")
            print("* VALR ASK ORDER BOOK *")
            print(f"Weighted Average Price = {int(aw_avg_price)}")
            print(f"Volume > {vol_cond} BTC= {avol.__round__(3)}")
            print(f"Cumulative Value= {int(acum_value)}")
            print(f"Order Position= {aindex_loc}")
            print(f"Spread = R {int(spread)}")
            print(f"WA Spd = R {int(aw_avg_price-w_avg_price)}")
            print("-----------------------------")

    # Create Webscocket
        c = WebSocketClient(api_key=API_KEY, api_secret=API_SECRET, currency_pairs=pair,
                            ws_type=WebSocketType.TRADE.name,
                            trade_subscriptions=[TradeEvent.AGGREGATED_ORDERBOOK_UPDATE.name],
                            hooks={TradeEvent.AGGREGATED_ORDERBOOK_UPDATE.name: pretty_hook})
    # Async Loop
        loop = asyncio.get_event_loop()
        loop.run_until_complete(c.run())


if __name__ == '__main__':
    data_v = Valrws().run()
