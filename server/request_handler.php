<?php
$post_data = file_get_contents("php://input"); //as you send data as raw json

if ($post_data) { // post from RPi sensor script
    $json_data = json_encode($post_data);
    if (file_put_contents("data.txt", $json_data)) {
        echo "Ok";
    } else {
        http_response_code(400); // data did not save
        echo "Bad Request";
    }
} else { // web app make a call to the request handler
    $previous_data = file_get_contents("data.txt");
    echo $previous_data;
}
