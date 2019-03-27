public class Solution {
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    static int n;
    public int findPeak(int[] A) {
        // write your code here
        n = A.length;
        int l = 0, r = n - 1;
        return check(l, r, A);
    }
    public int check(int l, int r, int[] A){
        if(r - l + 1 == 3){
            return l + 1;
        }
        int mid = (l + r) >> 1;
        if(A[mid] > A[mid+1] && A[mid] > A[mid - 1]) return mid;
        if(A[mid] < A[mid-1] && A[mid] < A[mid+1]){
            return check(l, mid, A);
            //check(mid+1, r, A);
        }else if(A[mid] < A[mid+1]){
            return check(mid+1, r, A);
        }else{
            return check(l, mid, A);
        }
    }
}