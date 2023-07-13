#!/bin/bash


# API Key

api_key="78b281d2b4msh199334df031c217p10b9b9jsne3f21c135a2c"


# API URL

api_url="https://basketball-data.p.rapidapi.com/tournament/leaderboard/point?tournamentId=1"


# GET Request

response=$(curl -s -H "X-RapidAPI-Key: $api_key" "$api_url")


# Output

echo "$response"
