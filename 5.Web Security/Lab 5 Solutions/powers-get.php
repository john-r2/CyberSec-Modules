<!-- compute powers of a number -->
<html>
<title> Powers</title>
<body>
<h4>Powers of a number</h4>

<?php
$stop = $_GET['stop'];
echo "n" . "&nbsp" . "n^2" . "&nbsp" . "n^3" . "<br>";
for ($x = 1; $x <= $stop; $x++)
{
  echo $x . "&nbsp".  $x*$x . "&nbsp". $x*$x*$x . "<br>";
}
?>
</body></html>

