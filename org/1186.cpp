#include <iostream>

using namespace std;

int main(){
	int aux = 1, i, j;//i = lines, j = columns
	char t;
	double m[12][12], sum = 0.0;
	cin >> t;

	for(i = 0; i <= 11; i++){
		for(j = 0; j <= 11; j++){
			cin >> m[i][j];
		}
	}

	for(i = 11; i >= 1; i--){
		for(j = 11; j >= aux; j--){
			sum += m[i][j];
		}	
		aux++;
	}

	if(t == 'S'){
		printf("%.1lf\n", sum);
	}else{
		printf("%.1lf\n", sum/66.0);
	}


	return 0;
}
