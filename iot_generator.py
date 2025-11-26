import json
import time
import random
import csv
from kafka import KafkaProducer
from datetime import datetime


KAFKA_TOPIC = 'iot_sensor_data'
CSV_FILE = 'iot_data_log.csv'


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

def generate_data():
    """Simulates data from Part 1, 2, and 3 of your README"""
    data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "sensor_id": random.choice(["Kitchen_Temp", "LivingRoom_Motion", "SmartPlug_TV", "FrontDoor_Lock"]),
        "sensor_type": "",
        "value": 0,
        "unit": ""
    }

    if "Temp" in data["sensor_id"]:
        data["sensor_type"] = "Environment"
        data["value"] = round(random.uniform(18.0, 35.0), 2) 
        data["unit"] = "C"
    elif "Motion" in data["sensor_id"]:
        data["sensor_type"] = "Security"
        data["value"] = random.choice([0, 1]) 
        data["unit"] = "Boolean"
    elif "SmartPlug" in data["sensor_id"]:
        data["sensor_type"] = "Energy"
        data["value"] = round(random.uniform(50.0, 500.0), 2) # Watts
        data["unit"] = "Watts"
    elif "Door" in data["sensor_id"]:
        data["sensor_type"] = "Security"
        data["value"] = random.choice([0, 1]) # 0=Closed, 1=Open
        data["unit"] = "State"
    return data






with open(CSV_FILE, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "sensor_id", "sensor_type", "value", "unit"])

print(f"Starting Data Simulation for 'The Data Pioneers' Project...")
try:
    while True:
        iot_data = generate_data()
        producer.send(KAFKA_TOPIC, value=iot_data)
        with open(CSV_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(iot_data.values())
        print(f"Sent: {iot_data}")
        time.sleep(5) 
except KeyboardInterrupt:
    print("Simulation Stopped.")
    
    
    
    
    
