#!/bin/bash

# v 1.0.2
# https://gist.github.com/mbierman/03b2a962ac04963ef5bbc8354d0ed5d1
# 2022 mbierman

sleep="${1:-5}"
regex="^([0-9A-F]{2}[:]){5}([0-9A-F]{2})$"

# Generate a random MAC address using OpenSSL and sed
mac=$(openssl rand -hex 6 | sed 's/\(..\)\(..\)\(..\)\(..\)\(..\)\(..\)/\1:\2:\3:\4:\5:\6/')

# Set the adapter to "en0" (Wi-Fi)
adapter="en0"

# Set the type of the adapter (Ethernet or Wi-Fi) 
type="Wi-Fi"


# # Prompt the user to confirm the adapter and its type
# read -p "Is $adapter $type (y|n)? " -n 1 -r

# # If the user doesn't confirm, exit the script
# if [[ ! $REPLY =~ ^[Yy]$ ]];  then
#     echo "Exiting. Run again"
#     exit
# fi

# Disable the adapter, sleep for the specified time, enable the adapter, set the MAC address, and detect new hardware
sudo ifconfig $adapter down && sleep $sleep  && sudo ifconfig $adapter up && \
sudo ifconfig $adapter ether $mac && sudo networksetup -detectnewhardware