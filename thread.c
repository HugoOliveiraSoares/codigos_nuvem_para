#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

int x = 0;
int y = 0;

void *funcao1(void *arg) {
  x = 1;
  sleep(1);
  if (y == 0) {
    printf("1 \n");
  }

  return NULL;
}

void *funcao2(void *arg) {
  y = 1;
  sleep(1);
  if (x == 0) {
    printf("2 \n");
  }
  return NULL;
}

int main() {
  pthread_t t1, t2;

  pthread_create(&t1, NULL, funcao1, NULL);
  pthread_create(&t2, NULL, funcao2, NULL);

  pthread_join(t1, NULL);
  pthread_join(t2, NULL);

  return 0;
}
