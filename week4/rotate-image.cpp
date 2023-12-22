class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
          for(int i=0; i<matrix.size(); i++){
        for(int j=i; j<matrix.size(); j++){
            if(i!=j){
           
            int temp=matrix[i][j];
            matrix[i][j]=matrix[j][i];
            matrix[j][i]=temp;
            }
        }

    }
    int i, j;
  for(int k=0; k<matrix.size(); k++){
    i=0; j=matrix.size()-1;
    while(i<j){
        int temp = matrix[k][i];
        matrix[k][i]=matrix[k][j];
        matrix[k][j]=temp;
        i++;
        j--;
        
    }  
    }
    }
};