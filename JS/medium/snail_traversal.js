/**
 * https://leetcode.com/problems/snail-traversal/submissions/1336949174/
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    if (rowsCount * colsCount != this.length) {
        return [];
    }
    const ans = [];
    for (let i = 0; i < rowsCount; i++) {
        ans.push([]);
    }
    let rowCounter = 0;
    let direction = 1;

    return this.reduce((p, curr) => {
        p[rowCounter].push(curr);
        rowCounter += direction
        if (rowCounter == rowsCount) {
            rowCounter = rowsCount - 1;
            direction = -1
        }
        else if (rowCounter == -1) {
            rowCounter = 0;
            direction = 1
        }
        return p
    }, ans)
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */
