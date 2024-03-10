#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
	int stackArr[10000];
	int top;
} Stack;

void push(Stack* stack, int num);
int pop(Stack *stack);
int size(Stack* stack);
int empty(Stack* stack);
int top(Stack* stack);

int main() {
	int n, num;
	char order[10];
	Stack* stack = (Stack*)malloc(sizeof(Stack));
	stack->top = -1;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", order);
		getchar();
		if (!strcmp(order, "push")) {
			scanf("%d", &num);
			getchar();
			push(stack, num);
		}
		else if (!strcmp(order, "pop")) {
			printf("%d\n", pop(stack));
		}
		else if (!strcmp(order, "size")) {
			printf("%d\n", size(stack));
		}
		else if (!strcmp(order, "empty")) {
			printf("%d\n", empty(stack));
		}
		else if (!strcmp(order, "top")) {
			printf("%d\n", top(stack));
		}
	}
	free(stack);
	return 0;
}
void push(Stack* stack, int num) {
	stack->stackArr[++stack->top] = num;
}
int pop(Stack* stack) {
	if (stack->top == -1) {
		return -1;
	}
	else
		return stack->stackArr[stack->top--];
}
int size(Stack* stack) {
	return stack->top + 1;
}
int empty(Stack* stack){
	if (stack->top == -1) {
		return 1;
	}
	else {
		return 0;
	}
}
int top(Stack* stack) {
	if (stack->top == -1) {
		return -1;
	}
	else {
		return stack->stackArr[stack->top];
	}
}