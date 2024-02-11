import time

import requests
from dataclasses import dataclass
from typing import Final

BASE_URL: Final[str] = 'https://api.coingecko.com/api/v3/coins/markets'


@dataclass
class Coin:
    name: str
    symbol: str
    current_price: float
    high_24h: float
    low_24h: float
    price_change_24h: float
    price_change_percentage_24h: float

    def __str__(self):
        return f'{self.name} ({self.symbol}): ${self.current_price:,}'


def get_coins() -> list[Coin]:
    payload: dict = {'vs_currency': 'usd', 'order': 'market_cap_desc'}
    data = requests.get(BASE_URL, params=payload)
    json: dict = data.json()

    coin_list: list[Coin] = []
    for item in json:
        current_coin: Coin = Coin(name=item.get('name'),
                                  symbol=item.get('symbol'),
                                  high_24h=item.get('high_24h'),
                                  low_24h=item.get('low_24h'),
                                  price_change_24h=item.get('price_change_24h'),
                                  price_change_percentage_24h=item.get('price_change_percentage_24h'),
                                  current_price=item.get('current_price'))
        coin_list.append(current_coin)
    return coin_list


def alert(symbol: str, bottom_price: float, top_price: float, coins_list: list[Coin]):
    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top_price or coin.current_price < bottom_price:
                print(coin, '!!TRIGGERED!!')
            else:
                print(coin)


def main():
    coins: list[Coin] = get_coins()
    while True:
        time.sleep(30)
        alert('btc', bottom_price=20_000, top_price=28_000, coins_list=coins)
        alert('eth', bottom_price=1800, top_price=1900, coins_list=coins)
        alert('sol', bottom_price=20_000, top_price=28_000, coins_list=coins)
        print("")


if __name__ == '__main__':
    main()
