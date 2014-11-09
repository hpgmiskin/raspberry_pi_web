import urllib.request as request


def getPublicIP():

	responce = request.urlopen("http://ipecho.net/plain")
	html = responce.read()

	return html.decode("utf-8")

if __name__ == "__main__":
	publicIP = getPublicIP()
