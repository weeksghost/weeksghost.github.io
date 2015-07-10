import os
import time

path = os.getcwd() + '/_posts/'
namefile = raw_input('Enter post title: ')
timestr = time.strftime('%Y-%m-%d')
filename = '{}-{}.md'.format(timestr, namefile)

postitem = open(filename, 'w+')
