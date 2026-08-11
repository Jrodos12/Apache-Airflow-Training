def get_order_price_data():
    order_price_data = {
        'o1':234.45,
        'o2':10,
        'o3':34.77,
        'o4':45.66,
        'o5':399
        }
    return order_price_data

def compute_sum(order_price_data: dict):
    return sum(order_price_data.values())

def compute_avg(order_price_data: dict):
    return sum(order_price_data.values()) / len(order_price_data)
    

def display_result(total:float, average:float):
    print(f"Total price of goods:{total}")
    print(f"Average price of goods:{average}")