class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target: number, position: number[], speed: number[]): number {
        const combined = position.map((p, idx) =>  [p, speed[idx]]).sort(([a], [b]) => b - a)
        const fleets = combined.reduce((fleets, [p, s]) => {
            const count = (target-p) / s
            if (!fleets.length) {
                fleets.push(count)
            } else {
                const top = fleets[fleets.length - 1]
                if (count > top) {
                    fleets.push(count)
                }

            }
            return fleets
        }, [])

        return fleets.length

    }
}
