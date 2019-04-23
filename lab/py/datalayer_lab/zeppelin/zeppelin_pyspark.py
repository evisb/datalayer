#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys, getopt, traceback

from py4j.java_gateway import java_import, JavaGateway, GatewayClient
from py4j.protocol import Py4JJavaError
from pyspark.conf import SparkConf
from pyspark.context import SparkContext
from pyspark.rdd import RDD
from pyspark.files import SparkFiles
from pyspark.storagelevel import StorageLevel
from pyspark.accumulators import Accumulator, AccumulatorParam
from pyspark.broadcast import Broadcast
from pyspark.serializers import MarshalSerializer, PickleSerializer

# for back compatibility
from pyspark.sql import SQLContext, HiveContext, SchemaRDD, Row

#######################################################
#             ___       __       __
#   _______  / _ \___ _/ /____ _/ /__ ___ _____ ____
#  _______  / // / _ `/ __/ _ `/ / _ `/ // / -_) __/
# _______  /____/\_,_/\__/\_,_/_/\_,_/\_, /\__/_/
#                                    /___/
#
#######################################################

import StringIO

def show(p):
  img = StringIO.StringIO()
  p.savefig(img, format='svg')
  img.seek(0)
  print "%html <div style='width:600px'>" + img.buf + "</div>"

#######################################################

import numpy as np

def arrayToNumpy(ar):
  anArray = np.array([])
  for el in ar:
    anArray = np.append(anArray, el)

  return anArray

def dnaToNumpy(arOfAr):
  myMatrix = np.array([])

  for row in arOfAr:
    aRow = arrayToNumpy(row)

    if (len(myMatrix) > 0):
      myMatrix = np.vstack([myMatrix, aRow])
    else:
      myMatrix = aRow

  return myMatrix

def npToJavaArray(arr):
  myArray = gateway.new_array(gateway.jvm.double, len(arr))
  for el in range(0, len(arr)):
    myArray[el] = arr.item(el)

####################################################

class Logger(object):
  def __init__(self):
    self.out = ""

  def write(self, message):
    self.out = self.out + message

  def get(self):
    return self.out

  def reset(self):
    self.out = ""


class PyZeppelinContext(dict):
  def __init__(self, zc):
    self.z = zc

  def show(self, obj):
    from pyspark.sql import DataFrame
    if isinstance(obj, DataFrame):
      print gateway.jvm.org.apache.zeppelin.spark.ZeppelinContext.showDF(self.z, obj._jdf)
    else:
      print str(obj)

  # By implementing special methods it makes operating on it more Pythonic
  def __setitem__(self, key, item):
    self.z.put(key, item)

  def __getitem__(self, key):
    return self.z.get(key)

  def __delitem__(self, key):
    self.z.remove(key)

  def __contains__(self, item):
    return self.z.containsKey(item)

  def add(self, key, value):
    self.__setitem__(key, value)

  def put(self, key, value):
    self.__setitem__(key, value)

  def get(self, key):
    return self.__getitem__(key)

  def getDF(self):
    return self.z.getDF()


output = Logger()
sys.stdout = output
sys.stderr = output

client = GatewayClient(port=int(sys.argv[1]))
sparkVersion = sys.argv[2]

if sparkVersion.startswith("1.4"):
  gateway = JavaGateway(client, auto_convert = True)
else:
  gateway = JavaGateway(client)

java_import(gateway.jvm, "org.apache.spark.SparkEnv")
java_import(gateway.jvm, "org.apache.spark.SparkConf")
java_import(gateway.jvm, "org.apache.spark.api.java.*")
java_import(gateway.jvm, "org.apache.spark.api.python.*")
java_import(gateway.jvm, "org.apache.spark.mllib.api.python.*")

intp = gateway.entry_point
intp.onPythonScriptInitialized()

jsc = intp.getJavaSparkContext()

if sparkVersion.startswith("1.2"):
  java_import(gateway.jvm, "org.apache.spark.sql.SQLContext")
  java_import(gateway.jvm, "org.apache.spark.sql.hive.HiveContext")
  java_import(gateway.jvm, "org.apache.spark.sql.hive.LocalHiveContext")
  java_import(gateway.jvm, "org.apache.spark.sql.hive.TestHiveContext")
elif sparkVersion.startswith("1.3"):
  java_import(gateway.jvm, "org.apache.spark.sql.*")
  java_import(gateway.jvm, "org.apache.spark.sql.hive.*")
elif sparkVersion.startswith("1.4"):
  java_import(gateway.jvm, "org.apache.spark.sql.*")
  java_import(gateway.jvm, "org.apache.spark.sql.hive.*")


java_import(gateway.jvm, "scala.Tuple2")

jconf = intp.getSparkConf()
conf = SparkConf(_jvm = gateway.jvm, _jconf = jconf)
sc = SparkContext(jsc=jsc, gateway=gateway, conf=conf)
sqlc = SQLContext(sc, intp.getSQLContext())
sqlContext = sqlc

z = PyZeppelinContext(intp.getZeppelinContext())

while True :
  req = intp.getStatements()
  try:
    stmts = req.statements().split("\n")
    jobGroup = req.jobGroup()
    final_code = None

    for s in stmts:
      if s == None:
        continue

      # skip comment
      s_stripped = s.strip()
      if len(s_stripped) == 0 or s_stripped.startswith("#"):
        continue

      if final_code:
        final_code += "\n" + s
      else:
        final_code = s

    if final_code:
      compiledCode = compile(final_code, "<string>", "exec")
      sc.setJobGroup(jobGroup, "Zeppelin")
      eval(compiledCode)

    intp.setStatementsFinished(output.get(), False)
  except Py4JJavaError:
    excInnerError = traceback.format_exc() # format_tb() does not return the inner exception
    innerErrorStart = excInnerError.find("Py4JJavaError:")
    if innerErrorStart > -1:
       excInnerError = excInnerError[innerErrorStart:]
    intp.setStatementsFinished(excInnerError + str(sys.exc_info()), True)
  except:
    intp.setStatementsFinished(traceback.format_exc(), True)

  output.reset()