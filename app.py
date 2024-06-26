import hashlib
import json
import subprocess
import psycopg2
from datetime import date

def mask_pii(val):
    return hashlib.sha256(val.encode()).hexdigest()
def version_to_int(version):
    parts = version.split('.')
    parts = [part.zfill(2) for part in parts]
    return int(''.join(parts))
def get_msg_record_values(msg):
    msg_body = json.loads(msg['Body'])

    user_id = msg_body['user_id']
    device_type = msg_body['device_type']
    masked_ip = mask_pii(msg_body['ip'])
    masked_device_id = mask_pii(msg_body['device_id'])
    locale = msg_body['locale']
    app_version = version_to_int(msg_body['app_version'])
    create_date = date.today()

    values = (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)
    return values

# connect to db
connection = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port=5432)
cursor = connection.cursor()
cursor.execute("select * from user_logins;")
records = cursor.fetchall()

# get message from queue
command = "awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/login-queue"
res = subprocess.run(command, capture_output=True, text=True, shell=True, executable="/bin/bash")
json_res = json.loads(res.stdout)
messages = json_res['Messages']

for message in messages:
    values = get_msg_record_values(message)
    cursor.execute("INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date) VALUES (%s, %s, %s, %s, %s, %s, %s)",values)

connection.commit()
cursor.execute("select * from user_logins;")
records = cursor.fetchall()
connection.close()
