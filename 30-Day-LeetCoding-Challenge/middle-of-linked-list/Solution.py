# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        return nodes[len(nodes) // 2]

def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for elem in arr[1:]:
        new_node = ListNode(elem)
        current.next = new_node
        current = new_node
    return head


def print_from_middle(head):
    nodes = []
    while head:
        nodes.append(head.val)
        head = head.next
    return nodes

if __name__ == "__main__":
    sol = Solution()
    
    linked_list = create_linked_list([1,2,3,4,5])
    middle_node = sol.middleNode(linked_list)
    print(print_from_middle(middle_node))

    linked_list = create_linked_list([1,2,3,4,5,6])
    middle_node = sol.middleNode(linked_list)
    print(print_from_middle(middle_node))
