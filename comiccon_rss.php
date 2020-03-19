<?php
	header("Content-type:text/xml");	
	$feed = file_get_contents("comiccon.xml");
	echo $feed;
?>
