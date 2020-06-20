
import gzip
with gzip.open('pyTutFile_01.csv.gz', 'rb') as f:
    file_content = f.read()

