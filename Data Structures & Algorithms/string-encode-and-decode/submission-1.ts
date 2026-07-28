class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs: string[]): string {
        let encoded = ""
        for (const str of strs) {
            encoded += `${str.length}-${str}`
        }
        return encoded
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str: string): string[] {
        const decoded = []
        const strArr = str.split('')
        while (strArr.length !== 0) {
            const sepIdx = strArr.findIndex(x => x === '-')
            const length = Number(strArr.slice(0, sepIdx).join(''))
            decoded.push(strArr.slice(sepIdx+1, sepIdx + length + 1).join(''))
            strArr.splice(0, sepIdx + length + 1)
        }
        return decoded
    }
}
