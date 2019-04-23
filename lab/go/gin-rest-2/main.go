package main

import (
	"github.com/datalayer/datalayer/lab/go/gin-api-demo/dao"
	"github.com/datalayer/datalayer/lab/go/gin-api-demo/middleware"
	"github.com/datalayer/datalayer/lab/go/gin-api-demo/resources"
	"github.com/datalayer/datalayer/lab/go/gin-api-demo/util"
	"github.com/gin-gonic/gin"
	log "github.com/sirupsen/logrus"
)

func main() {
	util.LoadEnvVars()
	util.UseJSONLogFormat()

	dao.InitDb()

	gin.SetMode(gin.ReleaseMode)

	r := gin.New()

	r.Use(middleware.JSONLogMiddleware())
	r.Use(gin.Recovery())
	r.Use(middleware.RequestID(middleware.RequestIDOptions{AllowSetting: false}))
	r.Use(middleware.Auth())
	r.Use(middleware.CORS(middleware.CORSOptions{}))

	resources.NewUserResource(r)

	port := util.GetEnv("PORT", "8080")
	log.Info("Service starting on port " + port)

	r.Run(":" + port) // listen and serve
}
