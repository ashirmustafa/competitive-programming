struct Node {
    value: i32,
    next: Option<Box<Node>>,
}

struct CircularSinglyLinkedList {
    head: Option<Box<Node>>,
}

impl CircularSinglyLinkedList {
    fn new() -> Self {
        Self { head: None }
    }

    fn push_front(&mut self, val: i32) {
        let mut new_node = Box::new(Node { value: val, next: None });

        if self.head.is_none() {
            new_node.next = Some(new_node.clone());
            self.head = Some(new_node);
        } else {
            let mut tail = self.head.as_mut().unwrap();

            while let Some(ref mut next_node) = tail.next {
                if std::ptr::eq(&**next_node, &*self.head.as_ref().unwrap()) {
                    break;
                }
                tail = next_node;
            }

            new_node.next = self.head.take();
            tail.next = Some(new_node.clone());
            self.head = Some(new_node);
        }
    }
}
