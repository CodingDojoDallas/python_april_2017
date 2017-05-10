
//problem 1

console.log(first_variable);
var first_variable;

function firstFunc() {
  first_variable = "Not anymore!!!";
  console.log(first_variable);
}

first_variable = "Yipee I was first!";
console.log(first_variable);
firstFunc()

//problem 2
var food = "Chicken";
function eat() {
  food = "half-chicken";
  console.log(food);
  food = "gone";       // CAREFUL!
  console.log(food);
}
eat();
console.log(food);

//problem3
new_word = "NEW!";
function lastFunc() {
  new_word = "old";
}
lastFunc()
console.log(new_word);