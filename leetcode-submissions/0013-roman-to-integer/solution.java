class Solution {
    public int romanToInt(String s) {
        if (s == null) return 0;
        char[] romans = s.toCharArray();
        int result = 0;
        int size = 0;
        for (int i = 0; i < romans.length; i += size) {
            if (i + 1 < romans.length && followingPair(romans[i], romans[i + 1]) != 0) {
                result += followingPair(romans[i], romans[i + 1]);
                size = 2;
            } else if (romanTranslate(romans[i]) != 0) {
                result += romanTranslate(romans[i]);
                size = 1;
            } else {
                return 0;
            }
        }
        return result;
    }



    public int romanTranslate(char x) {
        if (x == 'I') return 1;
        else if (x == 'V') return 5;
        else if (x == 'X') return 10;
        else if (x == 'L') return 50;
        else if (x == 'C') return 100;
        else if (x == 'D') return 500;
        else if (x == 'M') return 1000;
        else return 0;
    }

    public int followingPair(char a, char b) {
        if (a == 'I' && b == 'V') return 4;
        else if (a == 'I' && b == 'X') return 9;
        else if (a == 'X' && b == 'L') return 40;
        else if (a == 'X' && b == 'C') return 90;
        else if (a == 'C' && b == 'D') return 400;
        else if (a == 'C' && b == 'M') return 900;
        else return 0;
    }
}
