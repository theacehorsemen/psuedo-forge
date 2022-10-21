#include<stdio.h>
#include<math.h>
int main()
{
    float i,j;
    //printf("%d ",pow(2,3));
    printf("::::::::::::TABLE OF POWERS::::::::::::::");
    printf("\n");
    for(i=1;i<6;i++)
    {
        for(j=1;j<6;j++)
        printf("%0.1f \t",pow(i,j));
        printf("\n");
    }
}
    