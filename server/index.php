<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple PHP Page with Washer and Dryer</title>
</head>
<body>
    <h1>Welcome to My Simple PHP Page</h1>
    <p><?php echo date('Y-m-d H:i:s'); ?></p>

    <h2>Washer</h2>
    <p>Status: <span id="washerStatus"><?php echo "Not Running"; ?></span></p>

    <h2>Dryer</h2>
    <p>Status: <span id="dryerStatus"><?php echo "Not Running"; ?></span></p>

</body>
</html>
