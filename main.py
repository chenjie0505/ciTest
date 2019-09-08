import json
i = 1
while i*100<total+100:
  issues_url = 'https://api.github.com/search/issues?q=language:python+label:performance+state:closed+created:2019-01-01..2019-02-01&sort=created&order=asc&page=%s&per_page=100&access_token=dbba492f97f0f694f5667a48a3888d46f7d8e6ea'%(i)
  issues = readURL(issues_url)
  issues = issues and json.loads(issues)
  if not issues:
	  print '   no issue obtained with performance at page%s'%i
	else:
	  print '   getting  %s/%s, %s '%(i, total,len(issues['items']))
  i = i + 1
  
  
def readURL(url):
  response = urllib.urlopen(url)
	content = response.read()
	return content
