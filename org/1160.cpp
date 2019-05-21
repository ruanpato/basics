#include <iostream>

using namespace std;
//pa City A population //pb City B population //g1 City A population growth //city B population growth

int main(){
	int t, pa, pb, y;
	double g1, g2;
	cin >> t;
	while(t--){
		cin >> pa >> pb >> g1 >> g2;
		y = 0;
		
		while(pa <= pb){
			pa += pa * (g1/100);
			pb += pb * (g2/100);
			y++;
			if(y >100)break;
		}

		if(y > 100)
			cout << "Mais de 1 seculo." << endl;
		else
			cout << y << " anos." << endl;

	}
	return 0;
}

