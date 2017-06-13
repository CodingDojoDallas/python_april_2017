//Create a simple for loop that sums all the integers between x and y (inclusive). Have it console log the final sum.
x = [1, 5, 90, 25, -3, 0]

function sum(x,y){
	var sum=0;
	for(var i=x;i<=y;i++){
		sum = sum + i;
	}
	return sum;
}

//Write a loop that will go through an array, find the minimum value, and then return it

function findMin(arr){
	min = arr[0]
	for(var i=0;i<arr.length;i++){
		if(min>arr[i]){
			min = arr[i]
		}
	}
	return min;
}
//Write a loop that will go through an array, find the average of all of the values, and then return it

function avg(array){
	var min = array[0];
	var avg = 0;
	var sum = 0;
	for(var i=0; i<array.length;i++){
		sum = sum+array[i]
	}
	return sum/array.length;
}

var sum = function(x,y){
	var sum=0;
	for(var i=x;i<=y;i++){
		sum = sum + i;
	}
	return sum;
}

var findMin=function(arr){
	min = arr[0]
	for(var i=0;i<arr.length;i++){
		if(min>arr[i]){
			min = arr[i]
		}
	}
	return min;
}

var avg=function(array){
	var min = array[0];
	var avg = 0;
	var sum = 0;
	for(var i=0; i<array.length;i++){
		sum = sum+array[i]
	}
	return sum/array.length;
}


function jsFundamentalsII(){
	this.result = 0;

	this.sum = function(x,y){
		var sum=0;
		for(var i=x;i<=y;i++){
			sum = sum + i;
		}
		this.result = sum;
		return sum;
	}

	this.findMin=function(arr){
		min = arr[0]
		for(var i=0;i<arr.length;i++){
			if(min>arr[i]){
				min = arr[i]
			}
		}
		return min;
	}

	this.avg=function(array){
		var min = array[0];
		var avg = 0;
		var sum = 0;
		for(var i=0; i<array.length;i++){
			sum = sum+array[i]
		}
		return sum/array.length;
	}


}

function person(){
	this.name = "Md Rahaman";
	this.distance_travel = 0;

	this.say_name = function(){
		console.log(this.name)
	}

	this.say_something = function(arg){
		console.log(this.name+' says '+arg)
	}

	this.walk = function(){
		console.log(this.name+' is walking.')
		this.distance_travel += 3
	}

	this.running = function(){
		console.log(this.name+ ' is running.')
		this.distance_travel += 10
	}

	this.crawling = function(){
		console.log(this.name+ ' is crawling.')
		this.distance_travel += 1
	}
}







// console.log(sum(2,10))
// console.log(findMin(x))
// console.log(avg(x))
// console.log(sum(2,3))
// console.log(findMin(x))
// console.log(avg(x))

var person1 = new person()
person1.say_name()
person1.say_something('i am cool')
person1.walk()
person1.running()
person1.crawling()
console.log(person1.distance_travel)

// var jsfun = new jsFundamentalsII()
// console.log(jsfun.sum(3,5))
// console.log(jsfun.findMin(x))
// console.log(jsfun.avg(x))


