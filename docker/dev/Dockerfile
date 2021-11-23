
FROM ubuntu:latest

LABEL version="2.0"
LABEL Christian Sargusingh "https://github.com/cSDes1gn"

# Grab dependencies and generate locale
RUN apt update && apt upgrade -y && apt install -y git sudo locales && locale-gen en_US.UTF-8

WORKDIR /app

# add package dependancy indices
COPY requirements.txt . 

# install dependancies
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT [ "./docker/dev/entry.sh" ]