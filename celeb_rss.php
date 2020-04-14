<?php
	header("Content-type:text/xml");	
	$feed = file_get_contents("celeb.xml");
	echo $feed;
?>
