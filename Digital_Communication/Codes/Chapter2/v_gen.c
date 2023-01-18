#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

void v_gen(char *str, int len)
{
 uniform("uni.dat", 1000000);

 FILE *fp,*fp1;
 double x, V;
 double log10( double arg );
 fp = fopen("v.dat","w");
 fp1 = fopen("uni.dat","r");

 while(fscanf(fp1,"%lf",&x)!=EOF)
 {
  V=-2*log(1-x);
  fprintf(fp,"%lf\n",V);
 }
 fclose(fp1);
 fclose(fp);
}
int  main(void)
{ 

 v_gen("v.dat",1000000);

 return 0;
}
