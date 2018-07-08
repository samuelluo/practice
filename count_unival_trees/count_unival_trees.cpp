// g++ -std=c++17 count_unival_trees.cpp
/*
A unival tree (which stands for "universal value") is a tree where all nodes
under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
*/

// works: new Node; new Node();
// works: root_node = new Node; Node* root = &root;
// does not work: new Node('a'); no constructor & not type Node*
#include <iostream>

// --------------------------------------------------------
struct Node {
    // Forward declarations can only be defined as pointers
    char val;
    Node* left;
    Node* right;
};

Node* newNode(char val) {
    Node* root = new Node;
    root->val = val;
    root->left = NULL;
    root->right = NULL;
    return root;
}

// --------------------------------------------------------
bool is_unival(Node* root, char val) {
    if (root == NULL) return true;
    bool curr_match = root->val == val;
    bool left_match = is_unival(root->left, val);
    bool right_match = is_unival(root->right, val);
    return curr_match && left_match && right_match;
}
bool is_unival(Node* root) {
    return is_unival(root, root->val);
}
int count_unival_trees_1(Node* root) {
    /*
    Problem:
    For root.left, checking is_unival() twice - once for root, once for root.left
    */
    if (root == NULL) return 0;
    int num_unival = 0;
    num_unival += count_unival_trees_1(root->left);
    num_unival += count_unival_trees_1(root->right);
    if (is_unival(root)) num_unival += 1;
    return num_unival;
}
// --------------------------------------------------------
std::pair<int, bool> count_unival_trees_2_helper(Node* root) {
    if (root == NULL) return std::pair<int, bool>(0, true);
    int num_unival = 0;
    auto[num_left, left_unival]   = count_unival_trees_2_helper(root->left);
    auto[num_right, right_unival] = count_unival_trees_2_helper(root->right);
    num_unival = num_left + num_right;
    if ((left_unival && right_unival) &&
        (root->left == NULL || root->val == root->left->val) &&
        (root->right == NULL || root->val == root->right->val)) {
        return std::pair<int, bool>(num_unival + 1, true);
    } else {
        return std::pair<int, bool>(num_unival, false);
    }
}
int count_unival_trees_2(Node* root) {
    auto[count, is_unival] = count_unival_trees_2_helper(root);
    return count;
}

// --------------------------------------------------------
void count_unival_trees(Node* root) {
    bool result = is_unival(root);
    if (result) {
        std::cout << "Is a unival tree" << std::endl;
    } else {
        std::cout << "Not a unival tree" << std::endl;
    }
    int count = count_unival_trees_1(root);
    std::cout << count << std::endl;
    count = count_unival_trees_2(root);
    std::cout << count << std::endl;
    std::cout << std::endl;
}

// --------------------------------------------------------
int main() {
    Node* root;

    // Answer: 3
    root = newNode('a');
    root->left = newNode('a');
    root->right = newNode('a');
    count_unival_trees(root);

    // Answer: 3
    root = newNode('a');
    root->left = newNode('a');
    root->right = newNode('a');
    root->right->left = newNode('a');
    root->right->right = newNode('A');
    count_unival_trees(root);

    // Answer: 5
    root = newNode('a');
    root->left = newNode('c');
    root->right = newNode('b');
    root->right->left = newNode('b');
    root->right->right = newNode('b');
    root->right->right->right = newNode('b');
    count_unival_trees(root);

    // Answer: 2
    root = newNode('b');
    root->right = newNode('b');
    count_unival_trees(root);
}