<!DOCTYPE html>
<html lang="en">
<head>
    <script>
      function updateData() {
        const xhr = new XMLHttpRequest();
        xhr.open("GET", "http://rpi-laundry:80/request_handler.php");
        xhr.onreadystatechange = function() {
          if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
              const data = JSON.parse(xhr.responseText);
              document.getElementById("dryer_status").innerHTML = data.dryer_status;
            } else {
              console.error(xhr.statusText);
            }
          }
        };
        xhr.send();
      }
      setInterval(updateData, 1000);
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Washer and Dryer Status Page</title>
</head>
<body>
    <p><?php echo date('Y-m-d H:i:s'); ?></p>

    <h2>Washer</h2>
    <p>Status: <span id="washerStatus"><?php echo "Coming Soon"; ?></span></span></p>

    <h2>Dryer</h2>
    <p>Status: <span id="dryer_status">&#8451;</span></p>

</body>
</html>
