import base64
import sys

if (len(sys.argv) >2):
    print("Usage: b64 {-e|-d}\"<string>\"")
    exit(-1)

print(base64.b64encode(sys.argv[1].encode()).decode())
