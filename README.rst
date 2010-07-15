Presentoh - King of Presentations
=================================

Introduction
------------

I made this simple, and very unpolished, tool because I had one major problem. That problem was that all presentation tools including Powerpoint, Google Docs, etc. all handle video in a horrible fashion. I realized that because of the new video tag, I could make a presentation in HTML5 which handled video awesomely.

The only other major requirement I had was that this slide show worked with my Logitech Cordless Presenter. By including the jQuery hotkeys for changing slides, that requirement has been met.

Usage
-----

There are three steps required to make a presentation in Presentoh. The first step is to load your media. Put all video files into the video folder and all image files into the img folder. 

NOTE: Because of all the bullshit surrounding HTML5 video codecs, make sure you make all of your videos the same format. For my presentations I made sure all of my videos were in H.264 format with a file extension of mp4. The presentations worked perfectly in Chrome and Safari. I have not tried using Ogg to test in Firefox. Since you are making a presentation for yourself, and not for the world, this is not an issue. Pick a video codec, and use the browser that goes with it.

The next step is to build the slideshow in json. There is an example.json file provided. Basically, there are only four kinds of slides, because that's how I like my presentations. 

* Title slides - One big headline in the middle of the page.
* Video slides - Full Screen video that auto plays when the slide starts.
* Image slides - Full Screen image
* List slides - Bulleted list with a header

You can also specify in the json file which keys you would like to use to control moving the slides forward and backward. Be careful with using the mouse combined with video slides. If you try to click to control the video, you will probably advance the slide unintentionally. See the js/jquery.hotkeys.js for details on which keys are available for binding.

There are examples of each kind of slide in the example.json file. 

The last step is to build the presentation. 

    python presentoh.py yourslides.json output_directory

Make sure that output_directory does not exist when you run this command. presentoh will create all the necessary directory and copy all of the necessary html, css, js, images, and videos into it. The resulting directory is 100% portable. It can be moved to a USB stick, zipped up, or whatever. Just open the HTML file for the desired slide in your browser, and you are good to go.

OPTIONAL: If you want to customize the design and/or layout of the slides you will want to look at the template.html file and also the css/presentation.css file. If you know HTML and CSS, it should be self explanatory what is going on.

NOTE: For security reasons, no web browser will actually allow full screen images or videos to be forced on the user. Therefore, I can not automatically make a video or imaeg truly full screen on any slide. Instead I did the next best thing. There is a file maxsize.js. It will automatically take any video or image, calculate the aspect ratio, then make it as large as possible in the current browser window without having any scroll bars appearing, and without changing the aspect ratio of the media.

Test photo by Per Ola Wiberg via Flickr
http://www.flickr.com/photos/powi/2738544608/

Test video taken by me, Scott Rubin, on my iPhone 4.

This project includes two other python modules:

* simplejson - http://code.google.com/p/simplejson/
* jinja2 - http://jinja.pocoo.org/2/
