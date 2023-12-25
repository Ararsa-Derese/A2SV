class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int i=0,j=0,sum=0;
        while(i<mat.size() && j<mat.size()){
            sum+=mat[i][j];
            i++;
            j++;
        }
        i=mat.size()-1;
        j=0;
        while(j<mat.size() and i>=0){
            sum+=mat[i][j];
            j++;
            i--;
        }
        if(mat.size()%2==1)
        sum-=mat[mat.size()/2][mat.size()/2];
        return sum;
    }
};