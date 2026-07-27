class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        s = s.toLowerCase()
            .split("")
            .filter(x => (
                (x >= 'a' && x <= 'z') || 
                (x >= '0' && x <= '9')
            ))
            
        let start = 0
        let end = s.length - 1

        while (start < end) {
            if (s[start] !== s[end]) return false
            start += 1
            end -= 1
        }

        return true
    }
}
