package com.shaunak;

public class Main2 {
    public static void main(String args[]){

        /* int num = 14;
        boolean isPrime=true;

        for (int i=2; i<num/2; i++){
            if(num%i==0){
                isPrime=false;
                break;
            }
        }
        if(isPrime)
        {
            System.out.println(num+ " is a prime Number!");
        }
        else{
            System.out.println(num+ " is NOT a prime Number!");
        }*/

        System.out.println("1St line is Main");
        drawLine();
        System.out.println("\n2nd line in Main");
        drawLine(45);

    }

    static void drawLine(){
        for (int i=0;i<100;i++){
            System.out.print("-");
        }
    }

    static void drawLine(int width){
        for (int i=0;i<width;i++){
            System.out.print("-");
        }
    }

}
