##############3 Three in One##############
class MultiStack:
    def __init__(self, n_stacks, size):
        self.stacklist = [None] * (n_stacks * size)  # The combined storage for all stacks
        self.n_stacks = n_stacks
        self.size = size  # Maximum size of each stack
        self.sizes = [0] * n_stacks  # Current sizes of each stack

    def is_full(self, stack_number):
        if stack_number >= self.n_stacks or stack_number < 0:
            return None
        return self.sizes[stack_number] == self.size

    def is_empty(self, stack_number):
        if stack_number >= self.n_stacks or stack_number < 0:
            return None
        return self.sizes[stack_number] == 0

    def push(self, stack_number, value):
        if stack_number >= self.n_stacks or stack_number < 0:
            raise IndexError("Invalid stack number.")
        if self.is_full(stack_number):
            raise OverflowError(f"Stack {stack_number} is full.")
        index = stack_number * self.size + self.sizes[stack_number]
        self.stacklist[index] = value
        self.sizes[stack_number] += 1

    def pop(self, stack_number):
        if stack_number >= self.n_stacks or stack_number < 0:
            raise IndexError("Invalid stack number.")
        if self.is_empty(stack_number):
            raise IndexError(f"Stack {stack_number} is empty.")
        index = stack_number * self.size + self.sizes[stack_number] - 1
        value = self.stacklist[index]
        self.stacklist[index] = None  # Clear the value
        self.sizes[stack_number] -= 1
        return value

    def peek(self, stack_number):
        if stack_number >= self.n_stacks or stack_number < 0:
            raise IndexError("Invalid stack number.")
        if self.is_empty(stack_number):
            raise IndexError(f"Stack {stack_number} is empty.")
        index = stack_number * self.size + self.sizes[stack_number] - 1
        return self.stacklist[index]
    
########################Stack Min#######################
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class StackMin():
    def __init__(self, data= None):
        if data is None:
            self.top = None
            self.minNode = None
        else:
            self.top = StackNode(data)
            self.minNode = self.top

    def push(self, data):
        node = StackNode(data)
        node.next = self.top
        self.top = node
        
        if min(self.minNode.data, data) == data:
            new_node = StackNode(data)
            new_node.next = self.minNode
            self.minNode = new_node

    def pop(self):
        node = self.top
        if node is None:
            return None

        if self.top.next:
            self.top = self.top.next
            if node == self.minNode:
                self.minNode = self.minNode.next
        else:
            self.top = None
            self.minNode = None
        return node.data

    def min(self):
        if self.minNode is None:
            return None
        return self.minNode.data

class OneStack():
    def __init__(self, max_size, data=None):
        if data is None:
            self.top = None
            self.size = 0
        else:
            node = StackNode(data)
            self.top = node
            self.size = 1
        self.max_size = max_size

    def pop(self):
        if self.size == 0:
            return None
        else:
            popped = self.top
            self.top = self.top.next
            self.size -= 1
            popped.next = None
            return popped.data

    def push(self, data):
        if self.size < self.max_size:
            node = StackNode(data)
            node.next = self.top
            self.top = node
            self.size +=1

    def peek(self):
        if self.size == 0:
            return None
        else:
            return self.top.data
        
class StackPlates():
    def __init__(self, max_size, data=None):
        self.stacks = []
        self.max_size = max_size
        if data is not None:
            self.stacks.append(OneStack(max_size, data))
    
    def push(self, data):
        if len(self.stacks):
            stack = self.stacks[-1]
            if stack.size < self.max_size:
                stack.push(data)
            else:
                self.stacks.append(OneStack(self.max_size, data))
        else:
            self.stacks.append(OneStack(self.max_size, data))    
    
    def pop(self):
        if not self.stacks:
            return None
        popped = self.stacks[-1].pop()
        if self.stacks[-1].size == 0:
            self.stacks.pop()
        return popped

    def peek(self):
        if not self.stacks:
            return None
        peeked = self.stacks[-1].peek()
        return peeked

    def popAt(self, index: int):
        if 0 <= index < len(self.stacks):
            popped = self.stacks[index].pop()
            if self.stacks[index].size == 0:
                self.stacks.pop(index)
            return popped
        else:
            return None

    def peekAt(self, index: int):
        if 0 <= index < len(self.stacks):
            peeked = self.stacks[index].peak()
            return peeked
        else:
            return None

class QueueFromStack:
    def __init__(self, max_size):
        self.in_stack = OneStack(max_size)
        self.out_stack = OneStack(max_size)
        self.size = 0

    def enqueue(self, data):
        if self.size < self.in_stack.max_size:  # Ensure the queue doesn't exceed the max size
            self.in_stack.push(data)
            self.size += 1
        else:
            print("Queue is full")

    def dequeue(self):
        if self.out_stack.size == 0:
            while self.in_stack.size > 0:
                self.out_stack.push(self.in_stack.pop())
        if self.out_stack.size > 0:
            popped = self.out_stack.pop()
            self.size -= 1
            return popped
        print("Queue is empty")
        return None

    def peek(self):
        if self.out_stack.size == 0:
            while self.in_stack.size > 0:
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.peek()
        
class AnimalQueue():
    def __init__(self, animal=None):
        self.size = 0
        if animal is None:
            self.first = None
            self.last = None
        else:
            self.first = StackNode(animal)
            self.first = self.last
            self.size += 1
    
    def enqueue(self, animal):
        if animal is not None:
            node = StackNode(animal)
            if self.size == 0:
                self.first = self.last = node
            else:
                self.last.next = node
                self.last = node
            self.size += 1
            return True
        else:
            return False

    def dequeue(self):
        if self.size != 0:
            popped = self.first
            self.first = self.first.next
            self.size -= 1
            return popped.data
        else:
            return None


class AnimalShelter:
    def __init__(self):
        self.dog_queue = AnimalQueue()
        self.cat_queue = AnimalQueue()
        self.all_queue = AnimalQueue()

    def enqueue(self, animal, animal_type):
        if animal_type == 'dog':
            self.dog_queue.enqueue(animal)
        elif animal_type == 'cat':
            self.cat_queue.enqueue(animal)
        self.all_queue.enqueue((animal_type, animal))

    def dequeueAny(self):
        if self.all_queue.size > 0:
            animal_type, animal = self.all_queue.dequeue()
            if animal_type == 'cat':
                self.cat_queue.dequeue()
            elif animal_type == 'dog':
                self.dog_queue.dequeue()
            return animal
        return None

    def dequeueDog(self):
        if self.dog_queue.size > 0:
            dog = self.dog_queue.dequeue()
            self._removeFromAllQueue('dog', dog)
            return dog
        return None

    def dequeueCat(self):
        if self.cat_queue.size > 0:
            cat = self.cat_queue.dequeue()
            self._removeFromAllQueue('cat', cat)
            return cat
        return None

    def _removeFromAllQueue(self, animal_type, animal):
        # Remove the specific animal from the all_queue
        current = self.all_queue.first
        previous = None
        while current:
            if current.data == (animal_type, animal):
                if previous is None:  # Removing the first node
                    self.all_queue.first = current.next
                else:
                    previous.next = current.next
                self.all_queue.size -= 1
                return
            previous = current
            current = current.next

    


        
        
    



