
#include <avr/io.h>
#include <stdbool.h>
int main (void)
{
bool x,y,z,w,f;
while(1)
{
DDRD |= 0b00000000;
DDRB |= (( 1 << DDB5 ));
x = (PIND & (1<<PIND2)) == (1<<PIND2); 
y=(PIND & (1<<PIND3)) == (1<<PIND3);
z= (PIND & (1<<PIND4)) == (1<<PIND4);
w= (PIND & (1<<PIND5)) == (1<<PIND5);
f = ( (x&&(!y))||(x&&(!z)&&(!w))||(x&&z&&w)||((!y)&&(!z))||((!x)&&y&&z&&(!w)) );
PORTB = (f<<PB5);
}
return 0;
}
