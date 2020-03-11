/* Criando um arquivo sequencial */
#include <stdio.h>
int main( void )
{
	int conta; /* número da conta */
	char nome[ 30 ]; /* nome da conta */
	double saldo; /* saldo da conta */
	FILE *arquivo; /* ponteiro de arquivo arquivo = clientes.dat */
	/* fopen abre arquivo. Sai do programa se não pode criar arquivo */
	if ( ( arquivo = fopen( "clientes.dat", "w" ) ) == NULL ) {
		printf( "Arquivo não pode ser aberto\n" );
	} /* fim do if */
	else {
		printf( "Digite o número de conta, o nome e o saldo.\n" );
		printf( "Digite fim de arquivo (CTRL+D) para terminar a entrada.\n" );
		printf( "? " );
		scanf( "%d%s%lf", &conta, nome, &saldo );
		/* grava conta, nome e saldo no arquivo com fprintf */
		while ( !feof( stdin ) ) {
			fprintf( arquivo, "%d %s %.2f\n", conta, nome, saldo );
			printf( "? " );
			scanf( "%d%s%lf", &conta, nome, &saldo );
		} /* fim do while */
		 fclose( arquivo ); /* fclose fecha arquivo */
	} /* fim do else */
	return 0; /* indica conclusão bem-sucedida */
} /* fim do main */
