from pprint import pprint
from stations import get_abbr

tests = """
millbrae
civic center
12th street oakland city
16th mission
""".strip().splitlines()


for test in tests:
  print(test, get_abbr(test))
  