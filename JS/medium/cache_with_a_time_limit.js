/*
 * https://leetcode.com/problems/cache-with-time-limit/submissions/1336957038/
 */
var TimeLimitedCache = function() {
    this.map = {};
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    let result = false;
    if (key in this.map) {
        clearTimeout(this.map[key].timeoutId);
        result = true;
    }
    else {
        this.map[key] = {};
    };

    const id = setTimeout(() => {
        delete this.map[key]
    }, duration);

    this.map[key].value = value;
    this.map[key].timeoutId = id;
    return result;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (this.map[key]) {
        return this.map[key].value;
    }
    else {
        return -1;
    }
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return Object.keys(this.map).length;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */
