<!-- compute powers of a number -->
<html>
<title> Powers</title>
<body>
<h4>Powers of a number</h4>

<?php
$tab = "&nbsp &nbsp &nbsp &nbsp";
echo "n" . $tab . "n^2" . $tab . "n^3" . "<br>";
$x = 1;
$stop = $_POST['stop'];

while ($x <= $stop) {
echo $x . $tab . $x*$x . $tab . $x*$x*$x . "<br>";
$x ++;
}

?>

</body></html>