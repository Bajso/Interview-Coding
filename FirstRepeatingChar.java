// Java program to find the first repeated character in a string
import java.util.*;

public class FirstRepeatingCharacter {

    public static char firstRepeating(String s) {
        // Creates an empty hashset
        HashSet<Character> hashSet = new HashSet<>();
        // Or an empty hashmap
        HashMap<Character, Integer> hashMap = new HashMap<>();

        char[] charArr = s.toCharArray();

        for(char c: charArr) {
            // check if element in hashset
            if(hashSet.contains(c)) {
                return c;
            }
            hashSet.add(c);
        }

        for(char c: charArr) {
            // get count, if greater than
            if (hashMap.get(c) != null) {
                return c;
            }
            hashMap.put(c, 1);
        }

        return '0';
    }

    public static void main(String[] args) {
        String s = "thisisteststring";
        s = s.toLowerCase();
        System.out.println(firstRepeating(s));
    }
}
