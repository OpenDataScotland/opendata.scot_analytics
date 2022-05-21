import os
import sys, getopt
import requests
import simplejson

def get_data(date, key):
    url = "https://plausible.io/api/v1/stats/timeseries?site_id=opendata.scot&period=day&date=" + date + "&interval=date&metrics=visitors,pageviews,bounce_rate,visit_duration,visits"

    payload={}
    headers = {
    'Authorization': 'Bearer ' + key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    filename = ".//timeseries/output-" + date + ".json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    f = open(filename, "a")
    f.write(simplejson.dumps(simplejson.loads(response.text), indent=4, sort_keys=True))
    f.close()

def main(argv):
   date = ''
   key = ''
   try:
      opts, args = getopt.getopt(argv,"hd:k:",["date=","key="])
   except getopt.GetoptError:
      print ('script.py -d <date> -k <key>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('script.py -d <date> -k <key>')
         sys.exit()
      elif opt in ("-d", "--date"):
         date = arg
      elif opt in ("-k", "--key"):
         key = arg

   get_data(date,key)

if __name__ == "__main__":
   main(sys.argv[1:])


