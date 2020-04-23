<?php
	header('Content-Type:application/json');
	extract($_GET);
	$res=array();
	$file=fopen("Final.csv","r");
	while(!feof($file)){
		$line=fgetcsv($file);
		if(isset($line[8]) && strncasecmp($line[8],$term,strlen($term))==0){
			$res[]=$line[8];
		}	
	}
	echo json_encode($res);
?>
	
	