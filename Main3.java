package com.shaunak;

public class Main3 {
    public static void main(String[] args) {
        Greet g = new Greet(); // creating Instance of "Greet" Class
        g.greet("Shaunak"); //Invoking greet() method

        System.out.println(g.n);
        g.n = 100; //n exists as long as "g" exists!!
        System.out.println(g.n);
    } // "g" is destroyed
}
