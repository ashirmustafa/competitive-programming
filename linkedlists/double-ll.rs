use std::rc::Rc;
use std::cell::RefCell;

type NodeRef = Rc<RefCell<Node>>;

struct Node {
    value: i32,
    next: Option<NodeRef>,
    prev: Option<NodeRef>,
}

struct DoublyLinkedList {
    head: Option<NodeRef>,
    tail: Option<NodeRef>,
}

impl DoublyLinkedList {
    fn new() -> Self {
        Self { head: None, tail: None }
    }

    fn push_back(&mut self, val: i32) {
        let new_node = Rc::new(RefCell::new(Node {
            value: val,
            next: None,
            prev: self.tail.clone(),
        }));

        match self.tail.take() {
            Some(old_tail) => {
                old_tail.borrow_mut().next = Some(new_node.clone());
            }
            None => {
                self.head = Some(new_node.clone());
            }
        }

        self.tail = Some(new_node);
    }

    fn print_forward(&self) {
        let mut current = self.head.clone();
        while let Some(node) = current {
            print!("{} <-> ", node.borrow().value);
            current = node.borrow().next.clone();
        }
        println!("None");
    }
}
