class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:    
        return [[elem ^ 1 for elem in reversed(image)] for image in image]
        # for im in image:
        #     im.reverse()
        #     for idx in range(len(im)):
        #         im[idx] ^= 1
        # return image
