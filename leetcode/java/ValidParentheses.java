import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class ValidParentheses {

    public static void main(String[] args) {
        System.out.println(new ValidParentheses().isValid("({{{{}}}))"));
    }

    public boolean isValid(String s) {
        Map<Character, Character> brackets = Map.of(
                ')', '(',
                ']', '[',
                '}', '{'
        );

        List<Character> stack = new ArrayList<>();

        for (char c : s.toCharArray()) {
            if (brackets.containsValue(c)) { // Opening
                stack.add(c);

            } else if (brackets.containsKey(c)) { // Closing
                if (stack.isEmpty() || !stack.getLast().equals(brackets.get(c))) {
                    return false;
                }

                stack.removeLast();
            } else {
                return false; // Invalid char
            }
        }

        return stack.isEmpty();
    }

}
