/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* curr;
        ListNode* prev;
        prev = nullptr;
        if(head == nullptr){
            return nullptr;
        }
        while(head != nullptr && head->val == val){
            ListNode* temp = head;
            head = head->next;
            delete temp;
        }
        curr = head;
        while(curr != nullptr){
            if(curr->val == val){
            ListNode* temp;
            temp = curr;
            prev->next = curr->next;
            curr = curr->next;
            delete temp;
            }else{
                prev = curr;
                curr = curr->next;
            }
        }
        return head;
    }
};