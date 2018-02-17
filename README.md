# miningPoller

Mining Poller will Poll ahashpool.  It loops through the wallets in wallets.dat

install the following dependencies:

1.  pip install bitcoing-price-api
2.  pip install bs4

This file outputs a csv file in currentbalance.csv with the following items:

wallet, time, cleared balance, uncleared total balance, cleared usd balance, uncleared total usd balance, btc price in usd


| Wallet     | Time    | Balance (Cleared) | Balance (Total) | USD Balance (Cleared) | USD Balance (Total) | BTC Price in USD|
| --------|---------|-------|--------|---------|-------|----------|
|"17QaUWVZ2vT5XbCMiQwHwCs11FMaTSk7b"|"2018-02-17 14:25:59"|"0.00347361"|"0.00433728"|"36.820266"|"45.975168"|"10600.0"|
|"17QaUWVZ2vT5XbCMiQwHwCs11FMaTSk7b"|"2018-02-17 14:25:59"|"0.00347361"|"0.00433728"|"36.820266"|"45.975168"|"10600.0"|
| Tuesday | chicken | $8    |
