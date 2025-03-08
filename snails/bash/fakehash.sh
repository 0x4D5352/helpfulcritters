#!/bin/bash

# _____ _____  _   _           _       ____                 _   _          
# | ____|__  / | | | | __ _ ___| |__   |  _ \ _ __ __ _  ___| |_(_) ___ ___ 
# |  _|   / /  | |_| |/ _` / __| '_ \  | |_) | '__/ _` |/ __| __| |/ __/ _ \
# | |___ / /_  |  _  | (_| \__ \ | | | |  __/| | | (_| | (__| |_| | (_|  __/
# |_____/____| |_| |_|\__,_|___/_| |_| |_|   |_|  \__,_|\___|\__|_|\___\___|

# MVP - spit out fake /etc/shadow with X usernames in format user:md5hash
# Planned Upgrades:
    # Customizable hash type
    # Custom Password List
    # Custom User List
    # custom file length

# variable assignments
usercount=10
userlist=/Users/Shared/wordlists/usernames.txt
wordlist=/Users/Shared/wordlists/rockyou.txt
output=./hashlist

for x in $(seq 1 $usercount)
do
    name=$(head -n $[$RANDOM % $(wc -l $userlist | awk '{print $1}')] $userlist | tail -1)
    pass=$(md5 -s $(head -n $[$RANDOM % $(wc -l $wordlist | awk '{print $1}')] $wordlist | tail -1) | awk '{print $4}')
    echo $name:$pass >> $output
done
