#include <stdio.h>

int main()
{
	float soma = 0;
	for(int i=0;i<1000;i++){
		soma += 0.9999999;
	}

	printf("A soma é igual a %f \n",soma);
}
