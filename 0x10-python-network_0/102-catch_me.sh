#!/bin/bash
# Catch me if you can!
curl -s -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me | grep -o "You got me!"
