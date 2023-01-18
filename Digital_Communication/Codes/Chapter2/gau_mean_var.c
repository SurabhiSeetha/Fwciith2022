#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"
double mean2(char *str);

double mean2(char *str)
{
int count=0;
FILE *fp;
double k, sqsum=0.0;

fp = fopen(str,"r");
while(fscanf(fp,"%lf",&k)!=EOF)
{

count+=1;

sqsum += (k*k);
}
fclose(fp);
return (sqsum/(count-1));
}

int  main(void) 
{
 double x,y,var;


x = mean("gau.dat");
printf("Mean: %lf\n",x);
y = mean2("gau.dat");
var = y-x*x;
printf("Variance: %lf\n",var);

//printf("Mean: %lf\n",mean("gau.dat"));
//printf("Variance: %lf\n",variance("gau.dat"));

return 0;
}
