# include <iostream>
# include <queue>
using namespace std;

int main() {
    queue<int> q; //
    for (int i = 1; i <= 5; i++) {
        if (q.empty())
            cout << "queue is empty" << '\n';
        q.push(i);

        cout << "After inserting value " << i << " to queue, the front of queue is "
            << "q.front()" << " and the back of the queue is " << q.back()
            << " with size = " << q.size() << '\n';
    }
    while (!q.empty()){
        cout << "After removing items " << q.front() << " from queue";
        q.pop();
        if (!q.empty())
            cout << " the front of the queue is " << q.front() << " and the back of queue is " << q.back() << '\n';
        else 
            cout << "the queus is empty" << '\n';
    }
}

// push(): enqueue
// enqueue: insert at the end
// dequeue: delete from the front
// FIFO: first in first out
// no iterator for queue, we're not suppose to traverse a queue