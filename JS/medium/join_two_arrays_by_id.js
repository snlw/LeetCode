/**
 * https://leetcode.com/problems/join-two-arrays-by-id/submissions/1336834315/
 * reduce() hits TLE on a test case.
 
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const mp = {}
    const arr = arr1.concat(arr2)

    arr.map((e) => {
        if (mp[e.id]){
            mp[e.id] = {...mp[e.id], ...e}
        }
        else {
            mp[e.id] = e
        }
    })
    return Object.values(mp)
};
