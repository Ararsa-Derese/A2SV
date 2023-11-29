class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans="";
        if(strs.size()==1)
        return strs[0];
        int j=0;
        int c=0;
        for(int i=0; i>=0; i++){
            for( j=0; j<strs.size()-1; j++){
                if(strs[j]=="")
                return ans;
                if(i==strs[j].size()-1)
                     c++;
                if(strs[j][i]!=strs[j+1][i])
                  return ans;
            } 
            if(j==0)
            break;
            ans+=strs[j][i];
           
            if(c!=0)
            break;
        }
        return ans;
    }
};