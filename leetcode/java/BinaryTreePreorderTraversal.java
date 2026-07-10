import java.util.ArrayList;
import java.util.List;

public class BinaryTreePreorderTraversal {
    /**
     * First solve for left so go left until I get as null? Then go back up solve for right
     */
    public List<Integer> preorderTraversal(TreeNode root) {
        var result = new ArrayList<Integer>();
        goLeft(root, result);
        return result;
    }

    private void goLeft(TreeNode root, List<Integer> result) {
        if (root == null) {
            return;
        }
        result.add(root.val);
        goLeft(root.left, result);
        goLeft(root.right, result);
    }
}
