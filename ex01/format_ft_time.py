from time import time
from datetime import datetime

timeRegular = "{:,.3f}".format(time())
timeScientific = "{:.3e}".format(time())
date = datetime.now().strftime("%b %d %Y")

print("Seconds since January 1, 1970: ", timeRegular, " or ", timeScientific, " in scientific notation")
print(date)