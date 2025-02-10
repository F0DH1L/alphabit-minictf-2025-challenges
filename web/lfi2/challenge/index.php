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
    <title>LFI Level 2</title>
</head>
<body>
<br /><br />
    <div class="container">
        <h1 id="h1">hello again, hacker !!!</h1>
        <hr />
        <h2 id="challenge">Can you explore my colors directory?</h2>
        <hr />
        <u><b>Challenge</b></u>
        <pre>Select a color of your choice: red, blue, or find something hidden! </pre>
        <p><b>HINT:</b> Use the <code>color</code> parameter to explore the <code>colors</code> directory.</p>
        <p><b>Note:</b> Approved paths only! I'll block any illegal ones. 😉</p>
        <hr />
        <p>
            <?php
                error_reporting(0);
                ini_set('display_errors', 0);

                if (isset($_GET['color'])) {
                    echo "<u><b>Look Here !!!</b></u> <br />";

                    # Remove dangerous traversal attempts
                    $color = str_replace("../", "", $_GET['color']);

                    if ($_GET['color'] == "red"){
                        # include a file in place of the text !
                        include("red.php");   
                    }
                    elseif ($_GET['color'] == "blue"){
                        # include a file in place of the text !
                        include("blue.php");}

                    # The only way to bypass is using `./colors/..././..././..././..././etc/passwd`
                    elseif ($_GET['color']== "./colors/..././..././..././..././etc/passwd") {
                        echo "&#127881; Hooray you made it! &#127881; <br />";
                        echo "The flag is: Alphabit{u_sill_b4by_f0r_m3_until_us0lveit}";
                        include($_GET['color']);
                
                    } else {
                        echo "Invalid file!";
                    }
                }
            ?>
        </p>
    </div>
</body>
</html>
