class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        j = 0
        for num in range(1, n + 1):
            res.append("Push")
            if num == target[j]:
                j += 1
                if j == len(target):
                    break
            else:
                res.append("Pop")
        return res

"""    
class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> res = new ArrayList();
        int j=0;
        for( int i=1; i<=n+1; i++ ){
            res.add("Push");
            if(target[j]==i){
                j++;
                if (j==target.length){
                    break;
                }
            }
            else{
                res.add("Pop");
            }
        }
        return res;
    }
}
"""