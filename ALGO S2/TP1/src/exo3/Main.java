package exo3;

public class Main {
    public static void main(String[] args) {
        int n=35;
        int ppd=2;
        while (n%ppd!=0){
            ++ppd;
        }
        System.out.printf(""+ppd);
    }
}
