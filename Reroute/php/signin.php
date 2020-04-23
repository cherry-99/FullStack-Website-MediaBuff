<?php
//    $host        = "host = localhost";
//    $port        = "port = 5432";
//    $dbname      = "dbname = project";
//    $credentials = "user = postgres";

   $db = pg_connect("host=127.0.0.1 port=5432 dbname=project");
   if(!$db) {
      echo "Error : Unable to open database\n";
   } else {
      echo "Opened database successfully\n";
   }

   $sql =<<<EOF
      SELECT * from USERS;
EOF;

   $ret = pg_query($db, $sql);
   if(!$ret) {
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