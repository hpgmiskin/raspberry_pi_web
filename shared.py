#Shared Code

def loadFile(filename):
	"load a file with the given filename"

	try:
		with open(filename,'r') as openFile:
			content = openFile.read()
	except FileNotFoundError:
		content = ""
		saveFile(filename,content)

	return content

def saveFile(filename,content):
	"Save a file with the given filename and content"

	with open(filename,"w") as openFile:
		openFile.write(content)