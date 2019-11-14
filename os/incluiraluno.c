#include <stdio.h>
#include <stdlib.h>

#define COMPRIMENTO 20

int main(int args, char *arg[])
{
	FILE *arquivo;	
        char nome[COMPRIMENTO];
	//char enter = '\n';	

	printf("Digite o nome do aluno:");
	fgets(nome, COMPRIMENTO, stdin);

	// abre o arquivo para gravação
	arquivo = fopen("nomes.txt","a");
        if (arquivo == NULL)
	{
		printf("Não conseguiu abrir o arquivo\n");
		system("pause");
		return 0; 
	}
	//fprintf(arquivo,"%s %c",nome,enter); // se quiser saltar uma linha a cada registro, habilite a variável enter
	fprintf(arquivo,"%s",nome);
	fclose(arquivo);
	printf("\nAluno incluído.\n");
}


