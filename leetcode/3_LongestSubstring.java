import java.util.*;



class Solution {
    public int lengthOfLongestSubstring(String s) {
        List<String> list = new ArrayList<String>();
        list.add(String.valueOf(s.charAt(0)));
        int ct = 0;
        for (int i = 1; i < s.length(); i++) {
            if(list.get(ct) != String.valueOf(s.chartAt(i))) {
                list.add(String.valueOf(s.charAt(i)));
                ct++;
            } else {
                return ct+1;
            }
        }
    }
}
