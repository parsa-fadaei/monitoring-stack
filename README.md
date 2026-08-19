# Monitoring Stack with Prometheus, Grafana & Docker Compose

A production-style monitoring and observability stack built using Docker Compose.

This project demonstrates infrastructure monitoring, container monitoring, database monitoring, web server monitoring, and application observability using the Prometheus ecosystem.

---

## Overview

The goal of this project is to build a complete monitoring platform capable of collecting, storing, visualizing, and alerting on system and application metrics.

The stack monitors:

- Linux host resources
- Docker containers
- PostgreSQL database
- NGINX web server
- FastAPI application metrics

---

## Architecture

(Architecture diagram will be added here)

---

## Technologies

| Component | Purpose |
|---|---|
| Docker Compose | Container orchestration |
| Prometheus | Metrics collection and querying |
| Grafana | Dashboards and visualization |
| Alertmanager | Alert processing and routing |
| node_exporter | Linux system metrics |
| cAdvisor | Container metrics |
| postgres_exporter | PostgreSQL metrics |
| nginx exporter | NGINX metrics |
| FastAPI | Instrumented application |

---

## Features

- Host resource monitoring
- Container monitoring
- Database monitoring
- NGINX monitoring
- Application metrics instrumentation
- PromQL queries
- Grafana dashboards
- Histogram-based latency monitoring
- Prometheus alert rules
- Alertmanager integration
