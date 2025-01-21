<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Washer and Dryer Status Page</title>
</head>
<body>
    <h2>Washer Status:</h2>
    <p><span id="washerStatus">
    <pre>
    <?php
    // Path to the file
    $file_path = 'washer_data.txt';

    // Check if the file exists
    if (file_exists($file_path)) {
        // Read the contents of the file
        $file_contents = file_get_contents($file_path);

        // Display the contents
        echo htmlspecialchars($file_contents);
    } else {
        echo 'File not found!';
    }
    ?>
    </pre>
    </span></p>

    <h2>Dryer Status:</h2>
    <p>*not quite working - isn't sensitive enough to detect the full cycle *</p>
    <p><span id="dryer_status">
    <pre>
    <?php
    // Path to the file
    $file_path = 'dryer_data.txt';

    // Check if the file exists
    if (file_exists($file_path)) {
        // Read the contents of the file
        $file_contents = file_get_contents($file_path);

        // Display the contents
        echo htmlspecialchars($file_contents);
    } else {
        echo 'File not found!';
    }
    ?>
    </pre>
    </span></p>

</body>
</html>
