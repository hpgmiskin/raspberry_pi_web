# Include the Dropbox SDK
import dropbox
from shared import *
from secret import ACCESS_TOKEN

class DropboxAPI():
	"""Class for communication with Dropbox"""

	def __init__(self):
		self.client = dropbox.client.DropboxClient(ACCESS_TOKEN)

	def saveFile(self,filename):
		"method to save the given content with the given filename to dropbox"

		with open(filename,"rb") as localFile:
			response = self.client.put_file("/{}".format(filename),localFile,overwrite=True)

		self.saveLog(response)
		
	def loadFile(self,filename):
		"method to load a file to local with the given filename"

		remoteFile,metadata = self.client.get_file_and_metadata("/{}".format(filename))
		with open(filename,"wb") as localFile:
			localFile.write(remoteFile.read())

		self.saveLog(response)

	def saveLog(self,logData):
		"method to update the log file"

		logFilename = "dropbox-log.txt"

		log = "File: {} - {}".format(logData['path'],logData['client_mtime'])

		fullLog = loadFile(logFilename)
		fullLog += log + "\n"

		#print(log)
		saveFile(logFilename,fullLog)

if __name__ == "__main__":
	dropboxAPI = DropboxAPI()
	dropboxAPI.saveFile("requirements.txt")