// Brute force approach
// 1. Checks if the target string contains the * wildcard
// 2. If so it iterates through each string in the array given
//      1. Check if the target string and current word are of comparable size
//      2. IF comparable get the target string's wildcard index
//      3. Remove the wild card from the target string
//      4. Remove the characterd from the curr string at the wildcard's index
//      5. Compare the stripped target and current strings return TRUE if match
// 3. If no wildcard is found or the wildcard for loop doesn't find a match rely on javascript's array includes to return a match

// NOTES: Time and space complexity likely O(n2) or worse since it's a brute force method

class stringSearch {
    constructor(strArray) {
        this.dict = strArray;
    }
    
    isInDict(targetStr) {
        if(targetStr.indexOf('*') > -1) {
            for(let i = 0; i < this.dict.length; i++) {
                const currStr = this.dict[i];
                if(targetStr.length === currStr.length) {
                    const wildCardIndex = targetStr.indexOf('*');
                    const cleanTargetStr = targetStr.slice(0,wildCardIndex) + targetStr.slice(wildCardIndex + 1);
                    const cleanCurrStr = currStr.slice(0,wildCardIndex) + currStr.slice(wildCardIndex + 1);

                    if(cleanTargetStr === cleanCurrStr) {
                        return true;
                    }
                }
            }
        }
        
        return this.dict.includes(targetStr);
    }
}

const test = new stringSearch(['cat', 'car', 'bar']);
console.log(test.isInDict('ba*'));