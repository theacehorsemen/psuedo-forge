/*Program to find roots of quadratic equation*/
#include<stdio.h>
#include<math.h>
int main()
{
    float a,b,c,real,num,imag,root1,root2,disc;
    int k;
    printf("Input a,b and c\n");
    scanf("%f %f %f",&a,&b,&c);
    if (a!=0)
    {
        disc=b*b-4*a*c;
        printf("Discriminant=%5.2f\n",disc);
        if (disc<0)k=1;
        else if (disc==0)k=2;
        else if (disc>0)k=3;
        switch(k)
        {
            case 1:
            printf("Roots are imaginary\n");
            real=-b/2*a;
            disc=-disc;
            num=pow((double)disc,(double)0.5);
            imag=num/2*a;
            printf("Root1=%5.2f+j%5.2f\n",real,imag);
            printf("Root1=%5.2f-j%5.2f\n",real,imag);
            break;
            case 2:
            printf("Roots are real and equal\n");
            root1=b/2*a;
            printf("Root1=Root2=%5.2f",root1);
            break;
            case 3:
            printf("Roots are real and distinct\n");
            root1=(-b+sqrt((double)disc)/2*a);
            root2=(-b-sqrt((double)disc)/2*a);
            printf("Root1=%7.2f  Root2=%7.2f\n",root1,root2);
            break;
        }
    }
    else printf("Equation is linear\n");
}