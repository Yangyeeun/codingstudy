import java.util.*;
import java.util.Arrays;

public class B20200907 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        int[] arr = new int[N + 1];

        for (int j = 0; j < N; j++) {
            arr[j] = s.nextInt();
        }
        Arrays.sort(arr);
        StringBuilder sb = new StringBuilder();
        int M = s.nextInt();
        for(int i=0;i<M;i++)
        {
            int input = s.nextInt();
            if(Arrays.binarySearch(arr,input)>0)
            {
                sb.append("1\n");
            }else{sb.append("0\n");}
        }
        System.out.println(sb.toString());
    }
}
