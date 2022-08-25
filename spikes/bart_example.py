from pprint import pprint
import datetime

# from tobe.utils import ds

from pybart.api import BART

bart = BART(json_format=True) 

# goal 1: show api working :D
# root = bart.stn.stninfo('16TH')
# station = root['stations']['station']
# print(station['address'] + ', ' + station['city'])

# goal 2: show next to train to station X

# goal 3: last train to station Y

def next_train_to_endpoint(dst_name):
  for item in bart.etd.etd('16TH')['station'][0]['etd']:
    print(item['destination'])

# next_train_to_endpoint('Daly')

# goal 3: show last train to station Y  



def schedule(x, y): 
  now = datetime.datetime.now() 
  in_5_mins = now + datetime.timedelta(minutes=5)
  time = in_5_mins.strftime('%-I:%M%p').lower()
  trips = bart.sched.depart(orig=x, dest=y, b=0, a=2, time=time)['schedule']['request']['trip']
  pprint([x['@origTimeMin'] for x in trips])

schedule('16TH', 'MONT')