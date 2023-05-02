#!/bin/bash

# set the input and vendor files
input_file="input.txt"
vendor_file="vendor.txt"

# loop through each line in the input file
while read -r line
do
  # extract the hostname, IP, and MAC address from the input line
  hostname=$(echo $line | awk '{print $1}')
  ip=$(echo $line | awk '{print $2}')
  mac=$(echo $line | awk '{print $3}')

  # parse the MAC address to extract the first 6 octets
  mac_prefix=$(echo $mac | tr -d ':' | cut -c 1-12)

  # search the vendor file for the MAC address prefix
  vendor=$(grep -i "^$mac_prefix" $vendor_file | awk '{print $2}')

  # print the results
  echo "Hostname: $hostname"
  echo "IP Address: $ip"
  echo "MAC Address: $mac"
  echo "Vendor: $vendor"
  echo ""
done < "$input_file"
