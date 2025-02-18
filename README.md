# Docker Networking and Volume Management

This assignment demonstrates Docker container networking and volume management using Docker Compose. The setup consists of two containers:

- **Producer**: Generates random data and serves it over a network.
- **Consumer**: Retrieves data from the Producer and stores it persistently using a Docker volume.

## Components
- **Producer (producer/)**: Contains `app.py`, which generates and serves random data via an HTTP endpoint.
- **Consumer (consumer/)**: Contains `app.py`, which fetches data from the Producer and stores it in `/data/logs.txt`.
- **Dockerfiles (producer/Dockerfile and consumer/Dockerfile)**: Define how each container is built, including dependencies and setup.
- **docker-compose.yml**: Defines the services, networking, and volume configuration.
- **README.md**: Documentation explaining setup and usage.

## Project Structure
```
docker-networking-volume/
│── producer/          # Data Producer container
│   ├── app.py        # Generates random data
│   ├── Dockerfile    # Defines Producer image
│   └── requirements.txt # Dependencies
│
│── consumer/          # Data Consumer container
│   ├── app.py        # Fetches and stores data
│   ├── Dockerfile    # Defines Consumer image
│   └── requirements.txt # Dependencies
│
│── docker-compose.yml # Defines and manages services
│── README.md          # Project documentation
```

## How to Build and Run the Containers

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd <your-repo-name>
```

### 2. Build the Docker Images
```sh
docker-compose build
```

### 3. Start the Containers
```sh
docker-compose up -d
```

### 4. Verify Running Containers
```sh
docker ps
```

### 5. Check Stored Data in Consumer Container
```sh
docker exec -it $(docker ps -q -f name=consumer) bash
cat /data/logs.txt
```

## Stopping and Cleanup
To stop and remove containers:
```sh
docker-compose down
```

To remove unused images and volumes:
```sh
docker system prune -a
```






