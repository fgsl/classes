<?php
$insert = 'INSERT INTO oco ('codigo_ocorrencia','ocorrencia_classificacao',...) VALUES ('; 

$handle = fopen('oco.csv','r');
$sql = '';
while (!feof($handle)){
	$registro = fgetcsv($handle);
	$sql .= $insert;
	foreach($registro as $campo){
		$sql .= "'" . $campo . "',";		
	}
	$sql = substr($sql,0,strlen($sql)-1);
	$sql.= ');';
}
fclose($handle);
file_put_contents('oco.sql',$sql);
