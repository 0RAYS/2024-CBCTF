<?php

$notes_directory = '/var/www/html'; 

extract($_REQUEST);
if (!isset($file)) {
    echo 'Error: Missing file parameter.';
    exit;
}
if(preg_match('/^[a-z0-9._]+$/', $file)){
    $filePath = $notes_directory . '/' . $file;
}else{
    die("waf!");
}


if (!file_exists($filePath) || !is_file($filePath)) {
    echo 'Error: File not found : '.$filePath;
    exit;
}

header('Content-Type: text/plain; charset=UTF-8');
readfile($filePath);
// flag in /flag
?>
