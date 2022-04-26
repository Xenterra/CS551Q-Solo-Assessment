from django.db import models

# Create your models here.
class gameList(models.Model):
	gameID = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	price = models.IntegerField(max_length=6)
	ageRating = models.CharField(max_length=4)
	primaryGenre = models.CharField(max_length=20)

	class Meta:
		db_table = "gamelist"

class gameDetails(models.Model):
	uniqueid = models.IntegerField(primary_key=True)
	gameID = models.IntegerField(max_length=10)
	appURL = models.Field(max_length=1000)
	subtitle = models.Field(max_length=50)
	iconURL = models.Field(max_length=1000)
	averageUserRating = models.CharField(max_length=3)
	numberOfRating = models.IntegerField(max_length=7)
	inAppPurchases = models.CharField(max_length=10)
	description = models.CharField()
	developer = models.CharField(max_length=30)
	languages = models.CharField(max_length=30)
	size = models.IntegerField(max_length=10)
	genres = models.CharField(max_length=30)
	originalReleaseDate = models.DateField()
	CurrentVersionReleaseDate = models.DateField()


	class Meta:
		db_table = "gamedetails"