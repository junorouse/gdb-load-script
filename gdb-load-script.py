from os import environ
from pprint import pprint

# pprint(environ)

filename = environ['PWD'] + "/gscript"

try:
 f = open(filename, "rb")
 data = f.read()
 f.close()

 for x in data.decode("utf-8").split("\n"):
  gdb.execute(x)
except Exception as e:
 pprint (e)
