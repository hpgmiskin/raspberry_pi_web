import time
import urllib.request as request
from dropboxAPI import DropboxAPI
from shared import *

def getPublicIP():

	responce = request.urlopen("http://ipecho.net/plain")
	html = responce.read()

	return html.decode("utf-8")

def updatePublicIP():
	"Single function to update the public IP of the Pi"

	filename = "public-ip.txt"
	dropboxAPI = DropboxAPI()

	publicIP = getPublicIP()
	saveFile(filename,publicIP)
	dropboxAPI.saveFile(filename)


def loopUpdatePublicIP():
	"Inifnite loop to keep the public ip up to date"

	maxTime = 24
	maxTime = 24*60*60
	sleepTime = 20		#minutes
	sleepTime *= 60 	#seconds
	totalTime = 0

	filename = "public-ip.txt"
	dropboxAPI = DropboxAPI()

	while (totalTime < maxTime):
		publicIP = getPublicIP()
		saveFile(filename,publicIP)
		dropboxAPI.saveFile(filename)

		time.sleep(sleepTime)
		totalTime += sleepTime

if __name__ == "__main__":
	updatePublicIP()
