import subprocess
import json
import psycopg2
from database import db_connect, db_close
from processing import process_messages

connection, cursor = "", ""

try:
    # Load configuration from config.json
    with open('config.json', 'r') as f:
        config = json.load(f)

    connection, cursor = db_connect(config)

    if connection and cursor:
        command = config['sqs']['receive_command']
        res = subprocess.run(command, capture_output=True, text=True, shell=True, executable="/bin/bash")

        if res.returncode != 0:
            print(f"Error receiving message: {res.stderr}")
        else:
            json_res = json.loads(res.stdout)
            messages = json_res.get('Messages', [])

            process_messages(config, messages, cursor)

            try:
                connection.commit()
                cursor.execute(config['queries']['select_all_user_logins'])
                records = cursor.fetchall()
                print(f"Updated records: {records}")
            except psycopg2.DatabaseError as e:
                print(f"Error during commit or fetch: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    db_close(connection, cursor)
