/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    let m = matrix.length;
    let n = matrix[0].length;
    console.log(m,n);
    let cols = new Array(m);
    let rows = new Array(n);
    for(let i=0; i<m; i++){
        for(let j=0; j<n; j++){
            if(matrix[i][j]==0){
                cols[i]=1;
                rows[j]=1;
            };
        };
    };
    for(let i=0; i<m; i++){
        for(let j=0; j<n; j++){
            if(cols[i]==1 || rows[j]==1){
                matrix[i][j]=0;
            };
        };
    };
};
