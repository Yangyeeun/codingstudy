class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        int min, max;
        if(a>b){min=b;max=a;}else if(a==b){return a;}else{min=a;max=b;}
        for(int i=min;i<=max;i++)
        {
            answer+=i;
        }
        return answer;
    }
}
