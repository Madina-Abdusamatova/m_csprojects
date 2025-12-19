def book_session(members_db, schedule_db, member_id, class_name, spots):
    if member_id not in members_db:
        raise KeyError("Member ID not found")

    if class_name not in schedule_db:
        raise KeyError("Class not found")
 
    if type(spots) is not int or spots < 1:
        raise ValueError("Spots must be positive integer")
    
    cost_per_spot = schedule_db[class_name]["cost"]
    member = members_db[member_id]
    
    if member["pass_type"] == "Premium":
        total_cost = 0
    else:
        total_cost = spots * cost_per_spot

    if member["credits"] < total_cost:
        raise ValueError("Insufficient credits")

    member["credits"] -= total_cost
    
    return total_cost


def process_gym_bookings(members_db, schedule_db, booking_queue):
    total_credits_used = 0
    declined_count = 0
    
    for member_id, class_name, spots in booking_queue:
        try:
            cost = book_session(members_db, schedule_db, member_id, class_name, spots)
            total_credits_used += cost
        except KeyError as e:
            print(f"Booking Error for {member_id}: '{e}'")
            declined_count += 1
        except ValueError as e:
            print(f"Booking Error for {member_id}: {e}")
            declined_count += 1
    
    return {"credits_used": total_credits_used, "declined_bookings": declined_count}


schedule = {
    "Yoga": {"cost": 5},
    "Boxing": {"cost": 10}
}

members = {
    "M1": {"credits": 20, "pass_type": "Standard"},
    "M2": {"credits": 5,  "pass_type": "Premium"}
}

queue = [
    ("M1", "Yoga", 2),     
    ("M2", "Boxing", 10),   
    ("M1", "Boxing", 2),    
    ("M9", "Zumba", 1),     
    ("M1", "Pilates", 1),   
    ("M2", "Yoga", 0)       
]

result = process_gym_bookings(members, schedule, queue)
print(result)