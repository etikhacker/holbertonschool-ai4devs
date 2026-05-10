// bug6.java
// Intended behavior: Check whether a given string is a palindrome.
// Ignore case and non-alphanumeric characters (e.g. "A man, a plan, a canal: Panama" → true).

public class bug6 {

    public static boolean isPalindrome(String s) {
        // BUG: replaceAll pattern keeps only letters, but digits should also be kept
        String cleaned = s.replaceAll("[^a-zA-Z]", "").toLowerCase();
        //                                              correct pattern: [^a-zA-Z0-9]

        int left = 0;
        int right = cleaned.length();   // BUG: should be cleaned.length() - 1
                                        //      causes StringIndexOutOfBoundsException

        while (left < right) {
            if (cleaned.charAt(left) != cleaned.charAt(right)) {  // BUG: right is out of bounds
                return false;
            }
            left++;
            right++;    // BUG: should be right-- (moving inward, not outward)
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome("racecar"));                      // expected: true
        System.out.println(isPalindrome("hello"));                        // expected: false
        System.out.println(isPalindrome("A man a plan a canal Panama"));  // expected: true
        System.out.println(isPalindrome("Was it a car or a cat I saw")); // expected: true
        System.out.println(isPalindrome("race a car"));                   // expected: false
    }
}
