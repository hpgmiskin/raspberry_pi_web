import time
import urllib.request as request
from dropboxAPI import DropboxAPI
from shared import *

def getPublicIP():

	responce = request.urlopen("http://ipecho.net/plain")
	html = responce.read()

	return html.decode("utf-8")

def updatePublicIP():
	"Inifnite loop to keep the public ip up to date"

	sleepTime = 0.5			#hours
	sleepTime *= 60*60	#seconds

	filename = "public-ip.txt"
	dropboxAPI = DropboxAPI()

	while (True):
		publicIP = getPublicIP()
		saveFile(filename,publicIP)
		dropboxAPI.saveFile(filename)

		time.sleep(sleepTime)

if __name__ == "__main__":
	updatePublicIP()
