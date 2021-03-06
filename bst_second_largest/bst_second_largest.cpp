// g++ -std=c++17 bst_second_largest.cpp
/*
Given the root to a binary search tree, find the second largest node in the tree.
*/

#include <deque>       // std::deque
#include <iostream>    // std::cout, std::endl

// ------------------------------------------------------------------
struct Node {
    // Forward declarations can only be defined as pointers
    int val;
    Node* left;
    Node* right;
};

Node* newNode(int val) {
    Node* root = new Node;
    root->val = val;
    root->left = NULL;
    root->right = NULL;
    return root;
}

Node* bst_insert(Node* root, int val) {
    if (root == NULL)
        return newNode(val);
    if (val < root->val)
        root->left = bst_insert(root->left, val);
    else if (val > root->val)
        root->right = bst_insert(root->right, val);
    return root;
}

// ------------------------------------------------------------------
void bst_second_largest_1(Node* root) {
    int largest = 0;
    int second_largest = 0;
    std::deque<Node*> queue = {root};
    while (!queue.empty()) {
        Node* node = queue.front();
        queue.pop_front();
        if (node->val > largest) {
            second_largest = largest;
            largest = node->val;
        }
        else if (node->val > second_largest) {
            second_largest = node->val;
        }
        if (node->left != NULL) {
            queue.push_back(node->left);
        }
        if (node->right != NULL) {
            queue.push_back(node->right);
        }
    }
    std::cout << "Second largest: " << second_largest << std::endl;
}

int bst_second_largest_2_helper(Node* root, int count) {
    if (root == NULL) {
        return count;
    }
    count = bst_second_largest_2_helper(root->right, count);
    count += 1;
    if (count == 2) {
        std::cout << "Second largest: " << root->val << std::endl;
    }
    count = bst_second_largest_2_helper(root->left, count);
    return count;
}

void bst_second_largest_2(Node* root) {
    /*
    For a BST, in-order traversal will pass through the nodes in
    increasing order.
    Use reverse in-order traversal to pass through nodes in 
    decreasing order.
    */
    bst_second_largest_2_helper(root, 0);
}

// ------------------------------------------------------------------
int main() {
    Node* root;

    // Answer: 7
    root = newNode(5);
    root = bst_insert(root, 3);
    root = bst_insert(root, 2);
    root = bst_insert(root, 4);
    root = bst_insert(root, 7);
    root = bst_insert(root, 6);
    root = bst_insert(root, 8);
    bst_second_largest_1(root);
    bst_second_largest_2(root);
    std::cout << std::endl;

    // Answer: 4
    root = newNode(1);
    root = bst_insert(root, 2);
    root = bst_insert(root, 3);
    root = bst_insert(root, 4);
    root = bst_insert(root, 5);
    bst_second_largest_1(root);
    bst_second_largest_2(root);
    std::cout << std::endl;
}
