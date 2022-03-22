import json
from datetime import datetime

def lambda_handler(event, context):
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }