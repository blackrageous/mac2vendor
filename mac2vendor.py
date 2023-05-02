Sure! Here's an example Python script that achieves the same functionality as the Bash script in my previous response:

```python
#!/usr/bin/env python3

# Set the input and vendor files
input_file = "input.txt"
vendor_file = "vendor.txt"

# Read the vendor file into a dictionary
vendor_dict = {}
with open(vendor_file, "r") as f:
    for line in f:
        fields = line.strip().split()
        vendor_dict[fields[0]] = fields[1]

# Loop through each line in the input file
with open(input_file, "r") as f:
    for line in f:
        # Extract the hostname, IP, and MAC address from the input line
        fields = line.strip().split()
        hostname = fields[0]
        ip = fields[1]
        mac = fields[2]

        # Parse the MAC address to extract the first 6 octets
        mac_prefix = mac.replace(":", "")[:12]

        # Search the vendor dictionary for the MAC address prefix
        if mac_prefix in vendor_dict:
            vendor = vendor_dict[mac_prefix]
        else:
            vendor = "Unknown"

        # Print the results
        print("Hostname: {}".format(hostname))
        print("IP Address: {}".format(ip))
        print("MAC Address: {}".format(mac))
        print("Vendor: {}".format(vendor))
        print()
```

In this Python script, we first read the vendor file into a dictionary, where each key is a MAC address prefix and each value is the corresponding vendor name. We then use a `with` statement to open the input file and loop through each line. For each line, we extract the hostname, IP address, and MAC address.

Next, we parse the MAC address to extract the first 6 octets, which we store in the `mac_prefix` variable. We then use an `if` statement to check whether the `mac_prefix` is in the vendor dictionary. If it is, we retrieve the corresponding vendor name. If it's not, we set the vendor name to "Unknown".

Finally, we print out the results, including the hostname, IP address, MAC address, and vendor name. The `print()` function adds a blank line between each set of results to make the output more readable.