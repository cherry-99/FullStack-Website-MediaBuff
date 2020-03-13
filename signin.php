<?php
   extract($_POST);
   $host        = "host = localhost";
   $port        = "port = 5432";
   $dbname      = "dbname = postgres";
   $credentials = "user = postgres password=12345";

   $db = pg_connect("$host $port $dbname");
   if(!$db) {
      echo "Error : Unable to open database\n";
   } else {
      echo "Opened database successfully\n";
   }

   $sql =<<<EOF
      SELECT * from users WHERE email='".$name."' AND password='".$psw."';
EOF;

   $ret = pg_query($db, $sql);
   if(!$ret) {
      // echo "HELLO!";
      echo pg_last_error($db);
      exit;
   } 
   $rows = pg_num_rows($result);
   if($rows > 0 )
   {
    echo "Operation done successfully\n";   
   }
//    while($row = pg_fetch_row($ret)) {
//       echo "ID = ". $row[0] . "\n";
//       echo "NAME = ". $row[1] ."\n";
//       echo "ADDRESS = ". $row[2] ."\n";
//       echo "SALARY =  ".$row[4] ."\n\n";
//    }
   //echo "Operation done successfully\n";
   pg_close($db);
?>