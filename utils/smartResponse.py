import sendText

def smartResponse(to, inputText):
	outputText = "Text to return"
	sendText.sendText(to, outputText)