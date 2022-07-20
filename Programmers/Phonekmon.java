import java.util.*;

public class Phonekmon {
    public int solution(int[] nums) {
        int[] disnum = Arrays.stream(nums).distinct().toArray();
        if (nums.length/2 > disnum.length) return disnum.length;
        else return nums.length/2;
    }
}
