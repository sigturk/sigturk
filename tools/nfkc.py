import unicodedata
import os
import sys

fix = "--fix" in [unicodedata.normalize("NFKC", i) for i in sys.argv]

for README_file in [i for i in os.listdir() if i.startswith("README.")]:
  contents = open(README_file).read()
  normalized = unicodedata.normalize("NFKC", contents)
  if contents != normalized:
    if fix:
      open(README_file, "w").write(normalized)
    else:
      raise SystemExit('Error: README.* files are not NFKC normalized.')
