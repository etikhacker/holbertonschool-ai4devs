public class bug5_fixed {

    public static int sumArray(int[] arr) {
        int total = 0;
        for (int i = 0; i < arr.length; i++) {
            total += arr[i];
        }
        return total;
    }

    public static String repeatString(String text, int times) {
        String result = "";
        for (int i = 0; i < times; i++) {
            result += text;
        }
        return result;
    }

    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};
        assert sumArray(numbers) == 15 : "Test 1 failed";
        assert sumArray(new int[]{}) == 0 : "Test 2 failed";
        assert repeatString("hello ", 3).equals("hello hello hello ") : "Test 3 failed";
        assert repeatString("ab", 2).equals("abab") : "Test 4 failed";
        System.out.println("bug5_fixed.java: All tests passed");
        System.out.println("Sum: " + sumArray(numbers));
        System.out.println(repeatString("hello ", 3));
    }
}
