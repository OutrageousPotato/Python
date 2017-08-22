from datetime import datetime, time, timedelta

portland = datetime.now()

london = portland + timedelta(hours=8)
newYork = portland + timedelta(hours=3)

def checkStatus(branch, local):
    if time(10,30) <= local.time() <= time(20,30):        
        print "{} branch is currently open".format(branch)
    else:
        print "{} branch is currently closed".format(branch)

checkStatus("Portland", portland)
checkStatus("London", london)
checkStatus("New York", newYork)
