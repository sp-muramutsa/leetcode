class Node:
    def __init__(self, value: int):
        self.value = value
        self.prev = None
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.max_size = k
        self.curr_size = 0
        self.front = Node(-1)
        self.rear = Node(1001)
        self.front.prev = self.rear
        self.rear.next = self.front

    def enQueue(self, value: int) -> bool:
        """
        Inserts an element into the circular queue. Return true if the operation is successful.
        - self.rear -> <- self.front
        - if full:
            - return False

        - new_node with val
        - Isolate the node formally at the back: self.rear.next
            - Our new node is going to point at this node with its next pointer
            - This node is going to point to our new node with its prev pointer
        - Reconnect the rear tracker to the new node
            - rear track next points to new node
            - new node prev points to rear trackers
        - Increment curr_size
        """

        if self.curr_size >= self.max_size:
            return False

        # 1
        new_node = Node(value)
        old_rear_node = self.rear.next
        new_node.next = old_rear_node
        old_rear_node.prev = new_node

        # 2
        self.rear.next = new_node
        new_node.prev = self.rear

        # 3
        self.curr_size += 1

        return True

    def deQueue(self) -> bool:
        """
        Deletes an element from the circular queue. Return true if the operation is successful.

        - isolate the node at the front
            - old_front = self.front.prev
        - get its prev i.e. new front node
            - new_front = old_front.prev

        - Redo front tracker connection
            - new_front.next = self.front
            - self.front.prev = new_front

        """

        if self.curr_size <= 0:
            return False
        # 1
        old_front = self.front.prev

        # 2
        new_front = old_front.prev

        # 3
        new_front.next = self.front
        self.front.prev = new_front

        self.curr_size -= 1
        return True

    def Front(self) -> int:
        """
        Gets the front item from the queue. If the queue is empty, return -1.
        """

        if self.curr_size <= 0:
            return -1
        return self.front.prev.value

    def Rear(self) -> int:
        """
        Gets the last item from the queue. If the queue is empty, return -1.
        """

        if self.curr_size <= 0:
            return -1
        return self.rear.next.value

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.curr_size <= 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.curr_size >= self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

