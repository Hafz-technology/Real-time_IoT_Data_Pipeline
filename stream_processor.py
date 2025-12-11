
import json
from kafka import KafkaConsumer
from sqlalchemy import create_engine, text



db_string = "postgresql://depi:123456@localhost:5432/iot_db"
engine = create_engine(db_string)

consumer = KafkaConsumer(
    'iot_sensor_data',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Listening for Real-time Events...")

for message in consumer:
    data = message.value
    alert_msg = None
    

    if data['sensor_id'] == 'FrontDoor_Lock' and data['value'] == 1:
        alert_msg = f"ALERT: Security Breach! {data['sensor_id']} opened."
    

    elif "Temp" in data['sensor_id'] and data['value'] > 30.0:
        alert_msg = f"WARNING: High Temp detected: {data['value']}C"

    if alert_msg:
        print(f">>> {alert_msg}")
        with engine.connect() as conn:
            query = text("INSERT INTO alerts (timestamp, message) VALUES (:t, :m)")
            conn.execute(query, {"t": data['timestamp'], "m": alert_msg})
     
            
            
            

            
            
            
            
            
            
            
            