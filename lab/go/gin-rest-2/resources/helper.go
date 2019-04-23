package resources

import (
	"strconv"

	"github.com/datalayer/datalayer/lab/go/gin-rest-2/models"
	"github.com/gin-gonic/gin"
	log "github.com/sirupsen/logrus"
)

func getIntParam(c *gin.Context, name string) (int64, error) {
	idStr := c.Params.ByName(name)
	id, err := strconv.ParseInt(idStr, 10, 64)
	if err != nil {
		log.Error(err)
		return 0, err
	}
	return id, nil
}

func getStringParam(c *gin.Context, name string) (string, error) {
	return c.Params.ByName(name), nil
}

func getCurrentUser(c *gin.Context) models.User {
	return c.MustGet("user").(models.User)
}
