class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freqs = {}
        for (const num of nums) {
            freqs[num] = (freqs[num] ?? 0) + 1
        }
        return Object
                .entries(freqs)
                .sort(([n1_, freq1], [n2_, freq2])=> freq2 - freq1)
                .slice(0, k)
                .map(([n, freq_]) => n)
    }
}
