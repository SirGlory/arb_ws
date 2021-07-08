import asyncio
from luno_updater import Updater

L_API_KEY, L_API_SECRET = 'k2dmhxm8fxc3c', 'r-dpNkeG6YMWNYtDh1WBOGQKhe6yBMj9rCNP0QrlAuQ'

L_pair = 'XBTZAR'

vol_cond = 1.0      #  <--------- Set minimum volume condition
depth = 20          #  <--------- Also adjust depth, higher for greater volume condition
                    #             Recommended depth=20 for volume=1.0
class Lunows:

    def run(self):

        def print_it(consolidated_order_book): # was (consolidated_order_book,trades) <--see line 87 in luno_updater.py

        # Bid Calculations
            cum_value=0
            vol =0
            index_loc=0
            for i in range(0,depth):
                vol += float(consolidated_order_book["bids"][i][1])
                cum_value += float(consolidated_order_book["bids"][i][1])*float(consolidated_order_book["bids"][i][0])
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
                avol += float(consolidated_order_book["asks"][x][1])
                acum_value += float(consolidated_order_book["asks"][x][1])*float(consolidated_order_book["asks"][x][0])
                aindex_loc = x
                #print(f"Current Volume= {vol}")
                if avol > vol_cond:
                    break
            aw_avg_price=acum_value/avol
            spread = consolidated_order_book["asks"][0][0] - consolidated_order_book["bids"][0][0]

        # Text Output
            print("* LUNO BID ORDER BOOK * ")
            print(f"Order Position= {index_loc}")
            print(f"Cumulative Value= {int(cum_value)}")
            print(f"Vol > 1 BTC = {vol.__round__(3)}")
            print(f"Weighted Average Price = {int(w_avg_price)}")
            print("*   *   *   *   *   * ")
            print("* LUNO ASK ORDER BOOK * ")
            print(f"Weighted Average Price = {int(aw_avg_price)}")
            print(f"Vol > {vol_cond} BTC = {avol.__round__(3)}")
            print(f"Cumulative Value = {int(acum_value)}")
            print(f"Order Position = {aindex_loc}")
            print(f"Spread = R {int(spread)}")
            print(f"WA Spd = R {int(aw_avg_price - w_avg_price)}")
            print("--------------------------------------")

    # Create Webscocket
        updater = Updater(
            pair_code=L_pair,
            api_key=L_API_KEY,
            api_secret=L_API_SECRET,
            hooks=[print_it],
        )

    # Async Loop
        loop = asyncio.get_event_loop()
        loop.run_until_complete(updater.run())

if __name__ == '__main__':
    data_l = Lunows().run()
