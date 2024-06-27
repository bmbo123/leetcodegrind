/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(headA == nullptr || headB == nullptr){
            return nullptr;
        }
        ListNode* A = headA;
        ListNode* B = headB;
        unordered_map<ListNode*, int> hashmap;
        while(A != nullptr){
            hashmap[A] = 1;
            A = A->next;
        }
        while(B != nullptr){
            if(hashmap.find(B) != hashmap.end()){
                return B;
            }
            B = B->next;
        }
        return nullptr;

    }
};