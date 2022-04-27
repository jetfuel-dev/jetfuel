# Build Frontend
FROM node:17 AS frontend_builder
WORKDIR /bin/jetfuel

COPY ./dashboard .

# Install Yarn and build frontend
RUN yarn --pure-lockfile
RUN yarn build

# Build Release Image
FROM python:3.9.12
WORKDIR /bin/jetfuel

# Creating logging directory (Uvicorn fails if this directory doesn't exist)
RUN mkdir -p /var/log/jetfuel/

RUN apt-get update && \
    apt-get install -y software-properties-common

# Install Pip
RUN python3 -m pip install --upgrade pip

# Install Python Dependencies
COPY ./server/requirements.txt /bin/jetfuel/requirements.txt
RUN python3 -m pip install --no-cache-dir -r /bin/jetfuel/requirements.txt
RUN rm /bin/jetfuel/requirements.txt

# Copy Server
COPY ./server /bin/jetfuel

# Copy Static Frontend
COPY --from=frontend_builder /bin/jetfuel/build ./frontend

EXPOSE 9000

CMD ["bash", "start.sh"]
