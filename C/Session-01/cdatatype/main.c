#include <stdio.h>
#include <stdlib.h>

int main()
{

    int a=10;
    float b=10.05;
    double bd=100.10;
    char c='C';
    char  d[]="welcome";

    int x,y,z;
    x=25;
    y=26;
    z=27;
    printf("%d\t%d\t%i\n",x,y,z);


    /*
    format Specifiers:
    %d or %i --- > integer(int)
    %f or %F --- > decimal number (float)
    %c       --- > character(char)
    %s       --- > string or collection of character (char[])
    */

    printf("%d\n",a);
    printf("%i\n",a);
    printf("%.2f\n",b);
    printf("%.3F\n",b);
    printf("%c\n",c);
    printf("%s\n",d);
    printf("%lf\n",bd);
    return 0;
}
