from linked_list import LinkedList
from hash_table import HashTable
from stack import Stack, is_balanced
from queue import Queue
from general_tree import build_product_tree
from binary_search_tree import build_tree
from graph import Graph

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['kek', 'lol', 'orbidol'])
    ll.print()
    ll.remove_at(1)
    print("length", ll.get_length())
    ll.print()
    ll.insert_at(1, 'lol')
    ll.print()
    ll.insert_after_value('lol', 'kekus')
    ll.print()
    ll.remove_by_value('kekus')
    ll.print()

    t = HashTable()
    t['kek'] = 'lol'
    t['lol'] = 'kek'

    print(t['kek'])
    t = HashTable()
    t["march 6"] = 310
    t["march 7"] = 420
    t["march 8"] = 67
    t["march 17"] = 63457
    print(t['march 6'])
    print(t['march 17'])
    print(t.arr)

    s = Stack()
    s.push(7)
    s.push(5)
    s.push(3)
    s.pop()

    print(is_balanced('([{dd]]dd}dd)'))
    print(is_balanced('][]'))

    q = Queue()

    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(5)
    q.dequeue()

    tree = build_product_tree()
    tree.print_tree()

    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    tree = build_tree(numbers)
    print(tree.search(1))
    print(tree.find_max())
    print(tree.find_min())
    print(tree.calculate_sum())
    print(tree.in_order_traversal())
    print(tree.pre_order_traversal())
    print(tree.post_order_traversal())
    tree.delete(9)
    print(tree.in_order_traversal())

    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    route_graph = Graph(routes)
    startPoint = "Mumbai"
    endPoint = "New York"
    print(route_graph.get_paths(startPoint, endPoint))
    print(route_graph.get_shortest_path(startPoint, endPoint))
