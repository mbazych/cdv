#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]){
    FILE *wp;
    char word[50];

  if((wp = fopen("dane", "a+")) == NULL){
      fprintf(stderr, "Can't open a file\n");
      return 2;
  }

  rewind(wp);

  printf("\nContent of the file: \n\n");
  int i = 0;
  while(fscanf(wp, "%s", word) == 1)
  {
    if(i)
      printf("%s ", word)
    i++;
  }

return 0;
}
