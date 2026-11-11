let randomnumber=Math.floor(Math.random()*100)+1
console.log(randomnumber);
let Guesessinput=document.getElementById("Guesessinput")
let GuesessButton=document.getElementById("GuesessButton")
let message=document.getElementById("message")
let bug=document.getElementById("bug")
GuesessButton.onclick=function(){
        const guess = Number(Guesessinput.value);
        console.log(guess);
        if(!Guesessinput.value || guess < 1 || guess > 100){
        message.innerHTML="Please enter a valid number between 1 and 100.";
        }else if(guess === randomnumber){
        message.innerHTML="Correct! You guessed the number.";
        GuesessButton.disabled=true;   
        }else if(guess < randomnumber){
        message.innerHTML="Too low. Try again!";
        }else{
        message.innerHTML="Too high. Try again!";
        }
}