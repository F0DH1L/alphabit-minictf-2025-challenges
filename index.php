<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
      integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="main.css" />
    <title>LFI </title>
</head>
<body>
<br /><br />
    <div class="container">
        <h1 id="h1">hello sir !!!</h1>
        <hr />
        <h2 id="challenge">I have 2 colors !</h2>
        <hr />
        <u><b>Challenge</b></u>
        <pre>Please Select a color of your choice : red/blue </pre>
        <p><b>HINT :</b> use the <code>color  parameter </code> :)</p>
        <hr />
        <p>
            <?php
                error_reporting(0);
                ini_set('display_errors', 0);
                if (isset($_GET['color'])) {
                    echo "<u><b>Look Here !!!</b></u> <br />" ;

                    if ($_GET['color'] == "red"){
                        # include a file in place of the text !
                        include("red.php");   
                    }
                    elseif ($_GET['color'] == "blue"){
                        # include a file in place of the text !
                        include("blue.php");
                    }
                    else {
                        if ($_GET['color'] == "../../../etc/passwd"){
                            echo "&#127881; Hooray you made it ! &#127881;";
                            echo "<br />";
                            echo "the flag is : Alphabit{b4by_lf1_f0r_0ur_n3wb4bi3s1}
";
                                                }  
                        include($_GET['color']);
                    }
                    
                }

            ?>
        </p>
    </div>
</body>
</html>