import os
from datetime import datetime

now = datetime.now()
data = 'data/app-data.txt'
assert os.path.exists(data)
with open(data,'w') as f:
    f.writelines([f"{now.strftime('%m/%d/%Y %H:%M:%S')}\t Run with {os.cpu_count()} cpu"])
