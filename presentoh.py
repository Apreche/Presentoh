#!/usr/bin/env python

import os, sys, errno, shutil

UTIL_ROOT = os.path.join(os.path.dirname(__file__), 'utils')
sys.path.insert(0, UTIL_ROOT)

import simplejson as json

# create output dir(s) if necessary
output_dir = sys.argv[2]
try:
    os.makedirs(output_dir)
    os.makedirs("%s/video" % output_dir)
    os.makedirs("%s/img" % output_dir)
except OSError as exc:
    if exc.errno == errno.EEXIST:
        pass
    else:
        raise exc

# move all css and js
src, dest = "css", "%s/css" % output_dir 
shutil.copytree(src, dest)
src, dest = "js", "%s/js" % output_dir 
shutil.copytree(src, dest)

# parse json
json_filename = sys.argv[1]
json_file = open(json_filename)
data = json.load(json_file)

presentation_title = data['presentation_title']
forward_keys = data['forward_keys']
back_keys = data['back_keys']

from jinja2 import Template
template_text = open('template.html').read()
template = Template(template_text)

for slide in data['slides']:
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
