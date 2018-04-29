import java.util.Scanner;

class exercise5{
    public static void main(String args[]){
        double sum = 0;
        Scanner stdIn = new Scanner(System.in);

        System.out.println("sum x and y!!");

        System.out.println("please input x");
        double x = stdIn.nextDouble();

        System.out.println("please input y");
        double y = stdIn.nextDouble();

        sum = sum(x,y);
        System.out.println("x:"+x);
        System.out.println("y:"+y);
        System.out.println("x+y:"+sum);

    }

    public static double sum(double x, double y){
        return x+y;
    }

}