class Solution {
public:
    bool isHappy(int n) {
       int sum=0;
        while(n)
        {
            sum+=((n%10)*(n%10));
            n/=10;
        }
        if(sum<10){
            if(sum==1 || sum==7)
            return true;
            else 
            return false;
        }
        else
        return isHappy(sum);
    }
    
};