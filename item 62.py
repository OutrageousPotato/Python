from datetime import datetime, timedelta

portlandTime = datetime.now()
londonTime = portlandTime + timedelta(hours=9)


print(portlandTime)
print(londonTime)
