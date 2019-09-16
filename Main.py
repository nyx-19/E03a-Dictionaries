
if __name__ == '__main__':
	
	birthdays = {
		'Courtney Young': 'June 26',
		'Sarah Lamb': 'November 23',
		'Ilsa Shaikh': 'March 18',
		'Kevin Morton': 'June 17' }
		
	print('This is my tiny library of my friends\' birthdays! The birthdays we have on record are:')
	for name in birthdays:
		print (name)

	print('Who\'s bithday would you like to know?')
	name = input()
	if name in birthdays:
		print('{}\'s birthday is {}.' .format(name, birthdays[name]))
	else:
		print('Sorry, but that person is not in my Library.'.format (name))