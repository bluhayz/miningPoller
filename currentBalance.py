# import libraries
import urllib2
from bs4 import BeautifulSoup
from time import gmtime, strftime

time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# specify the url
#quote_page = "https://www.ahashpool.com/wallet.php?wallet=1PHCV247CMzpXCiaRzCwRJ2Fn7ggcn4vbM"
quote_page = "https://www.ahashpool.com/wallet_wallet_results.php?wallet=1PHCV247CMzpXCiaRzCwRJ2Fn7ggcn4vbM"

# query the website and return the html to the variable page
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

rows = soup.findAll("tr", { "class" : "ssrow" })

#print table
data=[]
for row in rows:
    cells = row.find_all("td")
    cells = [ele.text.strip() for ele in cells]
    data.append([ele for ele in cells if ele])
#print data
balance = 0
#figure out the values for balance, unpaid, and paid
for keyval in data:
    #print keyval[0] + ": " +keyval[1]
    if keyval[0] == u'Balance':
        balance = keyval[1]

print time + ", " + balance
