<?php
	header("Content-type:text/xml");	
	$feed = file_get_contents("movie.xml");
	echo $feed;
?>
