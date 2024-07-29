/**
 * https://leetcode.com/problems/flatten-deeply-nested-array/submissions/1336909121/
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    if ( n == 0 ) {
        return arr
    };

    return arr.reduce((p, c) => {
        if (Array.isArray(c)) {
            p.push(...flat(c, n - 1))
        }
        else {
            p.push(c)
        }

        return p
    }, [])
};
