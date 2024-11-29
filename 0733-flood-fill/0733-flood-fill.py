class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def bfs(image, l, r, color, old):
            if l < 0 or l>= len(image) or r < 0 or r >= len(image[0]) or image[l][r]!= old:
                return
            image[l][r] = color
            bfs(image,l+1,r,color,old)
            bfs(image,l-1,r,color,old)
            bfs(image,l,r+1,color,old)
            bfs(image,l,r-1,color,old)
        
        old = image[sr][sc]

        if old == color:
            return image
        else:
            bfs(image,sr,sc,color,old)
            return image
