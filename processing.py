import json
from datetime import date
from hashlib import sha256
import psycopg2


def mask_pii(val):
    return sha256(val.encode()).hexdigest()


def version_to_int(version):
    parts = version.split('.')
    parts = [part.zfill(2) for part in parts]
    return int(''.join(parts))


def get_msg_record_values(msg):
    try:
        msg_body = json.loads(msg['Body'])
        user_id = msg_body['user_id']
        device_type = msg_body['device_type']
        masked_ip = mask_pii(msg_body['ip'])
        masked_device_id = mask_pii(msg_body['device_id'])
        locale = msg_body['locale']
        app_version = version_to_int(msg_body['app_version'])
        create_date = date.today()

        return user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date
    except KeyError as e:
        print(f"Missing key in message: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None


def process_messages(config, messages, cursor):
    insert_query = config['queries']['insert_user_login']
    for message in messages:
        values = get_msg_record_values(message)
        if values:
            try:
                cursor.execute(insert_query, values)
            except psycopg2.DatabaseError as e:
                print(f"Error inserting into database: {e}")
    return
