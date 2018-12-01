while True:

	x = 0

	string = input()
	
	if string == '*':
		break;
	
	string = string.split(" ")
	
	for i in range(len(string) - 1):
		if(string[i][:1].lower() == string[i + 1][:1].lower()):
			x = 1;
		else: 
			x = 0;

	if x == 1:
		print("{}".format("Y"))
	else:
		print("{}".format("N"))