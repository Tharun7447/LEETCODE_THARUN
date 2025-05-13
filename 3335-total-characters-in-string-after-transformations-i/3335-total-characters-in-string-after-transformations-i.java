class Solution {
    public int lengthAfterTransformations(String s, int t) {
        int[] count = new int[26];
        int mod = (int)(1e9 + 7);
        for(char c:s.toCharArray())
            count[c-'a']++;
        while(t-- != 0){
            int  c = count[25];
            for(int i=24;i>=0;i--){
                count[i+1] = count[i];
            }
            count[0] = c;
            count[1] = (count[1]+c)%mod;
        }
        int ans = 0;
        for(int i:count){
            ans = ( ans+i)%mod;
        }
        return ans;
    }
}