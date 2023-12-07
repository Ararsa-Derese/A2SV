class Solution {
public:
    int missingNumber(vector<int>& nums) { 
       sort(nums.begin(), nums.end());
        int k=0, num=-1;
        for(int i=0; i<nums.size(); i++){
            if(nums[i]!=k){
                num=k;
                break;
            }
               k++;}
        if(num==-1)
        return k++;
            return num;
    }
};