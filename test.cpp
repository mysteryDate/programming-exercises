#include <iostream>
using namespace std;

struct treeNode {
  int value;
};

class Node {
  public:
    Node(int d) {
      data = d;
    }
  private:
    Node *next = null;
    int data;
    void appendToTail(int d) {
      Node end = new Node(d);
      Node n = this;
      while (n.next != null) {
        n = n.next;
      }
      n.next = end;
    }
}

class Stack {
  public:
    Stack(int capacity) { this.capacity = capacity; }
    bool isAtCapacity() { return capacity == size; }
    void join(Node above, Node below) {
      if (below != null) below.above = above;
      if (above != null) above.below = below;
    }
    bool push(int v) {
      if (size >= capacity) return false; size++;
      Node n = new Node(v);
      if (size == 1) bottom = n;
      join(n, top);
      top=n;
      return true;
    }
    int pop() { Node t = top;
      top = top.below; size--;
      return t.value;
    }
    bool isEmpty() { return size == 0; }
    int removeBottom() {
      Node b = bottom;
      bottom = bottom.above;
      if (bottom != null) bottom.below = null; size--;
      return b.value;
    }
    Node top, bottom;
    int size = 0;
  private:
    int capacity;
}

int main() {
  cout << "Hello World\n";
  treeNode a;
  a.value = 1;
  cout << a.value << endl;
  Stack<T> s;
  s.push(1);
  s.push(2);
  int c = s.pop();
  cout << c << endl;
  return 0;
}
