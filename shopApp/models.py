from django.db import models

# Create your models here.
class gameList(models.Model):
	gameID = models.IntegerField(primary_key=True)
	gameName = models.CharField(max_length=30)
	price = models.FloatField()
	ageRating = models.CharField(max_length=4)
	primaryGenre = models.CharField(max_length=20)

	class Meta:
		db_table = "gameList"

class gameDetails(models.Model):
	uniqueid = models.IntegerField(primary_key=True)
	gameID = models.IntegerField()
	appURL = models.CharField(max_length=1000)
	subtitle = models.CharField(max_length=50)
	iconURL = models.CharField(max_length=1000)
	averageUserRating = models.CharField(max_length=3)
	numberOfRating = models.IntegerField()
	inAppPurchases = models.CharField(max_length=10)
	description = models.CharField(max_length=1000)
	developer = models.CharField(max_length=30)
	languages = models.CharField(max_length=30)
	size = models.IntegerField()
	genres = models.CharField(max_length=30)
	originalReleaseDate = models.DateField()
	CurrentVersionReleaseDate = models.DateField()


	class Meta:
		db_table = "gameDetails"