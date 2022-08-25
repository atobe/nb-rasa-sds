import random
from string import Template

templates = [
  'when is the next train to $station_name',
  'last train to $station_name',
]

station_names = [
  '12th St. Oakland City Center',
  '16th St. Mission',
  '19th St. Oakland',
  '24th St. Mission',
  'Antioch',
  'Ashby',
  'Balboa Park',
  'Bay Fair',
  'Berryessa North San Jose',
  'Castro Valley',
  'Civic Center UN Plaza',
  'Coliseum',
  'Colma',
  'Concord',
  'Daly City',
  'Downtown Berkeley',
  'Dublin Pleasanton',
  'El Cerrito del Norte',
  'El Cerrito Plaza',
  'Embarcadero',
  'Fremont',
  'Fruitvale',
  'Glen Park',
  'Hayward',
  'Lafayette',
  'Lake Merritt',
  'MacArthur',
  'Millbrae',
  'Milpitas',
  'Montgomery St',
  'North Berkeley',
  'North Concord/Martinez',
  'Oakland International Airport',
  'Orinda',
  'Pittsburg Bay Point',
  'Pittsburg Center',
  'Pleasant Hill/Contra Costa Centre',
  'Powell St',
  'Richmond',
  'Rockridge',
  'San Bruno',
  'San Francisco International Airport',
  'San Leandro',
  'South Hayward',
  'South San Francisco',
  'Union City',
  'Walnut Creek',
  'Warm Springs South Fremont',
  'West Dublin Pleasanton',
  'West Oakland'
]

for station_name in station_names:
  template = Template(random.choice(templates))
  replacement = f'[{station_name}]{{"entity":"station_name"}}'
  print(template.substitute(station_name=replacement))

print()
print()

for station_name in station_names:
  template = Template(random.choice(templates).replace('next', 'last'))
  replacement = f'[{station_name}]{{"entity":"station_name"}}'
  print(template.substitute(station_name=replacement))  