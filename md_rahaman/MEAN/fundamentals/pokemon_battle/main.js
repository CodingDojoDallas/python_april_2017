


var game = {
  players: [],
  addPlayer: function(player){
  	this.players.push(player);
  },
  playGame: function(){
  	//randomly select 2 players to battle
  	$('body').append(this.players[0].name)
  	console.log(this.players[0].name, " it is your turn!")
  	console.log('Your pokemon is ', this.players[0].hand[0].name)
  	console.log('your opponent', this.players[1].name)
  	console.log('Your pokemon is ', this.players[1].hand[0].name)
  }

};



function playerConstructor(name){
  player = {};
  player.name = name;
  player.hand = [];
  player.addCard = function(card){
  	// console.log('upper scope', this)
  	var self = this;
  	rand = Math.floor((Math.random() * 811) + 1);
	url = "http://pokeapi.co/api/v2/pokemon/"+rand+"/";
	$.get(
		url,
		function(res){
			self.hand.push(res);
		},
		'json'
	)
  };
  game.addPlayer(player)
  return player;
};

var json = playerConstructor("json")
var md = playerConstructor("Md")
// game.addPlayer(json)
// game.addPlayer(md)




