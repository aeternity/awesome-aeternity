import os
import shutil

def pre_build(**kwargs):
  # dest = 'docs'
  # shutil.copy('../README.md', dest)
  filenames = ['hidenav.txt', '../README.md']
  with open('docs/README.md', 'w') as outfile:
      for fname in filenames:
          with open(fname) as infile:
              outfile.write(infile.read())