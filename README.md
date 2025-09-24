# Real-time_IoT_Data_Pipeline
The Real-time IoT Data Pipeline project involves building a system that can collect, process, and analyze data from various Internet of Things (IoT) devices as it's generated.  The goal is to create a seamless, end-to-end flow of information, from the sensors to the end-user, with minimal delay. This pipeline must be scalable to handle a large volume of data and flexible enough to integrate with different types of devices and platforms.
# The Data Pioneers
# Team members
* Maysara Abdulmageed
* Ahmed Mohamed
* Aya Hussein
* Huda Hosny
* Hesham Gamal
* Khalil Hafez
## Project Goal: To build a scalable and flexible end-to-end data pipeline for collecting, processing, and analyzing real-time data from various IoT devices with minimal delay.

## key areas of data engineering:

* Data Ingestion: Sourcing data from various IoT devices, which might involve different protocols (e.g., MQTT, HTTP, CoAP).

* Stream Processing: Handling the continuous flow of data in real-time. Technologies like Apache Kafka, Apache Flink, or Apache Spark Streaming could be used here.

* Data Storage: Storing both raw and processed data efficiently. This could involve time-series databases, data lakes, or data warehouses.

* Data Analysis & Visualization: Creating insights from the processed data and presenting them to end-users with minimal latency.

## Project Part1: smart home automation
The end-goal: We're building a system to monitor and control a smart home, which allows for interesting analysis and a user-friendly dashboard.
### Data Types: a simple ON/OFF state, temperature readings, motion detection events, and light intensity levels.

## Project Part2: Smart Energy Monitoring
The end-goal: We are building a dashboard that shows real-time power usage, a historical graph of consumption over time, and identify which appliances are "energy hogs." We implement an alert system to notify the user if consumption exceeds a certain threshold.
### Data Types: Simulate data from smart plugs or power meters that measure energy consumption for different appliances.

## Project Part3: Home Security and Environmental Monitoring
The end-goal: Our system will trigger a real-time alert whenever a door is opened unexpectedly or motion is detected when no one is home. We will also create a historical log of all security events and a dashboard showing the current temperature and humidity in different rooms.
### Data Types: Simulate data from various sensors like motion detectors, door/window sensors, smoke alarms, and temperature/humidity sensors.


**************************************************************************************************************************************************************

## Project Stages
### Stage 1: Data Simulation and Ingestion
 Objectives:
 * Simulate IoT data and push it into a file or message queue 
Tasks:
 1. Create a Python script to generate sensor data (every 5 seconds)
 2. Write to a file or Kafka/Stream (optional) 
Deliverables:
* Python generator script
* Sample data logs

### Stage 2: Batch Data Pipeline (ETL)
 Objectives:
* Ingest data, process it, and store it in a data warehouse
 Tasks: 
1.Use Python or Azure Data Factory to:
* Extract data (CSV or stream) 
* Transform it (e.g., flag anomalies, average)
* Load into SQL or Data Lake 
Deliverables: 
* ETL script or ADF pipeline
* Processed dataset in storage

### Stage 3: Streaming Pipeline with Alerts
 Objectives:
 * Implement streaming analytics and alerting
 Tasks:
1.	Use Azure Stream Analytics or Apache Kafka to:
* Process real-time data
* Raise alerts for threshold breaches 
Deliverables: 
* Streaming pipeline setup 
* Alert logic code and output

### Stage 4:  Dashboard & Final Report
 Objectives:
* Visualize metrics and summarize results 
Tasks:
 1. Create a real-time dashboard (Power BI, Streamlit, Grafana)
 2. Report on key findings and system performance
Deliverables: 
* Dashboard screenshot/live demo
* Final project report
 
 
 ## Final stages Summary:
 ### Stage-------------------------------------Key Deliverables
 1. Data Simulation----------------------------Python generator
 2. Batch ETL----------------------------------ETL pipeline
 3. Streaming Analytics------------------------Real-time alerts
 4. Dashboard & Report-------------------------Dashboard + PDF report

