<!-- compute powers of a number -->
<html>
<title> Powers</title>
<body>
<h4>Powers of a number</h4>
<table>
<tr>
  <th>n</td>
  <th>n^2</td>
  <th>n^3</td>
</tr>
<?php
$x = 1;
echo "<tr>";
echo "  <td>". $x. "</td>";
echo "  <td>". $x*$x ,"</td>";
echo "  <td>" . $x*$x*$x ,"</td>";
echo "</tr>";

$x = 2;
echo "<tr>";
echo "  <td>". $x. "</td>";
echo "  <td>". $x*$x ,"</td>";
echo "  <td>". $x*$x*$x ,"</td>";
echo "</tr>";

$x = 3;
echo "<tr>";
echo "  <td>". $x. "</td>";
echo "  <td>". $x*$x ,"</td>";
echo "  <td>". $x*$x*$x ,"</td>";
echo "</tr>";
?>
</table>
</body></html>

