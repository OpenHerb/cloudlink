# OpenHerb Cloudlink
[![deploy](https://github.com/OpenHerb/cloud-link/actions/workflows/deploy.yaml/badge.svg)](https://github.com/OpenHerb/cloud-link/actions/workflows/deploy.yaml)

![img](/docs/img/icon.png)

Cloud link microservices

## Quickstart

### Production
Add the cloudlink microservice to the production stack:
```yaml
services:
  cloudlink:
	image: ghcr.io/openherb/cloudlink:latest
    container_name: cloudlink
	restart: always
	depends_on:
      - rmq
    devices:
      - "/dev/ttyUSB0:/dev/ttyUSB0"
    environment:
      - RABBITMQ_ADDR=rmq:1883
      - TELEMETRY_TOPIC=topic/telemetry
      - CLIENT_ID=d1db92fb-ba15-4dcd-8603-64e0bcf1828b
```

### Development
Start the local development stack mounting the repository root:
```
docker compose up
```

Teardown the development stack
```bash
docker compose down --rmi "all"
```

## RabbitMQ Management
Access the rabbitmq management server at http://localhost:15672/

### Admin Login Credentials
user: `admin`
password: `admin`


## License
[GNU General Public License v3.0](/LICENSE)