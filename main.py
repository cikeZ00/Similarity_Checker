from thefuzz import fuzz
from thefuzz import process
import os

files = {}
output = {}

for file in os.listdir("Documents"):
    key = str(file)
    with open(f"Documents/{file}") as f:
        files[key] = f.readlines()

for key, value in files.items():
    for key_compared, value_compared in files.items():
        fuzz_ratio = fuzz.ratio(value, value_compared)
        print(f"Comparison between \"{key}\" and \"{key_compared}\": {fuzz_ratio}% ")
        
