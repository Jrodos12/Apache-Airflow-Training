import os,csv
from dotenv import load_dotenv

load_dotenv()

def export_csv(filter_data:list):
        os.makedirs(os.getenv('OUTPUT_FOLDER'), exist_ok=True)

        with open(os.getenv('DB_OUTPUT'), "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Product', 'Price'])

            for row in filter_data:
                writer.writerow(row)