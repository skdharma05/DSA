public class Main {

    public static int binarySearch(int[] nums, int target) {
        int n = nums.length;
        int low = 0;
        int high = n - 1;

        while (low <= high) {
            int mid = (low + high) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (target > nums[mid]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] num = {-1, 0, 3, 5, 9, 12};
        int result = binarySearch(num, 9);
        System.out.println(result);
    }
}
