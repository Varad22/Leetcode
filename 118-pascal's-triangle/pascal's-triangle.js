/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    let rows = [...Array(numRows)].fill([1]);
    for( let i= 1; i<=numRows; i++){
        rows[i-1]=[...Array(i)].fill(1);
    };
    for(let i=0; i<rows.length; i++){
        for( let j=0; j< rows[i].length; j++){
            if (rows[i].length>2 && j>0 && rows[i].length-1>j){
                rows[i][j]=rows[i-1][j]+rows[i-1][j-1]
            };
        };
    };
    return rows
};
