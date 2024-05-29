class Solution {
    public String reverseVowels(String s) {
        char[] chars = s.toCharArray();
        int endpointer = chars.length - 1;
        for (int i = 0; i < chars.length; i++) {
            if (isVowel(chars[i])) {
                for (int j = endpointer; j > i; j--) {
                    if (isVowel(chars[j])) {
                        char temp = chars[i];
                        chars[i] = chars[j];
                        chars[j] = temp;
                        endpointer = j - 1;
                        break;
                    }
                }
            }
            if (i >= endpointer) {
                break;
            }
        }
        return String.valueOf(chars);
    }

    public boolean isVowel(char c) {
        return c == 'i' || c == 'u' || c == 'o' ||
        c == 'a' ||c == 'e' || c == 'I' || c == 'U' || c == 'O' ||
        c == 'A' ||c == 'E';
    }
}
