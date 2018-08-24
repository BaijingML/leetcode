class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        L = len(points)
        S = 0
        for i in range(L-2):
            for j in range(i+1, L-1):
                for k in range(j+1, L):
                    S = max(S, abs(0.5*(points[i][0]*points[j][1] + points[j][0]*points[k][1]+points[k][0]*points[i][1]
                                    -points[j][0]*points[i][1]-points[k][0]*points[j][1]-points[i][0]*points[k][1])))
        return S

if __name__ == '__main__':
    solu = Solution()
    print(solu.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))