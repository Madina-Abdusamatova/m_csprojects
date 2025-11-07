def add_new_orders(orders, new_orders):
    for order in new_orders:
        orders.append(order)

def process_orders(orders, num_to_process):
    new_list = []
    index = 0

    while index < num_to_process and len(orders)>0:
        new_list.append(orders[0])
        orders.pop(0)
        index+=1
    return new_list


def cancel_order(orders, order_id):
    # for i in orders:
    #     if i == order_id:
    #         orders.remove(i)
    #         return True
    # return False

    if order_id in orders:
        orders.remove(order_id)
        return True
    return False




def manage_orders(initial_orders, new_orders_to_add, orders_to_process, order_to_cancel):
    # 1. Copying list for not losing any values of it
    copied_list = initial_orders[:]
    # 2. Adding new orders to orders list
    add_new_orders(copied_list, new_orders_to_add)

    # 3. Canceling the given orders from list
    cancel_order(copied_list, order_to_cancel)

    # 4. Processing the orders from the front of queue
    processed_list = process_orders(copied_list, orders_to_process)

    return copied_list, processed_list

initial = [101, 102, 103, 104]
new = [105, 106]
process_count = 3
cancel_id = 103

final_result_list, list_of_processed_orders = manage_orders(initial, new, process_count, cancel_id)

print(f"Test Case 1 Results: \nfinal_state: {final_result_list} \nprocessed: {list_of_processed_orders} \n\nOriginal initial list (should be unchanged): {initial}")
