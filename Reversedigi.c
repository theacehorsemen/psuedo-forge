#include<stdio.h>
#include<math.h>
int main()
{
    int num,a,i,b;
    printf("Enter a  number:");
    scanf("%d",&num);
    a=log10(num)+1;
    printf("The reversed number is:\n");
    for(i=0;i<a;i++)
    {
        b=num%10;
        printf("%d",b);
        num=num/10;

    }
    /*printf("%d\n",a);
    i=0;
    reverse=0;
    for(i;i<=a;i++)
    {
        if(i==0)
        {
            b=num;
        }
        //printf("%d\n",i);
       else
       b=(num/(i*10));
        //printf("%d\n ",b);
        spl=b%10;
        //printf("\n %d\n",spl);
        reverse += spl*(a-i)*10;
        //printf("\n  %d\n",reverse);
        
    }*/

    /*a=num%10;
    b=(num/10)%10;
    c=(num/100)%10;
    d=(num/1000)%10;
    e=(num/10000)%10;
    reverse=a*10000+b*1000+c*100+d*10+e*1;*/
    
    //printf("Reversed number is %d",reverse);



}