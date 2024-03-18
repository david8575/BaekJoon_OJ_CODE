#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include <math.h>

void hanoiTower(int a, int b, int c, int n);
int main() {

	int n;
	int a = 1;
	int b = 2;
	int c = 3;
	
	scanf("%d", &n);

	printf("%.0lf\n", pow(2,n)-1);
	hanoiTower(a, b, c, n);

	return 0;
}
void hanoiTower(int a, int b, int c, int n) {
	if (n == 1) {
		printf("%d %d\n", a, c);
	}
	else {
		hanoiTower(a, c, b, n - 1);
		printf("%d %d\n", a, c);
		hanoiTower(b, a, c, n - 1);
	}
}