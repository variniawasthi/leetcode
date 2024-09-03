class Solution {
    public void sortColors(int[] nums) {
        int n = nums.length;
        // int i, c0 = 0, c1 = 0, c2 = 0;
        // for(i=0; i<n; i++){
        //     if(nums[i]==0)
        //         c0++;
        //     else if(nums[i]==1)
        //         c1++;
        //     else 
        //         c2++;
        // }
        // for(i=0; i<c0; i++)
        //     nums[i] = 0;
        // for(i=c0; i<(c0 + c1); i++)
        //     nums[i] = 1;
        // for(i=(c0 + c1); i<n; i++)
        //     nums[i] = 2; 
        int temp, low = 0, mid = 0, high = n-1;
        while(mid <= high){
            if(nums[mid] == 0){
                temp = nums[low];
                nums[low] = nums[mid];
                nums[mid] = temp;
                low++;
                mid++;
            }
            else if(nums[mid] == 1){
                mid++;
            }
            else{
                temp = nums[mid];
                nums[mid] = nums[high];
                nums[high] = temp;
                high--;
            }
        }
    }
}