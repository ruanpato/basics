#include <stdio.h>
#include <string.h>
#include <ctype.h>

//Latin alphabet {A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z};
int abc[26] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
char nome[11234];

void lettersUsed();
void setLetters();
void permutations();

int main(){
	scanf("%[^\n]", nome);
	lettersUsed();
	setLetters();
	permutations();

	return 0;
}

void lettersUsed(){
	int i;
	printf("%d\n", strlen(nome));
	for(i = 0; i < strlen(nome); i++){
		//algoritmo desconsidera acentuação
		if(nome[i] == 'A' || nome[i] == 'a'){
			abc[0] = 1;
		}else if(nome[i] == 'B' || nome[i] == 'b'){
			abc[1] = 1;
		}else if(nome[i] == 'C' || nome[i] == 'c'){
			abc[2] = 1;
		}else if(nome[i] == 'D' || nome[i] == 'd'){
			abc[3] = 1;
		}else if(nome[i] == 'E' || nome[i] == 'e'){
			abc[4] = 1;
		}else if(nome[i] == 'F' || nome[i] == 'f'){
			abc[5] = 1;
		}else if(nome[i] == 'G' || nome[i] == 'g'){
			abc[6] = 1;
		}else if(nome[i] == 'H' || nome[i] == 'h'){
			abc[7] = 1;
		}else if(nome[i] == 'I' || nome[i] == 'i'){
			abc[8] = 1;
		}else if(nome[i] == 'J' || nome[i] == 'j'){
			abc[9] = 1;
		}else if(nome[i] == 'K' || nome[i] == 'k'){
			abc[10] = 1;
		}else if(nome[i] == 'L' || nome[i] == 'l'){
			abc[11] = 1;
		}else if(nome[i] == 'M' || nome[i] == 'm'){
			abc[12] = 1;
		}else if(nome[i] == 'N' || nome[i] == 'n'){
			abc[13] = 1;
		}else if(nome[i] == 'O' || nome[i] == 'o'){
			abc[14] = 1;
		}else if(nome[i] == 'P' || nome[i] == 'p'){
			abc[15] = 1;
		}else if(nome[i] == 'Q' || nome[i] == 'q'){
			abc[16] = 1;
		}else if(nome[i] == 'R' || nome[i] == 'r'){
			abc[17] = 1;
		}else if(nome[i] == 'S' || nome[i] == 's'){
			abc[18] = 1;
		}else if(nome[i] == 'T' || nome[i] == 't'){
			abc[19] = 1;
		}else if(nome[i] == 'U' || nome[i] == 'u'){
			abc[20] = 1;
		}else if(nome[i] == 'V' || nome[i] == 'v'){
			abc[21] = 1;
		}else if(nome[i] == 'W' || nome[i] == 'w'){
			abc[22] = 1;
		}else if(nome[i] == 'X' || nome[i] == 'x'){
			abc[23] = 1;
		}else if(nome[i] == 'Y' || nome[i] == 'y'){
			abc[24] = 1;
		}else if(nome[i] == 'Z' || nome[i] == 'z'){
			abc[25] = 1;
		}
	}printf("Letras: { ");
	for(i = 0; i < 26; i++)
		if(abc[i] == 1)
			printf("%c ", (65+i));
	printf("}\n");
}

void permutations(){
	FILE *arquivo;
	char subConjunto[26], filename[30];
	strcpy(filename, nome);
	strcat(filename, ".txt");
	printf("%s\n", filename);
	arquivo = fopen(filename, "w");
	unsigned MAX, MASK, NUM;
	int i, j;

	MAX = ~(1 << strlen(nome));

	/* Primeiro número é o 1. */
	NUM = 1;

	printf("{ }\n");//Conjunto vazio
	fprintf(arquivo, "{ }\n");
	/* Quando o número alcançar MAX, o loop
	* será encerrado.
	*/
	while(MAX & NUM){
		MASK = 1;
		i = j = 0;

		while( MAX & MASK ){
			/* Verdadeiro se NUM tem um bit 1
			* na posição indicada por MASK. */
			if ( NUM & MASK ) {
				/* Gera a combinação em subConjunto. */
				subConjunto[i] = nome[j];
				i++;
			}
			j++;
			/* Desloca a máscara */
			MASK = MASK << 1;
		}

	subConjunto[i]=0;
	//subconjunto
	printf("{%s}\n", subConjunto);
	fprintf(arquivo, "{%s}\n", subConjunto);
	NUM++;
	}
	fclose(arquivo);
}

void setLetters(){
	int i;char aux[2];
	strcpy(nome, "");
	for(i = 0; i < 26; i++){
		if(abc[i] == 1){
			aux[0] = (65+i);
			strcat(nome, aux);
		}
	}
}