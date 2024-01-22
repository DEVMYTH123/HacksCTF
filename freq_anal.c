#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct hash{
   int freq;
   char name[100];
};

int search( struct hash hashes[40],int len,char str[100]){
    for(int i=0; i<len; i++){
        if( strcmp(hashes[i].name,str) == 0){
            return i;
        }
    }
    return -1;
}

int main(){
    FILE* fp = fopen("output.txt","r");

    if(fp == NULL){
        printf("\nFile does not exist\n");
        return 1;
    }    
    struct hash hashes[40];
    int n = 0; 
    int i = 0;
    char str[100];
    while(fscanf(fp,"%s",str) == 1){
        i = search(hashes,n+1,str);    
        if(i != -1){
            hashes[i].freq++;
        }else{
            strcpy(hashes[n].name,str);
            hashes[n].freq = 1;
            n++;
        }
    }

    for(int j=0; j<=n; j++){
        printf("%s : %d \n",hashes[j].name,hashes[j].freq);
    }
    fclose(fp);
    return 0;
}
