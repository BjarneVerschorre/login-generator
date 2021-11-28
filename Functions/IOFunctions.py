def inputInformation() -> dict:
	return {
		"site": input("Site you're using: "),
		"secret": input("Your secret phrase: "),
	}

def outputData(data) -> None:
	print(f"\nYour Account Information:\n * Username: {data['username']}\n * Password: {data['password']}\n")