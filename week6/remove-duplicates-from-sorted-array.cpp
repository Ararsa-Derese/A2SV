class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int num=nums[0],i=0,j=1;
        if(nums.size()==1){
            return 1;
        }
        while(i<nums.size()){
            if(nums[i]!=num){
        
                nums[j]=nums[i];
                num = nums[i];
                j++;
            }
            i++;
        }
        return j;
    }
};