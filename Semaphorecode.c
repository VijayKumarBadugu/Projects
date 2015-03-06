//This code prints "I am Vijay OK1 OK2 OK3" using semaphores
//I OK1 are defined in Thread1
//AM OK2 are defined in Thread 2
//Vijay OK3 are defined in OK3
//


#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
sem_t a,b,c,d;



void *mythread1(void*arg) 
{
printf("%s\n", (char *) arg);
sem_post(&b);
sem_wait(&a);
printf("OK1 \n");
sem_post(&b);
return NULL;
}

void *mythread2(void*arg) 
{
sem_wait(&b);
printf("%s\n", (char *) arg);
sem_post(&c);
sem_wait(&b);
printf("OK2 \n");
sem_post(&c);
return NULL;
}

void *mythread3(void*arg) 
{
sem_wait(&c);
printf("%s\n", (char *) arg);
sem_post(&a);
sem_wait(&c);
printf("OK3 \n");
sem_post(&d);
return NULL;
}
int main()
{

pthread_t p1,p2,p3;
sem_init(&a, 0, 0);
sem_init(&b, 0, 0);
sem_init(&c, 0, 0);
pthread_create(&p1, NULL, mythread1, "I");
pthread_create(&p2, NULL, mythread2, "am");
pthread_create(&p3, NULL, mythread3, "Vijay");
pthread_join(p3, NULL);
//sem_wait(&d);
return 0;
}

