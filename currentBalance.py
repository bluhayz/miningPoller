# import libraries
import urllib2
import re
from bs4 import BeautifulSoup
from time import gmtime, strftime
from exchanges.bitfinex import Bitfinex
import csv

btc = Bitfinex().get_current_price()
time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

#given a wallet this function will return the balance in btc earned and
#the total uncleared balance earned in btc from ahashpool
def pullBalanceFromWallet(wallet):
    # specify the url
    address = "https://www.ahashpool.com/wallet_wallet_results.php?wallet=" + wallet
    page = urllib2.urlopen(address)

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
    rows = soup.findAll("tr", { "class" : "ssrow" })

    #grab table with all the values
    data=[]
    for row in rows:
        cells = row.find_all("td")
        cells = [ele.text.strip() for ele in cells]
        data.append([ele for ele in cells if ele])

    #figure out the values for balance, unpaid, and paid
    for keyval in data:
        if keyval[0] == u'Balance (cleared)':
            clearedval = keyval[1]
        if keyval[0] == u'Total Unpaid (pending clearing + cleared)':
            unclearedval = keyval[1]
    #Page annoyingly adds BTC to the output so just grabbing the digits
    balancearr = re.findall(r'\d+\.\d+', clearedval)
    uncleararr = re.findall(r'\d+\.\d+', unclearedval)
    return balancearr[0], uncleararr[0]

wallet = "17QaUWVZ2uGnXbCMiQwHwCs11FMaTSk7a"
balance, unclearbal = pullBalanceFromWallet(wallet)

#Calculate dollar values based off current price at time of poll
totalearned = float(balance) * float(btc)
totaluncleared = float(unclearbal) * float(btc)

#print "Total earned: " + str(totalearned)

#create output for the csv file to store the data
mylist =[]
mylist.append(wallet)
mylist.append(time)
mylist.append(str(balance))
mylist.append(str(unclearbal))
mylist.append(totalearned)
mylist.append(totaluncleared)
mylist.append(str(btc))

print mylist

with open('currentbalance.csv', 'a') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(mylist)
