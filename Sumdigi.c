#include<stdio.h>
int main()
{
    int a;
    int sum=0;
    printf("Enter a number");
    scanf("%d",&a);
    while(a!=0)
        {
            sum += a % 10;
            a = a/10;
        }
    printf("digit sum is %d",sum);
    return 0;
}