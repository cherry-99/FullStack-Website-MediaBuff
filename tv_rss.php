<?php
	header("Content-type:text/xml");	
	$feed = file_get_contents("tv.xml");
	echo $feed;
?>
