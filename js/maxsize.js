function maxresize(){
	var ww = $(window).width();
	var wh = $(window).height();
	var wa = ww/wh;

	var vw = $('video').width();
	var vh = $('video').height();
	var va = vw/vh;

	if (va > wa){
		$('video').width('95%');
		$('video').height('auto');


	}else{
		$('video').width('auto');
		$('video').height('95%');
	}

	var iw = $('img').width();
	var ih = $('img').height();
	var ia = iw/ih;

	if (ia > wa){
		$('img').width('95%');
		$('img').height('auto');
	}else{
		$('img').width('auto');
		$('img').height('95%');
	}
	$('#debug').html('foo');
}

$(document).ready(function() {
	setTimeout(maxresize, 100);
	$(window).resize(maxresize);

});
