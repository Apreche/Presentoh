#!/usr/bin/env python

import os, sys

UTIL_ROOT = os.path.join(os.path.dirname(__file__), 'utils')
sys.path.insert(0, UTIL_ROOT)

import simplejson as json

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
    slide_name = "slides/%s.html" % slide['name']
    f = open(slide_name, 'w')
    context = {
        'presentation_title': presentation_title,
        'forward_keys': forward_keys,
        'back_keys': back_keys,
        'slide': slide,
    }
    context[slide['type']] = True
    rendered_template = template.render(context)
    f.write(rendered_template)
    f.close()