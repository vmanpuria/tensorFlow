import os
import re
import scrubadub

dirPath="batch10"
cleanFilePath="batch10/clean/batch10.tsv"

cleanFile=open(cleanFilePath, 'w')

for name in os.listdir(dirPath):
  fileName = dirPath+'/'+name
  if (os.path.isfile(fileName)):
    with open(fileName) as file:
      body=file.read()
      cleanBody=scrubadub.clean(body)
      cleanFile.write('1'+'\t'+re.sub('\s+', ' ', cleanBody)+'\n')

cleanFile.close()
