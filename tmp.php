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