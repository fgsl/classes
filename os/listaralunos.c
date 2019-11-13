#include <stdio.h>
#include <stdlib.h>

#define COMPRIMENTO 20

int limparNome(char nome[])
{
	for(int i=0;i<COMPRIMENTO;i++)
	{
		nome[i] = 0;
	}
	return 0;
}

int main(int args, char *arg[])
{
	FILE *arquivo;
        char nome[COMPRIMENTO];        

	// abre o arquivo somente para leitura
	arquivo = fopen("nomes.txt","r");
        if (arquivo == NULL)
	{
		printf("Não conseguiu abrir o arquivo\n");
		system("pause");
		return 0; 
	}
	while (!feof(arquivo))
	{
		fgets(nome, 20, arquivo);
                for(int i=0; i<COMPRIMENTO;i++)
		{
			printf("%c",nome[i]);
		}
		limparNome(nome);
	}
	fclose(arquivo);
	printf("\n");
}


