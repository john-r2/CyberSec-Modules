<html><title> Guessing Game, with XSS Flaw </title>
<body>
<h4> I'm thinking of a number between 1 and 10.  Try to guess it.</h4><br>
<?php
$mynumber = 3;

// The first time through, the user will not have entered a guess
// Check to see if there is anything in guess so we don't error out
// Only show right/wrong if guess was entered
if (isset($_GET['guess'])) {
  $guess = $_GET['guess'];

    echo "You guessed ". $guess . "<br>";

  if ($guess == $mynumber) {
	echo "You're right!  The number is ". $mynumber;
  }  if ($guess < $mynumber) {
	echo "Too low!  Try again.";
  }  if ($guess > $mynumber) {
	echo "Too high!  Try again.";
  }
}
?>
<!-- Now let the user enter their guess -->
<br>
<form action="guess.php" method="get">
 Your guess: <input name="guess" type="text" />
 <input type="submit" />
</form>
</body>
</html>