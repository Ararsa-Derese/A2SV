class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(s.begin(),s.end());
        sort(g.begin(),g.end());
        int ans=0,j=0;
        for(int i=0; i<s.size(); i++){
            if(s[i]>=g[j]){
                ans++;
                j++;

            }
            if(j==g.size())
             break;

        }
        return ans;
    }
};
 