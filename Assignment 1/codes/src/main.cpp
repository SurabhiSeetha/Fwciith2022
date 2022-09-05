//Declaring all variables as integers
int Z,Y,X,W,F;

//Code released under GNU GPL.  Free to use for anything.
void disp_7447(int D, int C, int B, int A)
{
  digitalWrite(6, A); //LSB
  digitalWrite(7, B); 
  digitalWrite(8, C); 
  digitalWrite(9, D); //MSB

}
// the setup function runs once when you press reset or power the board
void setup() {
    pinMode(6, OUTPUT);  
    pinMode(7, OUTPUT);
    pinMode(8, OUTPUT);
    pinMode(9, OUTPUT);
    pinMode(2, INPUT);  
    pinMode(3, INPUT);
    pinMode(4, INPUT);
    pinMode(5, INPUT);
    
}

// the loop function runs over and over again forever
void loop() {
X = digitalRead(2); //LSB
Y = digitalRead(3); 
Z = digitalRead(4); 
W = digitalRead(5); //MSB

F=(X&&!Y)||(X&&!Z&&!W)||(X&&Z&&W)||(!Y&&!Z)||(!X&&Y&&Z&&!W);

if(F==1){
disp_7447(0,0,0,1);
}
else if (F==0) {
disp_7447(0,0,0,0);
} 
}
