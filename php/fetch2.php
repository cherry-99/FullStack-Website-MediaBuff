<?php
    header('Content-Type:application/json');
	extract($_GET);
    $res;
    $res2;
	$file=fopen("Final.csv","r");
	while(!feof($file)){
		$line=fgetcsv($file);
		if(isset($line[8]) && strncasecmp($line[8],$term,strlen($term))==0){
			$res=$line; // $res has the row from the CSV containing the all the required details pertaining to the movie.
		}	
    }

    // This loop is for reading the posters_locations.csv and fetching the image.
    $file2=fopen("poster_locations.csv","r");
	while(!feof($file2)){
		$line2=fgetcsv($file2);
		if(isset($line2[0]) && strncasecmp($line2[0],$term,strlen($term))==0){
			$res2=$line2; // $res has the row from the CSV containing the all the required details pertaining to the movie.
		}	
    }
    // echo $res2[1];

    // Fetching the details and putting them in appropriate variables.
    $movie_color = $res[1];
    $movie_director = $res[2];
    $movie_duration = $res[3];
    $movie_actor1 = $res[4];
    $movie_gross_income = $res[5];
    $movie_genre = $res[6];
    $movie_actor2 =$res[7];
    $movie_name = $res[8];
    $movie_actor3 = $res[10];
    $movie_IMDB = $res[13];
    $movie_language = $res[15];
    $movie_PEGI = $res[17];
    $movie_rating = $res[20];
    $movie_poster = $res2[1];

    // Name of the template file.
    $template_file = 'movie_template.php';

    // Posted data.
    $data['movie_name'] = $movie_name;
    $data['movie_director'] = $movie_director;
    $data['movie_duration'] = $movie_duration;
    $data['movie_actor1'] = $movie_actor1;
    $data['movie_actor2'] = $movie_actor2;
    $data['movie_actor3'] = $movie_actor3;
    $data['movie_gross_income'] = $movie_gross_income;
    $data['movie_genre'] = $movie_genre;
    $data['movie_PEGI'] = $movie_PEGI;
    $data['movie_rating'] = $movie_rating;
    $data['movie_IMDB'] = $movie_IMDB;
    $data['poster_location'] = $movie_poster;

    // Data array (Should match with data above's order).
    $placeholders = array("movie_name", "movie_director", "movie_duration", "movie_actor1","movie_actor2","movie_actor3","movie_gross_income","movie_genre","movie_PEGI","movie_rating","movie_IMDB","poster_location");
    // Get the movie_template.php as a string.
    $template = file_get_contents($template_file);

    // Fills the template.
    $new_file = str_replace($placeholders, $data, $template);
    echo $new_file;

    // Save file
    //$fp = fopen("/Users/chiragtubakad/.bitnami/stackman/machines/xampp/volumes/root/htdocs/FullStack-Website-MediaBuff/dynamic.html", "w");
    $fp = fopen("dynamic.html", "w");
    fwrite($fp, $new_file);
    fclose($fp);
?>