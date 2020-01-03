
<html>
<head>
    <title>Text Prediction</title>
    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    <style>
        .center1 {
            padding: 10% 30%;
            text-align: center;
        }

        ::placeholder {
            text-align: center;
        }
    </style>
</head>

<body>
    <nav class="black">
        <div class="nav-wrapper">
            <a href="home.php" class="brand-logo">Text Prediction</a>
            <ul id="nav-mobile" class="right hide-on-med-and-down">
                <li><a href="download.html">Download</a></li>
               <!-- <li><a href="collapsible.html">About Project</a></li>-->
            </ul>
        </div>
    </nav>
<form action="pre.php" method="POST">
    <div class="center1">
        <div class="input-field col s10">
        <?php $msg="";
            if (isset($_POST['original_text'])) {$msg=$_POST['original_text'];}
            ?>
            <input placeholder="Enter Input" type="text" name="input_text" id="input_text" value="<?php echo $msg;?>">
            <input type="submit" value="predict">
        </div>
        <div class="input-field col s7">
            <?php $msg1="";$msg2="";$msg3="";
            if (isset($_POST['result_text1']))
            {
                $msg1=$_POST['result_text1'];
                $msg2=$_POST['result_text2'];
                $msg3=$_POST['result_text3'];
            }
            ?>
            <input placeholder="Output will be shown here" type="text" id="tb2" value="<?php echo $msg1;?>"/>
            <input placeholder="Output will be shown here" type="text" id="tb3" value="<?php echo $msg2;?>"/>
            <input placeholder="Output will be shown here" type="text" id="tb4" value="<?php echo $msg3;?>"/>
            <input type="hidden" name="response_filename" id="response_filename" value="<?php echo basename($_SERVER['PHP_SELF']);?>" />
        </div>
    </div>
</form>
</body>

</html>