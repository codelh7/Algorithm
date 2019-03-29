/**
 * public class SVNRepo {
 *     public static boolean isBadVersion(int k);
 * }
 * you can use SVNRepo.isBadVersion(k) to judge whether 
 * the kth code version is bad or not.
*/
public class Solution {
    /**
     * @param n: An integer
     * @return: An integer which is the first bad version.
     */
    public int findFirstBadVersion(int n) {
        // write your code here
        int l = 1, r = n;
        int ans = n;
        while(l <= r){
            int mid = l + (r - l  + 1) / 2;
            //System.out.println(mid);
            if(SVNRepo.isBadVersion(mid)){
                ans = mid;
                r = mid - 1;
            }else l = mid + 1;
        }
        return ans;
    }
}