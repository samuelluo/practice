// g++ -std=c++17 count_nodes.cpp
/*
Given a binary tree, count the number of nodes.
*/
#include <iostream>    // std::cout, std::endl
#include <queue>       // std::queue

struct Node {
    int val = 0;
    Node* left = NULL;
    Node* right = NULL;
};

int count_nodes_1(Node* root) {
    if (root == NULL)
        return 0;
    return 1 + count_nodes_1(root->left) + count_nodes_1(root->right);
}

int count_nodes_2(Node* root) {
    std::queue<Node*> node_queue;
    node_queue.push(root);
    int count = 0;
    while (!node_queue.empty()) {
        Node* node = node_queue.front();
        node_queue.pop();
        count += 1;
        if (node->left != NULL)
            node_queue.push(node->left);
        if (node->right != NULL)
            node_queue.push(node->right);
    }
    return count;
}

int main() {
    int result;
    Node* root;
    
    root = new Node; root->val = 1;
    root->left = new Node; root->left->val = 2;
    root->right = new Node; root->right->val = 3;
    root->left->left = new Node; root->left->left->val = 4;
    root->left->right = new Node; root->left->right->val = 5;
    result = count_nodes_1(root);
    std::cout << result << std::endl;
    result = count_nodes_2(root);
    std::cout << result << std::endl;
}