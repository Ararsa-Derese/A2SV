class Solution {
public:
   int numTimesAllBlue(vector<int>& flips) {
    int maxBulb = 0, turnedOn = 0, moments = 0;
    for (int i = 0; i < flips.size(); ++i) {
        maxBulb = max(maxBulb, flips[i]);
        turnedOn++;
        if (maxBulb == turnedOn) {
            moments++;
        }
    }
    return moments;
}
        
        };