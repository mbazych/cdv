#include <stdio.h>
#include <stdlib.h>

int dlugosc(char *s){
    int i;
    for(i=0; s[i]!=0; i++);
    return i;
}

void toupp(char *s){
    int i;
    for(i=0; s[i]!=0; i++){
        if(s[i]>= 'a' && s[i]<= 'z'){
            s[i] += 'A' - 'a';
        }
    }

}

void odwracanie(char *s){
    int i;

    for(i=0; s[i]!=0; i++){
        if ((s[i]>= 'a' && s[i]<='z') || (s[i] >= 'A' && s[i] <= 'Z')){
            s[i] ^= 32;
        }
    }
}

void bezIndeksu(char *s){

    for(s; *s != 0; s++){
      if ((*s>= 'a' && *s<='z') || (*s >= 'A' && *s <= 'Z')) {
          *s ^= 32;
    }
  }
}

int charToInt(char *s){
  int x = 0;
  for(s; *s!=0; s++){
    x = x * 10 + *s - '0';
  }
  return x;
}

int main()
{
    char str1[20] = "ala ma kota";

    printf("%d", dlugosc(str1));
    toupp(str1);

    printf("\n");

    int i=0;

    for(i=0; str1[i]!=0; i++){
        printf("%c", str1[i]);
    }
    printf("\n");
    odwracanie(str1);
    for(i=0; str1[i]!=0; i++){
        printf("%c", str1[i]);
    }
    printf("\n");
    bezIndeksu(str1);
    for(i=0; str1[i]!=0; i++){
        printf("%c", str1[i]);
    }
    printf("\n");
    char num[] = "2359";
    printf("%d", charToInt(num));

    printf(typeof(num));
    return 0;
}
