
import zipfile

with zipfile.ZipFile("world_bank.zip") as myzip:
    print(myzip.namelist())





