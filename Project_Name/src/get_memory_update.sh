#!/bin/bash

# add itself to telegram channel to get live updates
# https://t.me/joinchat/<your_telegram_bot_link>

if [ $# -ne 1 ]; then
    echo $0: usage: get_memory_update.sh MESSAGE
    exit 1
else
    MESSAGE=$1
fi

# Fetches system logs, memory updates and message
pwd=`pwd`; date=`date`; sysname=`whoami`
machine_addr=`whoami;hostname -I | awk '{print $1}'` 
machine_addr=`echo ${machine_addr} | tr ' ' '@'`
MESSAGE=`echo -e '\n'${date}'\n'SystemInfo: ${machine_addr}'\n'ProjectDir: ${pwd}'\n\n'Log:'\n'${MESSAGE}`


TOKEN=<your_token>
CHAT_ID=<your_chat_id>
URL="https://api.telegram.org/bot${TOKEN}/sendMessage"

# telegram curl request
curl -s -X POST $URL -d chat=${CHAT_ID} -d text="${MESSAGE}"
