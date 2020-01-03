
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
            <a href="#" class="brand-logo">Home</a>
            <ul id="nav-mobile" class="right hide-on-med-and-down">
                <li><a href="modelA.php">Model-A</a></li>
                <li><a href="modelB.php">Model-B</a></li>
                <li><a href="download.html">Download</a></li>
               <!-- <li><a href="badgesA.html">About Project</a></li> -->
            </ul>
        </div>
    </nav>
    <div >
				<h1>Next Word Prediction</h1>
                  <blockquote align="left">Application predicts next word to enter based on the already entered words.
                         It can be uses twitter, blogs and news corpora as a training set.</blockquote>
                  <blockquote align="left">It calculates how many times each word from the training set appears in the training set. 
                            After that it builds sequences of two words, 3 words, etc, up to 5 words and calculates how often each sequence 
                               appears in the text.</blockquote>
                  <blockquote align="left">When that is done, application builds predictive model using Long Short Term Memory , 
                               calculating probabilities of every word and every sequence. 
                               </blockquote>
                  <blockquote align="left">When user enters the text in the input field, application takes the input and searches among the previously built sequences to find those, 
								where input is a subsequence. Then it just picks the one with the highest probability and displays to user the tail of the sequence.
								</blockquote>
                </div>
</body>
</html>