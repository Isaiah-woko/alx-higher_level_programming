#!/bin/bash
# Catch me if you can!
curl -s -L -X PUT -d "user_id=98" "0.0.0.0:5000/catch_me" | grep -q "You got me!" && echo "You got me!"

