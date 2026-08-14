from app import app
from models import db, Question, User

SEED_QUESTIONS = [
    # ==========================================
    # 1. FRONTEND & JAVASCRIPT
    # ==========================================
    {
        "category": "Frontend",
        "title": "Event Loop & Microtask vs Macrotask Queue",
        "difficulty": "Hard",
        "question_text": "Explain how the JavaScript Event Loop handles Call Stack execution, Web APIs, Microtask Queue (Promises, process.nextTick), and Macrotask Queue (setTimeout, setInterval, I/O).",
        "sample_answer": "JavaScript is single-threaded:\n1. Synchronous code executes on the Call Stack.\n2. Asynchronous operations delegate callbacks to Web APIs.\n3. Microtasks (Promise callbacks, queueMicrotask) have higher execution priority than Macrotasks (setTimeout, setInterval, requestAnimationFrame).\n4. When the Call Stack clears, the Event Loop drains ALL Microtasks before processing a single Macrotask.",
        "tips": "Be ready to trace code snippets combining setTimeout(fn, 0) and Promise.resolve().then(fn).",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "JavaScript Closures & Memory Leak Prevention",
        "difficulty": "Medium",
        "question_text": "What is a closure in JavaScript? Provide practical examples of encapsulation using closures and explain potential memory leaks.",
        "sample_answer": "A closure is a function bundled with references to its surrounding lexical environment. It gives an inner function access to outer function scope variables even after the outer function has returned.\n\nUse cases: Private variables, function currying, event handler state preservation.\nMemory leaks: Unintentional references to large DOM nodes or event listeners held in outer variables that can never be garbage collected.",
        "tips": "Demonstrate the classic private counter module pattern using closures.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Prototypal Inheritance vs ES6 Classes",
        "difficulty": "Medium",
        "question_text": "Explain prototypal inheritance in JavaScript. How does object delegation work via the __proto__ and prototype properties?",
        "sample_answer": "JavaScript objects have an internal link to another object called its prototype. When accessing a property on an object, JS looks up the prototype chain until found or reaching null.\nES6 `class` syntax is syntactic sugar over prototype delegation, introducing `extends` and `super()` for cleaner OOP paradigms.",
        "tips": "Clarify that `Object.create(proto)` directly creates a new object linked to `proto`.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Debounce vs Throttle Implementation",
        "difficulty": "Medium",
        "question_text": "Compare Debouncing and Throttling in JavaScript. Write custom utility functions for both.",
        "sample_answer": "Debounce delays execution until a specified delay passes after the last trigger (ideal for search inputs, window resize).\nThrottle guarantees execution at most once every fixed interval (ideal for scroll events, drag & drop).\n\nDebounce Code:\n`function debounce(fn, delay) { let t; return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), delay); }; }`",
        "tips": "Highlight how debouncing saves backend API calls during rapid typing.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Virtual DOM & React Reconciliation Algorithm",
        "difficulty": "Medium",
        "question_text": "What is the Virtual DOM and how does React's reconciliation diffing algorithm optimize real DOM updates?",
        "sample_answer": "The Virtual DOM is an in-memory lightweight representation of actual DOM nodes.\nWhen state updates, React builds a new Virtual DOM tree and runs a diffing algorithm (O(N) complexity heuristics):\n1. Different element types recreate entire subtrees.\n2. Keys identify list items to reorder instead of re-rendering.\n3. Batched DOM mutations execute in a single browser repaint cycle.",
        "tips": "Always emphasize why keys must be stable, unique IDs rather than list index numbers.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "DOM Event Delegation & Propagation",
        "difficulty": "Easy",
        "question_text": "Explain Event Bubbling, Event Capturing, and Event Delegation with an example.",
        "sample_answer": "Propagation has 3 phases: Capturing (window down to target), Target, and Bubbling (target back up to window).\nEvent Delegation attaches a single event listener to a parent element to handle events on current and future child elements using `event.target`.",
        "tips": "Mention `event.stopPropagation()` vs `event.preventDefault()`. ",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "CSS Grid vs Flexbox Layout Models",
        "difficulty": "Easy",
        "question_text": "When should you use CSS Flexbox versus CSS Grid for responsive web design?",
        "sample_answer": "Flexbox is 1-dimensional (rows OR columns), perfect for alignment along a single axis (navbars, cards).\nGrid is 2-dimensional (rows AND columns), ideal for overall page layouts, complex dashboards, and overlapping grid templates.",
        "tips": "Discuss `flex-grow`, `flex-shrink`, `flex-basis`, and grid areas.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Web Performance & Core Web Vitals",
        "difficulty": "Hard",
        "question_text": "What are Core Web Vitals (LCP, INP/FID, CLS) and how do you optimize frontend loading speed?",
        "sample_answer": "Core Web Vitals measure user experience:\n- LCP (Largest Contentful Paint): Loading performance (<2.5s).\n- INP/FID (Interaction to Next Paint / First Input Delay): Interactivity.\n- CLS (Cumulative Layout Shift): Visual stability (<0.1).\nOptimizations: Code splitting (React.lazy), image optimization (WebP, lazy loading), CDN caching, minimizing blocking CSS/JS, and preloading key assets.",
        "tips": "Mention lighthouse audits and real user monitoring (RUM).",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Browser Storage: Cookies, LocalStorage & SessionStorage",
        "difficulty": "Easy",
        "question_text": "Compare Cookies, LocalStorage, and SessionStorage regarding capacity, expiration, and security.",
        "sample_answer": "Cookies: ~4KB, sent with HTTP requests, supports HTTPOnly and SameSite flags (best for auth tokens).\nLocalStorage: ~5-10MB, persistent across browser restarts, per-origin scope.\nSessionStorage: ~5MB, cleared when tab/window closes.",
        "tips": "Emphasize security risks of XSS when storing sensitive tokens in LocalStorage.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Async/Await vs Promises & Error Handling",
        "difficulty": "Easy",
        "question_text": "How does `async/await` work under the hood and how do you handle errors in concurrent API calls?",
        "sample_answer": "`async/await` is syntactic sugar built on top of Promises and Generators.\nError handling uses `try...catch` blocks for single promises or `Promise.allSettled()` to handle array promises where individual calls may fail without aborting others.",
        "tips": "Differentiate `Promise.all` (fails fast on first rejection) from `Promise.allSettled`.",
        "star_guide": None
    },

    # ==========================================
    # 2. PYTHON (CATEGORIZED AS FRONTEND)
    # ==========================================
    {
        "category": "Frontend",
        "title": "Python Memory Management & Garbage Collection",
        "difficulty": "Hard",
        "question_text": "Explain how CPython manages memory using reference counting, arena allocation, and cyclic garbage collection.",
        "sample_answer": "Python uses Reference Counting as its primary memory mechanism: every object tracks reference count. When count drops to 0, memory is immediately deallocated.\nCyclic Garbage Collector handles reference cycles (e.g. A references B, B references A) using generational collection (Gen 0, Gen 1, Gen 2) with tri-color marking algorithms.",
        "tips": "Mention `sys.getrefcount()` and the `gc` module.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Python Decorators & `@functools.wraps`",
        "difficulty": "Medium",
        "question_text": "What is a decorator in Python? Write a custom timing decorator that measures function execution time.",
        "sample_answer": "A decorator takes a function as argument, extends its behavior without modifying original source code, and returns a wrapper function.\n`@functools.wraps` preserves original function metadata (`__name__`, `__doc__`).\n\nExample:\n```python\nimport time, functools\ndef timer(fn):\n    @functools.wraps(fn)\n    def wrapper(*args, **kwargs):\n        t0 = time.time()\n        res = fn(*args, **kwargs)\n        print(f'{fn.__name__} took {time.time()-t0:.4f}s')\n        return res\n    return wrapper\n```",
        "tips": "Explain how decorators accept arguments by adding an extra outer wrapper layer.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Generators vs Iterators & `yield` Keyword",
        "difficulty": "Medium",
        "question_text": "Explain the difference between iterators and generators in Python. How does `yield` conserve memory during large data processing?",
        "sample_answer": "An Iterator implements `__iter__()` and `__next__()` methods.\nA Generator is a simple function returning a generator iterator using `yield` statements.\nInstead of computing and storing entire lists in RAM (O(N) memory), `yield` produces values lazily on-demand (O(1) memory state).",
        "tips": "Give an example of generator expressions vs list comprehensions `(x for x in data)` vs `[x for x in data]`.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Global Interpreter Lock (GIL) & Concurrency",
        "difficulty": "Hard",
        "question_text": "What is the Global Interpreter Lock (GIL) in CPython? How does it affect multithreading vs multiprocessing?",
        "sample_answer": "GIL is a mutex preventing multiple native threads from executing Python bytecode simultaneously in CPython.\nEffect: Multithreading does NOT achieve multi-core speedup for CPU-bound tasks (math, ML training). However, multithreading is effective for I/O-bound tasks (network, disk).\nWorkaround: Use `multiprocessing` to bypass GIL by spawning separate OS processes with independent memory spaces.",
        "tips": "Discuss Python 3.12/3.13 subinterpreters and experimental free-threaded CPython builds.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Mutable vs Immutable Default Function Arguments",
        "difficulty": "Easy",
        "question_text": "Why is using mutable objects (like lists or dicts) as default arguments in Python functions dangerous?",
        "sample_answer": "Default arguments are evaluated ONCE when the function definition is compiled, not at invocation.\nUsing `def append_to(element, target=[])` causes all calls without explicit target to mutate the exact same list instance in memory.\nCorrect Pattern: `def append_to(element, target=None): if target is None: target = []`",
        "tips": "Explain pass-by-object-reference semantics in Python.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Context Managers & `with` Statement Protocol",
        "difficulty": "Medium",
        "question_text": "How do Python context managers work? Write a class implementing `__enter__` and `__exit__`.",
        "sample_answer": "Context managers guarantee resource acquisition and cleanup (files, sockets, DB connections).\n`__enter__` sets up resource and returns it.\n`__exit__(exc_type, exc_val, exc_tb)` handles cleanup and can suppress exceptions by returning `True`.",
        "tips": "Mention `@contextlib.contextmanager` generator decorator shortcut.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "List Comprehensions vs Generator Expressions",
        "difficulty": "Easy",
        "question_text": "Compare List Comprehensions and Generator Expressions in terms of syntax, speed, and memory usage.",
        "sample_answer": "List comprehension `[x*2 for x in range(1000000)]` creates full list in memory immediately.\nGenerator expression `(x*2 for x in range(1000000))` returns a lazy generator object yielding one item at a time.",
        "tips": "Show memory usage differences using `sys.getsizeof()`.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "`*args` and `**kwargs` Unpacking Mechanics",
        "difficulty": "Easy",
        "question_text": "How do positional `*args` and keyword `**kwargs` argument packing and unpacking work in Python?",
        "sample_answer": "`*args` packs arbitrary positional arguments into a tuple.\n`**kwargs` packs named arguments into a dictionary.\nAlso used for unpacking: `func(*list_val)` or dictionary merging `{**d1, **d2}`.",
        "tips": "Show argument ordering rules: positional, `*args`, keyword-only, `**kwargs`.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Metaclasses & Class Instantiation (`__new__` vs `__init__`)",
        "difficulty": "Hard",
        "question_text": "What is a metaclass in Python? Distinguish between `__new__` and `__init__` in class instantiation.",
        "sample_answer": "A metaclass is a class whose instances are classes. `type` is the default metaclass.\n`__new__` is the static method that actually allocates and returns the new object instance.\n`__init__` initializes the created instance with parameters.\nMetaclasses intercept class creation to enforce standards, register plugins, or auto-generate attributes.",
        "tips": "Implement a thread-safe Singleton pattern using a metaclass.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Asyncio Event Loop & Asynchronous I/O",
        "difficulty": "Medium",
        "question_text": "Explain `asyncio` in Python. How do co-routines, tasks, and `asyncio.gather` execute non-blocking code?",
        "sample_answer": "`asyncio` uses a single-threaded cooperative multitasking event loop.\n`async def` defines coroutines. `await` yields control back to event loop while waiting for I/O.\n`asyncio.gather(*coroutines)` runs multiple asynchronous operations concurrently.",
        "tips": "Contrast asyncio with multithreading (cooperative vs preemptive multitasking).",
        "star_guide": None
    },

    # ==========================================
    # 3. JAVA (CATEGORIZED AS FRONTEND)
    # ==========================================
    {
        "category": "Frontend",
        "title": "JVM Architecture & Memory Structure",
        "difficulty": "Hard",
        "question_text": "Explain the JVM memory model: ClassLoader, Heap (Young/Old Generation), Stack, Metaspace, and Garbage Collection.",
        "sample_answer": "JVM divides memory into:\n- Heap: Shared across threads storing objects. Separated into Young Gen (Eden, Survivor spaces) and Old/Tenured Gen.\n- Stack: Thread-private frame storing primitives and local object references.\n- Metaspace: Stores class definitions and metadata (replaces PermGen in Java 8+).\nGarbage Collector automatically reclaims unreachable Heap memory.",
        "tips": "Explain Minor GC vs Major/Full GC performance impacts.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Java Collection Framework & Core Interfaces",
        "difficulty": "Medium",
        "question_text": "Compare `ArrayList` vs `LinkedList`, and `HashMap` vs `ConcurrentHashMap` in Java.",
        "sample_answer": "ArrayList: Dynamic array, O(1) random access by index, O(N) insertion/deletion middle.\nLinkedList: Doubly linked list, O(N) access, O(1) insertion/deletion with node reference.\nHashMap: Non-thread-safe hash table.\nConcurrentHashMap: Thread-safe, uses lock striping / synchronized buckets for high concurrency without locking full map.",
        "tips": "Contrast ConcurrentHashMap with Collections.synchronizedMap().",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "HashMap Internal Working & Collision Resolution",
        "difficulty": "Hard",
        "question_text": "How does `HashMap` work internally in Java 8+? Explain hashing, bucket index calculation, and Red-Black tree conversion.",
        "sample_answer": "HashMap uses an array of buckets (`Node<K,V>[]`).\nIndex calculated as `(n - 1) & hash(key)`.\nCollisions use chaining: when bucket size exceeds threshold (TREEIFY_THRESHOLD = 8) and map capacity >= 64, linked list converts to a Red-Black Tree (improving search from O(N) to O(log N)).",
        "tips": "Explain `hashCode()` and `equals()` contract requirement.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Abstract Classes vs Interfaces in Java 8+",
        "difficulty": "Medium",
        "question_text": "Compare Abstract Classes and Interfaces in Java. How did default and static methods in Java 8 alter this balance?",
        "sample_answer": "Abstract Class: Can have constructor, state/fields, partial method implementations, single inheritance (`extends`).\nInterface: Can have public static final constants, multiple inheritance (`implements`). Java 8 added `default` methods (behavioral defaults) and `static` methods. Java 9 added `private` methods for code reuse.",
        "tips": "Explain diamond problem resolution rules when multiple default interface methods conflict.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Multithreading: `volatile` vs `synchronized` vs `ReentrantLock`",
        "difficulty": "Hard",
        "question_text": "Explain thread synchronization mechanisms in Java. When would you use `volatile` vs `synchronized` vs `ReentrantLock`?",
        "sample_answer": "- `volatile`: Ensures visibility of variable writes across threads directly to main memory (prevents CPU cache staleness), but does NOT guarantee atomicity.\n- `synchronized`: Mutual exclusion lock (mutex) ensuring both visibility and atomicity for code blocks.\n- `ReentrantLock`: Explicit lock offering advanced features: fairness policy, lock polling (`tryLock`), interruptible locks, and multiple `Condition` variables.",
        "tips": "Discuss deadlock conditions and how `ReentrantLock.tryLock()` prevents indefinite blocking.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Java Exception Hierarchy & Try-With-Resources",
        "difficulty": "Easy",
        "question_text": "Explain Checked vs Unchecked exceptions in Java. How does `try-with-resources` simplify resource management?",
        "sample_answer": "Checked Exceptions (`IOException`, `SQLException`) extend `Exception`, checked at compile-time, must be caught or declared `throws`.\nUnchecked Exceptions (`NullPointerException`, `IllegalArgumentException`) extend `RuntimeException`.\n`try-with-resources` automatically closes objects implementing `AutoCloseable` interface in reverse declaration order.",
        "tips": "Explain suppressed exceptions in try-with-resources.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Java Streams API & Functional Operations",
        "difficulty": "Medium",
        "question_text": "Demonstrate the Java Streams API using intermediate and terminal operations (`filter`, `map`, `reduce`, `collect`).",
        "sample_answer": "Streams represent sequence of elements supporting lazy functional operations.\nIntermediate operations (`filter`, `map`, `sorted`) return a new Stream lazily.\nTerminal operations (`collect`, `forEach`, `reduce`) trigger stream execution.\nExample: `list.stream().filter(x -> x > 10).map(String::valueOf).collect(Collectors.toList());`",
        "tips": "Explain parallel streams and thread safety considerations with shared mutable state.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "String Immutability & String Constant Pool",
        "difficulty": "Easy",
        "question_text": "Why are Strings immutable in Java? Explain String Constant Pool and `StringBuilder` vs `StringBuffer`.",
        "sample_answer": "String immutability benefits: Security (network/DB credentials), Thread Safety, Caching `hashCode()`, and String Pool memory savings.\nLiteral strings `'hello'` are cached in String Constant Pool in Heap.\n`StringBuilder` is mutable and fast (non-thread-safe).\n`StringBuffer` is mutable and thread-safe (synchronized methods).",
        "tips": "Show difference between `new String(\"a\")` vs `\"a\"`.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "SOLID Principles in Object-Oriented Java Design",
        "difficulty": "Medium",
        "question_text": "Explain the 5 SOLID design principles with Java code examples.",
        "sample_answer": "S: Single Responsibility (Class should have one reason to change).\nO: Open-Closed (Open for extension, closed for modification).\nL: Liskov Substitution (Subclasses must be substitutable for base classes).\nI: Interface Segregation (Clients shouldn't be forced to depend on unused interfaces).\nD: Dependency Inversion (Depend upon abstractions, not concrete implementations).",
        "tips": "Reference Spring Framework Dependency Injection as an implementation of DIP.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Java Reflection API & Annotation Processing",
        "difficulty": "Hard",
        "question_text": "What is Java Reflection API? How do frameworks like Spring use Reflection for Dependency Injection and ORMs?",
        "sample_answer": "Reflection inspects or modifies runtime behavior of classes, interfaces, fields, and methods dynamically.\nSpring IoC container scans `@Component` annotations, uses Reflection `Class.forName()`, `getDeclaredFields()`, and sets private dependencies via `field.setAccessible(true)`.",
        "tips": "Highlight performance overhead and security manager restrictions of Reflection.",
        "star_guide": None
    },

    # ==========================================
    # 4. DATA STRUCTURES (CATEGORIZED AS FRONTEND)
    # ==========================================
    {
        "category": "Frontend",
        "title": "Reverse a Singly Linked List",
        "difficulty": "Easy",
        "question_text": "Given the head of a singly linked list, reverse the list and return the reversed list. Provide iterative and recursive solutions.",
        "sample_answer": "Iterative: Maintain `prev = None`, `curr = head`. Loop: `nxt = curr.next; curr.next = prev; prev = curr; curr = nxt`. Return `prev`.\nTime: O(N), Space: O(1).\nRecursive: Reverse rest of list, set `head.next.next = head; head.next = None`.\nTime: O(N), Space: O(N) call stack.",
        "tips": "Always test edge cases: empty list or single node list.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Two Sum Problem",
        "difficulty": "Easy",
        "question_text": "Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.",
        "sample_answer": "Use a Hash Map storing value-to-index mapping.\nIterate array: for each `num`, check if `target - num` exists in map. If yes, return current index and map value.\nTime Complexity: O(N), Space Complexity: O(N).",
        "tips": "Mention two-pointer approach if array is sorted (O(N log N) time, O(1) space).",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "LRU Cache Design & Implementation",
        "difficulty": "Hard",
        "question_text": "Design a Least Recently Used (LRU) cache supporting `get(key)` and `put(key, value)` operations in O(1) time complexity.",
        "sample_answer": "Combine Doubly Linked List with Hash Map:\n- Hash Map maps `key -> Node pointer` for O(1) lookup.\n- Doubly Linked List maintains access recency order (Most Recently Used near Head, Least Recently Used near Tail).\nOn `get` or `put`, move accessed node to Head. On eviction, remove node from Tail.",
        "tips": "Use dummy head and dummy tail nodes to simplify edge pointer updates.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Binary Tree Level Order Traversal (BFS)",
        "difficulty": "Medium",
        "question_text": "Given the root of a binary tree, return the level order traversal of its nodes' values level by level.",
        "sample_answer": "Use a Queue for Breadth-First Search (BFS):\n1. Push `root` to queue.\n2. While queue is not empty, get `level_size = len(queue)`.\n3. Loop `level_size` times: pop node, add value to current level list, push non-null `left` and `right` children.\nTime: O(N), Space: O(W) where W is maximum tree width.",
        "tips": "Contrast BFS queue level-order with DFS stack depth traversals.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Detect Cycle in a Directed Graph",
        "difficulty": "Hard",
        "question_text": "Given a directed graph with V vertices and E edges, determine if it contains a cycle.",
        "sample_answer": "Method 1: DFS with 3 node states (UNVISITED, VISITING, VISITED). Finding a neighbor in VISITING state indicates a back-edge / cycle.\nMethod 2: Kahn's Algorithm (Topological Sort BFS). If processed nodes count < V, graph has cycle.\nTime Complexity: O(V + E), Space Complexity: O(V).",
        "tips": "Explain difference between cycle detection in Directed vs Undirected graph (parent checking).",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Merge K Sorted Lists",
        "difficulty": "Hard",
        "question_text": "You are given an array of k linked lists, each linked list is sorted in ascending order. Merge all lists into one sorted list.",
        "sample_answer": "Use a Min-Heap (Priority Queue):\n1. Push initial head node of each of the k lists into Min-Heap.\n2. Extract minimum node, append to result list.\n3. If extracted node has `next`, push `next` into Min-Heap.\nRepeat until heap empty.\nTime Complexity: O(N log K) where N total nodes, K lists. Space: O(K).",
        "tips": "Compare heap solution with divide-and-conquer merge sort approach.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Valid Parentheses String Matching",
        "difficulty": "Easy",
        "question_text": "Given a string `s` containing `()`, `{}`, `[]`, determine if input string is valid.",
        "sample_answer": "Use a Stack:\nIterate characters: push opening brackets onto stack. For closing brackets, check if stack is non-empty and top element matches closing pair. Pop stack.\nReturn `True` if stack is empty at end.\nTime: O(N), Space: O(N).",
        "tips": "Use hash map `{')':'(', '}':'{', ']':'['}` for clean matching.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Lowest Common Ancestor in Binary Tree",
        "difficulty": "Medium",
        "question_text": "Given a binary tree and two nodes `p` and `q`, find their Lowest Common Ancestor (LCA).",
        "sample_answer": "Recursive DFS approach:\nIf current node is Null, `p`, or `q`, return current node.\nRecursively search `left = LCA(root.left, p, q)` and `right = LCA(root.right, p, q)`.\nIf both `left` and `right` are non-null, `root` is LCA.\nElse return non-null child.\nTime: O(N), Space: O(H) recursion height.",
        "tips": "Differentiate between standard Binary Tree LCA and Binary Search Tree LCA (O(H) using BST key comparisons).",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Dynamic Programming: 0/1 Knapsack Problem",
        "difficulty": "Hard",
        "question_text": "Given weights and values of N items, put these items in a knapsack of capacity W to get maximum value.",
        "sample_answer": "DP Table `dp[i][w]` represents max value using first `i` items with capacity `w`.\nState transition:\n`dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1][w - wt[i-1]])` if `wt[i-1] <= w` else `dp[i-1][w]`.\nTime Complexity: O(N * W), Space Complexity: O(N * W) reducible to O(W) 1D array.",
        "tips": "Differentiate 0/1 Knapsack (each item 1 instance) from Unbounded Knapsack (infinite instances).",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Search in Rotated Sorted Array",
        "difficulty": "Medium",
        "question_text": "Given a rotated sorted array `nums` and target, return target index or -1 in O(log N) time.",
        "sample_answer": "Modified Binary Search:\nFind `mid`. At least one half (`left..mid` or `mid..right`) MUST be sorted.\nIf `nums[left] <= nums[mid]`: left half is sorted. Check if target lies within `[nums[left], nums[mid]]`. If so, adjust `high = mid - 1`, else `low = mid + 1`.\nOtherwise: right half is sorted. Adjust boundaries accordingly.\nTime: O(log N), Space: O(1).",
        "tips": "Address duplicates scenario where `nums[low] == nums[mid] == nums[high]`.",
        "star_guide": None
    },

    # ==========================================
    # 5. MACHINE LEARNING (CATEGORIZED AS FRONTEND)
    # ==========================================
    {
        "category": "Frontend",
        "title": "Bias-Variance Tradeoff Explained",
        "difficulty": "Medium",
        "question_text": "Explain Bias, Variance, Underfitting, Overfitting, and how to strike the right balance.",
        "sample_answer": "Bias: Error from overly simplistic model assumptions (Underfitting).\nVariance: Error from model sensitivity to small fluctuations in training set (Overfitting).\nTotal Error = Bias^2 + Variance + Irreducible Error.\nBalance: Increase model capacity to reduce bias, add regularization / cross-validation to control variance.",
        "tips": "Draw learning curves showing train error vs validation error for underfitting vs overfitting.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Overfitting Prevention & Regularization Techniques",
        "difficulty": "Medium",
        "question_text": "How do L1 (Lasso) and L2 (Ridge) regularization prevent overfitting in machine learning models?",
        "sample_answer": "L1 (Lasso): Adds penalty `lambda * sum(|w_i|)`. Drives non-important weights strictly to zero, performing automatic feature selection.\nL2 (Ridge): Adds penalty `lambda * sum(w_i^2)`. Shrinks weight magnitudes uniformly, preventing dominance of single features.\nElasticNet combines L1 and L2 penalties.",
        "tips": "Explain geometric intuition of L1 diamond vs L2 circle constraints.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Gradient Descent Optimization Algorithms",
        "difficulty": "Hard",
        "question_text": "Compare Batch GD, Stochastic GD (SGD), Mini-Batch GD, and Adam Optimizer.",
        "sample_answer": "Batch GD computes gradients over whole dataset (slow, high RAM).\nSGD computes gradient per single sample (noisy, fast, escapes local minima).\nMini-Batch GD computes gradient per batch (balanced, GPU vectorization).\nAdam (Adaptive Moment Estimation) combines Momentum (first moment of gradients) and RMSProp (second raw moment) with bias correction for fast, stable convergence.",
        "tips": "Explain learning rate decay and learning rate warm-up schedules.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Classification Metrics: Precision, Recall, F1 & ROC-AUC",
        "difficulty": "Medium",
        "question_text": "Define Precision, Recall, F1-Score, and ROC-AUC. When should you prioritize Recall over Precision?",
        "sample_answer": "Confusion Matrix: TP, FP, TN, FN.\n- Precision = TP / (TP + FP): Quality of positive predictions.\n- Recall = TP / (TP + FN): Ability to find all positive instances.\n- F1-Score = 2 * (P * R) / (P + R): Harmonic mean.\n- ROC-AUC: Plots True Positive Rate vs False Positive Rate across decision thresholds.\nPrioritize Recall in medical diagnosis or fraud detection (where false negatives are catastrophic).",
        "tips": "Explain why Accuracy is misleading for imbalanced datasets.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Supervised vs Unsupervised vs Reinforcement Learning",
        "difficulty": "Easy",
        "question_text": "Contrast Supervised, Unsupervised, and Reinforcement Learning paradigms with real-world applications.",
        "sample_answer": "Supervised: Trains on labeled input-output pairs `(X, y)` (Linear Regression, ResNet, XGBoost). Applications: Spam detection, price forecasting.\nUnsupervised: Discovers hidden patterns in unlabeled data `X` (K-Means, PCA, Autoencoders). Applications: Customer segmentation, anomaly detection.\nReinforcement: Agent learns optimal policies via trial-and-error rewards from environment (Q-Learning, PPO). Applications: Game playing (AlphaGo), autonomous robotics.",
        "tips": "Mention Self-Supervised Learning used in LLMs (masked language modeling).",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Transformer Architecture & Self-Attention",
        "difficulty": "Hard",
        "question_text": "Explain the Self-Attention mechanism in Transformer models (Attention is All You Need).",
        "sample_answer": "Self-attention computes dynamic dependencies between all tokens in a sequence regardless of distance:\n1. Input embeddings project into Query (Q), Key (K), and Value (V) matrices.\n2. Attention Weights = `softmax( (Q * K^T) / sqrt(d_k) )`.\n3. Output = `Attention Weights * V`.\nMulti-Head Attention runs multiple attention heads in parallel to capture distinct positional/semantic relationships.",
        "tips": "Explain why scaling factor `1 / sqrt(d_k)` prevents vanishing gradients in softmax.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Feature Scaling: Normalization vs Standardization",
        "difficulty": "Easy",
        "question_text": "Distinguish between MinMax Normalization and Z-score Standardization. Why is feature scaling essential?",
        "sample_answer": "MinMax Normalization: `(X - X_min) / (X_max - X_min)` scales values to range [0, 1]. Sensitive to outliers.\nStandardization: `(X - mu) / sigma` transforms data to zero mean and unit variance. Less sensitive to outliers.\nEssential for distance-based algorithms (KNN, SVM, K-Means) and gradient descent optimization (prevents elongated loss contours).",
        "tips": "Note that Tree-based models (Random Forest, XGBoost) are scale-invariant.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Decision Trees & Ensemble Learning (Bagging vs Boosting)",
        "difficulty": "Medium",
        "question_text": "Explain how Decision Trees split nodes and compare Bagging (Random Forest) vs Boosting (XGBoost/LightGBM).",
        "sample_answer": "Splits use Gini Impurity `1 - sum(p_i^2)` or Entropy Information Gain.\nBagging (Bootstrap Aggregating): Trains multiple independent trees in parallel on random data subsets with replacement, averaging predictions to reduce variance (Random Forest).\nBoosting: Trains sequential trees sequentially, where each new tree focuses on errors/residuals of previous trees (XGBoost, Gradient Boosting). Reduces bias.",
        "tips": "Highlight key hyper-parameters: `max_depth`, `n_estimators`, `learning_rate`.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Convolutional Neural Networks (CNNs)",
        "difficulty": "Hard",
        "question_text": "Explain the architecture of a CNN: Convolutional Layers, Activation functions, Pooling, and Fully Connected Layers.",
        "sample_answer": "Convolutional Layer: Applies trainable filters (kernels) sliding across input image to extract spatial feature maps (edges, textures).\nActivation (ReLU): Introduces non-linearity.\nPooling (Max/Average): Downsamples spatial dimensions to reduce parameters and achieve translation invariance.\nFully Connected Layer: Flattens feature maps to output classification logits.",
        "tips": "Calculate output dimensions given input size W, Filter F, Padding P, and Stride S: `((W - F + 2P) / S) + 1`.",
        "star_guide": None
    },
    {
        "category": "Frontend",
        "title": "Handling Imbalanced Datasets in ML",
        "difficulty": "Medium",
        "question_text": "What strategies mitigate extreme class imbalance (e.g. 99% negative vs 1% positive class)?",
        "sample_answer": "1. Resampling: SMOTE (Synthetic Minority Over-sampling Technique) or Random Undersampling of majority class.\n2. Algorithmic adjustment: Adjust class weights in loss function (e.g. Focal Loss, `scale_pos_weight` in XGBoost).\n3. Evaluation: Avoid Accuracy; evaluate using Precision-Recall Curves, PR-AUC, or F1-score.",
        "tips": "Always perform SMOTE resampling AFTER splitting train/test sets to prevent data leakage.",
        "star_guide": None
    },

    # ==========================================
    # 6. QUANTITATIVE APTITUDE (3 SIDE HEADINGS & 17 SUB-TOPICS)
    # ==========================================
    # --- SIDE HEADING 1: NUMBER & ARITHMETIC ---
    {
        "category": "Aptitude",
        "sub_category": "Number & Arithmetic",
        "topic": "Number System",
        "title": "Number System - Unit Digit & Remainder Theorem",
        "difficulty": "Easy",
        "question_text": "Find the remainder when 2^31 is divided by 5.",
        "sample_answer": "Notice cyclicity of powers of 2 mod 5:\n2^1 = 2 (mod 5)\n2^2 = 4 (mod 5)\n2^3 = 3 (mod 5)\n2^4 = 1 (mod 5) -- Cyclicity of 4.\n31 = 4 * 7 + 3. Remainder is 2^3 (mod 5) = 8 (mod 5) = 3.",
        "tips": "Unit digit and remainder calculations repeat in cycles of 4 for powers.",
        "star_guide": None
    },
    {
        "category": "Aptitude",
        "sub_category": "Number & Arithmetic",
        "topic": "HCF & LCM",
        "title": "HCF & LCM - Product Formula & Ratios",
        "difficulty": "Easy",
        "question_text": "Two numbers are in the ratio 3:4. If their LCM is 180, find their HCF and the two numbers.",
        "sample_answer": "Let HCF = x. The numbers are 3x and 4x.\nLCM(3x, 4x) = 12x = 180 => x = 15.\nHence, HCF = 15.\nThe two numbers are 3 * 15 = 45 and 4 * 15 = 60.",
        "tips": "Formula: Product of Two Numbers = HCF * LCM.",
        "star_guide": None
    },
    {
        "category": "Aptitude",
        "sub_category": "Number & Arithmetic",
        "topic": "Divisibility",
        "title": "Divisibility Rules - Divisibility by 9",
        "difficulty": "Easy",
        "question_text": "Find the single digit value of x such that the 7-digit number 5678x42 is divisible by 9.",
        "sample_answer": "Divisibility rule for 9: Sum of digits must be divisible by 9.\nSum = 5 + 6 + 7 + 8 + x + 4 + 2 = 32 + x.\nNext multiple of 9 after 32 is 36.\n32 + x = 36 => x = 4.",
        "tips": "Sum of all digits must be a multiple of 9.",
        "star_guide": None
    },
    {
        "category": "Aptitude",
        "sub_category": "Number & Arithmetic",
        "topic": "Simplification",
        "title": "Simplification - BODMAS Rule Evaluation",
        "difficulty": "Easy",
        "question_text": "Evaluate the expression: 120 / 5 * 3 + (45 - 15) / 6.",
        "sample_answer": "Apply BODMAS Order (Brackets, Orders, Division/Multiplication, Addition/Subtraction):\n1. Brackets: (45 - 15) = 30.\n2. Division: 120 / 5 = 24 and 30 / 6 = 5.\n3. Multiplication: 24 * 3 = 72.\n4. Addition: 72 + 5 = 77.",
        "tips": "Always evaluate Brackets first, then Division and Multiplication from left to right.",
        "star_guide": None
    },
    {
        "category": "Aptitude",
        "sub_category": "Number & Arithmetic",
        "topic": "Averages",
        "title": "Averages - Teacher Inclusion Weight Problem",
        "difficulty": "Medium",
        "question_text": "The average weight of 10 students in a class is 45 kg. If the teacher's weight is included, the average weight increases by 1 kg. Find the weight of the teacher.",
        "sample_answer": "Total weight of 10 students = 10 * 45 = 450 kg.\nNew total count (students + teacher) = 11.\nNew average weight = 45 + 1 = 46 kg.\nTotal weight of 11 people = 11 * 46 = 506 kg.\nTeacher's Weight = 506 - 450 = 56 kg.",
        "tips": "Shortcut: Teacher Weight = Old Average + (New Count * Increase in Avg) = 45 + (11 * 1) = 56 kg.",
        "star_guide": None
    },
    {
        "category": "Aptitude",
        "sub_category": "Number & Arithmetic",
        "topic": "Percentages",
        "title": "Percentages - Inverse Percentage Difference",
        "difficulty": "Easy",
        "question_text": "If A's salary is 20% more than B's salary, by what percentage is B's salary less than A's salary?",
        "sample_answer": "Let B's salary = 100.\nA's salary = 120.\nDifference = 120 - 100 = 20.\nPercentage B is less than A = (20 / 120) * 100 = (1/6) * 100 = 16.67%.",
        "tips": "Shortcut Formula: Percentage Less = [R / (100 + R)] * 100 = [20 / 120] * 100 = 16.67%.",
        "star_guide": None
    },
    {
        "category": "Aptitude",
        "sub_category": "Number & Arithmetic",
        "topic": "Ratio & Proportion",
        "title": "Ratio & Proportion - Share Distribution",
        "difficulty": "Easy",
        "question_text": "Divide $1400 among A, B, and C in the ratio 2:3:5. Find the share of B.",
        "sample_answer": "Total ratio parts = 2 + 3 + 5 = 10 parts.\nValue of 1 part = 1400 / 10 = $140.\nB's share (3 parts) = 3 * 140 = $420.",
        "tips": "Share of X = (X's ratio / Sum of ratios) * Total Amount.",
        "star_guide": None
    },
    {
        "category": "Aptitude",
        "sub_category": "Number & Arithmetic",
        "topic": "Problems on Ages",
        "title": "Problems on Ages - Father & Son Age Ratio",
        "difficulty": "Easy",
        "question_text": "The ratio of the present ages of Father and Son is 7:2. After 10 years, the ratio of their ages will be 2:1. Find the present age of the Father.",
        "sample_answer": "Let present ages be 7x and 2x.\nAfter 10 years: (7x + 10) / (2x + 10) = 2 / 1.\nCross-multiplying: 7x + 10 = 4x + 20 => 3x = 10 => x = 10/3.\nFather's present age = 7 * (10/3) = 70/3 = 23.33 years.",
        "tips": "Set up linear equations comparing age ratios across time periods.",
        "star_guide": None
    },

    # --- SIDE HEADING 2: COMMERCIAL MATHEMATICS ---
    {
        "category": "Aptitude",
        "sub_category": "Commercial Mathematics",
        "topic": "Profit & Loss",
        "title": "Profit & Loss - Cost Price & Profit Percentage",
        "difficulty": "Easy",
        "question_text": "An item bought for $800 is sold for $960. Find the profit percentage.",
        "sample_answer": "Cost Price CP = $800. Selling Price SP = $960.\nProfit = SP - CP = 960 - 800 = $160.\nProfit % = (Profit / CP) * 100 = (160 / 800) * 100 = 20%.",
        "tips": "Profit percentage is always calculated on the Cost Price (CP).",
        "star_guide": None
    },
    {
        "category": "Aptitude",
        "sub_category": "Commercial Mathematics",
        "topic": "Simple Interest",
        "title": "Simple Interest - Interest & Amount Formula",
        "difficulty": "Easy",
        "question_text": "Calculate the Simple Interest on a principal of $5000 at an annual interest rate of 8% for 3 years.",
        "sample_answer": "Simple Interest Formula: SI = (P * R * T) / 100.\nSI = (5000 * 8 * 3) / 100 = 50 * 24 = $1200.\nTotal Amount A = P + SI = 5000 + 1200 = $6200.",
        "tips": "SI = (Principal * Rate * Time) / 100.",
        "star_guide": None
    },
    {
        "category": "Aptitude",
        "sub_category": "Commercial Mathematics",
        "topic": "Compound Interest",
        "title": "Compound Interest - Annual Compounding",
        "difficulty": "Medium",
        "question_text": "Calculate the Compound Interest on $10,000 at 10% per annum compounded annually for 2 years.",
        "sample_answer": "Amount Formula: A = P * (1 + R/100)^n.\nA = 10000 * (1 + 10/100)^2 = 10000 * (1.1)^2 = 10000 * 1.21 = $12,100.\nCompound Interest CI = Amount - Principal = 12100 - 10000 = $2100.",
        "tips": "CI = Amount - Principal = P[(1 + R/100)^n - 1].",
        "star_guide": None
    },
    {
        "category": "Aptitude",
        "sub_category": "Commercial Mathematics",
        "topic": "Discount",
        "title": "Discount - Successive Discount Percentage",
        "difficulty": "Medium",
        "question_text": "Successive discounts of 20% and 10% are equivalent to a single single discount of what percentage?",
        "sample_answer": "Let Marked Price MP = 100.\nAfter 1st discount (20%): Price = 100 * 0.80 = 80.\nAfter 2nd discount (10%): Price = 80 * 0.90 = 72.\nTotal Discount = 100 - 72 = 28%.\nShortcut Formula: Equivalent Discount = d1 + d2 - (d1 * d2)/100 = 20 + 10 - (200/100) = 28%.",
        "tips": "Formula: Equivalent Single Discount = A + B - (A*B)/100.",
        "star_guide": None
    },

    # --- SIDE HEADING 3: TIME-BASED PROBLEMS ---
    {
        "category": "Aptitude",
        "sub_category": "Time-Based Problems",
        "topic": "Time & Work",
        "title": "Time & Work - Combined Work Rate",
        "difficulty": "Easy",
        "question_text": "A can complete a piece of work in 12 days and B can complete the same work in 15 days. If they work together, how many days will it take to finish the work?",
        "sample_answer": "A's 1-day work = 1/12. B's 1-day work = 1/15.\nCombined 1-day work = (1/12) + (1/15) = (5 + 4)/60 = 9/60 = 3/20.\nTotal time taken = 20/3 = 6.67 days (6 days 16 hours).",
        "tips": "Formula: (A * B) / (A + B) = (12 * 15) / (12 + 15) = 180 / 27 = 20/3 = 6.67 days.",
        "star_guide": None
    },
    {
        "category": "Aptitude",
        "sub_category": "Time-Based Problems",
        "topic": "Pipes & Cisterns",
        "title": "Pipes & Cisterns - Leakage & Filling",
        "difficulty": "Medium",
        "question_text": "Two pipes A and B can fill a tank in 20 minutes and 30 minutes respectively. A third pipe C can empty the full tank in 40 minutes. If all three pipes are opened simultaneously, how long will it take to fill the tank?",
        "sample_answer": "Net 1-minute work = (1/20) + (1/30) - (1/40).\nLCM of 20, 30, 40 = 120.\nNet work = (6 + 4 - 3) / 120 = 7 / 120.\nTime taken = 120 / 7 minutes = 17.14 minutes (17 minutes 8 seconds).",
        "tips": "Inlet rates are positive; outlet/leak rates are negative.",
        "star_guide": None
    },
    {
        "category": "Aptitude",
        "sub_category": "Time-Based Problems",
        "topic": "Time, Speed & Distance",
        "title": "Time, Speed & Distance - Average Speed Formula",
        "difficulty": "Medium",
        "question_text": "A car travels from City A to City B (150 km) at a speed of 50 km/h and returns at a speed of 30 km/h. Find the average speed for the entire journey.",
        "sample_answer": "When distances are equal, Average Speed = (2 * x * y) / (x + y).\nAverage Speed = (2 * 50 * 30) / (50 + 30) = 3000 / 80 = 37.5 km/h.",
        "tips": "Average Speed is Harmonic Mean of speeds when distance traveled is equal.",
        "star_guide": None
    },
    {
        "category": "Aptitude",
        "sub_category": "Time-Based Problems",
        "topic": "Boats & Streams",
        "title": "Boats & Streams - Upstream & Downstream Speed",
        "difficulty": "Medium",
        "question_text": "A boat's speed in still water is 12 km/h and the stream speed is 3 km/h. Find the time taken by the boat to travel 45 km downstream and 45 km upstream.",
        "sample_answer": "Downstream Speed = Boat + Stream = 12 + 3 = 15 km/h.\nUpstream Speed = Boat - Stream = 12 - 3 = 9 km/h.\nDownstream Time = 45 / 15 = 3 hours.\nUpstream Time = 45 / 9 = 5 hours.\nTotal Time = 3 + 5 = 8 hours.",
        "tips": "Downstream = Speed_boat + Speed_stream; Upstream = Speed_boat - Speed_stream.",
        "star_guide": None
    },
    {
        "category": "Aptitude",
        "sub_category": "Time-Based Problems",
        "topic": "Trains",
        "title": "Trains - Train Crossing Platform Length",
        "difficulty": "Medium",
        "question_text": "A 180-meter long train running at a speed of 54 km/h crosses a railway platform in 20 seconds. What is the length of the platform?",
        "sample_answer": "Speed in m/s = 54 * (5/18) = 15 m/s.\nTotal distance covered in 20s = Speed * Time = 15 * 20 = 300 meters.\nTotal Distance = Train Length + Platform Length.\nPlatform Length = 300 - 180 = 120 meters.",
        "tips": "Convert km/h to m/s by multiplying by 5/18.",
        "star_guide": None
    }
]

def seed_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        # Create demo user if not exists
        demo_user = User.query.filter_by(username='demo').first()
        if not demo_user:
            demo_user = User(username='demo', email='demo@example.com', target_role='Software Engineer')
            demo_user.set_password('password123')
            db.session.add(demo_user)
            db.session.commit()

        # Delete existing questions and replace with curated questions with their proper categories
        Question.query.delete()
        for q_data in SEED_QUESTIONS:
            q = Question(**q_data)
            db.session.add(q)
        db.session.commit()
        print(f"Successfully seeded {len(SEED_QUESTIONS)} interview & aptitude questions into database!")

if __name__ == "__main__":
    seed_db()
