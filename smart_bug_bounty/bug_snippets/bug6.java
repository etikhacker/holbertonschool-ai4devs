public class bug6 {

    public static boolean isPalindrome(String s) {
        String cleaned = s.replaceAll("[^a-zA-Z]", "").toLowerCase();

        int left = 0;
        int right = cleaned.length();

        while (left < right) {
            if (cleaned.charAt(left) != cleaned.charAt(right)) {
                return false;
            }
            left++;
            right++;
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome("racecar"));
        System.out.println(isPalindrome("hello"));
        System.out.println(isPalindrome("A man a plan a canal Panama"));
        System.out.println(isPalindrome("Was it a car or a cat I saw"));
        System.out.println(isPalindrome("race a car"));
    }
}