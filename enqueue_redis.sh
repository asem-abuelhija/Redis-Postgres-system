while true; do
  echo "Enqueue"
  redis-cli rpush "channel:jawaker" "{\"username\":\"tarneeb\"}"
  sleep 1
done