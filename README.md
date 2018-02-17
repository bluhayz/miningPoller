# miningPoller

Mining Poller will Poll ahashpool.  It loops through the wallets in wallets.dat

install the following dependencies:

1.  pip install bitcoing-price-api
2.  pip install bs4

This file outputs a csv file in currentbalance.csv with the following items:

| Wallet     | Time    | Balance (Cleared) | Balance (Total) | USD Balance (Cleared) | USD Balance (Total) | BTC Price in USD|
| --------|---------|-------|--------|---------|-------|----------|
|17Qa....k7b|2018-02-17 14:25:59|0.00347361|0.00433728|36.820266|45.975168|10600.0|
|17Q....Mb|2018-02-17 14:25:59|0.00347361|0.00433728|36.820266|45.975168|10600.0|

Items for future development:
1.  Instructions to daemonize the script so it runs every 15 minutes or an hour
2.  Ability to run it with a config flag to add wallets to the tool
3.  Additional scripts that let you output graphs or other analytics based off the csv data
