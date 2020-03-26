#include <stdio.h>
/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* cur = head;
        while(cur != NULL) 
        {
            ListNode *Next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = Next;
        }
        return prev;
    }
};

int main()
{
    ListNode *node,*node1,*node2,*node3,*node4;
    node->val = 1;
    node->next = node1;
    node1->val = 2;
    node1->next = node2;
    node2->val = 3;
    node2->next = node3;
    node3->val = 4;
    node3->next = node4;
    node4->val = 5;
    Solution A;
    ListNode* result = A.reverseList(node);
    while (result != NULL)
    {
        printf("%d\n", result->val);
        result = result->next;
    }
    return 0;
}