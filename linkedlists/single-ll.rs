struct Node {
    value: i32,
    next: Option<Box<Node>>,
}

struct SinglyLinkedList {
    head: Option<Box<Node>>,
}

impl SinglyLinkedList {
    fn new() -> Self {
        Self { head: None }
    }

    fn push_front(&mut self, val: i32) {
        let new_node = Box::new(Node {
            value: val,
            next: self.head.take(), 
        });
        self.head = Some(new_node);
    }

    fn print(&self) {
        let mut current = self.head.as_ref();
        while let Some(node) = current {
            print!("{} -> ", node.value);
            current = node.next.as_ref();
        }
        println!("None");
    }
}

fn main() {
    let mut list = SinglyLinkedList::new();

    list.push_front(10);
    list.push_front(20);
    list.push_front(30);

    println!("Singly Linked List:");
    list.print(); 
}
