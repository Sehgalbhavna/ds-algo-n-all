
from datetime import datetime
now = datetime.now()
formatnow = now.strftime("%Y-%m-%d-%H-%M")
csv_header = "AWS_Account_name,AWS_Account_number,Region,VPCId,SubnetID,CiDrblock,AZ, AZId"
csv_file = "AWS-Subnets-" + formatnow + ".csv"
with open(csv_file, 'w') as csv:
    csv.write(csv_header + "\n")
    print("CSV is opened")