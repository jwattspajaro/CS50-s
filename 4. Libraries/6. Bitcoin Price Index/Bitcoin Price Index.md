### Bitcoin Price Index

#### [Bitcoin](https://en.wikipedia.org/wiki/Bitcoin) is a form of digitial currency, otherwise known as [cryptocurrency](https://en.wikipedia.org/wiki/Cryptocurrency). Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a [blockchain](https://en.wikipedia.org/wiki/Blockchain), to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

In a file called bitcoin.py, implement a program that:

⚫ Expects the user to specify as a command-line argument the number of Bitcoins, 
, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.

⚫ Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:
```python
import requests

try:
    ...
except requests.RequestException:
    ...
Outputs the current cost of 
```
 Bitcoins in USD to four decimal places, using , as a thousands separator.
 
### Hints
Recall that the sys module comes with argv, per [docs.python.org/3/library/sys.html#sys.argv.](https://docs.python.org/3/library/sys.html#sys.argv)
Note that the requests module comes with quite a few methods, per [requests.readthedocs.io/en/latest](https://requests.readthedocs.io/en/latest/), among which are get, per [requests.readthedocs.io/en/latest/user/quickstart/#make-a-request](https://cs50.harvard.edu/python/2022/psets/4/bitcoin/#:~:text=requests.readthedocs.io/en/latest/user/quickstart/%23make%2Da%2Drequest%2C), and json, per requests.readthedocs.io/en/latest/user/quickstart/#json-response-content. . You can install it with:

    pip install requests
    
Note that CoinDesk’s API returns a JSON response like:
```python
{
   "time":{
      "updated":"May 2, 2022 15:27:00 UTC",
      "updatedISO":"2022-05-02T15:27:00+00:00",
      "updateduk":"May 2, 2022 at 16:27 BST"
   },
   "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
   "chartName":"Bitcoin",
   "bpi":{
      "USD":{
         "code":"USD",
         "symbol":"&#36;",
         "rate":"38,761.0833",
         "description":"United States Dollar",
         "rate_float":38761.0833
      },
      "GBP":{
         "code":"GBP",
         "symbol":"&pound;",
         "rate":"30,827.6198",
         "description":"British Pound Sterling",
         "rate_float":30827.6198
      },
      "EUR":{
         "code":"EUR",
         "symbol":"&euro;",
         "rate":"36,800.2764",
         "description":"Euro",
         "rate_float":36800.2764
      }
   }
}
```
