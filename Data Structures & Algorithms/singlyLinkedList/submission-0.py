class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(-1) #Used a dummy node. It simplifies removal from the linked list
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current_node = self.head
        i = 0
        while current_node.next is not None:
            current_node = current_node.next
            if i == index:
                return current_node.val
            i += 1

        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

        if not node.next:
            self.tail = node


    def insertTail(self, val: int) -> None:
        node = Node(val)
        # node.next = self.tail.next Removed it because it's a repetition. node.next is alredy initialized to None when a new node is created
        self.tail.next = node

        self.tail = node

    def remove(self, index: int) -> bool:
        prev_node = self.head
        curr_node = self.head

        i = 0
        while curr_node.next:
            prev_node = curr_node
            curr_node = curr_node.next

            if i == index:
                prev_node.next = curr_node.next

                if curr_node == self.tail:
                    self.tail = prev_node

                return True

            i += 1
        return False

    def getValues(self) -> List[int]:
        curr_node = self.head.next  # head points to the dummy node, so head.next is the first real node
        linked_list = []
        while curr_node:
            linked_list.append(curr_node.val)

            curr_node = curr_node.next
        
        return linked_list

        
