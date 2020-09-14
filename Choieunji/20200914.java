import java.util.*;
class Solution {
    public int solution(int[] people, int limit) {
        Arrays.sort(people);
        int answer=0;
        int count=0;
        int i,j=0;

        for(i=people.length-1;i>j;i--)
        {
            int sum=0;
            sum=people[j]+people[i];
            if(sum<=limit)
            {
                count++;
                j++;
            }
            else{
               count++;
            }
        }
        if(i==j){count++;}
        return count;
    }
}
