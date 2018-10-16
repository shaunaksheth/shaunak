package com.shaunak;

public class Main {

    public static void main(String[] args) {
	// write your code here
        byte byteVar = 16;

        // example of widening / implicit conversion

        int intVar = byteVar;

        float floatVar = intVar;

        long longVar = intVar;

        floatVar = longVar;

        double doubleVar = floatVar;

        char charVal = '\u0041';
        intVar = charVal;

        System.out.println("Char in INT is:" + intVar);

        /*charVal = 'S';
        intVar = charVal;
        System.out.println("Char in charVal is:" + intVar);*/

        int n = 22/7; //loss of precision
        System.out.println("n = "+n);

        float f = (22/7);
        System.out.println("f =" + f);

        f = (float)22/7;
        System.out.println("f =" + f);


        double d = 22/7.0;
        System.out.println("d ="+d);



        }
}
