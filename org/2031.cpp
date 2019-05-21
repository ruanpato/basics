#include <stdio.h>
int main(){
	int Qnt;
	char Jogador1[6],Jogador2[6];
	scanf("%d",&Qnt);
	while(Qnt>0){
		scanf("%s %s",Jogador1,Jogador2);
			if (Jogador1[2]=='a' && Jogador2[2]=='a')printf("Aniquilacao mutua\n");							//J1ataqueVsJ2ataque||J2ataqueVsJ1ataque	1
			else if(Jogador1[2]=='p' && Jogador2[2]=='p')printf("Ambos venceram\n");						//J1papelVsJ2papel||J2papelVsJ1papel		2	
			else if(Jogador1[2]=='d' && Jogador2[2]=='d')printf("Sem ganhador\n");							//J1pedraVsJ2pedra||J2pedraVsJ1pedra		3
			else if(Jogador1[2]=='a' && Jogador2[2]=='d')printf("Jogador 1 venceu\n");						//J1ataqueVs2pedra							4
			else if(Jogador2[2]=='a' && Jogador1[2]=='d')printf("Jogador 2 venceu\n");						//J2ataqueVs2pedra							5
			else if(Jogador1[2]=='a' && Jogador2[2]=='p')printf("Jogador 1 venceu\n");						//J1ataqueVs2papel							6
			else if(Jogador2[2]=='a' && Jogador1[2]=='p')printf("Jogador 2 venceu\n");						//J2ataqueVsJ1papel							7
			else if(Jogador1[2]=='d' && Jogador2[2]=='p')printf("Jogador 1 venceu\n");						//J1pedraVsJ2papel							8
			else if(Jogador2[2]=='d' && Jogador1[2]=='p')printf("Jogador 2 venceu\n");						//J2pedraVsJ2papel							9
		Qnt--;
	}
	return 0;
}

