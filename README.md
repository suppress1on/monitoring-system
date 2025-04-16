The target of the project is to implement a system for monitoring the operation of the Nginx server using a combination of Prometheus and Grafana tools and sent alerts via a Telegram.

Overview:
In the docker-compose.yml file, all parts of the project are described: Prometheus, Grafana, Node Exporter, and Nginx Exporter. Exporters are needed so services can create metrics, which Prometheus collects. To collect metrics from a specific service, it must be listed as a "job" in the prometheus.yml file. When Prometheus collects the metrics, it stores them on its own server.
To see what Prometheus has collected, we use Grafana. In the Grafana interface, we create dashboards to show the metrics.
There is also an Alertmanager, which sends alerts to a special port on the webhook server. Everything sent to that server is forwarded to me via a Telegram bot.

A bit about Docker Compose:
Docker Compose is the tool that runs everything. It starts the containers, opens ports for them, and mounts system folders to save important data (like cache and dependencies).

A bit about Prometheus:
Prometheus is the main tool in this project. Everything depends on it. Without Prometheus, we could not see the metrics, and Alertmanager could not send alerts to the server. Alertmanager sends its alerts to port 5001.

A bit about Grafana:
The main goal was to send alerts to Telegram, but I also added Grafana to improve the system. Grafana connects to the Prometheus server and shows the metrics as graphs and charts.

A bit about the webhook:
The webhook is a small server that sends everything it receives to Telegram. It’s the final point in the project.

Extras:
I also added a pipeline that checks if everything starts correctly.
The system is already mostly automated, but I made a script called run-all.sh that launches everything with one command.

How to run:
You can use these two commands:

$ docker compose up -d  
$ python3 server.py

Or just run the script:

$ chmod +x run-all.sh  
$ ./run-all.sh
