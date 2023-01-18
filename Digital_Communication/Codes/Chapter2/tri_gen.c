#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

void tri_gen(char *str, int len)
{
	FILE *fp,*fp1,*fp2;
	double T,x,y;

        fp = fopen("t.dat","w");
	fp1 = fopen("uni1.dat","r");
	fp2 = fopen("uni2.dat","r");

	//get numbers from file
	while((fscanf(fp1,"%lf",&x)!=EOF) && (fscanf(fp2,"%lf",&y)!=EOF))
         
	{
		T=x+y;
		fprintf(fp,"%lf\n",T);

	}
	fclose(fp);
	fclose(fp1);
	fclose(fp2);

}

int  main(void) 
{
 

uniform("uni1.dat", 1000000);
uniform("uni2.dat", 1000000);

tri_gen("t.dat",1000000);

return 0;
}
