def get_order_price_data():
    order_price_data = {
        'o1':234.45,
        'o2':10,
        'o3':34.77,
        'o4':45.66,
        'o5':399
        }
    return order_price_data

def compute_sum_and_average(order_price_data: dict):
    return {'total':sum(order_price_data.values()),'average':sum(order_price_data.values()) / len(order_price_data)}

    

def display_result(summary_data:dict):
    print(f"Total price of goods:{summary_data['total']}")
    print(f"Average price of goods:{summary_data['average']}")