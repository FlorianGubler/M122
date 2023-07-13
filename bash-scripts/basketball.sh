#!/bin/bash


# Function to load NBA data

loaddata() {

  echo "Loading NBA Data"

  querystring="tournamentId=$1"

  headers=(

    "X-RapidAPI-Key: $2"

  )

  response=$(curl -s -G -H "${headers[@]}" --data-urlencode "$querystring" "$3")

  status_code=$(echo "$response" | jq -r '.status_code')

  if [[ $status_code -eq 200 ]]; then

    echo "Called NBA API successfully"

    echo "$response"

  else

    error_message=$(echo "$response" | jq -r '.error_message')

    echo "NBA API Call failed (StatusCode: $status_code), with Response: '$error_message'"

    exit 1

  fi

}


# Configuration

config_file="/config.json"

apikey="78b281d2b4msh199334df031c217p10b9b9jsne3f21c135a2c"


# Load data

loaddata "$config_file" "$apikey"
