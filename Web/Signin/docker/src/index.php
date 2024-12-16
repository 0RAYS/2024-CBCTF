<?php
highlight_file(__FILE__);
error_reporting(0);

if(isset($_GET['a']) && isset($_GET['b'])){
    $a = (string) $_GET['a'];
    $b = (string) $_GET['b'];
}else{
    die("welcome to CBCTF2024 :)");
}

if(ctype_print($a) && ctype_print($b)){
    if($a != $b && md5($a) === md5($b)){
        echo "<p>great</p>";
        echo file_get_contents("/flag");
    }else{
        echo "try again";
    }
}else{
    echo "no fastcoll :(";
}

