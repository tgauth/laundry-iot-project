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
    <p>Status: <span id="washerStatus"><?php echo isset($_POST['dryer_status']) ? htmlspecialchars($_POST['dryer_status']) : "I'm Broken"; ?></span></span></p>

    <h2>Dryer</h2>
    <p>Status: <span id="dryerStatus"><?php echo "Coming Soon"; ?></span></p>

</body>
</html>
