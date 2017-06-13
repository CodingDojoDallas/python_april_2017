x = [3,5,"Dojo", "rocks", "Michael", "Sensei"];
console.log(x)

for(var i=0; i<x.length;i++){
	document.write(x[i]);
	document.write("<br>");
}
document.write("\n");
document.write("<br>");
x.push(100);
document.write(x);
document.write("<br>");
x = ["hello", "world", "JavaScript is Fun"];
document.write(x);

//sum 1 to 5000:
var sum = 0;
for(var i=1;i<=5000;i++){
	sum = sum+i;
}
document.write("<h1>Sum between 1 to 5000:"+sum+"</h1")
document.write("<br>");

//finding minumim
var array = [1, 5, 90, 25, -3, 0]
var min = array[0];
// var avg = 0;
var sum = 0;
for(var i=0; i<array.length;i++){
	sum = sum+array[i]
	if(min>array[i]){
		min = array[i]
	}
}
document.write("<h1>Minimum of this array [1,5,90,25,-3,0]: "+ min+"</h1")
document.write("<br>");

document.write("<h1>Average of this array [1,5,90,25,-3,0]: "+ sum/array.length+"</h1")

var newNinja = {
 name: 'Jessica',
 profession: 'coder',
 favorite_language: 'JavaScript', //like that's even a question!
 dojo: 'Dallas'
}

document.write("<br>")

for (var key in newNinja){
	document.write("<h3>"+key+":"+newNinja[key]+"</h3>")
	document.write("<br>")
	// console.log(key);
	// console.log(newNinja[key])
}




