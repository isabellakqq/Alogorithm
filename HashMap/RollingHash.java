/*
Input: source, target
Output: int index 
        abcdef  bcd 1
    Return -1 if not exits

High-level:
    n = len(source), m = len(target)
    hash(taget)  // O(m)
    s_hash = hash(source[0:m]) // O(m)

    for i from 0 to n - m:
        if hash(source[i:i+m]) != hash(taget): continue   // O(1) -- rolling hash
        else:  check source[i:i+m] == taget => return i   // O(m) -- on average, if the hash function is good enough, this line runs at most c times, c is a contant number
    return -1
    
 Best-case: O(2m + 1*m + (n - m - 1) * 1) = O(n + 2m - 1) = O(n + m)
 Average-case: O(2m + c*m + (n - m - c) * 1) = O(n + (c + 1)*m - 1) = O(n + m)  // emphaszie 
 Space : O(1)


 hash(source[i:i+m]) -- O(1)

Rolling Hash: 
    shash(abc) = 31^2 * a + 31^1 * b + c
    shash(bcd) = 31^2 * b + 31^1 * c + d = shash(abc) * 31 + d - 31^3 * a

    s = abcdef, target = def
    sHash(abc), shash(bcd) = shash(abc) * 31
    tHash(def) 


source = "abcdef",
target = "bcd"
return 0
*/
public class Solution { 
    public int strStr2(String source, String target) {
        if (source == null || target == null || target.length() > source.length()) {
            return -1;
        }

        int sLen = source.length(); // 3
        int tLen = target.length(); // 0
        int sHash = 0;
        int tHash = 0;
        int power = 1;
        int base = 31;
        int mod = 10000007;
        for (int i = 0; i < tLen; i++) {
            sHash = (sHash * base + source.charAt(i)) % mod;
            tHash = (tHash * base + target.charAt(i)) % mod;
            power = (power * base) % mod;
        }
        
        for (int i = 0; i <= sLen - tLen; i++) { 
            if (i > 0) {
                // shash(abc) * 31 + d - 31^3 * a
                sHash = Math.floorMod((sHash * base + source.charAt(i + tLen - 1)) % mod - power * source.charAt(i - 1), mod);
            }
            if (sHash == tHash && source.substring(i, i + tLen).equals(target)) {
                return i;
            }
        }

        return -1;
    }
}