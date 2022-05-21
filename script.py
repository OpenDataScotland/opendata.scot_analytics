import os
import sys, getopt
import requests
import simplejson
from datetime import datetime, timedelta

def get_data(key):
    yesterday = datetime.now() - timedelta(1)
    date = datetime.strftime(yesterday, '%Y-%m-%d')

    url = "https://plausible.io/api/v1/stats/timeseries?site_id=opendata.scot&period=day&date=" + date + "&interval=date&metrics=visitors,pageviews,bounce_rate,visit_duration,visits"

    print ("Accessing " + url)

    payload={}
    headers = {
    'Authorization': 'Bearer ' + key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    filename = "timeseries/output-" + date + ".json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    print ("Writing to " + filename)

    f = open(filename, "a")
    f.write(simplejson.dumps(simplejson.loads(response.text), indent=4, sort_keys=True))
    f.close()

def main(argv):
   key = ''
   try:
      opts, args = getopt.getopt(argv,"h:k:",["key="])
   except getopt.GetoptError:
      print ('script.py -k <key>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('script.py -k <key>')
         sys.exit()
      elif opt in ("-k", "--key"):
         key = arg

   get_data(key)

if __name__ == "__main__":
   main(sys.argv[1:])


