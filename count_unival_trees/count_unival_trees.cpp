// g++ -std=c++14 count_unival_trees.cpp
#include <iostream>

// ----------------------------------------
struct Node {
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
int main() {
    Node* root = newNode('a');
    root->left = newNode('a');
    root->right = newNode('a');
    bool result = is_unival(root);
    if (result) std::cout << "Is a unival tree" << std::endl;
    else std::cout << "Not a unival tree" << std::endl;    
    int count = count_unival_trees(root);
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

    root = newNode('b');
    root->right = newNode('b');
    result = is_unival(root);
    if (result) std::cout << "Is a unival tree" << std::endl;
    else std::cout << "Not a unival tree" << std::endl;
    count = count_unival_trees(root);
    std::cout << count << std::endl;
}