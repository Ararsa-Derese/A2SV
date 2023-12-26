class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        for(int i=0; i<names.size(); i++){
            int smn=0,idx=i;
            for(int j=i; j<names.size(); j++){
                if(heights[j]>smn){
                         smn=heights[j];
                         idx=j;
                }
                        
         }
            int temp=heights[i];
                heights[i]=heights[idx];
                heights[idx]=temp;
                string t=names[i];
                names[i]=names[idx];
                names[idx]=t;      

        }
        return names;
    }
};