// g++ -std=c++17 count_unival_trees.cpp
#include <iostream>

// ----------------------------------------
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

// ----------------------------------------
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
int count_unival_trees(Node* root) {
    /*
    Problem:
    For root.left, checking is_unival() twice - once for root, once for root.left
    */
    if (root == NULL) return 0;
    int num_unival = 0;
    num_unival += count_unival_trees(root->left);
    num_unival += count_unival_trees(root->right);
    if (is_unival(root)) num_unival += 1;
    return num_unival;
}
// ----------------------------------------
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

// ----------------------------------------
int main() {
    // works: new Node, new Node();
    // does not work: new Node('a'); no constructor & not type Node*
    // root_node = new Node; Node* root = &root;
    Node* root = newNode('a');
    root->left = newNode('a');
    root->right = newNode('a');
    bool result = is_unival(root);
    if (result) std::cout << "Is a unival tree" << std::endl;
    else std::cout << "Not a unival tree" << std::endl;
    int count = count_unival_trees(root);
    std::cout << count << std::endl;
    count = count_unival_trees_2(root);
    std::cout << count << std::endl;

    root = newNode('a');
    root->left = newNode('a');
    root->right = newNode('a');
    root->right->left = newNode('a');
    root->right->right = newNode('A');
    result = is_unival(root);
    if (result) std::cout << "Is a unival tree" << std::endl;
    else std::cout << "Not a unival tree" << std::endl;
    count = count_unival_trees(root);
    std::cout << count << std::endl;
    count = count_unival_trees_2(root);
    std::cout << count << std::endl;

    root = newNode('a');
    root->left = newNode('c');
    root->right = newNode('b');
    root->right->left = newNode('b');
    root->right->right = newNode('b');
    root->right->right->right = newNode('b');
    result = is_unival(root);
    if (result) std::cout << "Is a unival tree" << std::endl;
    else std::cout << "Not a unival tree" << std::endl;
    count = count_unival_trees(root);
    std::cout << count << std::endl;
    count = count_unival_trees_2(root);
    std::cout << count << std::endl;

    root = newNode('b');
    root->right = newNode('b');
    result = is_unival(root);
    if (result) std::cout << "Is a unival tree" << std::endl;
    else std::cout << "Not a unival tree" << std::endl;
    count = count_unival_trees(root);
    std::cout << count << std::endl;
    count = count_unival_trees_2(root);
    std::cout << count << std::endl;
}