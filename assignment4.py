# Create a restaurant service analysis system that evaluates server performance and calculates gratuities. Your program should:
# Define a function calculate_sales_amount(meal_type, table_count, service_level) that:
price=0
def calculate_sales_amount(meal_type,table_count,service_level):
# For “breakfast”: generates $30/table at low level, $45 at medium, $60 at high
    if meal_type=="breakfast":
        if service_level=="low":
            price=30
        elif service_level=="medium":
            price= 45
        elif service_level=="high":
            price= 60
        
# For “lunch”: generates $40/table at low level, $65 at medium, $90 at high
    elif meal_type=="lunch":
         if service_level=="low":
            price=40
         elif service_level=="medium":
            price= 65
         elif service_level=="high":
            price= 90
# For “dinner”: generates $55/table at low level, $85 at medium, $125 at high
    elif meal_type=="dinner":
         if service_level=="low":
            price=55
         elif service_level=="medium":
            price= 85
         elif service_level=="high":
            price= 125
# Return the total sales amount
    return price*table_count
# Define a function calculate_efficiency_score(shift_years, standard_tables, served_tables) that:
def calculate_efficiency_score(shift_years, standard_tables, served_tables):
# Calculate expected tables: 1000 + (shift_years * 100)
    expected_tables=1000+(shift_years*100) #1300
# Calculate table capacity: expected_tables - standard_tables
    table_capacity=(expected_tables-standard_tables) #500
# Calculate efficiency percentage: (served_tables - standard_tables) / table_capacity * 100
    efficiency_percentage=(served_tables-standard_tables)/table_capacity*100 
# Return the efficiency percentage
    return round(efficiency_percentage,1)
# Define a function determine_service_rating(efficiency_percent) that:
rating_bonus=0
def determine_service_rating(efficiency_percent):
    global rating_bonus
    # Below 50%: “Learning Stage”
    if efficiency_percent<50:
        rating_bonus=0.5
        return "Learning stage"
    # 50-60%“Capable Stage”
    elif 50<=efficiency_percent<60:
        rating_bonus=1.0
        return "Capable Stage"
    # 60-70%: “Skilled Stage”
    elif 60<=efficiency_percent<70:
        rating_bonus=1.2
        return "Skilled Stage"
    # 70-85%: “Accomplished Stage”
    elif 70<=efficiency_percent<85:
        rating_bonus=1.5
        return "Accomplished stage"
    # Above 85%: “Master Stage”
    else:
        rating_bonus=1.8
        return "Master Stage"

# Define a : function calculate_tip_earnings(sales, tables, rating_bonus) that:
def calculate_tip_earnings(sales, tables, rating_bonus):
    # Base tips = sales * 0.05 + tables * 2
    base_tips=sales*0.05+tables*2
    final_tips=base_tips*rating_bonus
    return round(final_tips, 1)
    # Rating bonuses: Learning=0.5, Capable=1.0, Skilled=1.2, Accomplished=1.5, Master=1.8
    # Return the final tips rounded to 1 decimal place
# Define a function requires_mentoring(service_weeks, total_tables, avg_efficiency) that:
def requires_monitoring(service_weeks, total_tables,avg_efficiency):
    # Returns True if service_weeks >= 6 AND avg_efficiency < 50
    if service_weeks>=6 and avg_efficiency<50:
        return True
    # Returns True if total_tables < 100 AND avg_efficiency < 60
    elif total_tables < 100 and avg_efficiency < 60:
        return True
    # Returns True if service_weeks >= 4 AND avg_efficiency < 40
    elif service_weeks >= 4 and avg_efficiency < 40:
        return True
    # Otherwise returns False
    else:
        return False
# Define a function generate_service_summary(server, meal_type, tables, service_level, shift_years, standard_tables, served_tables, service_weeks) that

