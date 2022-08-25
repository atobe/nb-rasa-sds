from pprint import pprint
import fuzzy
import difflib

from stations import stations

dexer = fuzzy.Soundex(4)
sdexs = {dexer(name):abbr for (name, abbr) in stations.items()}
names = list(stations.keys())

tests = """
millbrae
civic center
12th street oakland
16th mission
""".strip().splitlines()


for test in tests:
  sdex = dexer(test)
  print(test, sdex, sdexs.get(sdex, 'X'), difflib.get_close_matches(test, names))
  