import psycopg2,os,glob
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def insert_laptop_data():
    conn = psycopg2.connect(
        host="localhost",
        database="laptop_db",
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    cur = conn.cursor()

    for file in glob.glob(os.getenv('LAPTOP_FILE_PATH')):
        print(f"Processing file: {file}")
        df = pd.read_csv(file)
        records = df.to_dict('records')

        for record in  records:
            query = f"""
                INSERT INTO laptops (id, company, product, type_name, price_euros)
                VALUES (
                    {record['Id']},
                    '{record['Company']}',
                    '{record['Product']}',
                    '{record['TypeName']}',
                    {record['Price_euros']}
                )
                ON CONFLICT (id) DO NOTHING
                """
            cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()


def filter_gaming_laptops():
    for file in glob.glob(os.getenv('LAPTOP_FILE_PATH')):
        print(f"Filtering Gaming laptops from: {file}")
        df = pd.read_csv(file)

        gaming_laptops_df = df[df['TypeName'] == 'Gaming']

        file_exists = os.path.isfile(os.getenv('OUPUT_LAPTOP_FILE').format('gaming_laptops'))

        gaming_laptops_df.to_csv(
            os.getenv('OUPUT_LAPTOP_FILE').format('gaming_laptops'),
            mode='a',
            index=False,
            header=not file_exists
        )

def filter_notebook_laptops():
    for file in glob.glob(os.getenv('LAPTOP_FILE_PATH')):
        print(f"Filtering Notebook laptops from: {file}")
        df = pd.read_csv(file)

        notebook_laptops_df = df[df['TypeName'] == 'Notebook']
        
        file_exists = os.path.isfile(os.getenv('OUPUT_LAPTOP_FILE').format('notebook_laptops'))

        notebook_laptops_df.to_csv(
            os.getenv('OUPUT_LAPTOP_FILE').format('notebook_laptops'),
            mode='a',
            index=False,
            header=not file_exists
        )


def filter_ultrabook_laptops():
    for file in glob.glob(os.getenv('LAPTOP_FILE_PATH')):
        print(f"Filtering Ultrabook laptops from: {file}")
        df = pd.read_csv(file)
        
        ultrabook_laptops_df = df[df['TypeName'] == 'Ultrabook']
        
        file_exists = os.path.isfile(os.getenv('OUPUT_LAPTOP_FILE').format('ultrabook_laptops'))

        ultrabook_laptops_df.to_csv(
            os.getenv('OUPUT_LAPTOP_FILE').format('ultrabook_laptops'),
            mode='a',
            index=False,
            header=not file_exists
        )
