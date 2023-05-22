public class Main {
    public static void main(String[] args) {
        
        sum([1, 2, 3, 4, 5]);
    }

    public long sum(int[] a) {
        long ans = 0;
        for(int i = 0; i < a.length; i++)
        {
            ans += a[i];
        }
        return ans;
    }
}