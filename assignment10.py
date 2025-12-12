print('Error Counts:')

def analyze_logs(log_entries):
    error_entries = {}
    
    for entry in log_entries:
        splitted_entry = entry.split("-")
        ip_adress = splitted_entry[0].strip()
        status_code = splitted_entry[1].strip()

        if status_code == "200":
            continue

        if status_code == "404" or status_code == "500":
            if ip_adress not in error_entries:
                error_entries[ip_adress] = 0

            error_entries[ip_adress] = error_entries[ip_adress] + 1

    return error_entries


def flag_suspicious_ips(error_dict):
    for key, value in error_dict.items():
        print(f"{key}: {value}")
    
    print('--------------------')    
    for key, value in error_dict.items():
        if value > 2:
            print(f"SECURITY ALERT: {key} has {value} errors.")









log_entries = [
    "192.168.1.1 - 200",
    "10.0.0.5 - 404",
    "192.168.1.1 - 200",
    "10.0.0.5 - 500",
    "172.16.0.1 - 404",
    "10.0.0.5 - 404",
    "192.168.1.1 - 500",
    "10.0.0.5 - 404"
]


flag_suspicious_ips(analyze_logs(log_entries))

# Expected Output:

# Error Counts:
# 10.0.0.5: 4
# 172.16.0.1: 1
# 192.168.1.1: 1
# --------------------
# SECURITY ALERT: 10.0.0.5 has 4 errors.
