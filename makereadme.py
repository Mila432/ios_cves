# -*- coding: utf-8 -*-
import os
import re
import sys
import io

def save(d,f):
	with io.open(f, 'a', encoding='utf8') as the_file:
		the_file.write('%s\n'%(unicode(d)))

def makeone(folder):
	print 'readme for %s'%(folder)
	files=[]
	for f in os.listdir(folder):
		if '.txt' not in f:	continue
		files.append(f.replace('.txt',''))
	files.sort(key=lambda s: map(int, s.split('.')))
	print files
	save('# iOS %s CVE Overview\n'%(folder.replace('iOS','')),'%s/README.md'%(folder))
	for f in files:
		fixed=set([])
		with open('%s/%s.txt'%(folder,f)) as fi:
			for l in fi.readlines():
				l=l.rstrip()
				fixed.add(l)
		save('With the release of **iOS %s**, a total of %s %s where fixed.\n\n**CVEs**: %s'%(f,len(fixed),'bugs'if len(fixed)>1 else 'bug',', '.join(['`%s`'%(x) for x in sorted(fixed)])),'%s/README.md'%(folder))
		save('\n\n','%s/README.md'%(folder))

if __name__ == "__main__":
	for f in os.listdir('.'):
		if 'iOS' in f:	makeone(f)