<?php
$start = microtime(true);

function fibonacci($n) {
   if ($n == 1 || $n == 2) 
   {
       return 1; 
   }
   return fibonacci($n-1) + fibonacci($n-2);
}

echo fibonacci((int)$argv[1]) . "\n";

echo 'Time: ' . ((microtime(true) - $start) * 1000000) . "\n";
