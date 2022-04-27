import csv
import os
from pathlib import Path
from django.db import models
from shopApp.models import gameList, gameDetails
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
	help = 'Load data from csv'
	def handle(self, *args, **options):
		gameList.objects.all().delete()
		gameDetails.objects.all().delete()

		# Refill the model database
		with open('appstore_games.csv', newline='') as f:
			count = 0;
			reader = csv.reader(f, delimiter=",")
			next(reader) # skip the header line
			for row in reader:
				count += 1;
				if row[0] != '':
					gList = gameList.objects.create(
					gameID = row[1],
					gameName = row[2],
					price = row[7],
					ageRating = row[11],
					primaryGenre = row[14],
					)
					gList.save()
				print("Completed Row "+str(count)+":",row[2])
			print("Game List Complete")

		with open('appstore_games.csv', newline='') as f:
			reader = csv.reader(f, delimiter=",")
			count = 0;
			next(reader) # skip the header line
			for row in reader:
				count += 1;
				if row[0] != '':
					gdList = gameDetails.objects.create(
					uniqueid = count,
					gameID = row[1],
					appURL = row[0],
					subtitle = row[3],
					iconURL = row[4],
					averageUserRating = row[5],
					numberOfRating = row[6],
					inAppPurchases = row[8],
					description = row[9],
					developer = row[10],
					languages = row[12],
					size = row[13],
					genres = row[15],
					originalReleaseDate = row[16],
					CurrentVersionReleaseDate = row[17],
					)
					gdList.save()
				print("Completed Row "+str(count)+":",row[1],row[2],row[13])
			print("Details List Complete")