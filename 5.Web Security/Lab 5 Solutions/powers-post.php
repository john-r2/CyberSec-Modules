<!-- compute powers of a number -->
<html>
<title> Powers</title>
<body>
<h4>Powers of a number</h4>
<table align = "left" border = "1" cellpadding = "3" cellspacing = "0">
<tr>
  <th>n</td>
  <th>n^2</td>
  <th>n^3</td>
</tr>
<?php
$stop = $_POST['stop'];
for ($x = 1; $x <= $stop; $x++)
{
  echo "<tr>";
  echo "  <td>". $x. "</td>";
  echo "  <td>". $x*$x ,"</td>";
  echo "  <td>" . $x*$x*$x ,"</td>";
  echo "</tr>";
}
?>
</table>
</body></html>

