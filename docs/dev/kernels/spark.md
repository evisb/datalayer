---
title: Spark Kernel
---

# Spark Kernel

## Toree Kernel

```bash
pip install --pre toree
pip install https://dist.apache.org/repos/dist/dev/incubator/toree/0.2.0/snapshots/dev1/toree-pip/toree-0.2.0.dev1.tar.gz
```

```bash
export SPARK_HOME=/opt/spark
cd $DLAHOME/repos/jupyter-toree
make clean release APACHE_SPARK_VERSION=2.2.0
# pip install toree --no-index --find-links=./dist/toree-pip/toree-0.3.0.dev1.tar.gz
pip install --upgrade ./dist/toree-pip/toree-0.3.0.dev1.tar.gz
pip freeze | grep toree
```

```bash
jupyter toree install --spark_home=/opt/spark --interpreters=Scala,PySpark,SparkR,SQL
jupyter notebook
```

```bash
jupyter kernelspec list
Available kernels:
  python3                 /opt/miniconda3/envs/datalayer/share/jupyter/kernels/python3
  apache_toree_pyspark    /usr/local/share/jupyter/kernels/apache_toree_pyspark
  apache_toree_scala      /usr/local/share/jupyter/kernels/apache_toree_scala
  apache_toree_sparkr     /usr/local/share/jupyter/kernels/apache_toree_sparkr
  apache_toree_sql        /usr/local/share/jupyter/kernels/apache_toree_sql
```

```bash
jupyter kernelspec remove apache_toree_pyspark
```

Near the end of this file: /usr/local/share/jupyter/kernels/apache_toree_pyspark/bin/run.sh (which is invoked by the pyspark kernel)

```bash
    --master k8s://https://rb-spark:6443 \
    --conf spark.executor.instances=3 \
    --conf spark.kubernetes.container.image=node001:5000/brightcomputing/spark-py:v2.3.0 \
    --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark \
```

So the exec call looks like this:

```bash
eval exec \
  "${SPARK_HOME}/bin/spark-submit" \
  --name "'Apache Toree'" \
  "${SPARK_OPTS}" \
  --master k8s://https://rb-spark:6443 \
  --conf spark.executor.instances=3 \
  --conf spark.kubernetes.container.image=node001:5000/brightcomputing/spark-py:v2.3.0 \
  --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark \
  --class org.apache.toree.Main \
  "${TOREE_ASSEMBLY}" \
  "${TOREE_OPTS}" \
  "$@"
```

## SparkMagic

[SparkMagic with Livy Kernel](https://github.com/jupyter-incubator/sparkmagic)
