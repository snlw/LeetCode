/**
 * https://leetcode.com/problems/memoize/submissions/1336838936/
 * This uses the closure function in JS 
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const memoMap = {}
    return function(...args) {
        const key = JSON.stringify(args);
        if (key in memoMap) {
            return memoMap[key];
        }
        const result = fn(...args);
        memoMap[key] = result
        return result;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
