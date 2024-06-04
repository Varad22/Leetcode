/**
 * @param {string} s
 * @return {number}
 */


var lengthOfLongestSubstring = function(s) {
    let lst=[];
    let lengths=[];
    let value=0;
    if(s.length>0){
        if(s!=" "){
            for(let i=0; i<s.length; i++){
                if(s[i] != " "){
                    if(lst.includes(s[i])==false){
                        lst.push(s[i]);
                        lengths.push(parseInt(lst.length));
                    }
                    else if(lst.includes(s[i]) && s[i]==s[i-1]){
                        lst=[];
                        lst.push(s[i]);
                        lengths.push(parseInt(lst.length));
                    }
                    else if(lst.includes(s[i])){
                        lst=lst.slice(lst.indexOf(s[i])+1);
                        lengths.push(parseInt(lst.length));
                        lst.push(s[i]);
                    }
                }
                else if(s[i]==" "){
                    lengths.push(parseInt(lst.length));
                    lst=[];
                    lst.push(s[i]);
                };    
            };
        }
        else{
                lengths=[1];
        };     
    }
    else{
        lengths=[0]
    };
    value=Math.max(...lengths);
    return value
};
