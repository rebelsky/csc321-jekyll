#!/usr/bin/env python

import os
import re
import subprocess
import sys

def convert_file(filename):
  f = open(filename)
  file_contents = f.read()
  f.close()
  
  (empty, frontmatter, html_content) = file_contents.split('---', 2)
  
  p = subprocess.Popen(['pandoc', '--from=html', '--to=markdown_github', '--atx-headers'],
                       stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  markdown_content, err = p.communicate(html_content)
  
  markdown_content = re.sub(r'-{5,}\n\n', '', markdown_content)
  markdown_content = re.sub(r'</?(div|span)[^>]*>', '', markdown_content)
  markdown_content = re.sub(r'``` programlisting', '```', markdown_content)
  markdown_content = re.sub(r'``` screen', '```', markdown_content)
  markdown_content = re.sub(r'\[\]\(\)', '', markdown_content)
  markdown_content = re.sub(r'`\*? \*`', ' ', markdown_content)
  markdown_content = re.sub(r'`\*\)', ')`{:.signature}', markdown_content)
  markdown_content = re.sub(r'`\*? ... \*`', ' ... ', markdown_content)
  markdown_content = re.sub(r'`\*? ...\)', ' ...)`{:.signature}', markdown_content)
  
  name, ext = filename.rsplit('.', 1)
  output_filename = name+'.md'
  
  os.system('git mv '+filename+' '+output_filename)
  
  f = open(output_filename, 'w')
  f.write('---'+frontmatter+'---\n'+markdown_content)
  f.close()

for filename in sys.argv[1:]:
  print 'Converting', filename
  convert_file(filename)
