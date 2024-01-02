class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i=0,j=numbers.size()-1;
        while(i<j){
            if(numbers[i]+numbers[j]==target){
                int a=distance(numbers.begin(),find(numbers.begin(),numbers.end(),numbers[i]));
                int b=distance(numbers.begin(),find(numbers.begin(),numbers.end(),numbers[j]));
                if(a==b){
                  return {a+1,b+2};  
                }
                return {a+1,b+1};
                
            }
            else if(numbers[i]+numbers[j]>target)
             j--;
            else
             i++;
        
        }
        return {0,0};
    }
};