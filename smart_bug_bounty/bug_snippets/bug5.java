// bug5.java
// Intended behavior: A singly linked list with append, delete (by value),
// and printList methods.

public class bug5 {

    static class Node {
        int data;
        Node next;
        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    static class LinkedList {
        Node head;

        void append(int data) {
            Node newNode = new Node(data);
            if (head == null) {
                head = newNode;
                return;
            }
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }

        void delete(int value) {
            if (head == null) return;

            if (head.data == value) {
                head = head.next;
                return;
            }

            Node current = head;
            while (current.next != null) {
                if (current.next.data == value) {
                    current.next = current.next.next;
                    return;
                }
                current = current.next;
            }
            // BUG: no indication that the value was not found (silent failure)
        }

        void printList() {
            Node current = head;
            while (current != null) {
                System.out.print(current.data);   // BUG: missing separator between values
                current = current.next;            //      should print current.data + " -> "
            }
            System.out.println();                  // BUG: should print "null" at end for clarity
        }

        int length() {
            int count = 0;
            Node current = head;
            while (current != null);   // BUG: infinite loop — missing `current = current.next`
            {
                count++;
                current = current.next;
            }
            return count;
        }
    }

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.append(1);
        list.append(2);
        list.append(3);
        list.append(4);
        list.printList();    // expected: 1 -> 2 -> 3 -> 4 -> null
        list.delete(2);
        list.printList();    // expected: 1 -> 3 -> 4 -> null
        System.out.println(list.length());  // expected: 3
    }
}
