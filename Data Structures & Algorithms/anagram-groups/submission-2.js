class Solution {
    /**
     * Groups items by a key produced from each item by the given mapper function.
     *
     * @template T
     * @param {function(T): string} fn - Function that maps an item to a group key.
     * @param {Iterable<T>} iterable - Items to group.
     * @returns {{[key: string]: T[]}} An object where each key is a group and the value is the array of items in that group.
     */
    groupBy(fn, iterable) {
        const grouped = Object.create(null)
        for (const item of iterable) {
            const groupKey = fn(item)
            if (!Object.hasOwn(grouped, groupKey)) grouped[groupKey] = []
            grouped[groupKey].push(item)
        }
        return grouped
    }
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const groupedByAnagrams = this.groupBy(str => str.split("").sort().join(""), strs)
        return Object.values(groupedByAnagrams)
    }
}
