<?php
$directory = '/var/www/html'; 

if (!is_dir($directory)) {
    echo json_encode(['error' => 'Directory not found']);
    exit;
}
function endWith($str, $suffix)
{   
    $length = strlen($suffix);
    if ($length == 0) {
        return true;
    }   
    return (substr($str, -$length) === $suffix);
} 
$files = array_filter(scandir($directory), function ($file) use ($directory) {
    if(endWith($file,".txt")){
        return is_file("$directory/$file");
    }
});

header('Content-Type: application/json');
echo json_encode(array_values($files));
?>
