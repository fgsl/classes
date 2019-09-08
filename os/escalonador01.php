<?php
define('SOURCE',__DIR__ . "/processos");
$files = scandir(SOURCE);
unset($files[0]);
unset($files[1]);
foreach($files as $file){
	echo "Executando processo $file...\n";
        $handle = fopen(SOURCE . "/$file",'r');
        while (!feof($handle)){
            $instruction = fgets($handle,6);
            if (!empty(trim($instruction))) {
	            echo "Executando instrução " . $instruction . "\n";
	    }
        }
        fclose($handle);
}
