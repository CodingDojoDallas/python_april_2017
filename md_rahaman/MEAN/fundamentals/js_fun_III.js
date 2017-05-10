function person(name){
	this.name = name;
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

function ninjaConstructor(name, cohort){
	this.name = name;
	this.cohort = cohort;
	this.belt = "yello";

	this.levelUp = function(param){
		this.belt = param
	}
}

var ninja1 = new ninjaConstructor("Md Rahaman", "uptown Func")
ninja1.levelUp("black")
console.log(ninja1.belt)



// var person1 = new person("Md Rahaman")
// person1.say_name()
// person1.say_something('i am cool')
// person1.walk()
// person1.running()
// person1.crawling()
// console.log(person1.distance_travel)



