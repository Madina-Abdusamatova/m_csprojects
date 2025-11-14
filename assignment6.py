# You are a sales manager evaluating the performance of your sales team. 
#The data is organized as a list of tuples, where each tuple contains an employee’s (employee_id, region, quarterly_sales_list). 
#Your assignment is to write a Python script to analyze this sales data.

# You must implement the following functions:

# calculate_average_sales(sales_list):
def calculate_average_sales(sales_list):
# Input: A list of numbers (an employee’s quarterly sales).
    if sales_list == []:
        return 0.0
# Output: The average of the sales figures in the list. Should return 0.0 for an empty list.
    return sum(sales_list)/len(sales_list)
# find_top_salesperson(sales_data):
def find_top_salesperson(sales_data):
    top_salesperson = ""
    top_average = 0
    for employee_id,region,quarterly_sales_list in sales_data:
        average=calculate_average_sales(quarterly_sales_list) 
        if average >= top_average:
            top_average=average
            top_salesperson=employee_id
    return top_salesperson
        

# Input: The main list of sales data.
# Output: The employee_id of the salesperson with the highest average quarterly sales. If there’s a tie, return the ID that comes first alphabetically.
# get_employees_in_region(sales_data, region_name):
# Input: The sales data list and a string region_name.
def get_employees_in_region(sales_data, region_name):
    regional_employee_id=[]
    for item in sales_data:
        if region_name == item[1]:
            regional_employee_id.append(item[0])
    regional_employee_id.sort()
# Output: A list of employee_ids for salespeople in that region. The list should be sorted alphabetically.
    return regional_employee_id

# get_regional_sales_total(sales_data):
# Input: The sales data list.
# Logic: Find all unique regions. For each region, calculate the total combined sales from all quarters for all employees in that region.
# Output: A list of tuples ('region_name', total_sales). This list must be sorted alphabetically by region name.
def get_regional_sales_total(sales_data):
    unique_regions=[]
    total_sales_data=[]
    for item in sales_data:
        if item[1] not in unique_regions:
            unique_regions.append(item[1])
    for region in unique_regions:
        total=0
        for each_num in sales_data:
            if region in each_num:
                total+=sum(each_num[2])
        total_sales_data.append((region, total))

    total_sales_data.sort()
    return total_sales_data
# Finally, create a main function analyze_sales_data(sales_data) that uses your helper functions to return a summary tuple containing: (top_salesperson_id, north_region_employees, regional_summary) where north_region_employees is the result of calling get_employees_in_region() with 'North'.
def analyze_sales_data(sales_data):

    top_seller = find_top_salesperson(sales_data)

    region_specific_result = get_employees_in_region(sales_data, "North")

    sales_total = get_regional_sales_total(sales_data)

    return (top_seller, region_specific_result, sales_total)
# Testing Inputs:+-
sales_data = [
    ('E101', 'North', [50000, 60000, 55000]), # Avg: 55000
    ('E201', 'South', [70000, 75000, 80000]), # Avg: 75000
    ('E102', 'North', [85000, 90000, 95000]), # Avg: 90000
    ('E301', 'West', [65000, 60000, 58000])  # Avg: 61000
]
# Expected Output:

print(analyze_sales_data(sales_data))
# ('E102', ['E101', 'E102'], [('North', 435000), ('South', 225000), ('West', 183000)])