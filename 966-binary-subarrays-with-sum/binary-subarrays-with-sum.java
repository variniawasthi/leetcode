class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        int count = 0;
        int temp, lst[];
        for(int i = 0;i < nums.length;++i){
            temp = 0;
            for(int j = i;j < nums.length;++j){
                temp = temp + nums[j];
                if(temp == goal){
                    ++count;
                }
            }
        }
        return count;
    }
}