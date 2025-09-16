<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Assignment 2</title>
</head>

<body>
    <h2>Insert the values</h2>

    <form action="index.php" method="get">
        <label for="a">Value for a:</label>
        <input type="number" step="any" id="a" name="a" required
            value="<?php echo isset($_GET['a']) ? htmlspecialchars($_GET['a']) : ''; ?>">
        <br><br>
        <label for="b">Value for b:</label>
        <input type="number" step="any" id="b" name="b" required
            value="<?php echo isset($_GET['b']) ? htmlspecialchars($_GET['b']) : ''; ?>">
        <br><br>
        <label for="c">Value for c:</label>
        <input type="number" step="any" id="c" name="c" required
            value="<?php echo isset($_GET['c']) ? htmlspecialchars($_GET['c']) : ''; ?>">
        <br><br>
        <input type="submit" value="Calculate">
    </form>

    <hr>

    <?php
    if (isset($_GET['a']) && isset($_GET['b']) && isset($_GET['c'])) {
        $queryString = http_build_query([
            'a' => $_GET['a'],
            'b' => $_GET['b'],
            'c' => $_GET['c']
        ]);

        $command = "QUERY_STRING=" . escapeshellarg($queryString) .
            " python3 " . escapeshellarg("/var/www/html/assignment_2/calculate.py");

        $output = shell_exec($command);

        echo "<h2>Calculation Result:</h2>";
        echo "<pre style='font-family: monospace; font-size: 16px;'>$output</pre>";
    }
    ?>
</body>

</html>