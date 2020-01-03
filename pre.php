<?php
$hi= $_POST["input_text"];
$response_filename=$_POST['response_filename'];

if ($response_filename=="modelA.php"){
    $command="python testA.py "."\"".$hi."\"";
	$out = system($command);
	#echo $command; 
	$str_arr = explode (" ", $out);
	$out1=$str_arr[0]." ".$str_arr[1]." ".$str_arr[2];
	$out2=$str_arr[3]." ".$str_arr[4]." ".$str_arr[5];
	$out3=$str_arr[6]." ".$str_arr[7]." ".$str_arr[8];
}
else{
	$command="python testB.py "."\"".$hi."\"";
	$out = system($command);
	#echo $command; 
	$str_arr = explode ("  ", $out);
	$out1=$str_arr[0];
	$out2=$str_arr[1];
	$out3=$str_arr[2];
}

#$command="python testA.py "."\"".$hi."\"";


?>

<html>
    <head></head>
<body onload="gogo()">
<form action="<?php echo $response_filename;?>" method="POST">
    <input type="hidden" name='result_text1' id='result_text1' value="<?php echo $out1;?>">
    <input type="hidden" name='result_text2' id='result_text2' value="<?php echo $out2;?>">
    <input type="hidden" name='result_text3' id='result_text3' value="<?php echo $out3;?>">
    <input type="hidden" name='original_text' id='original_text' value="<?php echo $hi;?>"> 
    <input type="submit" name="go" value="go" id="go">
</form>
<script>
    document.getElementById("go").click();
</script>
</body>
</html>