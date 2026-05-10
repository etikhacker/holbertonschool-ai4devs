public class bug5 {

    public static int sumArray(int[] arr) {
        int total = 0;
        for (int i = 0; i <= arr.length; i++) {
            total += arr[i];
        }
        return total;
    }

    public static String repeatString(String text, int times) {
        String result = "";
        for (int i = 1; i < times; i++) {
            result += text;
        }
        return result;
    }

    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};
        System.out.println("Sum: " + sumArray(numbers));

        System.out.println(repeatString("hello ", 3));
    }
}