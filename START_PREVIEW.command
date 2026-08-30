#!/bin/bash
cd "$(dirname "$0")"
PORT=5500
lsof -tiTCP:$PORT -sTCP:LISTEN | xargs kill -9 2>/dev/null
echo "Starting Prime site preview on http://127.0.0.1:$PORT/"
echo "Leave this window open. Close it to stop the preview."
python3 -m http.server "$PORT" --bind 127.0.0.1 &
PID=$!
sleep 0.5
open "http://127.0.0.1:$PORT/"
wait $PID
