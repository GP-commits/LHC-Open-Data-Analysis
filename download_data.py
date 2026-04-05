import urllib.request
import os

urls = [
    "http://opendata.web.cern.ch/record/5501/files/HZZ12.root",      # Signal
    "http://opendata.web.cern.ch/record/5501/files/ZZ4mu12.root",    # ZZ -> 4mu background
    "http://opendata.web.cern.ch/record/5501/files/ZZ4e12.root",     # ZZ -> 4e background
    "http://opendata.web.cern.ch/record/5501/files/ZZ2mu2e12.root"   # ZZ -> 2mu2e background
]

os.makedirs("data", exist_ok=True)

for url in urls:
    filename = os.path.join("data", url.split('/')[-1])
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f"Downloaded {filename}")
    else:
        print(f"{filename} already exists.")
