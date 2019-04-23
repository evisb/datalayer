---
title: Install with Docker
---

# Install with Docker

> Check the [requirements](/devops/requirements.md) to setup your local environment.

You can install Datalayer a single node local system, e.g. on your laptop or any single node server.

```bash
# Install DSP locally.
dla dsp-local-install
```

This will install the services shown on the following images. You will have to continue with the next steps of this document to start the services and check they are operational.

**Minimal DSP Services with Docker**

![Minimal DSP with Docker](/_images/dsp/dsp-docker-min.svg)

**Full DSP Services with Docker**

![Full DSP with Docker](/_images/dsp/dsp-docker.svg)

## Start the Services

Pull the `jupyterlab` docker image and start the services.

```bash
# Seed DSP platform.
dla dsp-swarm-up seed
```

Configure the secret in the `~/.datalayer` folder.

```bash
# Start DSP platform.
dla dsp-swarm-up
```

```bash
# Tail the logs.
dla dsp-swarm-logs
# Tail the logs of a specific container.
dla dsp-swarm-logs explorer
```

```bash
# Show the local platform status.
dla dsp-swarm-status
```

## Check Traefik Service

```bash
# Check Traefik Service.
```

## Check IAM Service

```bash
# Check Keycloak Service.
```

```bash
# Check LDAP Service.
```

## Check Kuber Service

```bash
# Check Kuber Service.
```

## Check Zookeeper Service

```bash
# Check Zookeeper Service.
dla zk-cli
```

```bash
# If useful for you (debugging...), you can run some of the services without Docker.
# Init Configuration and Start Zookeeper.
dla zk-conf-gen && dla zk-init && dla zk-start
```

## Check HDFS Service

```bash
# Check HDFS Service.
# NAMENODE_IP=$(docker inspect --format '{{ .NetworkSettings.Networks.hdfs_default.IPAddress }}' namenode)
# echo http://$NAMENODE_IP:9870
echo http://0.0.0.0:9870 # browse namenode ui
echo http://0.0.0.0:9864 # browse datanode ui
dla hdfs dfs -mkdir /tmp
dla hdfs dfs -ls / # list root folder
```

```bash
# If useful for you (debugging...), you can run some of the services without Docker.
# Init Configuration and Start HDFS.
dla hdfs-conf-gen && dla hdfs-init && dla hdfs-start
```

## Check HBase Service

```bash
# Check HBase Service.
```

```bash
# If useful for you (debugging...), you can run some of the services without Docker.
# Init Configuration and Start HBase.
dla hbase-conf-gen && dla hbase-start
```

## Check Solr Service

```bash
# Check Solr Service.
```

```bash
# If useful for you (debugging...), you can run some of the services without Docker.
# Init Configuration nd Start Solr.
dla solr-conf-gen && dla solr-start
```

## Check Kafka Service

```bash
# Check Kafka Service.
```

## Check JanusGraph Service

```bash
# Check JanusGraph Service.
```

## Check IPFS Service

```bash
# Check IPFS Service.
```

## Check JupyterHub Service

```bash
# Check JupyterHub Proxy HTTP Service.
```

```bash
# Check JupyterHub Hub Service.
```

```bash
# Check JupyterHub Single User Service.
```

## Check Kernels Service

```bash
# Check Kernels Service.
```

## Check Spark Service

```bash
# Check Spark Service.
```

```bash
# Check Spark Python Service.
```

```bash
# Check Spark R Service.
```

## Check Explorer Service

```bash
# Check Explorer Service.
```

## Check Library Service

```bash
# Check Library Service.
```

## Stop the Services

To stop the services, run the following command.

```bash
# Stop DSP locally.
dla dsp-swarm-down
```

## Backup the Volumes

```bash
dla dsp-swarm-backup
```
