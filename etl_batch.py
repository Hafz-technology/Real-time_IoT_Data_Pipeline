import pandas as pd
from sqlalchemy import create_engine

# Database Connection
db_string = "postgresql://depi:123456@localhost:5432/iot_db"

db = create_engine(db_string)




def run_etl_pipeline():
    print("--- Starting Batch ETL Job ---")
    
    # Extract
    try:
        df = pd.read_csv('iot_data_log.csv')
        print(f"Extracted {len(df)} records.")
    except FileNotFoundError:
        print("No data file found yet.")
        return

    # Transform
    df['status'] = 'Normal'
    df.loc[(df['sensor_type'] == 'Energy') & (df['value'] > 300), 'status'] = 'Energy Hog'
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Load to SQL
    df.to_sql('historical_data', db, if_exists='replace', index=False)
    # Remove the entire 'with db.connect() as conn:' block and conn.commit()
    print("Data loaded to PostgreSQL table 'historical_data'.")
    # with db.connect() as conn: 
    #     df.to_sql('historical_data', conn, if_exists='replace', index=False)
    #     conn.commit() # <-- Explicitly commit the transaction
    # print("Data loaded to PostgreSQL table 'historical_data'.")















if __name__ == "__main__":
    run_etl_pipeline()
    
    
    
    
