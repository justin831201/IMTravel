

var Billy = screen.width / 1280;
//alert(Billy);

  $(document).ready(function(){
	$(".control").each(function(){
		width = $(this).width() * Billy;
		$(this).css("width", width);
	});
});

  $(document).ready(function(){
	$(".adjust").each(function(){
		$(this).css("left", ($(this).position().left * Billy));
		$(this).css("top", ($(this).offset().top * Billy));
	});
});
