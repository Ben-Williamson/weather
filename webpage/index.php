<!DOCTYPE html>
<html>
<head>
	<title>BGS Weather</title>
	<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet"> 
	<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
	<link rel="stylesheet" type="text/css" href="css/style.css?<?php echo rand();?>">
</head>


<?php
$today = getdate();
if($today["mday"] > 9) {
	$date = $today["mday"]."-".$today["mon"]."-".$today["year"];
}	else {
	$date = "0".$today["mday"]."-".$today["mon"]."-".$today["year"];
}

$urlvalue = htmlspecialchars($_GET["date"]);

if($urlvalue != "") {
	$date = $urlvalue;
}
$temperature = file_get_contents('data/Current/temperature.csv');
$air_qual = file_get_contents('data/Current/air_qual.csv');
$humidity = file_get_contents('data/Current/humidity.csv');
$pressure = file_get_contents('data/Current/pressure.csv');
$rain = file_get_contents('data/Current/rain.csv');
$wind_direction = file_get_contents('data/Current/wind_direction.csv');
$wind_speed = file_get_contents('data/Current/wind_speed.csv');
?>

<body>
	<div id="graphs">
		<div id="temperature" class="graph-container">
			<img src="data/<?php echo $date; ?>/graphs/temperature.png" alt="No Data"/>
		</div>

		<div id="title" class="graph-container">
			<h1 id="welcome">Welcome to the BGS Weather Station</h1>
			<h2 style="text-align: center;">Current Values:</h2>
			<h3>Temperature: <?php echo $temperature ?></h3>
			<h3>Air Quality: <?php echo $air_qual ?></h3>
			<h3>Humidity: <?php echo $humidity ?></h3>
			<h3>Pressure: <?php echo $pressure ?></h3>
			<h3>Rainfall: <?php echo $rain ?></h3>
			<h3>Wind Speed: <?php echo $wind_speed ?></h3>
			<h3>Wind Direction: <?php echo $wind_direction ?></h3>
		</div>

		<div class="graph-container">
			<img src="data/<?php echo $date; ?>/graphs/humidity.png" alt="No Data"/>
		</div>

		<div class="graph-container">
			<img src="data/<?php echo $date; ?>/graphs/wind_speed.png" alt="No Data"/>
		</div>

		<div class="graph-container">
			<img src="data/<?php echo $date; ?>/graphs/air_qual.png" alt="No Data"/>
		</div>

		<div class="graph-container">
			<img src="data/<?php echo $date; ?>/graphs/pressure.png" alt="No Data"/>
		</div>

		<div class="graph-container">
			<img src="data/<?php echo $date; ?>/graphs/rain.png" alt="No Data"/>
		</div>

		<div class="graph-container">
			<img src="data/<?php echo $date; ?>/graphs/wind_direction.png" alt="No Data"/>
		</div>
	</div>
</body>

<script type="text/javascript">
function title_height() {
    $("#title").css("height", $("#temperature").height());
}

window.onresize = function() {
	title_height();
};

title_height();
</script>
</html>
