#include <stdio.h>
#include <stdlib.h>

int main()
{
// assignment operator

    int a;

    a=20;
    printf("%i\n",a);

/* logical operator


Operator	Name	            Example	            Description
-------------------------------------------------------------
&& 	        Logical and	        x < 5 &&  x < 10	Returns 1 if both statements are true
|| 	        Logical or	        x < 5 || x < 4	    Returns 1 if one of the statements is true
!	        Logical not	        !(x < 5 && x < 10)  Reverse the result, returns 0 if the result is 1

*/

    int x =6;
    printf("logical and output : \t%d\n", (x < 5 &&  x < 10));

    printf("logical or output : \t%d\n", (x < 5 ||  x < 10));


    printf("logical not output : \t%d\n", !(x < 5 &&  x < 10));


    // const usage

    int yy=100;
    const int y=10;
    printf("normal variable declaration     %d\n",yy);
    printf("const variable declaration     %d\n",y);
    //y=25;
   // printf("%d",y);
    yy=25;
    printf("normal variable re-assignment   %d",yy);


    return 0;
}
