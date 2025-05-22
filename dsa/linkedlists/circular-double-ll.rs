use std::rc::Rc;
use std::cell::RefCell;

type NodeRef = Rc<RefCell<Node>>;

struct Node {
    value: i32,
    next: Option<NodeRef>,
    prev: Option<NodeRef>,
}

struct CircularDoublyLinkedList {
    head: Option<NodeRef>,
}

impl CircularDoublyLinkedList {
    fn new() -> Self {
        Self { head: None }
    }

    fn push(&mut self, val: i32) {
        let new_node = Rc::new(RefCell::new(Node {
            value: val,
            next: None,
            prev: None,
        }));

        if let Some(head) = self.head.clone() {
            let tail = head.borrow().prev.clone().unwrap();

            new_node.borrow_mut().next = Some(head.clone());
            new_node.borrow_mut().prev = Some(tail.clone());

            tail.borrow_mut().next = Some(new_node.clone());
            head.borrow_mut().prev = Some(new_node.clone());
        } else {
            new_node.borrow_mut().next = Some(new_node.clone());
            new_node.borrow_mut().prev = Some(new_node.clone());
            self.head = Some(new_node);
        }
    }

    fn print(&self) {
        if let Some(start) = self.head.clone() {
            let mut current = start.clone();
            loop {
                print!("{} <=> ", current.borrow().value);
                current = current.borrow().next.clone().unwrap();
                if Rc::ptr_eq(&current, &start) {
                    break;
                }
            }
            println!("(back to start)");
        }
    }
}
