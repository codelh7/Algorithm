public class Solution {
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
	 solution:这个题目的主要关键点在于抓住 A[1] > A[0] 和 A[len-2] > A[len-1]这两个题目说明
	 所以可以采用二分，当mid不满足条件的时候，判断A[mid-1]和A[mid]的关系 与 A[mid+1]和A[mid]的关系
	 若A[mid+1] > A[mid]，则[mid + 1, r]中肯定存在答案满足条件，因为若后面是一个递增的情况，则答案就是倒数第二个元素(A[len-2] > A[len-1]);
	 若后面不是一个递增的情况，即存在一个下标i， mid ... i递增,而A[i] > A[i+1]则答案就是下标i指向的元素
	 A[mid-1] > A[mid]的情况类似讨论
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
