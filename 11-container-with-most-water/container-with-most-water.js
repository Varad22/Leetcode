/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let startIdx = 0;
    let endIdx = (height.length) -1;
    let area = 0;
    while(endIdx>startIdx){
        area = Math.max(area, Math.min(height[endIdx],height[startIdx]) *(endIdx-startIdx));
        if(height[endIdx] > height[startIdx]){
            startIdx+=1;
        }
        else{
            endIdx-=1;
        }
    };
    return area;
};
