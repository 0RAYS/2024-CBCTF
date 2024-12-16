<?php

// easy unserialize chain OuO

class notes{
    function __construct($filepath){
        readfile($filepath);
    }
}

// flag in /flag , let's go !!

class _0rays{
    public $jbn;
    public $pankas;
    function __wakeup(){
        if(call_user_func($this -> jbn)){
            throw new Exception($this -> pankas);
        }else{
            echo "ha?";
        }
    }
}

class lets{
    public static $yolbby = "nonono";
    public $mak4r1;
    public $ech0;
    public $rocket;
    public $errmis;
    function __toString(){
        $humb1e = md5($this -> mak4r1);
        $k0rian = substr($humb1e,-4,-1);
        $this -> rocket -> dbg = $k0rian;
        return "O.o?";
    }
    function __set($a, $b){
        self::$yolbby = $b;
        $int_barbituric = $this -> ech0 -> gtg;

    }

    function __invoke(){
        new notes($this -> errmis);
    }

}

class go{
    public $ed_xinhu;

    function __get($c){
        if(lets::$yolbby === "666"){
            $dilvey = $this -> ed_xinhu;
            return $dilvey();
        }else{
            echo "you are going to win !";
        }
    }

}


function check($filePath) {
    if(!file_exists($filePath)){
        return false;
    }
    $realPath = realpath($filePath);
    if (strpos($realPath, '/notes') === 0 ) {
        return true;
    }
    return false; 
}

function listnote() {
    $directory = '/notes'; 
    $files = array_filter(scandir($directory), function ($file) use ($directory) {
        return is_file("$directory/$file");
    });
    foreach ($files as $f) {
        $link = '<a href="/index.php?note=/notes/' . htmlspecialchars($f) . '">' . htmlspecialchars($f) . '</a> <p></p>';
        echo $link;
    }
    echo '<a href="/index.php?note=show-me-source">show source</a>';
}

// upload your own note ? (under development)
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $file = $_FILES['user_note'] ?? null;
    if ($file && strtolower(pathinfo($file['name'], PATHINFO_EXTENSION)) === 'txt') {
        $randomFileName = uniqid() . '.txt';
        $targetFilePath = "/notes/" . $randomFileName;
        if (move_uploaded_file($file['tmp_name'], $targetFilePath)) {
            echo "Your note successfully saved in :".$targetFilePath;
            exit;
        }
    }
    die("error");   
}

$note = @$_GET['note'];
if($note){
    if($note === "show-me-source"){
        highlight_file(__FILE__);
    }else{
        if(check($note)){
            header('Content-Type: text/plain; charset=UTF-8');
            new notes($note);
        }else{
            die("hacker...");
        }
    }
}else{
    echo "<h1>这里是mak自己悄悄留给你的一些笔记哦，打开看看吧</h1>";
    echo "<h2>Notes List:<h2>";
    listnote();
}


