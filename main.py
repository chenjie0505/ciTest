import json
import ssl
import urllib.request
def loadData():
	i = 1
	total = 1000
	while i*100<total+100:
		issues_url = 'https://api.github.com/search/issues?q=language:python+label:performance+state:closed+created:2019-01-01..2019-02-01&sort=created&order=asc&page=%s&per_page=100'%(i)
		issues = readURL(issues_url)
		issues = issues and json.loads(issues)
		total = issues['total_count']
		if not issues:
			print ('   no issue obtained with performance at page%s'%i)
		else:
			print ('   getting  %s/%s, %s '%(i, total,len(issues['items'])))
		i = i + 1


def readURL(url):
	ssl._create_default_https_context = ssl._create_unverified_context
	response = urllib.request.urlopen(url)
	content = response.read()
	return content
