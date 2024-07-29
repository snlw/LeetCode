/**
 * https://leetcode.com/problems/check-if-object-instance-of-class/submissions/1336960966/
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    while (obj != null) {
        if (obj.constructor == classFunction) {
            return true;
        }
        obj = Object.getPrototypeOf(obj)
    };
    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
