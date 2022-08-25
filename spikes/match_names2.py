from pprint import pprint
import difflib

from stations import stations

names = list(stations.keys())

tests = """
millbrae
civic center
12th street oakland city
16th mission
""".strip().splitlines()


for test in tests:
  print(test, stations[difflib.get_close_matches(test, names)[0]])
  