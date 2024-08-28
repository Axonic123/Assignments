#!/bin/bash

# Define the log file path
LOG_FILE="access.log"

# Check if the file exists
if [[ ! -f "$LOG_FILE" ]]; then
    echo "Log file $LOG_FILE does not exist."
    exit 1
fi

# 1. Count the different HTTP response status codes
echo "HTTP_STATUS"
awk '{print $9}' "$LOG_FILE" | sort | uniq -c | awk '{print $2 " - " $1}' | sort -n

# Separator
echo "=="

# 2. Count unique client IP addresses
UNIQUE_IP_COUNT=$(awk '{print $1}' "$LOG_FILE" | sort | uniq | wc -l)
echo "UNIQUE_CLIENT_ADDRESS - $UNIQUE_IP_COUNT"

# Separator
echo "=="

# 3. Count the number of words in each line
echo "Line count_of_words"
echo "Line_Number | Count"
LINE_NUMBER=1
while IFS= read -r line; do
    word_count=$(echo "$line" | wc -w)
    echo "$LINE_NUMBER | $word_count"
    LINE_NUMBER=$((LINE_NUMBER + 1))
done < "$LOG_FILE"

