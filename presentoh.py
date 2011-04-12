#!/usr/bin/env python

import os, sys, errno, shutil

CURRENT_DIR = os.path.dirname(__file__)
UTIL_ROOT = os.path.join(CURRENT_DIR, 'utils')
sys.path.insert(0, UTIL_ROOT)

import simplejson as json

# create output dir(s) if necessary
try:
    output_dir = sys.argv[2]
except IndexError:
    output_dir = os.path.join(CURRENT_DIR, 'example')
if os.path.isdir(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)
os.makedirs("%s/video" % output_dir)
os.makedirs("%s/img" % output_dir)

# move all css and js
src, dest = "css", "%s/css" % output_dir 
shutil.copytree(src, dest)
src, dest = "js", "%s/js" % output_dir 
shutil.copytree(src, dest)

# parse json
try:
    json_filename = sys.argv[1]
except IndexError:
    json_filename = 'example.json'
json_file = open(json_filename)
data = json.load(json_file)

presentation_title = data['presentation_title']
forward_keys = data['forward_keys']
back_keys = data['back_keys']

from jinja2 import Template
template_text = open('template.html').read()
template = Template(template_text)

num_slides = len(data['slides'])
for index, slide in enumerate(data['slides']):
    if index > 0:
        prev = index - 1
        slide['prev'] = "%s" % prev
    if (index + 1) < num_slides:
        next = index + 1
        slide['next'] = "%s" % next
    slide['name'] = "%s" % index 

    slide_name = "%s/%s.html" % (output_dir, slide['name'])
    f = open(slide_name, 'w+')
    context = {
        'presentation_title': presentation_title,
        'forward_keys': forward_keys,
        'back_keys': back_keys,
        'slide': slide,
    }
    context[slide['type']] = True

    if slide['type'] == 'video':
        src = "video/%s" % slide['video_name']
        dest = "%s/video" % output_dir
        shutil.copy(src, dest)
    if slide['type'] == 'image':
        src = "img/%s" % slide['image_name']
        dest = "%s/img" % output_dir
        shutil.copy(src, dest)

    rendered_template = template.render(context)
    f.write(rendered_template)
    f.close()
