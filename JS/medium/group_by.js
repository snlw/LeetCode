/**
 * https://leetcode.com/problems/group-by/submissions/1336902305/
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    return this.reduce((p, c) => {
        const key = fn(c);
        if (key in p) {
            p[key].push(c)
        }
        else {
            p[key] = [c]
        }
        return p
    }, {})
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
