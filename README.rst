Presentoh - King of Presentations
=================================

Introduction
------------

I made this simple, and very unpolished, tool because I had one major problem. That problem was that every presentation tool out there including Powerpoint, Google Docs, etc. all handled video in a horrible fashion. I realized that because of the new video tag, I could make a presentation in HTML5 which handled video awesomely.

The only other major reuirement I had was that this slide show worked with my Logitech Cordless Presenter. By including the jQuery hotkeys for changing slides, that requirement has been met.

Usage
-----

There are three steps required to make a presentation in Presentoh. The first step is to load your media. Put all video files into the video folder and all image files into the img folder. 

NOTE: Because of all the bullshit surrounding HTML5 video codecs, make sure you make all of your videos the same format. For my presentations I made sure all of my videos were in H.264 format with a file extension of mp4. The presentations worked perfectly in Chrome and Safari. I have not tried using Ogg to test in Firefox.

The next step is to build the slideshow in json. There is an example.json file provided. Basically, there are only four kinds of slides, because that's how I like my presentations. 

* Title slides - One big headline in the middle of the page.
* Video slides - Full Screen video that auto plays when the slide starts.
* Image slides - Full Screen image
* List slides - Bulleted list with a header

You can also specify in the json file which keys you would like to use to control moving the slides forward and backward. Be careful with using the mouse combined with video slides. If you try to click to control the video, you will probably advance the slide unintentionally. See the js/jquery.hotkeys.js for details on which keys are available for binding.

There are examples of each kind of slide in the example.json file. 

The last step is to build the presentation. 

    python presentoh.py yourslides.json

This will build the HTML for all of your slides and the files will appear in the slides folder. Open up the starting slide in your browser, make the browser go full screen, and you're ready to rock and roll.

OPTIONAL: If you want to customize the design and/or layout of the slides you will want to look at the template.html file and also the css/presentation.css file. If you know HTML and CSS, this should be self explanatory what is going on.

Test photo by Per Ola Wiberg via Flickr
http://www.flickr.com/photos/powi/2738544608/

Test video taken by me on my iPhone 4.

This project includes two other python modules:

* simplejson - http://code.google.com/p/simplejson/
* jinja2 - http://jinja.pocoo.org/2/
