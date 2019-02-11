# -*- coding: utf-8 -*-
import requests
import re
import io

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

start_page=201347
start_page_max=209520

def save(d,f):
	with io.open(f, 'a', encoding='utf8') as the_file:
		the_file.write('%s\n'%(unicode(d)))

def checkpage(id):
	print 'checking id:%s'%(id)
	r=requests.get('https://support.apple.com/en-us/HT%s'%(id),headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'},verify=False)
	if 'About the security content of iOS' not in r.content:	return None
	ios_version=re.search('of iOS ([0-9\.]*) ',r.content).group(1)
	cves=re.findall('(CVE-[0-9]*-[0-9]*)',r.content)
	print 'CVEs for %s:'%(ios_version)
	for cve in cves:
		print cve
		save(cve,'%s.txt'%(ios_version))

if __name__ == "__main__":
	while(start_page<=start_page_max):
		checkpage(start_page)
		start_page+=1