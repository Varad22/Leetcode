/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let median = 0;
    if(nums1.length > 0){
        for(let i=0; i<nums2.length; i++){
            nums1.push(nums2[i]);
        };
    }
    else{
        nums1=nums2;
    };
    if((nums1.length)%2==1){
        median = nums1.sort(function(a, b){return a-b})[Math.floor((nums1.length)/2)];
    }
    else if((nums1.length)%2==0){
        median = (nums1.sort(function(a, b){return a-b})[Math.floor((nums1.length)/2)] + nums1.sort(function(a, b){return a-b})[(Math.floor((nums1.length)/2))-1])/2;
    };
return median
};
