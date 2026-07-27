class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false
        
        let charset = Array(26).fill(0)
        for (let i = 0; i < s.length; i++){
            charset[s.charCodeAt(i) - 97] += 1
            charset[t.charCodeAt(i) - 97] -= 1
        }
        return charset.every(x => x === 0)
    }
}
