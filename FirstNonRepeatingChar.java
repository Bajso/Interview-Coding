public class FirstNonRepeatingCharacter {

    public static char firstNonrepeatingCharacterInAlphabet(String s) {
        // get char array
        char[] charArr = s.toCharArray();
        // create empty alphabet array
        char[] alphabet = new char[26];
        // initialise values to 0
        for(int i = 0; i < alphabet.length; i++) {
            alphabet[i] = 0;
        }

        int letterA = (int) 'a';
        for(char c: charArr) {
            // get ascii code for each character
            int ascii = (int) c;

            // assign count to each character in the alphabet
            alphabet[ascii - letterA] += 1;
        }

        // loop through the alphabet
        for(int i = 0; i < alphabet.length; i++) {
            if(alphabet[i] == 1){
                return (char) (i + letterA);
            }
        }

        return '0';
    }

    public static char firstNonRepeatingCharacterInString(String s) {
        // get char array
        char[] charArr = s.toCharArray();
        // create empty alphabet array
        char[] alphabet = new char[26];
        // initialise values to 0
        for(int i = 0; i < alphabet.length; i++) {
            alphabet[i] = 0;
        }

        int letterA = (int) 'a';
        for(char c: charArr) {
            // get ascii code for each character
            int ascii = (int) c;

            // assign count to each character in the alphabet
            alphabet[ascii - letterA] += 1;
        }

        // loop through the string
        for(char c: charArr) {
            if(alphabet[(int) c - letterA] == 1) {
                return c;
            }
        }

        return '0';
    }


    public static void main(String[] args) {
        String testString = "yisthistrue";
        testString = testString.toLowerCase();
        System.out.println(firstNonrepeatingCharacterInAlphabet(testString));
        System.out.println(firstNonRepeatingCharacterInString(testString));

    }

}
