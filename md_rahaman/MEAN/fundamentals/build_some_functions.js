
function runningLogger(){
	console.log("I am running");
}

function multiplyByTen(val){
	console.log(val*10)
	return val*10;
}

function stringReturnOne(){
	return "Md"
}


function stringReturnTow(){
	return "Rahaman"
}

function caller(arg){
	console.log(arg)
	if (typeof arg === "function"){
		console.log("typeof may be useful")
	}
	console.log(stringReturnTow())
}

function myDoubleConsoleLog(arg1,arg2){
	if(typeof(arg1) === "function" && typeof(arg2) === "function"){
		console.log(arg1())
		console.log(arg2())
	}
}


function caller2(param){
  console.log('starting');
  var x = setTimeout(function(){
    if (typeof(param)=='function'){
      // notice the passed parameters...
      param(stringReturnOne, stringReturnTow);
    }
  }, 2000);
  console.log('ending');
  return "interesting";
}





multiplyByTen(5)
console.log(stringReturnOne())
console.log(stringReturnTow())
caller(stringReturnTow)
myDoubleConsoleLog(stringReturnOne,stringReturnTow)
caller2(myDoubleConsoleLog)


