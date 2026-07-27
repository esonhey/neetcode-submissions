class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        s = s.toLowerCase().split("").filter(x => {
            const charCode = x.charCodeAt(0)
            return (charCode >= 97 && charCode <= 122) || (charCode >= '0'.charCodeAt(0) && charCode <= '9'.charCodeAt(0))
            })
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
