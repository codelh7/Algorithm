public class Solution {
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    public int binarySearch(int[] nums, int target) {
        // write your code here
        int n = nums.length;
        int l = 0, r = n - 1, ans = -1;
        while(l <= r){
            int mid = (l + r + 1) >> 1;
            //System.out.println(nums[mid]);
            if(nums[mid] > target){
                r = mid - 1;
            }else if(nums[mid] < target){
                l = mid + 1;
            }else{
                if(ans == -1) ans = mid;
                else ans = Math.min(ans, mid);
                r = mid - 1;
            }
        }
        return ans;
    }
}