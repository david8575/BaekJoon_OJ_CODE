#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


typedef struct {
	int queueArr[10000];
	int last;
} Queue;

void push(Queue* queue, int i);
int pop(Queue *queue);
int size(Queue *queue);
int empty(Queue *queue);
int front(Queue* queue);
int back(Queue* queue);

int main() {

	int n, num;
	char order[10];
	Queue* queue = (Queue*)malloc(sizeof(Queue));
	queue->last = -1;
	scanf("%d", &n);
	
	for (int i = 0; i < n; i++) {
		scanf("%s", &order);
		getchar();
		if (!strcmp(order, "push")) {
			scanf("%d", &num);
			getchar();
			push(queue, num);
		}
		else if (!strcmp(order, "pop")) {
			printf("%d\n", pop(queue));
		}
		else if (!strcmp(order, "size")) {
			printf("%d\n", size(queue));
		}
		else if (!strcmp(order, "empty")) {
			printf("%d\n", empty(queue));
		}
		else if (!strcmp(order, "front")) {
			printf("%d\n", front(queue));
		}
		else if (!strcmp(order, "back")) {
			printf("%d\n", back(queue));
		}
	}
	free(queue);
	return 0;
}

void push(Queue *queue, int i) {
	queue->queueArr[++queue->last] = i;
}
int pop(Queue *queue) {
	if (queue->last == -1) {
		return -1;
	}
	int num = queue->queueArr[0];
	for (int i = 0; i < queue->last; i++) {
		queue->queueArr[i] = queue->queueArr[i + 1];
	}
	queue->last--;
	return num;
}
int size(Queue *queue) {
	return queue->last + 1;
}
int empty(Queue *queue) {
	if (queue->last == -1) {
		return 1;
	}
	else {
		return 0;
	}
}
int front(Queue* queue) {
	if (queue->last == -1) {
		return -1;
	}
	else {
		return queue->queueArr[0];
	}
}
int back(Queue* queue) {
	if (queue->last == -1) {
		return -1;
	}
	else {
		return queue->queueArr[queue->last];
	}
}