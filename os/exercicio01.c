#include <stdio.h>

int main(int argc, char *argv[])
{
    char simbolos[7];
    int valores[7];

    printf("O valor de argc é %d\n",argc);

    simbolos[0] = 'I'; valores[0] = 1;
    simbolos[1] = 'V'; valores[1] = 5;
    simbolos[2] = 'X'; valores[2] = 10;
    simbolos[3] = 'L'; valores[3] = 50;
    simbolos[4] = 'C'; valores[4] = 100;
    simbolos[5] = 'D'; valores[5] = 500;
    simbolos[6] = 'M'; valores[6] = 1000; 

    for (int i = 0; i < 7; i++)
    {
	    if (*argv[1] == simbolos[i])
	    {
		printf("O símbolo %s é igual a %d\n",argv[1],valores[i]);
		break;
	    }
    }
}

