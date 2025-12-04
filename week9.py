def parse_config(config_string, required_setting):

    if config_string[-1] != ">":
        return "Error: Incomplete configuration"


    missing_keys=[]
    for key in required_setting:
        if key not in config_string:
            missing_keys.append(key)
            return f"Error: Missing settings: {missing_keys}"
           
    parsed_list= []
    a_list=config_string.replace(">","").split("--")
   
    for item in required_setting:
        for key_value in a_list:
            splitted = key_value.split("::")
            if item in splitted:
                parsed_list.append(splitted[1])


    return parsed_list
    
# Test Case 1: Valid config
conf1 = "SSID::GuestNet--PASS::Secret123--IP::DHCP>"
req1 = ["SSID", "PASS", "IP"]
print(parse_config(conf1, req1))

# Test Case 2: Valid config but missing a setting
conf2 = "SSID::HomeWifi--CHANNEL::6>"
req2 = ["SSID", "PASS"]
print(parse_config(conf2, req2))

# Test Case 3: Invalid format (missing end bracket)
conf3 = "SSID::Office--PASS::Admin"
req3 = ["SSID"]
print(parse_config(conf3, req3))

conf4 = "TIMEOUT::30--PORT::8080--HOST::Localhost>"
req4 = ["HOST", "PORT", "TIMEOUT"]
print(parse_config(conf4, req4))


# Expected Output:

# ['GuestNet', 'Secret123', 'DHCP']
# Error: Missing settings: ['PASS']
# Error: Incomplete configuration.
# ['Localhost', '8080', '30']