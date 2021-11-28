from Functions.IOFunctions import inputInformation, outputData
from Functions.Generation import generateSeed, generatePassword, generateUsername

if __name__ == "__main__":
	information = inputInformation()
	randomSeed = generateSeed(information)

	accountData = {
		"username": generateUsername(randomSeed),
		"password": generatePassword(randomSeed)
	}

	outputData(accountData)
