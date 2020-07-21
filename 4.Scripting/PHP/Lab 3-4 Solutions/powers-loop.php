<!-- compute powers of a number using a while loop -->
<html>
<title> Powers</title>
<body>
<h4>Powers of a number</h4>
<!-- a competent HTLM coder would frown at my
	use of &nbsp, but it's simple...
-->
<?php
$tab = "&nbsp &nbsp &nbsp &nbsp";
echo "n" . $tab . "n^2" . $tab . "n^3" . "<br>";
$x = 1;
$stop = 5;

while ($x <= $stop) {
echo $x . $tab . $x*$x . $tab . $x*$x*$x . "<br>";
$x ++;
}

?>

</body></html>