#!/bin/bash
echo curl --request GET \
	--url 'https://basketball-data.p.rapidapi.com/tournament/leaderboard/point?tournamentId=89' \
	--header 'X-RapidAPI-Host: basketball-data.p.rapidapi.com' \
	--header 'X-RapidAPI-Key: 78b281d2b4msh199334df031c217p10b9b9jsne3f21c135a2c'
