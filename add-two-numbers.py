""" Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807. """

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def __init__(self):
        self.head = None          
    def insert_at_end(self, data):
        if self.head is None:
            self.head = ListNode(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next
        itr.next = ListNode(data, None)  
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
                          
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        result_head = ListNode(0) #we need to keep track of the head of the llist, to return it after
        result = result_head # so we just copy the head in this result variable
        val1 = ''
        val2 = ''
        while p:
            val1 += str(p.val) # we iterate over llist1, and we will store the values as a string "1234" 
            p=p.next
            
        while q:
            val2 += str(q.val) # we do the same with other llist
            q=q.next
            
        sum_vals = int(val1[::-1]) + int(val2[::-1]) # now, the sum the two values, but first we reverse it, it's pretty straighforward
        sum_vals = str(sum_vals)[::-1] # the sum of that we also reverse it.
        for i in sum_vals:  #now, we travel for our string characters and just create a new node and put the number in it
            newNode = ListNode(i)
            result.next = newNode
            result = result.next

        return result_head.next
        # itr1 = l1
        # itr2 = l2
        
        # result_head = ListNode(0)
        # result = result_head

        # list1_sum = ''
        # list2_sum = ''
        
        # while itr1:
        #     print(itr1.val)
        #     list1_sum += str(itr1.val)
        #     itr1 = itr1.next      
        # while itr2:
        #     list2_sum += str(itr2.val)
        #     itr2 = itr2.next
        # sum_value = int(list1_sum[::-1]) + int(list2_sum[::-1])
        # print(sum_value)
        # sum_value = str(sum_value[::-1])
        # print(sum_value)                        
        
if __name__ == '__main__':
    l1 = Solution()
    l1.insert_values([2,4,3])
    #l1.print()
    l2 = Solution()
    l2.insert_values([5,6,4])
    #l2.print()
    l3 = Solution()
    l3.addTwoNumbers(l1,l2)
    #print(response)
        