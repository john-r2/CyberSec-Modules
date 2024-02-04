<!-- compute powers of a number -->
<html>
<title> Powers</title>
<body>
<h4>Powers of a number</h4>

<?php
$stop = 5;
echo "n" . "&nbsp" . "n^2" . "&nbsp" . "n^3" . "<br>";
$x = 1;
while ($x <= $stop)
{
  echo $x . "&nbsp".  $x*$x . "&nbsp". $x*$x*$x . "<br>";
  $x ++;
}
?>
</body></html>

