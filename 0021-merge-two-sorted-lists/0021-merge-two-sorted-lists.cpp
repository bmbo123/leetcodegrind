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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1 == nullptr && list2 == nullptr){
        return nullptr;
        }else if(list1 == nullptr){
            return list2;
        }else if(list2 == nullptr){
            return list1;
        }
        ListNode* head = new ListNode(0);
        ListNode* tail;
        tail = head;

        while(list1 != nullptr && list2 != nullptr){
            if(list1->val > list2->val){
                tail->next = list2;
                list2 = list2->next;
            }else{
                tail->next = list1;
                list1 = list1->next;
            }
            tail = tail->next;
        }
        if(list1 == nullptr){
            tail->next = list2;
        }
         if(list2 == nullptr){
            tail->next = list1;
        }
        return head->next;
    }
};