def generate_service_summary(server, meal_type, table_count, service_level,shift_years, standard_tables, served_tables, service_weeks):
    # Calls all necessary functions to calculate metrics
    # Prints a formatted summary (no return value)
    # Include all calculated values and recommendations
    print("RESTAURANT SERVICE ANALYZER")
    print("*"*40)
    print(f"Service Summary for: {server}")
    print(f"Meal Type: {meal_type}")
    print(f"Tables Served: {table_count}")
    print(f"Service Level: {service_level}")
    print(f"Sales amount: ${calculate_sales_amount(meal_type,table_count,service_level)}")
    print(f"Efficiency Analysis:")
    print(f"Experience: {shift_years} years, Standar: {standard_tables}, Served tables: {served_tables}")
    print(f"Efficiency: {calculate_efficiency_score(shift_years, standard_tables, served_tables)} %")
    print(f"Service rating: {determine_service_rating(calculate_efficiency_score(shift_years, standard_tables, served_tables))}")
    print(f"Tip Earnings: ${calculate_tip_earnings(calculate_sales_amount(meal_type,table_count,service_level), table_count, rating_bonus)}")
    print(f"Service weeks: {service_weeks}")
    print(f"Mentoring required: { requires_monitoring(service_weeks, served_tables,calculate_efficiency_score(shift_years, standard_tables, served_tables))}")

server="Quinn"
meal_type="dinner"
table_count=45 
service_level="high"
shift_years= 3 
standard_tables=800
served_tables=1150
service_weeks=3
generate_service_summary(server, meal_type, table_count, service_level,shift_years, standard_tables, served_tables, service_weeks)

server="Reese"
meal_type="lunch"
table_count=60
service_level="medium"
shift_years= 5
standard_tables=900
served_tables=1300
service_weeks=5
generate_service_summary(server, meal_type, table_count, service_level,shift_years, standard_tables, served_tables, service_weeks)

server="Skyler"
meal_type="breakfast"
table_count=30
service_level="low"
shift_years= 8
standard_tables=850
served_tables=950
service_weeks=7
generate_service_summary(server, meal_type, table_count, service_level,shift_years, standard_tables, served_tables, service_weeks)
# Record 1: “Quinn”, “dinner”, 45 tables, “high”, shift_years=3, standard_tables=800, served_tables=1150, service_weeks=3
# Record 2: “Reese”, “lunch”, 60 tables, “medium”, shift_years=5, standard_tables=900, served_tables=1300, service_weeks=5
# Record 3: “Skyler”, “breakfast”, 30 tables, “low”, shift_years=8, standard_tables=850, served_tables=950, service_weeks=7
#     RESTAURANT SERVICE ANALYZER
# ========================================
# Service Summary for: Quinn
# ----------------------------------------
# Meal Type: dinner
# Tables Served: 45
# Service Level: high
# Sales Amount: $5625
# Efficiency Analysis:
#   Experience: 3 years, Standard: 800, Served Tables: 1150
#   Efficiency: 70.0%
#   Service Rating: Accomplished Stage
# Tip Earnings: $556.9
# Service Weeks: 3
# Mentoring Required: No

# ========================================
# Service Summary for: Reese
# ----------------------------------------
# Meal Type: lunch
# Tables Served: 60
# Service Level: medium
# Sales Amount: $3900
# Efficiency Analysis:
#   Experience: 5 years, Standard: 900, Served Tables: 1300
#   Efficiency: 66.7%
#   Service Rating: Skilled Stage
# Tip Earnings: $378.0
# Service Weeks: 5
# Mentoring Required: No

# ========================================
# Service Summary for: Skyler
# ----------------------------------------
# Meal Type: breakfast
# Tables Served: 30
# Service Level: low
# Sales Amount: $900
# Efficiency Analysis:
#   Experience: 8 years, Standard: 850, Served Tables: 950
#   Efficiency: 10.5%
#   Service Rating: Learning Stage
# Tip Earnings: $52.5
# Service Weeks: 7
# Mentoring Required: Yes





# Testing Inputs: Test your system with these service records:

