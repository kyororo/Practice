class exercise2 {
    public static void main (String args[]){
        int x = 32,y=27,z=30;
        
        int sum = 0;
        int ave = 0;

        sum = sum(x,y,z);
        ave = ave(sum,3);

        System.out.println("x:"+x);
        System.out.println("y:"+y);
        System.out.println("z:"+z);
        System.out.println("sum:"+sum);
        System.out.println("ave:"+ave);
    }

    private static int sum(int x, int y, int z){
        return x+y+z;
    }

    private static int ave(int sum, int element ){
        return sum/element;
    }
}