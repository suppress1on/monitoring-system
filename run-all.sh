# Running the all project with using one script.
# $ chmod +x run-all.sh
# $ ./run-all.sh

#!/bin/bash

echo "[*] Checking requirements..."
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
else
    echo "[!] File requirements.txt not found."
    exit 1
fi

echo "[*] Running docker-compose..."
docker compose up -d

echo "[*] Running webhook..."
python3 webhook/server.py
