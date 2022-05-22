#!/bin/bash
printf "Redis status \n\n\n" 
redis-cli lrange "channel:jawaker" 0 -1
printf "\n\n\n Database status \n\n\n"
sudo -u jawaker -H -- psql -d jawaker -c 'SELECT * FROM users;'
printf "\n\n\n Service status \n\n\n"
systemctl status rtpg

