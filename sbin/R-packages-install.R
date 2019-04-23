#!/usr/bin/env Rscript

# Licensed to Datalayer (https://datalayer.io) under one or more
# contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. Datalayer licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

install.packages("roxygen2", repos = "http://cran.us.r-project.org") # For Spark

install.packages("ggplot2", repos = "http://cran.us.r-project.org")
install.packages("knitr", repos = "http://cran.us.r-project.org")
install.packages("glmnet", repos = "http://cran.us.r-project.org")
install.packages("pROC", repos = "http://cran.us.r-project.org")
install.packages("data.table", repos = "http://cran.us.r-project.org")
install.packages("caret", repos = "http://cran.us.r-project.org")
install.packages("sqldf", repos = "http://cran.us.r-project.org")
install.packages("wordcloud", repos = "http://cran.us.r-project.org")
install.packages("RColorBrewer", repos = "http://cran.us.r-project.org")
install.packages("googleVis", repos = "http://cran.us.r-project.org")
install.packages("networkD3", repos = "http://cran.us.r-project.org")
install.packages("dygraphs", repos = "http://cran.us.r-project.org")
install.packages("scatterplot3d", repos = "http://cran.us.r-project.org")
# install.packages("rCharts", repos = "http://cran.us.r-project.org")
install.packages("devtools", repos = "http://cran.us.r-project.org")
install.packages("Rcpp", repos = "http://cran.us.r-project.org")
library(devtools)
library(Rcpp)
install_github('ramnathv/rCharts', repos = "http://cran.us.r-project.org")
