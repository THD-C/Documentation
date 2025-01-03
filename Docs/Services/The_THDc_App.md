# [The_THDc_App]

Microservices Application with Docker Compose

This repository contains a Docker Compose setup to deploy a microservices-based THD(C) application. 

The system is designed with the following features:
- Microservices-based architecture for modular development.
- API integrations with external services such as Stripe, Google, and CoinGecko.
- Monitoring and observability using Prometheus, Grafana, Loki, and Tempo.
- Database management using MongoDB and PostgreSQL.

![image](https://raw.githubusercontent.com/THD-C/.github/refs/heads/main/Pictures/architecture.png)

## Architecture Overview

The system is composed of the following key components:

### Application Access

- **App_Proxy**: Acts as a reverse proxy to route traffic to the WebServer and Frontend_API.
- **Grafana**: Provides dashboards for metrics visualization.

### Backend Services

- **Frontend_API**: Provides REST and OAuth endpoints, integrating with external services like Stripe and Google.
- **Price_Manager**: Fetches data from external APIs (e.g., CoinGecko).
- **Orders_Service**: Manages orders placed by the users.

### Databases

- **MongoDB**: Used for NoSQL data storage.
- **PostgreSQL**: Used for SQL data storage.
- **DB_Manager**: Interacts with PostgreSQL using an ORM and provides gRPC methods for other services.
- **Mongo_Manager**: Interacts with MongoDB using PyMongo and provides gRPC methods for other services.

### Logging, Monitoring, and Tracing

- **Prometheus**: Collects metrics from services.
- **Loki**: Manages logs with the help of Promtail to track traffic going through **App_Proxy**.
- **Tempo**: Handles distributed tracing, using Redis for cache.
