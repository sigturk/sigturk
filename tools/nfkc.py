import unicodedata
import subprocess
import sys

files = subprocess.run(
    ["git", "ls-files", "--recurse-submodules"], check=True, capture_output=True
).stdout.splitlines()

fix = "--fix" in [unicodedata.normalize("NFKC", i) for i in sys.argv]

for file in files:
    contents = open(file).read()
    normalized = unicodedata.normalize("NFKC", contents)
    if contents != normalized:
        if fix:
            open(file, "w").write(normalized)
        else:
            raise SystemExit("Error: README.* files are not NFKC normalized.")
