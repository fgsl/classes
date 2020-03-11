/* Lendo e imprimindo um arquivo sequencial */
#include <stdio.h>
int main( void )
{
	int conta; /* número da conta */
	char nome[ 30 ]; /* nome da conta */
	double saldo; /* saldo da conta */
	FILE *arquivo;
	/* ponteiro de arquivo arquivo = clientes.dat */
	/* fopen abre arquivo; sai do programa se o arquivo não puder ser aberto */
	if ( ( arquivo = fopen( "clientes.dat", "r" ) ) == NULL ) {
		printf( "arquivo não pode ser aberto\n" );
	} /* fim do if */
	else { /* lê conta, nome e saldo do arquivo*/
		printf( "%-10s%-13s%s\n", "Conta", "Nome", "Saldo" );
		fscanf( arquivo, "%d%s%lf", &conta, nome, &saldo );
		/* enquanto não é fim de arquivo */
		while ( !feof( arquivo ) ) {
			printf( "%-10d%-13s%7.2f\n", conta, nome, saldo );
			fscanf( arquivo, "%d%s%lf", &conta, nome, &saldo );
		} /* fim do while */
		fclose( arquivo ); /* fclose fecha o arquivo */
	} /* fim do else */
	return 0; /* indica conclusão bem-sucedida */
} /* fim do main */
