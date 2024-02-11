#include <stdio.h>
#include <stdlib.h>

int main()
{


/* comparison operator

Operator |	Name			|	        Example | 	Description
-----------------------------------------------------------------------------------
==		    Equal to			        x == y		Returns 1 if the values are equal
!=		    Not equal			        x != y		Returns 1 if the values are not equal
>		    Greater than			    x > y		Returns 1 if the first value is greater than the second value
<		    Less than			        x < y		Returns 1 if the first value is less than the second value
>=		    Greater than or equal to	x >= y		Returns 1 if the first value is greater than, or equal to, the second value
<=		    Less than or equal to		x <= y		Returns 1 if the first value is less than, or equal to, the second value

*/

    int a = 10;
    int b = 20;
    printf("equal to check                      %d\n", a == b);
    printf("not equal to check                  %d\n", a != b);
    printf("greater than check                  %d\n", a > b);
    printf("less than check                     %d\n", a < b);
    printf("greater than or equal to check      %d\n", a >= b);
    printf("less than or equal to check         %d\n", a <= b);

    return 0;
}
