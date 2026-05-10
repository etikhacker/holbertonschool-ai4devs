public class bug3 {

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

        void printList() {
            Node current = head;
            while (current != null) {
                System.out.print(current.data);
                current = current.next;
            }
            System.out.println();
        }

        int length() {
            int count = 0;
            Node current = head;
            while (current != null);
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
        list.printList();
        System.out.println(list.length());
    }
}