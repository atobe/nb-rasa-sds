from pprint import pprint
import difflib
import datetime
from pybart.api import BART
from dateutil.parser import parse

bart = BART(json_format=True) 

# {s['name'] : s['abbr'] for s in b.stn.stns()['stations']['station']}
stations = {'12th St. Oakland City Center': '12TH',
 '16th St. Mission': '16TH',
 '19th St. Oakland': '19TH',
 '24th St. Mission': '24TH',
 'Antioch': 'ANTC',
 'Ashby': 'ASHB',
 'Balboa Park': 'BALB',
 'Bay Fair': 'BAYF',
 'Berryessa/North San Jose': 'BERY',
 'Castro Valley': 'CAST',
 'Civic Center/UN Plaza': 'CIVC',
 'Civic Center': 'CIVC',
 'Coliseum': 'COLS',
 'Colma': 'COLM',
 'Concord': 'CONC',
 'Daly City': 'DALY',
 'Downtown Berkeley': 'DBRK',
 'Dublin Pleasanton': 'DUBL',
 'El Cerrito del Norte': 'DELN',
 'El Cerrito Plaza': 'PLZA',
 'Embarcadero': 'EMBR',
 'Fremont': 'FRMT',
 'Fruitvale': 'FTVL',
 'Glen Park': 'GLEN',
 'Hayward': 'HAYW',
 'Lafayette': 'LAFY',
 'Lake Merritt': 'LAKE',
 'MacArthur': 'MCAR',
 'Millbrae': 'MLBR',
 'Milpitas': 'MLPT',
 'Montgomery St': 'MONT',
 'North Berkeley': 'NBRK',
 'North Concord Martinez': 'NCON',
 'Oakland International Airport': 'OAKL',
 'Orinda': 'ORIN',
 'Pittsburg Bay Point': 'PITT',
 'Pittsburg Center': 'PCTR',
 'Pleasant Hill/Contra Costa Centre': 'PHIL',
 'Powell St': 'POWL',
 'Richmond': 'RICH',
 'Rockridge': 'ROCK',
 'San Bruno': 'SBRN',
 'San Francisco International Airport': 'SFIA',
 'airport': 'SFIA',
 'SFO': 'SFIA',
 'San Leandro': 'SANL',
 'South Hayward': 'SHAY',
 'South San Francisco': 'SSAN',
 'Union City': 'UCTY',
 'Walnut Creek': 'WCRK',
 'Warm Springs/South Fremont': 'WARM',
 'West Dublin/Pleasanton': 'WDUB',
 'West Oakland': 'WOAK'}

names = list(stations.keys())

def get_abbr(station_name):
  matches = difflib.get_close_matches(station_name, names)
  if len(matches) >= 1:
    return stations.get(matches[0], None)

def next_train(x, y):
  if x is None or y is None:
    return None
  now = datetime.datetime.now() 
  in_5_mins = now + datetime.timedelta(minutes=5)
  time = in_5_mins.strftime('%-I:%M%p').lower()
  trip = bart.sched.depart(orig=x, dest=y, b=0, a=1, time=time)['schedule']['request']['trip']
  departure_time = parse(trip['@origTimeMin'])
  return departure_time.hour, departure_time.minute
  
def last_train(x, y): 
  if x is None or y is None:
    return None
  now = datetime.datetime.now() 
  in_5_mins = now + datetime.timedelta(minutes=5)
  time = in_5_mins.strftime('%-I:%M%p').lower()
  trip = bart.sched.depart(orig=x, dest=y, b=0, a=1, time=time)['schedule']['request']['trip']
  departure_time = parse(trip['@origTimeMin'])
  return departure_time.hour, departure_time.minute
  
# print(next_train(get_abbr('16th and mission'), get_abbr('San Francisco International Airport')))
print(get_abbr('airport'))