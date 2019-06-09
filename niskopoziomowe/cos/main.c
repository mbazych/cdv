#include <stdio.h>
#include <stdlib.h>

float najmniejsza(float t[], int s){
    float min;
    int i;
    min = t[0];
    for(i=1; i<s/sizeof(float); i++)
        if(t[i]<min)
            min = t[i];
    return min;
}
float *minpointer(float t[], int s){
    float min;
    int i;
    min = t[0];
    for(i=1; i<s/sizeof(float); i++)
        if(t[i]<min)
            min = t[i];
    return min;
}

int main()
{ /*   Z INDEKSEM
    float tab[5] = {2.1, 3.7, 1.5, 4.3, 5.8};
    float min;
    int i;
    min = tab[0];
    for(i=1; i<sizeof(tab)/sizeof(float); i++)
        if(tab[i]<min)
            min = tab[i];

    printf("%f\n", min);
    return 0;
    */
    //  Z WSKANIKIEM
    /*float tab[5] = {2.1, 3.7, 1.5, 4.3, 5.8};
    float min;
    float *p;
    min = *tab;
    for(p=tab+1; p<tab + sizeof(tab)/sizeof(float); p++){
        printf("Adres: %p\n", p);
        if(*p < min)
            min=*p;
    }printf("%f\n", min);
    */
    float tab[5] = {2.1, 3.7, 1.5, 4.3, 5.8};
    int rozmiar = sizeof(tab);
    printf("%f", najmniejsza(tab, rozmiar));
}
