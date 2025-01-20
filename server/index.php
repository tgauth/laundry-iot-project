<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Washer and Dryer Status Page</title>
</head>
<body>
    <p><?php echo date('Y-m-d H:i:s'); ?></p>

    <h2>Washer</h2>
    <p>Status: <span id="washerStatus"><?php echo "Coming Soon"; ?></span></span></p>

    <h2>Dryer Status:</h2>
    <span id="dryer_status">
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
    </span>

</body>
</html>

