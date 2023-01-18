#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <float.h>
//#include "coeffs.h"

void main()
{
  //gaussian("gau.dat", 1000000);
  FILE *fp;
  int i, j, samples=1000000;
  double temp,x;
  fp= fopen("gau.dat", "w");
  for(i=0; i<samples;i++)
  {
    temp= 0;
    for(j=0; j<12;j++)
    {
      temp= temp + (double)rand()/RAND_MAX;
    }
    x= temp-6;
    fprintf(fp,"%lf\n",x);
  }
  fclose(fp);
}


