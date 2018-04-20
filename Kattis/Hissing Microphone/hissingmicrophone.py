import re

print('hiss' if re.search(r's{2}', input()) else 'no hiss')