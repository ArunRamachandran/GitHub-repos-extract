import requests
 
def get_git_repos(username):
	new = []
	response = requests.get('https://api.github.com/users/'+username+'/repos')
 
	if response.status_code != 200:
		return new
 
	else:
		for repo in response.json():
			r = format(repo['name'])
			l = format(repo['language'])
			com = [r,l]
			new.append(com)
			#new.append(format(repo['name']repo['language']))
    		return new
		#print '[{}] {}'.format(repo['language'], repo['name'])
	

username = raw_input('Give GitHub UserName : \n')
repos = get_git_repos(username)
if len(repos) == 0:
	print "Give a valid username"
else:
	for repo,lan in repos:
		print repo,'['+lan+']'
		
