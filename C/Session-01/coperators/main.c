#include <stdio.h>
#include <stdlib.h>

int main()
{


/* Operators in C: (Arithmetic Operators)

        operator |	Name	       |    Description	                            |   Example
        ------------------------------------------------------------------------------------
        +	        Addition	        Adds together two values	                x + y
        -	        Subtraction	        Subtracts one value from another	        x - y
        *	        Multiplication	    Multiplies two values	                    x * y
        /	        Division	        Divides one value by another	            x / y
        %	        Modulus	            Returns the division remainder	            x % y
        ++	        Increment	        Increases the value of a variable by 1	    ++x
        --	        Decrement	        Decreases the value of a variable by 1	    --x

*/
    int value1=10;
    int value2=20;
    int value3;
    float dvalue3;


    //addition
    value3= value1 + value2;
    printf("added value of 1 and 2 is :\t%i\n",value3);

    //subtraction
    value3= value1 - value2;
    printf("subtracted value of 1 and 2 is :\t%i\n",value3);

    // multiplication
    value3= value1 * value2;
    printf("Multiplication of 1 and 2 is :\t%i\n",value3);


    //division
    value3= value1 / value2;
    printf("Division of 1 and 2 is :\t%f\n",(float)value3); // wrong -- > type conversion

    printf("Division of 1 and 2 is :\t%f\n",(float)value1 / value2); // type conversion

    dvalue3= (float)value1 / value2; // type conversion

    printf("Division of 1 and 2 is :\t%f\n",dvalue3);



    //modulus
    value3= 7 % 3;
    printf("Modulus of 1 and 2 is :\t%d\n",value3);


    //increment
    value1++;
    // printf("Increment of 1 :\t%d\n",value1++);
    printf("Increment of 1 :\t%d\n",value1);


    //decrement
    value2--;
    // printf("decrement of 1 :\t%d\n",value2--);
    printf("Decrement of 2 :\t%d\n",value2);







    return 0;
}
