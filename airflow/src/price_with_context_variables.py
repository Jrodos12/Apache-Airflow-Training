def get_order_price_data():
    order_price_data = {
        'o1':234.45,
        'o2':10,
        'o3':34.77,
        'o4':45.66,
        'o5':399
        }
    return order_price_data

def compute_sum_and_average(order_price_data:dict,discount_rate:float,task_instance,dag_run):
    print(f"Task id: {task_instance.task_id}")
    print(f"Run id: {task_instance.run_id}")
    print(f"Dag run logical Date: {dag_run.logical_date}")

    return {'total':sum(order_price_data.values()) * (1 - discount_rate),'average':sum(order_price_data.values()) / len(order_price_data)}

    

def display_result(summary_data:dict):
    print(f"Total price of goods:{summary_data['total']}")
    print(f"Average price of goods:{summary_data['average']}")