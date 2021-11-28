import os, random, hashlib, string
from pathlib import Path

def get_path() -> Path:
    cwd = Path(__file__).parents[1]
    cwd = str(cwd)
    return cwd
def hash(strng) -> str:
	return hashlib.sha1(strng.encode()).hexdigest()

def generateSeed(info) -> dict:
	return hash(info["site"] + hash("DPMXN?Q23D.D" + info["secret"] + "2DS%*DFXY?XJQAU"))
def pickRandomWord(fileName, seed) -> str:
	cwd = get_path()
	random.seed(seed)

	with open(cwd + f"/Lists/{fileName}.txt", "r") as file:
		allText = file.read()
		words = list(map(str, allText.split()))
		randomWord = random.choice(words).lower().capitalize()

	return randomWord

def generateUsername(seed) -> str:
	return pickRandomWord("Adverbs", seed) + pickRandomWord("Nouns", seed)
def generatePassword(seed) -> str:
	characters = string.punctuation + string.ascii_letters + string.digits
	password = ""

	random.seed(seed)

	for char in range(25):
		rand = random.choice(characters)
		password = password + rand
	
	return password
