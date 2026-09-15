# Advanced Mock Interview Dataset - 10 Topics, 15 Questions Each

MOCK_TOPICS_DATA = {
    "python": {
        "name": "Python Programming (Advanced / Hard)",
        "questions": [
            {
                "id": 1,
                "title": "Python Metaclasses & Class Creation",
                "difficulty": "Hard",
                "question_text": "What is the precise execution order when Python instantiates a class whose metaclass overrides both <code>__new__</code> and <code>__init__</code>?",
                "options": [
                    "A) Metaclass __new__ -> Metaclass __init__ -> Class __new__ -> Class __init__",
                    "B) Class __init__ runs first -> Metaclass __new__ executes during import",
                    "C) Metaclass __init__ runs before Metaclass __new__",
                    "D) Metaclasses execute only when type() is called directly"
                ],
                "correct_option": "A",
                "explanation": "Metaclass __new__ constructs class object, __init__ initializes it, and class __new__/__init__ create instances."
            },
            {
                "id": 2,
                "title": "C3 Linearization & MRO Algorithm",
                "difficulty": "Hard",
                "question_text": "Python uses C3 Linearization for MRO. What exception is raised if an inheritance hierarchy breaks monotonicity?",
                "options": [
                    "A) RecursionError",
                    "B) TypeError: Cannot create a consistent method resolution order (MRO)",
                    "C) AttributeError",
                    "D) InheritanceError"
                ],
                "correct_option": "B",
                "explanation": "If class inheritance creates inconsistent ordering rules, Python raises TypeError at class definition time."
            },
            {
                "id": 3,
                "title": "Python __slots__ Memory Optimization",
                "difficulty": "Hard",
                "question_text": "What is the exact memory mechanism and side effect of defining <code>__slots__ = (\"x\", \"y\")</code> in Python?",
                "options": [
                    "A) Prevents inheritance",
                    "B) Replaces per-instance __dict__ dictionary with a fixed-size descriptor array, saving RAM",
                    "C) Stores attributes in C-stack",
                    "D) Converts floats to 32-bit int"
                ],
                "correct_option": "B",
                "explanation": "__slots__ allocates a compact descriptor array per instance instead of a dynamic dictionary."
            },
            {
                "id": 4,
                "title": "Descriptor Protocol Precedence",
                "difficulty": "Hard",
                "question_text": "What is the attribute lookup precedence order when accessing <code>obj.x</code> in Python?",
                "options": [
                    "A) Data Descriptor -> Instance __dict__ -> Non-Data Descriptor -> Class __dict__ -> __getattr__",
                    "B) Instance __dict__ -> Data Descriptor -> Class __dict__",
                    "C) __getattr__ -> Instance __dict__ -> Data Descriptor",
                    "D) Class __dict__ -> Instance __dict__ -> Data Descriptor"
                ],
                "correct_option": "A",
                "explanation": "Data descriptors (__set__/__delete__) override instance __dict__, while non-data descriptors (__get__) do not."
            },
            {
                "id": 5,
                "title": "Asyncio Event Loop Scheduling",
                "difficulty": "Hard",
                "question_text": "In Python <code>asyncio</code>, what happens when <code>await asyncio.sleep(0)</code> is executed inside a loop?",
                "options": [
                    "A) Blocks loop for 1 sec",
                    "B) Yields control back to event loop scheduler to execute pending tasks",
                    "C) Spawns OS thread",
                    "D) Resets GIL"
                ],
                "correct_option": "B",
                "explanation": "await asyncio.sleep(0) yields execution back to event loop queue so ready tasks execute."
            },
            {
                "id": 6,
                "title": "Programming Task 1: O(1) LRU Cache",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "class LRUCache:\n    def __init__(self, capacity: int):\n        # Initialize LRU Cache\n        pass\n\n    def get(self, key: int) -> int:\n        # Return value or -1\n        pass\n\n    def put(self, key: int, value: int) -> None:\n        # Insert or update key-value\n        pass",
                "question_text": "<strong>Problem Statement:</strong><br>Implement an LRU Cache with <code>get(key)</code> and <code>put(key, value)</code> in <strong>O(1) time complexity</strong>.<br><br>Write your Python solution:",
                "explanation": "Use Hash Map + Doubly Linked List."
            },
            {
                "id": 7,
                "title": "Programming Task 2: Token Bucket Rate Limiter",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "import time\nimport threading\n\nclass TokenBucketRateLimiter:\n    def __init__(self, capacity: int, refill_rate: float):\n        pass\n\n    def allow_request(self, tokens: int = 1) -> bool:\n        pass",
                "question_text": "<strong>Problem Statement:</strong><br>Implement a Thread-Safe Token Bucket Rate Limiter in Python.<br><br>Write your solution:",
                "explanation": "Refill tokens based on elapsed time under lock."
            },
            {
                "id": 8,
                "title": "Programming Task 3: Flatten Nested Dict",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "def flatten_dict(d, parent_key=\"\", sep=\".\"):\n    pass",
                "question_text": "<strong>Problem Statement:</strong><br>Write a recursive function <code>flatten_dict(d)</code> to flatten a nested dict with dot notation.<br><br>Write your solution:",
                "explanation": "Recursively concatenate parent_key + sep + k."
            },
            {
                "id": 9,
                "title": "Programming Task 4: Retry Decorator",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "import functools\nimport time\n\ndef retry(max_attempts=3, delay=1.0):\n    def decorator(func):\n        @functools.wraps(func)\n        def wrapper(*args, **kwargs):\n            pass\n        return wrapper\n    return decorator",
                "question_text": "<strong>Problem Statement:</strong><br>Write `@retry(max_attempts=3, delay=1.0)` decorator preserving signature.<br><br>Write your code:",
                "explanation": "Loop up to max_attempts, sleep on failure."
            },
            {
                "id": 10,
                "title": "Programming Task 5: Async Producer-Consumer",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "import asyncio\n\nasync def producer(queue, items):\n    pass\n\nasync def consumer(queue, result_list):\n    pass",
                "question_text": "<strong>Problem Statement:</strong><br>Implement async producer-consumer using <code>asyncio.Queue</code> and <code>None</code> sentinel.<br><br>Write your asyncio code:",
                "explanation": "Producer puts items and None sentinel. Consumer processes until None."
            },
            {
                "id": 11,
                "title": "Programming Task 6: Spiral Matrix Order",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "def spiral_order(matrix):\n    return []",
                "question_text": "<strong>Problem Statement:</strong><br>Return all 2D matrix elements in spiral order.<br><br>Write your code:",
                "explanation": "Traverse boundaries iteratively."
            },
            {
                "id": 12,
                "title": "Programming Task 7: File Chunk Generator",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "def read_in_chunks(file_path, chunk_size=1024):\n    pass",
                "question_text": "<strong>Problem Statement:</strong><br>Write a generator function reading a file in binary byte chunks without loading into RAM.<br><br>Write your generator:",
                "explanation": "Yield file.read(chunk_size) until empty."
            },
            {
                "id": 13,
                "title": "Programming Task 8: Group Anagrams",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "from collections import defaultdict\n\ndef group_anagrams(strs):\n    pass",
                "question_text": "<strong>Problem Statement:</strong><br>Group anagram strings together.<br><br>Write your solution:",
                "explanation": "Group by sorted string tuple key."
            },
            {
                "id": 14,
                "title": "Programming Task 9: Median of Two Sorted Arrays",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "def find_median_sorted_arrays(nums1, nums2):\n    pass",
                "question_text": "<strong>Problem Statement:</strong><br>Find median of two sorted arrays in <strong>O(log(min(M, N)))</strong>.<br><br>Write your solution:",
                "explanation": "Binary search on partition index."
            },
            {
                "id": 15,
                "title": "Programming Task 10: Thread-Safe Singleton",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "import threading\n\nclass Singleton:\n    _instance = None\n    _lock = threading.Lock()\n\n    def __new__(cls, *args, **kwargs):\n        pass",
                "question_text": "<strong>Problem Statement:</strong><br>Implement Thread-Safe Double-Checked Singleton in Python.<br><br>Write your class:",
                "explanation": "Double-check _instance is None around lock."
            }
        ]
    },
    "java": {
        "name": "Java Programming (Advanced / Hard)",
        "questions": [
            {
                "id": 1,
                "title": "JMM Volatile & Happens-Before Order",
                "difficulty": "Hard",
                "question_text": "In Java Memory Model (JMM), what is the exact semantic guarantee of a <code>volatile</code> variable write followed by a read?",
                "options": [
                    "A) Establishes a Happens-Before edge, preventing instruction reordering and forcing CPU cache flush to main memory",
                    "B) Prevents Garbage Collection on the variable",
                    "C) Converts primitive to BigInteger",
                    "D) Locks the entire JVM instance"
                ],
                "correct_option": "A",
                "explanation": "A volatile write happens-before subsequent reads, providing visibility and reordering barriers."
            },
            {
                "id": 2,
                "title": "G1 Garbage Collector Memory Allocation",
                "difficulty": "Hard",
                "question_text": "How does G1 GC handle objects larger than 50% of a region size?",
                "options": [
                    "A) Allocates them in special Humongous Regions directly in Old Generation",
                    "B) Throws OutOfMemoryError immediately",
                    "C) Allocates them in Metaspace",
                    "D) Converts them to ThreadLocal references"
                ],
                "correct_option": "A",
                "explanation": "G1 GC allocates large objects into contiguous Humongous Regions."
            },
            {
                "id": 3,
                "title": "ForkJoinPool Work-Stealing Algorithm",
                "difficulty": "Hard",
                "question_text": "How does ForkJoinPool achieve high throughput across worker threads?",
                "options": [
                    "A) Each worker thread owns a double-ended queue (deque); idle threads steal tasks from the tail of busy threads deques",
                    "B) Spawns OS processes per task",
                    "C) Uses blocking synchronized queues",
                    "D) Executes tasks in GPU memory"
                ],
                "correct_option": "A",
                "explanation": "ForkJoinPool uses work-stealing from deque tails to minimize lock contention."
            },
            {
                "id": 4,
                "title": "ReentrantLock CAS vs Synchronized",
                "difficulty": "Hard",
                "question_text": "What underlying AQS (AbstractQueuedSynchronizer) mechanism powers <code>ReentrantLock.tryLock()</code>?",
                "options": [
                    "A) Atomic Compare-And-Swap (CAS) state updates",
                    "B) OS Kernel mutex context switch",
                    "C) Java Native Interface Reflection",
                    "D) Garbage collector pause"
                ],
                "correct_option": "A",
                "explanation": "AQS uses CAS operations on an atomic state integer."
            },
            {
                "id": 5,
                "title": "Custom ClassLoader Delegation Hierarchy",
                "difficulty": "Hard",
                "question_text": "In Java ClassLoader delegation model, what is the default resolution order?",
                "options": [
                    "A) Bootstrap ClassLoader -> Extension/Platform ClassLoader -> Application ClassLoader",
                    "B) Application -> Bootstrap -> Platform",
                    "C) Platform -> Application -> Bootstrap",
                    "D) Random resolution order"
                ],
                "correct_option": "A",
                "explanation": "Parents are delegated to first: Bootstrap -> Platform -> App."
            },
            {
                "id": 6,
                "title": "Java Task 1: LRU Cache with LinkedHashMap",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "import java.util.LinkedHashMap;\nimport java.util.Map;\n\npublic class LRUCache<K, V> extends LinkedHashMap<K, V> {\n    private final int capacity;\n\n    public LRUCache(int capacity) {\n        super(capacity, 0.75f, True);\n        this.capacity = capacity;\n    }\n\n    @Override\n    protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {\n        // Return True when size > capacity\n        return False;\n    }\n}",
                "question_text": "<strong>Problem Statement:</strong><br>Implement an LRU Cache in Java by overriding <code>LinkedHashMap.removeEldestEntry</code>.<br><br>Write your Java solution:",
                "explanation": "Return `size() > capacity` inside removeEldestEntry."
            },
            {
                "id": 7,
                "title": "Java Task 2: Thread-Safe Blocking Queue",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "import java.util.LinkedList;\nimport java.util.Queue;\nimport java.util.concurrent.locks.Condition;\nimport java.util.concurrent.locks.ReentrantLock;\n\npublic class BoundedBlockingQueue<T> {\n    private final Queue<T> queue = new LinkedList<>();\n    private final int capacity;\n    private final ReentrantLock lock = new ReentrantLock();\n    private final Condition notFull = lock.newCondition();\n    private final Condition notEmpty = lock.newCondition();\n\n    public BoundedBlockingQueue(int capacity) {\n        this.capacity = capacity;\n    }\n\n    public void put(T item) throws InterruptedException {\n        // Implement put with lock & condition\n    }\n\n    public T take() throws InterruptedException {\n        // Implement take with lock & condition\n        return null;\n    }\n}",
                "question_text": "<strong>Problem Statement:</strong><br>Implement a Bounded Blocking Queue using <code>ReentrantLock</code> and <code>Condition</code> in Java.<br><br>Write your Java solution:",
                "explanation": "Lock around queue operations and wait on notFull / notEmpty conditions."
            },
            {
                "id": 8,
                "title": "Java Task 3: Binary Search Tree Iterator",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "import java.util.Stack;\n\nclass TreeNode {\n    int val;\n    TreeNode left, right;\n    TreeNode(int x) { val = x; }\n}\n\npublic class BSTIterator {\n    private Stack<TreeNode> stack = new Stack<>();\n\n    public BSTIterator(TreeNode root) {\n        pushAll(root);\n    }\n\n    public boolean hasNext() {\n        return !stack.isEmpty();\n    }\n\n    public int next() {\n        TreeNode node = stack.pop();\n        pushAll(node.right);\n        return node.val;\n    }\n\n    private void pushAll(TreeNode node) {\n        for (; node != null; stack.push(node), node = node.left);\n    }\n}",
                "question_text": "<strong>Problem Statement:</strong><br>Implement an in-order BST Iterator in Java using a Stack.<br><br>Write your Java solution:",
                "explanation": "Maintain stack of left children."
            },
            {
                "id": 9,
                "title": "Java Task 4: Top K Frequent Words PriorityQueue",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "import java.util.*;\n\npublic class TopKFrequent {\n    public List<String> topKFrequent(String[] words, int k) {\n        // Return top k frequent words using Min-Heap\n        return new ArrayList<>();\n    }\n}",
                "question_text": "<strong>Problem Statement:</strong><br>Find the top <code>k</code> most frequent words using a <code>PriorityQueue</code> Min-Heap in Java.<br><br>Write your Java solution:",
                "explanation": "Build frequency map, use Min-Heap size K sorted by freq and lexicographical order."
            },
            {
                "id": 10,
                "title": "Java Task 5: Custom ThreadPool Worker Queue",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "public class CustomThreadPool {\n    // Implement lightweight thread pool with Runnable task queue\n}",
                "question_text": "<strong>Problem Statement:</strong><br>Implement a lightweight Custom ThreadPool Executor in Java.<br><br>Write your solution:",
                "explanation": "Create worker threads polling a thread-safe Runnable queue."
            },
            {
                "id": 11,
                "title": "Java Task 6: String Run-Length Compression",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "public class StringCompressor {\n    public static String compress(String str) {\n        // \"aabcccccaaa\" -> \"a2b1c5a3\"\n        return str;\n    }\n}",
                "question_text": "<strong>Problem Statement:</strong><br>Compress a string using character run counts (e.g., <code>\"aabcccccaaa\"</code> to <code>\"a2b1c5a3\"</code>).<br><br>Write your Java solution:",
                "explanation": "Iterate characters counting consecutive duplicates and append to StringBuilder."
            },
            {
                "id": 12,
                "title": "Java Task 7: Design Immutable Class",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "import java.util.Date;\n\npublic final class ImmutableStudent {\n    private final String name;\n    private final Date dob;\n\n    public ImmutableStudent(String name, Date dob) {\n        this.name = name;\n        this.dob = new Date(dob.getTime()); // Defensive Copy\n    }\n\n    public String getName() { return name; }\n    public Date getDob() { return new Date(dob.getTime()); }\n}",
                "question_text": "<strong>Problem Statement:</strong><br>Design a completely Immutable class in Java with defensive copying for mutable fields.<br><br>Write your Java solution:",
                "explanation": "Make class final, fields final private, defensively copy mutable constructor parameters and getters."
            },
            {
                "id": 13,
                "title": "Java Task 8: Rotate Matrix 90 Degrees",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "public class MatrixRotator {\n    public void rotate(int[][] matrix) {\n        // Rotate N x N matrix 90 degrees clockwise in-place\n    }\n}",
                "question_text": "<strong>Problem Statement:</strong><br>Rotate an N x N 2D matrix 90 degrees clockwise in-place.<br><br>Write your Java solution:",
                "explanation": "Transpose matrix, then reverse each row."
            },
            {
                "id": 14,
                "title": "Java Task 9: Detect Loop in Linked List",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "class ListNode {\n    int val;\n    ListNode next;\n    ListNode(int x) { val = x; }\n}\n\npublic class LinkedListCycle {\n    public boolean hasCycle(ListNode head) {\n        // Floyd's Tortoise and Hare algorithm\n        return False;\n    }\n}",
                "question_text": "<strong>Problem Statement:</strong><br>Detect cycle in a Singly Linked List using Floyd's Tortoise and Hare algorithm.<br><br>Write your Java solution:",
                "explanation": "Use slow (1 step) and fast (2 steps) pointers; if slow == fast, cycle exists."
            },
            {
                "id": 15,
                "title": "Java Task 10: Thread-Safe Enum Singleton",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "public enum EnumSingleton {\n    INSTANCE;\n\n    public void executeOperation() {\n        // Implement singleton operation\n    }\n}",
                "question_text": "<strong>Problem Statement:</strong><br>Implement an idiomatic Thread-Safe Singleton in Java using <code>enum</code>.<br><br>Write your Java solution:",
                "explanation": "Enums guarantee thread safety and reflection-proof singleton creation."
            }
        ]
    },
    "sql": {
        "name": "SQL & Databases (Advanced / Hard)",
        "questions": [
            {
                "id": 1,
                "title": "ACID Isolation Levels & Phantom Reads",
                "difficulty": "Hard",
                "question_text": "Which SQL Isolation level guarantees prevention of Phantom Reads according to ANSI SQL standard?",
                "options": [
                    "A) SERIALIZABLE",
                    "B) READ COMMITTED",
                    "C) READ UNCOMMITTED",
                    "D) REPEATABLE READ"
                ],
                "correct_option": "A",
                "explanation": "SERIALIZABLE acquires range locks or uses SSI to prevent phantom reads."
            },
            {
                "id": 2,
                "title": "B-Tree Index Covering Scans",
                "difficulty": "Hard",
                "question_text": "What is an Index-Only Scan (Covering Index) in database execution plans?",
                "options": [
                    "A) Query engine fetches all requested columns directly from the index tree without visiting heap table pages",
                    "B) Index created only on primary keys",
                    "C) Full table scan",
                    "D) Temporary memory table"
                ],
                "correct_option": "A",
                "explanation": "If index contains all columns in SELECT/WHERE, heap page fetch is bypassed."
            },
            {
                "id": 3,
                "title": "PostgreSQL MVCC & VACUUM",
                "difficulty": "Hard",
                "question_text": "In PostgreSQL MVCC architecture, why is auto-VACUUM required?",
                "options": [
                    "A) To reclaim dead tuples (bloat) left by UPDATE/DELETE statements",
                    "B) To clear RAM cache",
                    "C) To restart database server",
                    "D) To rebuild primary keys"
                ],
                "correct_option": "A",
                "explanation": "MVCC creates tuple versions; VACUUM cleans up dead tuples."
            },
            {
                "id": 4,
                "title": "Deadlocks & Intent Lock Escalation",
                "difficulty": "Hard",
                "question_text": "What type of lock is acquired at table level before acquiring a row-level Exclusive (X) lock?",
                "options": [
                    "A) Intent Exclusive (IX) Lock",
                    "B) Shared Lock",
                    "C) Exclusive Lock",
                    "D) Schema Lock"
                ],
                "correct_option": "A",
                "explanation": "Intent Exclusive (IX) locks signal pending row-level updates."
            },
            {
                "id": 5,
                "title": "Database Normalization BCNF vs 3NF",
                "difficulty": "Hard",
                "question_text": "A relation is in Boyce-Codd Normal Form (BCNF) if and only if for every non-trivial functional dependency X -> Y:",
                "options": [
                    "A) X is a superkey",
                    "B) Y is a primary key",
                    "C) X is atomic",
                    "D) Y is a foreign key"
                ],
                "correct_option": "A",
                "explanation": "BCNF requires every determinant X to be a superkey."
            },
            {
                "id": 6,
                "title": "SQL Query 1: Running Total & Moving Average",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "-- TODO: Write an SQL query using Window Functions (SUM() OVER and AVG() OVER)\n-- to compute running total and 3-month moving average per customer.\n\n-- SELECT ...",
                "question_text": "<strong>Problem Statement:</strong><br>Write an SQL query using Window Functions (<code>SUM() OVER</code> and <code>AVG() OVER</code>) to compute running total and 3-month moving average per customer.<br><br>Write your SQL query below:",
                "explanation": "Use window frames PARTITION BY customer_id ORDER BY transaction_date."
            },
            {
                "id": 7,
                "title": "SQL Query 2: Nth Highest Salary per Department",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "-- TODO: Write an SQL query using DENSE_RANK()\n-- to find employees earning the 2nd highest salary in each department.\n\n-- WITH RankedSalaries AS (...)",
                "question_text": "<strong>Problem Statement:</strong><br>Write an SQL query using <code>DENSE_RANK()</code> to find employees earning the 2nd highest salary in each department.<br><br>Write your SQL query below:",
                "explanation": "Use CTE with DENSE_RANK() PARTITION BY department_id ORDER BY salary DESC."
            },
            {
                "id": 8,
                "title": "SQL Query 3: Island & Gap Continuous Active Logins",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "-- TODO: Solve the Island & Gap problem to identify continuous login streaks\n-- of 3 or more consecutive days for users.\n\n-- SELECT ...",
                "question_text": "<strong>Problem Statement:</strong><br>Solve the Island & Gap problem to identify continuous login streaks of 3 or more consecutive days.<br><br>Write your SQL query below:",
                "explanation": "Subtract ROW_NUMBER() from login_date to group consecutive date streaks."
            },
            {
                "id": 9,
                "title": "SQL Query 4: Recursive Employee Hierarchy",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "-- TODO: Write a Recursive CTE query (WITH RECURSIVE)\n-- to generate the organizational hierarchy tree depth for all employees.\n\n-- WITH RECURSIVE OrgHierarchy AS (...)",
                "question_text": "<strong>Problem Statement:</strong><br>Write a Recursive CTE query (<code>WITH RECURSIVE</code>) to generate the organizational hierarchy tree depth for all employees.<br><br>Write your SQL query below:",
                "explanation": "Anchor query selects top manager, recursive term joins employees on manager_id."
            },
            {
                "id": 10,
                "title": "SQL Query 5: Deduplicate Records keeping Latest",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "-- TODO: Write an SQL statement using ROW_NUMBER() to deduplicate records,\n-- keeping only the most recent record per email.\n\n-- DELETE FROM users ...",
                "question_text": "<strong>Problem Statement:</strong><br>Write an SQL statement to deduplicate records in a table, keeping only the most recent record per email.<br><br>Write your SQL query below:",
                "explanation": "Use ROW_NUMBER() PARTITION BY email ORDER BY updated_at DESC and delete rnk > 1."
            },
            {
                "id": 11,
                "title": "SQL Query 6: Monthly Cohort Retention Analysis",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "-- TODO: Write an SQL query to calculate 30-day user cohort retention percentage\n-- grouped by signup month.\n\n-- SELECT ...",
                "question_text": "<strong>Problem Statement:</strong><br>Write an SQL query to calculate 30-day user cohort retention percentage by signup month.<br><br>Write your SQL query below:",
                "explanation": "Group by signup month and left join active logs within 30 days."
            },
            {
                "id": 12,
                "title": "SQL Query 7: Pivot Monthly Sales into Columns",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "-- TODO: Write an SQL query to pivot monthly sales rows into columns (Jan, Feb, Mar)\n-- per year using conditional aggregation (CASE WHEN).\n\n-- SELECT ...",
                "question_text": "<strong>Problem Statement:</strong><br>Pivot monthly sales rows into columns (Jan, Feb, Mar) per year using conditional aggregation.<br><br>Write your SQL query below:",
                "explanation": "Aggregate SUM(CASE WHEN month = X THEN sales END) grouped by year."
            },
            {
                "id": 13,
                "title": "SQL Query 8: Customers Buying A and B but NOT C",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "-- TODO: Write an SQL query to find all customer IDs who purchased Product A AND Product B,\n-- but NEVER Product C using set operations.\n\n-- SELECT ...",
                "question_text": "<strong>Problem Statement:</strong><br>Find all customer IDs who purchased Product A AND Product B, but NEVER Product C.<br><br>Write your SQL query below:",
                "explanation": "Use INTERSECT for A and B, then EXCEPT for C."
            },
            {
                "id": 14,
                "title": "SQL Query 9: Audit Trail Trigger Function",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "-- TODO: Write a PostgreSQL trigger function (CREATE OR REPLACE FUNCTION)\n-- to log table mutation changes to an audit table in JSON format.\n\n-- CREATE OR REPLACE FUNCTION ...",
                "question_text": "<strong>Problem Statement:</strong><br>Write a PostgreSQL trigger function to log table mutation changes to an audit table in JSON format.<br><br>Write your SQL query below:",
                "explanation": "Use row_to_json(OLD) and row_to_json(NEW) inside trigger function."
            },
            {
                "id": 15,
                "title": "SQL Query 10: Optimize Query with Index Hint & Partitions",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "-- TODO: Write an optimized SQL query utilizing partition pruning\n-- to aggregate monthly sales data efficiently.\n\n-- SELECT ...",
                "question_text": "<strong>Problem Statement:</strong><br>Write an optimized SQL query utilizing partition pruning to aggregate monthly sales data efficiently.<br><br>Write your SQL query below:",
                "explanation": "Filter on partition key to enable partition pruning."
            }
        ]
    },
    "oops": {
        "name": "OOPs Concepts (Advanced / Hard)",
        "questions": [
            {
                "id": 1,
                "title": "OOPS Theory Concept #1",
                "difficulty": "Hard",
                "question_text": "Question 1: What is the core architectural principle regarding <code>OOPs Concepts (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for OOPs Concepts (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for OOPs Concepts (Advanced / Hard)."
            },
            {
                "id": 2,
                "title": "OOPS Theory Concept #2",
                "difficulty": "Hard",
                "question_text": "Question 2: What is the core architectural principle regarding <code>OOPs Concepts (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for OOPs Concepts (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for OOPs Concepts (Advanced / Hard)."
            },
            {
                "id": 3,
                "title": "OOPS Theory Concept #3",
                "difficulty": "Hard",
                "question_text": "Question 3: What is the core architectural principle regarding <code>OOPs Concepts (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for OOPs Concepts (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for OOPs Concepts (Advanced / Hard)."
            },
            {
                "id": 4,
                "title": "OOPS Theory Concept #4",
                "difficulty": "Hard",
                "question_text": "Question 4: What is the core architectural principle regarding <code>OOPs Concepts (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for OOPs Concepts (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for OOPs Concepts (Advanced / Hard)."
            },
            {
                "id": 5,
                "title": "OOPS Theory Concept #5",
                "difficulty": "Hard",
                "question_text": "Question 5: What is the core architectural principle regarding <code>OOPs Concepts (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for OOPs Concepts (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for OOPs Concepts (Advanced / Hard)."
            },
            {
                "id": 6,
                "title": "Programming Task: Create Student Class with Attributes & Display Method",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "class Student:\n    def __init__(self, name, roll_no, marks):\n        # TODO: Write code to initialize name, roll_no, and marks attributes\n        pass\n\n    def display(self):\n        # TODO: Write code to display all student details\n        pass\n\n# TODO: Create a Student object and display all details",
                "question_text": "<strong>Student Class Practical Task:</strong><br><br>Create a <code>Student</code> class with the following attributes:<br><ul><li><code>name</code></li><li><code>roll_no</code></li><li><code>marks</code></li></ul><br>Instantiate an object of the <code>Student</code> class, initialize its attributes, and write a method to display all details cleanly.",
                "explanation": "Define an __init__(self, name, roll_no, marks) constructor method to initialize instance variables, create an instance object of Student, and call display() to print name, roll_no, and marks."
            },
            {
                "id": 7,
                "title": "Programming Task: Create Circle Class with area() and circumference() Methods",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "import math\n\nclass Circle:\n    def __init__(self, radius: float):\n        # TODO: Write code to initialize radius attribute\n        pass\n\n    def area(self) -> float:\n        # TODO: Write code to calculate and return the area of the circle (pi * r^2)\n        pass\n\n    def circumference(self) -> float:\n        # TODO: Write code to calculate and return the circumference of the circle (2 * pi * r)\n        pass\n\n# TODO: Create a Circle object and call area() and circumference() methods",
                "question_text": "<strong>Circle Class Practical Task:</strong><br><br>Create a <code>Circle</code> class that accepts <code>radius</code> through its constructor (<code>__init__</code>).<br><br>Implement the following methods:<br><ul><li><code>area()</code>: Calculates and returns the area of the circle.</li><li><code>circumference()</code>: Calculates and returns the perimeter/circumference of the circle.</li></ul>",
                "explanation": "Store self.radius in __init__. Calculate area using math.pi * (self.radius ** 2) and circumference using 2 * math.pi * self.radius."
            },
            {
                "id": 8,
                "title": "Programming Task: Bank Account Class with Encapsulation & Private __balance Attribute",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "class BankAccount:\n    def __init__(self, initial_balance: float = 0.0):\n        # TODO: Initialize private attribute __balance\n        pass\n\n    def deposit(self, amount: float) -> None:\n        # TODO: Write code to add deposit amount to private __balance\n        pass\n\n    def withdraw(self, amount: float) -> bool:\n        # TODO: Write code to deduct amount from private __balance if funds exist\n        pass\n\n    def get_balance(self) -> float:\n        # TODO: Write code to return current private __balance\n        pass\n\n# TODO: Create a BankAccount object, perform deposit/withdraw operations, and print get_balance()",
                "question_text": "<strong>Bank Account Encapsulation Practical Task:</strong><br><br>Create a <code>BankAccount</code> class using Object-Oriented Encapsulation principles.<br><br><strong>Requirements:</strong><br><ul><li>Encapsulate account balance in a private variable <code>__balance</code>.</li><li><code>deposit(amount)</code>: Adds the specified amount to <code>__balance</code>.</li><li><code>withdraw(amount)</code>: Deducts the specified amount from <code>__balance</code>.</li><li><code>get_balance()</code>: Returns the current private <code>__balance</code> value.</li></ul>",
                "explanation": "Encapsulation hides object state behind private attributes (prefixed with __balance in Python). State mutations and access are handled securely through deposit(), withdraw(), and get_balance()."
            },
            {
                "id": 9,
                "title": "Programming Task: Single Inheritance (Vehicle → Car Class Hierarchy)",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "class Vehicle:\n    def start(self):\n        # TODO: Write code for start method\n        pass\n\n    def stop(self):\n        # TODO: Write code for stop method\n        pass\n\nclass Car(Vehicle):\n    def drive(self):\n        # TODO: Write code for drive method\n        pass\n\n# TODO: Create a Car object and call start(), drive(), and stop() methods",
                "question_text": "<strong>Single Inheritance Practical Task (Vehicle → Car):</strong><br><br>Implement a single inheritance hierarchy using OOP principles.<br><br><strong>Requirements:</strong><br><ul><li>Create a base class <code>Vehicle</code> with methods:<ul><li><code>start()</code>: Displays vehicle starting message.</li><li><code>stop()</code>: Displays vehicle stopping message.</li></ul></li><li>Create a derived class <code>Car</code> that inherits from <code>Vehicle</code> with method:<ul><li><code>drive()</code>: Displays car driving message.</li></ul></li></ul><br>Instantiate a <code>Car</code> object and call all three methods (<code>start()</code>, <code>drive()</code>, and <code>stop()</code>).",
                "explanation": "In OOP single inheritance, the derived class Car inherits base methods start() and stop() from Vehicle, while defining its own child method drive()."
            },
            {
                "id": 10,
                "title": "Programming Task: Method Overriding (Animal, Dog, and Cat Class Hierarchy)",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "class Animal:\n    def sound(self):\n        # TODO: Write code for base Animal sound method\n        pass\n\nclass Dog(Animal):\n    def sound(self):\n        # TODO: Override sound method for Dog\n        pass\n\nclass Cat(Animal):\n    def sound(self):\n        # TODO: Override sound method for Cat\n        pass\n\n# TODO: Create objects of Animal, Dog, and Cat, and call sound() on each object",
                "question_text": "<strong>Method Overriding Practical Task:</strong><br><br>Implement Object-Oriented Polymorphism and Method Overriding.<br><br><strong>Requirements:</strong><br><ul><li>Create a base class <code>Animal</code> with a <code>sound()</code> method.</li><li>Create a derived class <code>Dog</code> that inherits from <code>Animal</code> and overrides the <code>sound()</code> method.</li><li>Create a derived class <code>Cat</code> that inherits from <code>Animal</code> and overrides the <code>sound()</code> method.</li></ul><br>Instantiate objects of <code>Animal</code>, <code>Dog</code>, and <code>Cat</code>, and call the <code>sound()</code> method on each object to demonstrate dynamic method dispatch.",
                "explanation": "Method overriding allows child classes (Dog, Cat) to provide specific implementations of a method (sound()) that is already defined in their parent class (Animal)."
            },
            {
                "id": 11,
                "title": "Programming Task: Polymorphic Payment Gateway System (CreditCard, UPI, Cash)",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "class Payment:\n    def pay(self, amount: float):\n        # TODO: Base pay method\n        pass\n\nclass CreditCard(Payment):\n    def pay(self, amount: float):\n        # TODO: Implement CreditCard payment logic\n        pass\n\nclass UPI(Payment):\n    def pay(self, amount: float):\n        # TODO: Implement UPI payment logic\n        pass\n\nclass Cash(Payment):\n    def pay(self, amount: float):\n        # TODO: Implement Cash payment logic\n        pass\n\n# TODO: Demonstrate polymorphism by calling pay() on CreditCard, UPI, and Cash objects",
                "question_text": "<strong>Polymorphic Payment Gateway Task:</strong><br><br>Implement Object-Oriented Polymorphism for a Payment Gateway.<br><br><strong>Requirements:</strong><br><ul><li>Create a base class <code>Payment</code> with a <code>pay(amount)</code> method.</li><li>Create derived classes:<ul><li><code>CreditCard</code> (inherits from <code>Payment</code>)</li><li><code>UPI</code> (inherits from <code>Payment</code>)</li><li><code>Cash</code> (inherits from <code>Payment</code>)</li></ul></li><li>Each class must implement/override the <code>pay(amount)</code> method.</li></ul><br>Instantiate objects of <code>CreditCard</code>, <code>UPI</code>, and <code>Cash</code>, and call <code>pay(amount)</code> polymorphically.",
                "explanation": "Polymorphism allows objects of different classes (CreditCard, UPI, Cash) to be processed uniformly via a common interface method pay(amount), executing specialized behaviors dynamically."
            },
            {
                "id": 12,
                "title": "Programming Task: Abstract Base Class Shape (using abc Module with Circle & Rectangle)",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "from abc import ABC, abstractmethod\nimport math\n\nclass Shape(ABC):\n    @abstractmethod\n    def area(self) -> float:\n        # TODO: Define abstract method for area calculation\n        pass\n\nclass Circle(Shape):\n    def __init__(self, radius: float):\n        # TODO: Initialize radius attribute\n        pass\n\n    def area(self) -> float:\n        # TODO: Implement area calculation for Circle (pi * r^2)\n        pass\n\nclass Rectangle(Shape):\n    def __init__(self, width: float, height: float):\n        # TODO: Initialize width and height attributes\n        pass\n\n    def area(self) -> float:\n        # TODO: Implement area calculation for Rectangle (width * height)\n        pass\n\n# TODO: Create Circle and Rectangle objects, and print area() for both",
                "question_text": "<strong>Abstract Class Practical Task (Shape → Circle, Rectangle):</strong><br><br>Use Python's built-in <code>abc</code> (Abstract Base Class) module to enforce abstraction principles.<br><br><strong>Requirements:</strong><br><ul><li>Create an abstract base class <code>Shape</code> inheriting from <code>ABC</code>.</li><li>Define an abstract method <code>@abstractmethod def area(self):</code> in <code>Shape</code>.</li><li>Create derived concrete classes:<ul><li><code>Circle</code> (accepts <code>radius</code> in constructor)</li><li><code>Rectangle</code> (accepts <code>width</code> and <code>height</code> in constructor)</li></ul></li><li>Implement the <code>area()</code> method in both <code>Circle</code> and <code>Rectangle</code>.</li></ul><br>Instantiate <code>Circle</code> and <code>Rectangle</code> objects, and print their calculated areas.",
                "explanation": "Abstract base classes (created using ABC and @abstractmethod from the abc module) define a common blueprint/contract that all concrete subclasses (Circle, Rectangle) must implement."
            },
            {
                "id": 13,
                "title": "Programming Task: Restaurant Management System OOD (Restaurant, Food, Customer, Order)",
                "difficulty": "Medium",
                "is_coding": True,
                "starter_code": "class Food:\n    def __init__(self, name: str, price: float):\n        # TODO: Write code to initialize food item name and price\n        pass\n\nclass Customer:\n    def __init__(self, name: str, customer_id: int):\n        # TODO: Write code to initialize customer details\n        pass\n\nclass Order:\n    def __init__(self, order_id: int, customer: Customer):\n        # TODO: Write code to initialize order with customer and empty items list\n        pass\n\n    def add_food(self, food_item: Food):\n        # TODO: Write code to add food item to order\n        pass\n\n    def calculate_bill(self) -> float:\n        # TODO: Write code to calculate and return total bill sum\n        pass\n\n    def display_order(self):\n        # TODO: Write code to display customer details, ordered food items, and total bill\n        pass\n\nclass Restaurant:\n    def __init__(self, name: str):\n        # TODO: Write code to initialize restaurant name and menu list\n        pass\n\n    def add_food(self, food_item: Food):\n        # TODO: Write code to add food item to restaurant menu\n        pass\n\n    def place_order(self, customer: Customer, food_items: list) -> Order:\n        # TODO: Write code to create, populate, and return a new Order\n        pass\n\n# TODO: Demonstrate system: add food to menu, place an order, calculate bill, and display order",
                "question_text": "<strong>Restaurant Management System Object-Oriented Design Task:</strong><br><br>Design an Object-Oriented system for a Restaurant Order System.<br><br><strong>Classes to Create:</strong><br><ul><li><code>Food</code>: Represents food items with <code>name</code> and <code>price</code>.</li><li><code>Customer</code>: Represents customer details with <code>name</code> and <code>customer_id</code>.</li><li><code>Order</code>: Represents an order placed by a customer containing a list of food items.</li><li><code>Restaurant</code>: Manages the menu and customer orders.</li></ul><br><strong>Operations to Implement:</strong><br><ul><li><strong>Add food</strong> to restaurant menu</li><li><strong>Place order</strong> for a customer</li><li><strong>Calculate bill</strong> (sum of food item prices)</li><li><strong>Display order</strong> details (customer, ordered food items, total bill)</li></ul>",
                "explanation": "This problem demonstrates Object-Oriented Analysis & Design (OOAD) using Composition and Aggregation relationships between Restaurant, Food, Customer, and Order entities."
            },
            {
                "id": 14,
                "title": "Programming Task: TrainTicket Class (Store & Display Ticket Details)",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "class TrainTicket:\n    def __init__(self, passenger_name: str, train_number: int, ticket_price: float):\n        # TODO: Write code to initialize passenger_name, train_number, and ticket_price\n        pass\n\n    def display_ticket(self):\n        # TODO: Write code to display all ticket information\n        pass\n\n# TODO: Create a TrainTicket object with sample details and call display_ticket()",
                "question_text": "<strong>Train Ticket Practical Task:</strong><br><br>Create a <code>TrainTicket</code> class to manage reservation ticket information.<br><br><strong>Requirements:</strong><br><ul><li>Store the following attributes via constructor (<code>__init__</code>):<ul><li><code>passenger_name</code></li><li><code>train_number</code></li><li><code>ticket_price</code></li></ul></li><li>Implement a method <code>display_ticket()</code> to display all ticket information cleanly.</li></ul><br>Instantiate a <code>TrainTicket</code> object with sample data and call <code>display_ticket()</code>.",
                "explanation": "Define instance attributes (passenger_name, train_number, ticket_price) inside __init__ and output formatted ticket details in display_ticket()."
            },
            {
                "id": 15,
                "title": "Programming Task: Bird Sounds Hierarchy & Method Overriding (Bird, Sparrow, Parrot, Crow)",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "class Bird:\n    def sound(self):\n        # TODO: Write base Bird sound method\n        pass\n\nclass Sparrow(Bird):\n    def sound(self):\n        # TODO: Override sound method for Sparrow\n        pass\n\nclass Parrot(Bird):\n    def sound(self):\n        # TODO: Override sound method for Parrot\n        pass\n\nclass Crow(Bird):\n    def sound(self):\n        # TODO: Override sound method for Crow\n        pass\n\n# TODO: Create objects of Sparrow, Parrot, and Crow, and call sound() on each",
                "question_text": "<strong>Bird Sounds Method Overriding Task:</strong><br><br>Implement Object-Oriented Polymorphism and Method Overriding for a Bird classification hierarchy.<br><br><strong>Requirements:</strong><br><ul><li>Create a base class <code>Bird</code> with a <code>sound()</code> method.</li><li>Create derived classes inheriting from <code>Bird</code>:<ul><li><code>Sparrow</code></li><li><code>Parrot</code></li><li><code>Crow</code></li></ul></li><li>Override the <code>sound()</code> method in each derived class to output its characteristic bird call/sound.</li></ul><br>Instantiate objects of <code>Sparrow</code>, <code>Parrot</code>, and <code>Crow</code>, and call <code>sound()</code> on each object.",
                "explanation": "Method overriding enables each specific bird type (Sparrow, Parrot, Crow) to provide its own sound() behavior while sharing a common base interface Bird."
            }
        ]
    },
    "aws": {
        "name": "AWS Cloud Architecture (Advanced / Hard)",
        "questions": [
            {
                "id": 1,
                "title": "High-Scale Multi-VPC Architecture & Transit Gateway Failover",
                "difficulty": "Hard",
                "question_text": "An enterprise organization needs to connect 50 VPCs across two AWS regions (<code>us-east-1</code> and <code>eu-west-1</code>) and on-premises datacenters. The network architecture must support full transitive routing, centralized firewall inspection, and dynamic BGP routing over AWS Direct Connect. Which AWS networking architecture provides the most scalable, resilient design with minimal operational overhead?",
                "options": [
                    "A) Deploy an AWS Transit Gateway in each region, establish a Transit Gateway Peering connection between regions, attach VPCs to local Transit Gateways, and terminate Direct Connect Gateway on both Transit Gateways with active-active BGP.",
                    "B) Create full-mesh VPC Peering connections between all 50 VPCs across both regions and configure software VPN instances in each VPC connected to on-premises routers.",
                    "C) Attach all VPCs directly to an AWS Direct Connect Gateway and rely on default VPC route tables to handle cross-region inter-VPC transitive routing.",
                    "D) Deploy Network Load Balancers in every VPC and use AWS PrivateLink endpoints linked via AWS CloudFront for cross-region transitive data exchange."
                ],
                "correct_option": "A",
                "explanation": "AWS Transit Gateway acts as a regional network transit hub and supports cross-region Transit Gateway Peering. Transit Gateway supports transitive routing and attaches seamlessly to AWS Direct Connect Gateway with dynamic BGP routing. Full-mesh VPC peering does not scale across 50 VPCs and does not support transitive routing."
            },
            {
                "id": 2,
                "title": "Amazon S3 Multi-Region Access Points & Cross-Region Replication",
                "difficulty": "Hard",
                "question_text": "A global financial application requires real-time read and write capability for object storage across <code>us-west-2</code> and <code>ap-northeast-1</code> with failover handling in under 1 second. Objects written in one region must be replicated asynchronously to the second region with replication time control (RTC) guarantees. Which solution meets these requirements with automated routing?",
                "options": [
                    "A) Deploy Amazon S3 Multi-Region Access Points (MRAP) with S3 Cross-Region Replication (CRR) and S3 Replication Time Control (RTC) enabled, configured with Failover Controls.",
                    "B) Configure an Elastic Load Balancer (ALB) pointing to S3 buckets in both regions with health checks triggering AWS Route 53 DNS updates.",
                    "C) Store files in Amazon EFS and use EFS Replication without S3, pointing user uploads to local EC2 instances.",
                    "D) Create an AWS Lambda function triggered by S3 Event Notifications to manually read and upload S3 objects using Boto3 put_object() across regions."
                ],
                "correct_option": "A",
                "explanation": "S3 Multi-Region Access Points (MRAP) provide a single global endpoint for S3 buckets across regions with built-in active-active or active-passive failover controls. Combined with S3 CRR and S3 Replication Time Control (RTC), AWS guarantees 99.9% of objects replicate within 15 minutes supported by SLA."
            },
            {
                "id": 3,
                "title": "AWS IAM Permission Boundaries & Resource-Based Policy Evaluation",
                "difficulty": "Hard",
                "question_text": "An IAM User has an attached Identity Policy granting <code>s3:GetObject</code> on <code>arn:aws:s3:::corporate-data/*</code>. An IAM Permission Boundary attached to the user grants <code>s3:*</code>. However, the target S3 bucket has a Bucket Policy with an explicit <code>Deny</code> for <code>s3:GetObject</code> when the request originates from outside the corporate CIDR <code>203.0.113.0/24</code>. The user attempts <code>s3:GetObject</code> from IP <code>198.51.100.50</code>. What is the result of the IAM authorization evaluation?",
                "options": [
                    "A) Access Granted: Identity policies take precedence over bucket policies.",
                    "B) Access Denied: An explicit Deny in any applicable policy (Identity, Resource, or Permission Boundary) overrides all Allows.",
                    "C) Access Granted: The Permission Boundary grants s3:* which bypasses the Bucket Policy Deny.",
                    "D) Access Denied: Permission Boundaries override Identity policies even when conditions match."
                ],
                "correct_option": "B",
                "explanation": "AWS IAM policy evaluation logic follows a fundamental enforcement rule: By default, all requests are implicitly denied. An explicit Allow in any policy grants access UNLESS there is an explicit Deny anywhere in any applicable policy. An explicit Deny ALWAYS overrides any Allows."
            },
            {
                "id": 4,
                "title": "Amazon DynamoDB Global Tables & High Availability",
                "difficulty": "Hard",
                "question_text": "A mission-critical e-commerce platform uses Amazon DynamoDB for order processing. The platform requires multi-region active-active reads and writes with sub-10 millisecond latency and automatic multi-master conflict resolution. How does DynamoDB Global Tables resolve simultaneous concurrent writes to the same item in two different regions?",
                "options": [
                    "A) DynamoDB uses a 'Last-Writer-Wins' reconciliation policy based on client timestamp and internal NTP synchronization.",
                    "B) DynamoDB locks the item across all global replica regions using 2-Phase Commit (2PC) until all regions confirm write locks.",
                    "C) The write in the secondary region is rejected with a ConditionalCheckFailedException until the primary region syncs.",
                    "D) DynamoDB raises a GlobalConflictError requiring manual intervention via AWS CloudWatch Alarm triggers."
                ],
                "correct_option": "A",
                "explanation": "Amazon DynamoDB Global Tables provides multi-master active-active replication across AWS regions. When concurrent updates occur to the same item in multiple regions simultaneously, DynamoDB uses a 'Last-Writer-Wins' conflict resolution mechanism where the most recent write timestamp is preserved across all replicas."
            },
            {
                "id": 5,
                "title": "AWS Lambda & Amazon SQS FIFO Deduplication & Concurrency",
                "difficulty": "Hard",
                "question_text": "A banking transaction engine uses Amazon SQS FIFO queues to trigger AWS Lambda functions for payment processing. The queue receives duplicate messages containing unique <code>MessageDeduplicationId</code> hashes within a 5-minute deduplication interval. How does AWS SQS FIFO handle duplicate messages sent during this window?",
                "options": [
                    "A) SQS accepts duplicate messages, inserts them into the Dead Letter Queue (DLQ), and invokes Lambda twice.",
                    "B) SQS successfully acknowledges message delivery to the sender but does not deliver duplicate messages to consumers during the 5-minute deduplication window.",
                    "C) SQS throws an InvalidParameterValueException back to the publisher API immediately.",
                    "D) SQS converts the FIFO queue dynamically to a Standard Queue and processes messages out of order."
                ],
                "correct_option": "B",
                "explanation": "SQS FIFO queues enforce exact once processing. If a message with an identical MessageDeduplicationId is published within the 5-minute deduplication interval, SQS accepts the API call returning a successful message ID, but will not deliver the duplicate message to consumers."
            },
            {
                "id": 6,
                "title": "AWS KMS Key Management & Envelope Encryption Mechanics",
                "difficulty": "Hard",
                "question_text": "When encrypting large sensitive data files (e.g., 5 GB database backups) using AWS KMS Customer Managed Keys (CMK), what is the exact mechanism of Envelope Encryption?",
                "options": [
                    "A) KMS encrypts the entire 5 GB file directly inside the KMS Hardware Security Module (HSM) using the KMS Master Key.",
                    "B) KMS generates a unique Data Key (plaintext and ciphertext); the application encrypts the 5 GB file locally using the plaintext Data Key, wipes the plaintext key from memory, and stores the encrypted Data Key alongside the encrypted file.",
                    "C) KMS streams the file chunks over TLS to AWS CloudHSM where asymmetric RSA 4096-bit keys perform direct disk block encryption.",
                    "D) KMS delegates encryption to AWS Secrets Manager which automatically encrypts files using AES-128 GCM."
                ],
                "correct_option": "B",
                "explanation": "AWS KMS limits direct API data encryption (kms:Encrypt) to 4 KB of data. For larger data files, AWS uses Envelope Encryption: KMS generates a Data Encryption Key (DEK) via GenerateDataKey. The plaintext DEK encrypts the data locally, and the encrypted DEK is stored alongside the encrypted payload."
            },
            {
                "id": 7,
                "title": "Amazon CloudFront & CloudFront Functions vs Lambda@Edge",
                "difficulty": "Hard",
                "question_text": "A media streaming service requires lightweight HTTP header manipulation, URL rewrites, and basic cookie-based geo-routing at CloudFront edge locations with sub-millisecond execution times and execution scale exceeding 100,000 requests per second. Which edge computing solution should be selected?",
                "options": [
                    "A) CloudFront Functions: Lightweight JavaScript execution running directly in CloudFront edge locations with high scale and sub-millisecond latency.",
                    "B) Lambda@Edge: Full Node.js/Python runtime running in regional edge caches for heavy computational tasks.",
                    "C) AWS Step Functions: Distributed state machine orchestration triggered directly on HTTP viewer requests.",
                    "D) Elastic Beanstalk: Auto-scaling EC2 instance fleet behind an Application Load Balancer at every AWS edge location."
                ],
                "correct_option": "A",
                "explanation": "CloudFront Functions are built specifically for high-volume, latency-sensitive request manipulation (header transforms, URL rewrites) running directly in 450+ CloudFront edge locations with sub-1ms execution times."
            },
            {
                "id": 8,
                "title": "AWS Auto Scaling Group Target Tracking & Predictive Scaling",
                "difficulty": "Hard",
                "question_text": "An online retail platform experiences sudden unpredictable flash traffic spikes. The architecture uses an Auto Scaling Group (ASG) behind an Application Load Balancer (ALB). Which scaling policy strategy ensures rapid capacity expansion while preventing aggressive thrashing (rapid scaling up and down)?",
                "options": [
                    "A) Target Tracking Scaling policy based on ALBRequestCountPerTarget combined with an appropriate scale-in cooldown period.",
                    "B) Simple Scaling policy based on CPU utilization with a 0-second cooldown period.",
                    "C) Scheduled Scaling policy that creates 100 EC2 instances permanently every 5 minutes.",
                    "D) Dynamic Step Scaling policy that terminates instances whenever memory usage falls below 95%."
                ],
                "correct_option": "A",
                "explanation": "Target Tracking scaling policies continuously adjust ASG capacity to maintain a target metric. Combining Target Tracking with cooldown periods prevents rapid oscillation (thrashing) by allowing metrics to stabilize before subsequent scaling actions occur."
            },
            {
                "id": 9,
                "title": "Amazon Aurora Global Database & Disaster Recovery Metrics",
                "difficulty": "Hard",
                "question_text": "A healthcare SaaS provider requires a database architecture supporting Recovery Time Objective (RTO) of < 1 minute and Recovery Point Objective (RPO) of < 1 second across two AWS regions. Which Amazon Aurora deployment configuration meets these stringent DR requirements?",
                "options": [
                    "A) Amazon Aurora Global Database using storage-level physical cross-region replication.",
                    "B) Single-region Aurora Cluster with automated daily snapshot exports to Amazon S3 in another region.",
                    "C) Aurora PostgreSQL Read Replica connected via AWS Database Migration Service (DMS) running CDC over public internet.",
                    "D) Standard Amazon RDS MySQL with asynchronous logical replication scripts running inside cron jobs on EC2 instances."
                ],
                "correct_option": "A",
                "explanation": "Amazon Aurora Global Database uses dedicated storage-level physical replication infrastructure built into the Aurora storage layer. Replication latency is typically under 1 second (RPO < 1s), and a secondary region can be promoted to master in under 1 minute (RTO < 1min)."
            },
            {
                "id": 10,
                "title": "Amazon API Gateway Custom Lambda Authorizer & Token Caching",
                "difficulty": "Hard",
                "question_text": "Microservices fronted by Amazon API Gateway use a custom Lambda Authorizer (TOKEN type) to validate JWT bearer tokens. To minimize Lambda invocation costs and authorization latency, how should the API Gateway Authorizer be configured?",
                "options": [
                    "A) Enable Authorizer Result Caching in API Gateway with a configured TTL (e.g. 300 seconds) keyed on the Authorization header.",
                    "B) Store tokens in an EC2 Redis cluster and invoke Lambda on every request to fetch Redis keys.",
                    "C) Configure API Gateway to store plain text JWT secrets inside CloudWatch Logs for fast lookups.",
                    "D) Disable API Gateway caching and increase Lambda memory to 10 GB to speed up verification."
                ],
                "correct_option": "A",
                "explanation": "API Gateway custom authorizers support built-in result caching. When caching is enabled, API Gateway caches the IAM policy returned by the Lambda authorizer for the authorization token key, bypassing Lambda on subsequent requests with the same token."
            },
            {
                "id": 11,
                "title": "AWS PrivateLink Endpoint Services & Multi-Tenant SaaS Connectivity",
                "difficulty": "Hard",
                "question_text": "A SaaS provider hosts a multi-tenant analytics service inside a VPC (<code>10.100.0.0/16</code>). Enterprise clients want to access this service securely from their own VPCs (<code>10.100.0.0/16</code> - overlapping IP space) over private AWS infrastructure without exposing traffic to the internet and without needing IP subnet renumbering. Which solution accomplishes this?",
                "options": [
                    "A) Configure an AWS PrivateLink Endpoint Service (VPC Endpoint Service) fronted by a Network Load Balancer (NLB) in the SaaS VPC, allowing clients to create Interface VPC Endpoints in their VPCs.",
                    "B) Establish bidirectional VPC Peering between SaaS VPC and Client VPCs with NAT Gateway routing tables.",
                    "C) Connect all Client VPCs to the SaaS VPC using AWS Site-to-Site IPsec VPN over public IP addresses.",
                    "D) Attach AWS Transit Gateway to all VPCs and configure static route override entries for duplicate IP addresses."
                ],
                "correct_option": "A",
                "explanation": "AWS PrivateLink uses unidirectional ENIs placed inside consumer VPCs to connect securely to Network Load Balancers in service provider VPCs. Encapsulation via PrivateLink eliminates IP routing conflicts even with overlapping IPv4 CIDR blocks."
            },
            {
                "id": 12,
                "title": "AWS Security Hub & Amazon GuardDuty Automated Incident Response",
                "difficulty": "Hard",
                "question_text": "A SecOps team needs to automatically isolate compromised EC2 instances within seconds of Amazon GuardDuty detecting command-and-control (C&C) malware communication findings. What serverless event-driven architecture enables automated instance isolation?",
                "options": [
                    "A) GuardDuty emits findings to Amazon EventBridge -> EventBridge triggers an AWS Lambda function -> Lambda updates the instance's Security Group to drop all inbound and outbound traffic.",
                    "B) GuardDuty updates Route 53 DNS records to point the compromised EC2 instance to localhost.",
                    "C) GuardDuty sends an email via Amazon SES to the system administrator who manually terminates the instance via AWS Console.",
                    "D) GuardDuty executes an inline Bash script directly on the EC2 instance via SSH root login."
                ],
                "correct_option": "A",
                "explanation": "GuardDuty integrates natively with EventBridge. High-severity findings trigger EventBridge rules that invoke an AWS Lambda function to update the instance's Security Group and isolate it immediately."
            },
            {
                "id": 13,
                "title": "AWS ECS Fargate Task Placement & AZ Resiliency",
                "difficulty": "Hard",
                "question_text": "A containerized microservice deployed on AWS ECS Fargate needs to maintain 100% availability during AWS Availability Zone outages. The service runs 12 container task replicas across 3 Availability Zones behind an Application Load Balancer. Which task placement strategy guarantees even distribution across AZs?",
                "options": [
                    "A) ECS Fargate automatically distributes tasks evenly across all configured subnets and Availability Zones using built-in task placement balance mechanisms.",
                    "B) Deploy all 12 tasks into a single public subnet in us-east-1a to avoid inter-AZ bandwidth latency.",
                    "C) Write a custom cron script on an EC2 instance that kills and restarts Fargate tasks every 10 minutes.",
                    "D) Use ECS binpack strategy based on memory utilization to force tasks onto a single host."
                ],
                "correct_option": "A",
                "explanation": "On AWS ECS Fargate, when a Service spans multiple subnets across Availability Zones, the ECS scheduler natively balances task placement across those AZs. If an AZ fails, ECS health checks launch replacements in healthy AZs automatically."
            },
            {
                "id": 14,
                "title": "AWS Direct Connect & IPsec VPN High Availability & BGP Metrics",
                "difficulty": "Hard",
                "question_text": "An organization establishes a 10 Gbps AWS Direct Connect (DX) connection with a Dedicated Virtual Interface (VIF) to connect on-premises networks to AWS VPCs. To ensure automatic failover in the event of a fiber cut on the Direct Connect line, they deploy an AWS Site-to-Site IPsec VPN as a backup link. How should BGP routing metrics be configured on-premises to prefer Direct Connect for primary traffic and failover to VPN?",
                "options": [
                    "A) Advertise identical prefixes over both DX and VPN, but use AS PATH Prepending (longer AS PATH) and lower BGP Local Preference on the VPN link for outbound/inbound traffic control.",
                    "B) Static route configuration pointing default 0.0.0.0/0 traffic exclusively to the VPN Gateway interface.",
                    "C) Configure DNS Round-Robin between Direct Connect IP and VPN Tunnel IP endpoints.",
                    "D) Direct Connect automatically disables VPN interfaces via AWS CloudTrail events without BGP configuration."
                ],
                "correct_option": "A",
                "explanation": "AWS BGP routing policies prefer Direct Connect over AWS VPN when prefixes are identical. To enforce consistent outbound traffic flow from on-premises to AWS and return traffic, engineers advertise prefixes with AS PATH prepending and lower BGP Local Preference on the backup VPN link."
            },
            {
                "id": 15,
                "title": "AWS Well-Architected Framework: Stateless Batch Workloads & Spot Fleets",
                "difficulty": "Hard",
                "question_text": "A data analytics company runs stateless batch processing jobs daily that can tolerate interruptions and resume from checkpoints. The current EC2 On-Demand infrastructure costs $50,000/month. Which EC2 provisioning strategy provides up to 90% cost savings while maintaining job completion resilience?",
                "options": [
                    "A) Deploy an EC2 Spot Fleet using a diversified allocation strategy across multiple instance types and Availability Zones, combined with EC2 Instance Rebalance Recommendations and Spot Rebalance Notifications.",
                    "B) Purchase 3-Year Standard Reserved Instances (RI) for a single instance type (c5.18xlarge) with All Upfront payment.",
                    "C) Migrate all workloads to EC2 Dedicated Hosts with On-Demand billing.",
                    "D) Use EC2 On-Demand Capacity Reservations in a single Availability Zone."
                ],
                "correct_option": "A",
                "explanation": "EC2 Spot Instances offer up to 90% discount compared to On-Demand prices. For stateless fault-tolerant batch workloads, using Spot Fleet with a diversified allocation strategy minimizes the impact of Spot interruptions."
            }
        ]
    },
    "problem_solving": {
        "name": "Problem Solving & DSA (Advanced / Hard)",
        "questions": [
            {
                "id": 1,
                "title": "PROBLEM_SOLVING Theory Concept #1",
                "difficulty": "Hard",
                "question_text": "Question 1: What is the core architectural principle regarding <code>Problem Solving & DSA (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for Problem Solving & DSA (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for Problem Solving & DSA (Advanced / Hard)."
            },
            {
                "id": 2,
                "title": "PROBLEM_SOLVING Theory Concept #2",
                "difficulty": "Hard",
                "question_text": "Question 2: What is the core architectural principle regarding <code>Problem Solving & DSA (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for Problem Solving & DSA (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for Problem Solving & DSA (Advanced / Hard)."
            },
            {
                "id": 3,
                "title": "PROBLEM_SOLVING Theory Concept #3",
                "difficulty": "Hard",
                "question_text": "Question 3: What is the core architectural principle regarding <code>Problem Solving & DSA (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for Problem Solving & DSA (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for Problem Solving & DSA (Advanced / Hard)."
            },
            {
                "id": 4,
                "title": "PROBLEM_SOLVING Theory Concept #4",
                "difficulty": "Hard",
                "question_text": "Question 4: What is the core architectural principle regarding <code>Problem Solving & DSA (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for Problem Solving & DSA (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for Problem Solving & DSA (Advanced / Hard)."
            },
            {
                "id": 5,
                "title": "PROBLEM_SOLVING Theory Concept #5",
                "difficulty": "Hard",
                "question_text": "Question 5: What is the core architectural principle regarding <code>Problem Solving & DSA (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for Problem Solving & DSA (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for Problem Solving & DSA (Advanced / Hard)."
            },
            {
                "id": 6,
                "title": "Between Two Sets",
                "difficulty": "Medium",
                "is_coding": True,
                "starter_code": "def getTotalX(a, b):\n    # Write your code here\n    pass",
                "question_text": "<strong>Between Two Sets</strong><br><br>There will be two arrays of integers. Determine all integers that satisfy the following two conditions:<br>1. The elements of the first array are all factors of the integer being considered.<br>2. The integer being considered is a factor of all elements of the second array.<br><br>These numbers are referred to as being <em>between the two arrays</em>. Determine how many such numbers exist.<br><br><strong>Example:</strong><br><code>a = [2, 6]</code><br><code>b = [24, 36]</code><br><br>There are two numbers between the arrays: <code>6</code> and <code>12</code>.<br>- <code>6 % 2 = 0</code>, <code>6 % 6 = 0</code>, <code>24 % 6 = 0</code>, and <code>36 % 6 = 0</code> for the first value.<br>- <code>12 % 2 = 0</code>, <code>12 % 6 = 0</code>, <code>24 % 12 = 0</code>, and <code>36 % 12 = 0</code> for the second value. Return <code>2</code>.<br><br><strong>Function Description:</strong><br>Complete the <code>getTotalX</code> function. It should return the number of integers that are between the sets.<br><br><strong>Parameters:</strong><br>- <code>int a[n]</code>: an array of integers<br>- <code>int b[m]</code>: an array of integers<br><br><strong>Returns:</strong><br>- <code>int</code>: the number of integers that are between the sets",
                "explanation": "To solve 'Between Two Sets':\n1. Find the Least Common Multiple (LCM) of all elements in array a.\n2. Find the Greatest Common Divisor (GCD) of all elements in array b.\n3. Count how many multiples of the LCM divide the GCD evenly.\n\nTime Complexity: O(n log(max(a)) + m log(max(b)))\nSpace Complexity: O(1) auxiliary space."
            },
            {
                "id": 7,
                "title": "Grading Students",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "def gradingStudents(grades):\n    # Write your code here\n    pass",
                "question_text": "<strong>Grading Students</strong><br><br>HackerLand University has the following grading policy:<br>- Every student receives a <code>grade</code> in the inclusive range from <code>0</code> to <code>100</code>.<br>- Any <code>grade</code> less than <code>40</code> is a failing grade.<br><br>Sam is a professor at the university and likes to round each student's <code>grade</code> according to these rules:<br>- If the difference between the <code>grade</code> and the next multiple of <code>5</code> is less than <code>3</code>, round <code>grade</code> up to the next multiple of <code>5</code>.<br>- If the value of <code>grade</code> is less than <code>38</code>, no rounding occurs as the result will still be a failing grade.<br><br><strong>Examples:</strong><br>- <code>grade = 84</code>: round to <code>85</code> (85 - 84 is less than 3)<br>- <code>grade = 29</code>: do not round (result is less than 38)<br>- <code>grade = 57</code>: do not round (60 - 57 is 3 or higher)<br><br>Given the initial value of <code>grade</code> for each of Sam's <code>n</code> students, write code to automate the rounding process.<br><br><strong>Function Description:</strong><br>Complete the <code>gradingStudents</code> function.<br><br><strong>Parameters:</strong><br>- <code>grades[n]</code>: an array of integers representing the grades before rounding<br><br><strong>Returns:</strong><br>- <code>int[n]</code>: an array of integers representing the grades after rounding",
                "explanation": "To solve 'Grading Students':\nFor each grade in grades:\n- If grade < 38, do not round (append grade).\n- Otherwise, compute next_multiple = ((grade // 5) + 1) * 5.\n- If next_multiple - grade < 3, append next_multiple; else append grade.\n\nTime Complexity: O(n)\nSpace Complexity: O(n) for the output array."
            },
            {
                "id": 8,
                "title": "Staircase",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "def staircase(n):\n    # Write your code here\n    pass",
                "question_text": "<strong>Staircase</strong><br><br>This is a staircase of size <code>n = 4</code>:<br><pre>   #\n  ##\n ###\n####</pre><br>Its base and height are both equal to <code>n</code>. It is drawn using <code>#</code> symbols and spaces. The last line is not preceded by any spaces.<br><br>Write a program that prints a staircase of size <code>n</code>.<br><br><strong>Function Description:</strong><br>Complete the <code>staircase</code> function.<br><br><strong>Parameters:</strong><br>- <code>int n</code>: an integer denoting the size of the staircase<br><br><strong>Print:</strong><br>Print a staircase as described above. No value should be returned.<br><em>Note: The last line is not preceded by any spaces. All lines are right-aligned.</em><br><br><strong>Constraints:</strong><br><code>0 < n <= 100</code>",
                "explanation": "To solve 'Staircase':\nFor each row i from 1 to n:\n- Print (n - i) spaces followed by i '#' characters.\n\nTime Complexity: O(n)\nSpace Complexity: O(1) auxiliary space."
            },
            {
                "id": 9,
                "title": "Diagonal Difference",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "def diagonalDifference(arr):\n    # Write your code here\n    pass",
                "question_text": "<strong>Diagonal Difference</strong><br><br>Given a square matrix, calculate the absolute difference between the sums of its diagonals.<br><br>For example, the square matrix <code>arr</code> is shown below:<br><pre>1 2 3\n4 5 6\n9 8 9</pre><br>- The left-to-right diagonal = <code>1 + 5 + 9 = 15</code>.<br>- The right-to-left diagonal = <code>3 + 5 + 9 = 17</code>.<br>Their absolute difference is <code>|15 - 17| = 2</code>.<br><br><strong>Function Description:</strong><br>Complete the <code>diagonalDifference</code> function.<br><br><strong>Parameters:</strong><br>- <code>arr[n][m]</code>: a 2-D array of integers<br><br><strong>Returns:</strong><br>- <code>int</code>: the absolute difference in sums along the diagonals<br><br><strong>Constraints:</strong><br><code>-100 <= arr[i][j] <= 100</code>",
                "explanation": "To solve 'Diagonal Difference':\nLoop i from 0 to n-1:\n- Add arr[i][i] to left_sum (primary diagonal).\n- Add arr[i][n-1-i] to right_sum (secondary diagonal).\nReturn abs(left_sum - right_sum).\n\nTime Complexity: O(n)\nSpace Complexity: O(1) auxiliary space."
            },
            {
                "id": 10,
                "title": "Time Conversion",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "def timeConversion(s):\n    # Write your code here\n    pass",
                "question_text": "<strong>Time Conversion</strong><br><br>Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.<br><br><em>Note:</em><br>- <code>12:00:00AM</code> on a 12-hour clock is <code>00:00:00</code> on a 24-hour clock.<br>- <code>12:00:00PM</code> on a 12-hour clock is <code>12:00:00</code> on a 24-hour clock.<br><br><strong>Example:</strong><br>- <code>s = '12:01:00PM'</code> → Return <code>'12:01:00'</code>.<br>- <code>s = '12:01:00AM'</code> → Return <code>'00:01:00'</code>.<br><br><strong>Function Description:</strong><br>Complete the <code>timeConversion</code> function.<br><br><strong>Parameters:</strong><br>- <code>string s</code>: a time in 12-hour format (e.g. <code>hh:mm:ssAM</code> or <code>hh:mm:ssPM</code>)<br><br><strong>Returns:</strong><br>- <code>string</code>: the time in 24-hour format (e.g. <code>hh:mm:ss</code>)",
                "explanation": "To solve 'Time Conversion':\n- Extract period (last 2 chars: 'AM' or 'PM') and integer hour (first 2 chars).\n- If period is 'AM' and hour == 12, hour = 0.\n- If period is 'PM' and hour != 12, hour += 12.\n- Return formatted string f'{hour:02d}{s[2:8]}'.\n\nTime Complexity: O(1)\nSpace Complexity: O(1)"
            },
            {
                "id": 11,
                "title": "Birthday Cake Candles",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "def birthdayCakeCandles(candles):\n    # Write your code here\n    pass",
                "question_text": "<strong>Birthday Cake Candles</strong><br><br>You are in charge of the cake for a child's birthday. It will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Your task is to count how many candles are the tallest.<br><br><strong>Example:</strong><br><code>candles = [4, 4, 1, 3]</code><br><br>The tallest candles are <code>4</code> units high. There are <code>2</code> candles with this height, so the function should return <code>2</code>.<br><br><strong>Function Description:</strong><br>Complete the <code>birthdayCakeCandles</code> function.<br><br><strong>Parameters:</strong><br>- <code>int candles[n]</code>: the candle heights<br><br><strong>Returns:</strong><br>- <code>int</code>: the number of candles that are tallest<br><br><strong>Constraints:</strong><br>- <code>1 <= n <= 10^5</code><br>- <code>1 <= candles[i] <= 10^7</code>",
                "explanation": "To solve 'Birthday Cake Candles':\nFind max_height = max(candles).\nReturn candles.count(max_height).\n\nTime Complexity: O(n)\nSpace Complexity: O(1) auxiliary space."
            },
            {
                "id": 12,
                "title": "Apple and Orange",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "def countApplesAndOranges(s, t, a, b, apples, oranges):\n    # Write your code here\n    pass",
                "question_text": "<strong>Apple and Orange</strong><br><br>Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Determine the number of apples and oranges that land on Sam's house.<br><br><strong>Position Details:</strong><br>- Sam's house is between start point <code>s</code> and end point <code>t</code> inclusive.<br>- The apple tree is at point <code>a</code>, and the orange tree is at point <code>b</code>.<br>- When a fruit falls, it lands <code>d</code> units distance from its tree (positive = right, negative = left).<br><br><strong>Example:</strong><br><code>s = 7</code>, <code>t = 10</code><br>Apple tree <code>a = 4</code>, Orange tree <code>b = 12</code><br><code>apples = [2, 3, -4]</code> → landing positions: <code>[6, 7, 0]</code> (1 lands in range [7, 10])<br><code>oranges = [3, -2, -4]</code> → landing positions: <code>[15, 10, 8]</code> (2 land in range [7, 10])<br><br><strong>Function Description:</strong><br>Complete the <code>countApplesAndOranges</code> function.<br><br><strong>Parameters:</strong><br>- <code>int s</code>: house start point<br>- <code>int t</code>: house end point<br>- <code>int a</code>: Apple tree position<br>- <code>int b</code>: Orange tree position<br>- <code>int apples[m]</code>: distances each apple falls from tree<br>- <code>int oranges[n]</code>: distances each orange falls from tree<br><br><strong>Print:</strong><br>Print two integers on separate lines:<br>1. Number of apples that fall on Sam's house.<br>2. Number of oranges that fall on Sam's house.",
                "explanation": "To solve 'Apple and Orange':\n- Count apples where s <= a + d <= t.\n- Count oranges where s <= b + d <= t.\n- Print both counts on separate lines.\n\nTime Complexity: O(m + n)\nSpace Complexity: O(1) auxiliary space."
            },
            {
                "id": 13,
                "title": "Breaking the Records",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "def breakingRecords(scores):\n    # Write your code here\n    pass",
                "question_text": "<strong>Breaking the Records</strong><br><br>Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season.<br><br><strong>Example:</strong><br><code>scores = [12, 24, 10, 24]</code><br><br>Scores tabulated as follows:<br><ul><li>Game 0: Score 12 | Min 12, Max 12 | Count Min 0, Max 0</li><li>Game 1: Score 24 | Min 12, Max 24 | Count Min 0, Max 1</li><li>Game 2: Score 10 | Min 10, Max 24 | Count Min 1, Max 1</li><li>Game 3: Score 24 | Min 10, Max 24 | Count Min 1, Max 1</li></ul><br>Return <code>[1, 1]</code>.<br><br><strong>Function Description:</strong><br>Complete the <code>breakingRecords</code> function.<br><br><strong>Parameters:</strong><br>- <code>int scores[n]</code>: points scored per game<br><br><strong>Returns:</strong><br>- <code>int[2]</code>: An array with the numbers of times she broke her records. Index 0 is for breaking most points records, and index 1 is for breaking least points records.",
                "explanation": "To solve 'Breaking the Records':\nInitialize min_score = max_score = scores[0], and min_count = max_count = 0.\nLoop score in scores[1:]:\n- If score > max_score: max_score = score; max_count += 1\n- If score < min_score: min_score = score; min_count += 1\nReturn [max_count, min_count].\n\nTime Complexity: O(n)\nSpace Complexity: O(1) auxiliary space."
            },
            {
                "id": 14,
                "title": "Divisible Sum Pairs",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "def divisibleSumPairs(n, k, ar):\n    # Write your code here\n    pass",
                "question_text": "<strong>Divisible Sum Pairs</strong><br><br>Given an array of integers and a positive integer <code>k</code>, determine the number of <code>(i, j)</code> pairs where <code>i < j</code> and <code>ar[i] + ar[j]</code> is divisible by <code>k</code>.<br><br><strong>Example:</strong><br><code>ar = [1, 2, 3, 4, 5, 6]</code><br><code>k = 5</code><br><br>Three pairs meet the criteria: <code>[1, 4]</code> (sum = 5), <code>[2, 3]</code> (sum = 5), and <code>[4, 6]</code> (sum = 10). Return <code>3</code>.<br><br><strong>Function Description:</strong><br>Complete the <code>divisibleSumPairs</code> function.<br><br><strong>Parameters:</strong><br>- <code>int n</code>: the length of array <code>ar</code><br>- <code>int k</code>: the integer divisor<br>- <code>int ar[n]</code>: an array of integers<br><br><strong>Returns:</strong><br>- <code>int</code>: the number of pairs<br><br><strong>Constraints:</strong><br>- <code>2 <= n <= 100</code><br>- <code>1 <= k <= 100</code><br>- <code>1 <= ar[i] <= 100</code>",
                "explanation": "To solve 'Divisible Sum Pairs':\nLoop i from 0 to n-1 and j from i+1 to n-1:\n- If (ar[i] + ar[j]) % k == 0: count += 1\nReturn count.\nAlternatively, use remainder frequency array for O(n) solution.\n\nTime Complexity: O(n^2) or O(n + k)\nSpace Complexity: O(1) or O(k)"
            },
            {
                "id": 15,
                "title": "Forming a Magic Square",
                "difficulty": "Medium",
                "is_coding": True,
                "starter_code": "def formingMagicSquare(s):\n    # Write your code here\n    pass",
                "question_text": "<strong>Forming a Magic Square</strong><br><br>We define a magic square to be an <code>n x n</code> matrix of distinct positive integers from <code>1</code> to <code>n^2</code> where the sum of any row, column, or diagonal of length <code>n</code> is always equal to the same number: the magic constant.<br><br>You will be given a <code>3 x 3</code> matrix <code>s</code> of integers in the inclusive range <code>[1, 9]</code>. We can convert any digit <code>a</code> to any other digit <code>b</code> in the range <code>[1, 9]</code> at cost of <code>|a - b|</code>. Given <code>s</code>, convert it into a magic square at minimal cost.<br><br><strong>Example:</strong><br><pre>s = [[5, 3, 4],\n     [1, 5, 8],\n     [6, 4, 2]]</pre><br>We can convert it to the following magic square:<br><pre>[[8, 3, 4],\n [1, 5, 9],\n [6, 7, 2]]</pre><br>This took three replacements at a cost of <code>|5 - 8| + |8 - 9| + |4 - 7| = 3 + 1 + 3 = 7</code>. Return <code>7</code>.<br><br><strong>Function Description:</strong><br>Complete the <code>formingMagicSquare</code> function.<br><br><strong>Parameters:</strong><br>- <code>int s[3][3]</code>: a 3 x 3 array of integers<br><br><strong>Returns:</strong><br>- <code>int</code>: the minimal total cost of converting matrix <code>s</code> into a magic square",
                "explanation": "To solve 'Forming a Magic Square':\nThere are only 8 possible 3x3 magic squares using numbers 1..9 (with 5 in center, constant sum 15).\nPredefine all 8 magic square matrices.\nFor each pre-calculated magic square M:\n  Compute cost = sum(|s[i][j] - M[i][j]| for all i, j in 0..2)\nReturn min(cost) over all 8 magic squares.\n\nTime Complexity: O(1) (8 * 9 comparisons)\nSpace Complexity: O(1)"
            }
        ]
    },
    "c": {
        "name": "C Programming (Advanced / Hard)",
        "questions": [
            {
                "id": 1,
                "title": "C Theory Concept #1",
                "difficulty": "Hard",
                "question_text": "Question 1: What is the core architectural principle regarding <code>C Programming (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for C Programming (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for C Programming (Advanced / Hard)."
            },
            {
                "id": 2,
                "title": "C Theory Concept #2",
                "difficulty": "Hard",
                "question_text": "Question 2: What is the core architectural principle regarding <code>C Programming (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for C Programming (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for C Programming (Advanced / Hard)."
            },
            {
                "id": 3,
                "title": "C Theory Concept #3",
                "difficulty": "Hard",
                "question_text": "Question 3: What is the core architectural principle regarding <code>C Programming (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for C Programming (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for C Programming (Advanced / Hard)."
            },
            {
                "id": 4,
                "title": "C Theory Concept #4",
                "difficulty": "Hard",
                "question_text": "Question 4: What is the core architectural principle regarding <code>C Programming (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for C Programming (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for C Programming (Advanced / Hard)."
            },
            {
                "id": 5,
                "title": "C Theory Concept #5",
                "difficulty": "Hard",
                "question_text": "Question 5: What is the core architectural principle regarding <code>C Programming (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for C Programming (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for C Programming (Advanced / Hard)."
            },
            {
                "id": 6,
                "title": "Functions in C",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "#include <stdio.h>\n/*\nAdd `int max_of_four(int a, int b, int c, int d)` here.\n*/\n\nint main() {\n    int a, b, c, d;\n    scanf(\"%d %d %d %d\", &a, &b, &c, &d);\n    int ans = max_of_four(a, b, c, d);\n    printf(\"%d\", ans);\n    return 0;\n}",
                "question_text": "<strong>Functions in C</strong><br><br>In this challenge, you will learn simple usage of functions in C. Functions are a bunch of statements grouped together. A function is provided with zero or more arguments, and it executes the statements on it. Based on the return type, it either returns nothing (void) or something.<br><br><strong>Task:</strong><br>Write a function <code>int max_of_four(int a, int b, int c, int d)</code> which reads four arguments and returns the greatest of them.<br><br><strong>Example Input:</strong><br><pre>3\n4\n6\n5</pre>",
                "explanation": "To solve 'Functions in C':\nCompare all four integers using conditional logic:\nint max_of_four(int a, int b, int c, int d) {\n    int max = a;\n    if (b > max) max = b;\n    if (c > max) max = c;\n    if (d > max) max = d;\n    return max;\n}\n\nTime Complexity: O(1)\nSpace Complexity: O(1)"
            },
            {
                "id": 7,
                "title": "Conditional Statements in C",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\nint main() {\n    int n;\n    scanf(\"%d\", &n);\n    \n    // Write Your Code Here\n    \n    return 0;\n}",
                "question_text": "<strong>Conditional Statements in C</strong><br><br><code>if</code> and <code>else</code> are two of the most frequently used conditionals in C/C++, enabling execution of conditional statements.<br><br><strong>Task:</strong><br>Given a positive integer <code>n</code>:<br>- If <code>1 <= n <= 9</code>, print the lowercase English word corresponding to the number (e.g., <code>\"one\"</code> for 1, <code>\"two\"</code> for 2, etc.).<br>- If <code>n > 9</code>, print <code>\"Greater than 9\"</code>.<br><br><strong>Example Input:</strong><br><pre>5</pre>",
                "explanation": "To solve 'Conditional Statements in C':\nUse a string array or if/else chain:\nconst char* words[] = {\"one\", \"two\", \"three\", \"four\", \"five\", \"six\", \"seven\", \"eight\", \"nine\"};\nif (n >= 1 && n <= 9) {\n    printf(\"%s\\n\", words[n-1]);\n} else if (n > 9) {\n    printf(\"Greater than 9\\n\");\n}\n\nTime Complexity: O(1)\nSpace Complexity: O(1)"
            },
            {
                "id": 8,
                "title": "For Loop in C",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "#include <stdio.h>\n#include <string.h>\n#include <math.h>\n#include <stdlib.h>\n\nint main() \n{\n    int a, b;\n    scanf(\"%d\\n%d\", &a, &b);\n    // Complete the code.\n\n    return 0;\n}",
                "question_text": "<strong>For Loop in C</strong><br><br>In this challenge, you will learn the usage of the <code>for</code> loop in C.<br><br><strong>Task:</strong><br>For each integer <code>n</code> in the interval <code>[a, b]</code> (given as input):<br>- If <code>1 <= n <= 9</code>, print the English representation of it in lowercase (e.g. <code>\"one\"</code> for 1, <code>\"two\"</code> for 2, etc.).<br>- Else if <code>n > 9</code> and it is an even number, print <code>\"even\"</code>.<br>- Else if <code>n > 9</code> and it is an odd number, print <code>\"odd\"</code>.<br><br><strong>Example Input:</strong><br><pre>8\n11</pre>",
                "explanation": "To solve 'For Loop in C':\nLoop n from a to b:\nconst char* words[] = {\"one\", \"two\", \"three\", \"four\", \"five\", \"six\", \"seven\", \"eight\", \"nine\"};\nfor (int n = a; n <= b; n++) {\n    if (n >= 1 && n <= 9) printf(\"%s\\n\", words[n-1]);\n    else if (n % 2 == 0) printf(\"even\\n\");\n    else printf(\"odd\\n\");\n}\n\nTime Complexity: O(b - a + 1)\nSpace Complexity: O(1)"
            },
            {
                "id": 9,
                "title": "Printing Pattern Using Loops",
                "difficulty": "Medium",
                "is_coding": True,
                "starter_code": "#include <stdio.h>\n#include <string.h>\n#include <math.h>\n#include <stdlib.h>\n\nint main() \n{\n    int n;\n    scanf(\"%d\", &n);\n    // Complete the code to print the pattern.\n    return 0;\n}",
                "question_text": "<strong>Printing Pattern Using Loops</strong><br><br>Print a pattern of numbers from <code>1</code> to <code>n</code> as shown below. Each of the numbers is separated by a single space.<br><br><strong>Example for n = 4:</strong><br><pre>4 4 4 4 4 4 4\n4 3 3 3 3 3 4\n4 3 2 2 2 3 4\n4 3 2 1 2 3 4\n4 3 2 2 2 3 4\n4 3 3 3 3 3 4\n4 4 4 4 4 4 4</pre><br><strong>Input Format:</strong><br>The input will contain a single integer <code>n</code>.<br><br><strong>Constraints:</strong><br><code>1 <= n <= 1000</code>",
                "explanation": "To solve 'Printing Pattern Using Loops':\nThe total grid size is (2*n - 1) x (2*n - 1).\nFor any cell (i, j) in row 0..2n-2 and col 0..2n-2:\nFind distance to nearest edge: min(i, j, 2n-2-i, 2n-2-j).\nThe value at (i, j) is: n - min_distance.\nPrint values separated by space.\n\nTime Complexity: O(n^2)\nSpace Complexity: O(1) auxiliary space."
            },
            {
                "id": 10,
                "title": "Array Reversal",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\nint main()\n{\n    int num, *arr, i;\n    scanf(\"%d\", &num);\n    arr = (int*) malloc(num * sizeof(int));\n    for(i = 0; i < num; i++) {\n        scanf(\"%d\", arr + i);\n    }\n\n    /* Write the logic to reverse the array. */\n\n    for(i = 0; i < num; i++)\n        printf(\"%d \", *(arr + i));\n    return 0;\n}",
                "question_text": "<strong>Array Reversal</strong><br><br>Given an array of size <code>n</code>, reverse it in-place.<br><br><strong>Example:</strong><br>If <code>arr = [1, 2, 3, 4, 5]</code>, after reversing it, the array should be <code>arr = [5, 4, 3, 2, 1]</code>.<br><br><strong>Sample Input:</strong><br><pre>6\n16 13 7 2 1 12</pre><br><strong>Sample Output:</strong><br><pre>12 1 2 7 13 16</pre><br><strong>Constraints:</strong><br>- <code>1 <= n <= 1000</code><br>- <code>1 <= arr[i] <= 1000</code>",
                "explanation": "To solve 'Array Reversal':\nUse two pointers (start = 0, end = num - 1) and swap elements:\nfor (i = 0; i < num / 2; i++) {\n    int temp = arr[i];\n    arr[i] = arr[num - 1 - i];\n    arr[num - 1 - i] = temp;\n}\n\nTime Complexity: O(n)\nSpace Complexity: O(1) in-place auxiliary space."
            },
            {
                "id": 11,
                "title": "Digit Frequency",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "#include <stdio.h>\n#include <string.h>\n#include <math.h>\n#include <stdlib.h>\n\nint main() {\n    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    \n    return 0;\n}",
                "question_text": "<strong>Digit Frequency</strong><br><br>Given a string, <code>s</code>, consisting of alphabets and digits, find the frequency of each digit from <code>0</code> to <code>9</code> in the given string.<br><br><strong>Sample Input:</strong><br><pre>a11472o5t6</pre><br><strong>Sample Output:</strong><br><pre>0 2 1 0 1 1 1 1 0 0</pre><br><strong>Explanation:</strong><br>- 1 occurs 2 times.<br>- 2, 4, 5, 6, 7 occur 1 time each.<br>- 0, 3, 8, 9 do not occur.<br><br><strong>Constraints:</strong><br>- <code>1 <= len(s) <= 1000</code>",
                "explanation": "To solve 'Digit Frequency':\nMaintain a count array int freq[10] = {0}.\nRead input string s. Iterate through each character c in s:\n- If c >= '0' && c <= '9': freq[c - '0']++\nPrint freq[0] through freq[9] separated by spaces.\n\nTime Complexity: O(len(s))\nSpace Complexity: O(1) auxiliary space."
            },
            {
                "id": 12,
                "title": "Permutations of Strings",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint next_permutation(int n, char **s)\n{\n    /**\n    * Complete this method\n    * Return 0 when there is no next permutation and 1 otherwise\n    * Modify array s to its next permutation\n    */\n}\n\nint main()\n{\n    int n;\n    scanf(\"%d\", &n);\n    char **s = malloc(n * sizeof(char*));\n    for (int i = 0; i < n; i++) {\n        s[i] = malloc(11 * sizeof(char));\n        scanf(\"%s\", s[i]);\n    }\n    do {\n        for (int i = 0; i < n; i++)\n            printf(\"%s%c\", s[i], i == n - 1 ? '\\n' : ' ');\n    } while (next_permutation(n, s));\n    for (int i = 0; i < n; i++)\n        free(s[i]);\n    free(s);\n    return 0;\n}",
                "question_text": "<strong>Permutations of Strings</strong><br><br>Given an array of strings sorted in lexicographical order, print all of its permutations in strict lexicographical order. If two permutations look the same, only print one of them.<br><br>Complete the function <code>next_permutation</code> which generates the permutations in the described order.<br><br><strong>Example:</strong><br><code>s = [ab, bc, cd]</code><br>The six permutations in correct order are:<br><pre>ab bc cd\nab cd bc\nbc ab cd\nbc cd ab\ncd ab bc\ncd bc ab</pre><br><strong>Function Description:</strong><br>Implement <code>int next_permutation(int n, char **s)</code>:<br>- Modify array <code>s</code> to its next lexicographical permutation in-place.<br>- Return <code>1</code> if a next permutation exists, or <code>0</code> if <code>s</code> is in reversing / last permutation order.",
                "explanation": "To solve 'Permutations of Strings':\n1. Find largest index i such that s[i] < s[i+1]. If no such index exists, return 0.\n2. Find largest index j > i such that s[i] < s[j].\n3. Swap s[i] and s[j].\n4. Reverse elements from index i+1 to n-1.\n5. Return 1.\n\nTime Complexity: O(n) per call\nSpace Complexity: O(1) in-place auxiliary space."
            },
            {
                "id": 13,
                "title": "Students Marks Sum",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "#include <stdio.h>\n#include <string.h>\n#include <math.h>\n#include <stdlib.h>\n\nint marks_summation(int* marks, int number_of_students, char gender) {\n    // Write your code here.\n}\n\nint main() {\n    int number_of_students;\n    char gender;\n    int sum;\n\n    scanf(\"%d\", &number_of_students);\n    int *marks = (int *) malloc(number_of_students * sizeof(int));\n\n    for (int student = 0; student < number_of_students; student++) {\n        scanf(\"%d\", (marks + student));\n    }\n    \n    scanf(\" %c\", &gender);\n    sum = marks_summation(marks, number_of_students, gender);\n    printf(\"%d\\n\", sum);\n    free(marks);\n \n    return 0;\n}",
                "question_text": "<strong>Students Marks Sum</strong><br><br>You are given an array of integers, <code>marks</code>, denoting the marks scored by students in a class.<br>- Alternating elements <code>marks[0], marks[2], marks[4]...</code> denote marks of boys.<br>- Alternating elements <code>marks[1], marks[3], marks[5]...</code> denote marks of girls.<br><br><strong>Example:</strong><br><code>marks = [3, 2, 5]</code><br>- Boys marks: <code>marks[0] + marks[2] = 3 + 5 = 8</code><br>- Girls marks: <code>marks[1] = 2</code><br><br><strong>Function Description:</strong><br>Complete <code>int marks_summation(int* marks, int number_of_students, char gender)</code>:<br>- <code>gender = 'b'</code>: sum marks at even indices (0, 2, 4...)<br>- <code>gender = 'g'</code>: sum marks at odd indices (1, 3, 5...)<br><br>Return the total sum for the given gender.",
                "explanation": "To solve 'Students Marks Sum':\nint sum = 0;\nint start = (gender == 'b') ? 0 : 1;\nfor (int i = start; i < number_of_students; i += 2) {\n    sum += marks[i];\n}\nreturn sum;\n\nTime Complexity: O(n)\nSpace Complexity: O(1) auxiliary space."
            },
            {
                "id": 14,
                "title": "Printing Tokens",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "#include <stdio.h>\n#include <string.h>\n#include <math.h>\n#include <stdlib.h>\n\nint main() {\n    char *s;\n    s = malloc(1024 * sizeof(char));\n    scanf(\"%[^\\n]\", s);\n    s = realloc(s, strlen(s) + 1);\n    // Write your logic to print the tokens of the sentence here.\n    return 0;\n}",
                "question_text": "<strong>Printing Tokens</strong><br><br>Given a sentence, <code>s</code>, print each word of the sentence in a new line.<br><br><strong>Sample Input:</strong><br><pre>This is C</pre><br><strong>Sample Output:</strong><br><pre>This\nis\nC</pre><br><strong>Explanation:</strong><br>In the given string, there are three words [\"This\", \"is\", \"C\"]. We have to print each of these words on a new line.<br><br><strong>Constraints:</strong><br>- <code>1 <= len(s) <= 1000</code>",
                "explanation": "To solve 'Printing Tokens':\nIterate through string s char by char:\n- If s[i] == ' ', print '\\n'\n- Else, print s[i]\nAlternatively, use strtok(s, \" \") to split tokens.\n\nTime Complexity: O(len(s))\nSpace Complexity: O(1) auxiliary space."
            },
            {
                "id": 15,
                "title": "Calculate the Nth term",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "#include <stdio.h>\n#include <string.h>\n#include <math.h>\n#include <stdlib.h>\n\nint find_nth_term(int n, int a, int b, int c) {\n    // Write your code here.\n}\n\nint main() {\n    int n, a, b, c;\n    scanf(\"%d %d %d %d\", &n, &a, &b, &c);\n    int ans = find_nth_term(n, a, b, c);\n    printf(\"%d\", ans);\n    return 0;\n}",
                "question_text": "<strong>Calculate the Nth term</strong><br><br>This challenge will help you learn the concept of recursion.<br><br>There is a series, <code>S</code>, where the next term is the sum of the previous three terms. Given the first three terms of the series, <code>a</code>, <code>b</code>, and <code>c</code> respectively, output the <code>n</code>-th term of the series using recursion.<br><br><strong>Recursive Formula:</strong><br>- <code>S(1) = a</code><br>- <code>S(2) = b</code><br>- <code>S(3) = c</code><br>- <code>S(n) = S(n-1) + S(n-2) + S(n-3)</code> for <code>n > 3</code><br><br><strong>Function Description:</strong><br>Complete the function <code>int find_nth_term(int n, int a, int b, int c)</code>.",
                "explanation": "To solve 'Calculate the Nth term':\nImplement recursion base cases:\nif (n == 1) return a;\nif (n == 2) return b;\nif (n == 3) return c;\nreturn find_nth_term(n - 1, a, b, c) + find_nth_term(n - 2, a, b, c) + find_nth_term(n - 3, a, b, c);\n\nTime Complexity: O(3^n) naive recursion or O(n) iterative DP.\nSpace Complexity: O(n) recursion stack height."
            }
        ]
    },
    "cpp": {
        "name": "C++ & STL (Advanced / Hard)",
        "questions": [
            {
                "id": 1,
                "title": "CPP Theory Concept #1",
                "difficulty": "Hard",
                "question_text": "Question 1: What is the core architectural principle regarding <code>C++ & STL (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for C++ & STL (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for C++ & STL (Advanced / Hard)."
            },
            {
                "id": 2,
                "title": "CPP Theory Concept #2",
                "difficulty": "Hard",
                "question_text": "Question 2: What is the core architectural principle regarding <code>C++ & STL (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for C++ & STL (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for C++ & STL (Advanced / Hard)."
            },
            {
                "id": 3,
                "title": "CPP Theory Concept #3",
                "difficulty": "Hard",
                "question_text": "Question 3: What is the core architectural principle regarding <code>C++ & STL (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for C++ & STL (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for C++ & STL (Advanced / Hard)."
            },
            {
                "id": 4,
                "title": "CPP Theory Concept #4",
                "difficulty": "Hard",
                "question_text": "Question 4: What is the core architectural principle regarding <code>C++ & STL (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for C++ & STL (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for C++ & STL (Advanced / Hard)."
            },
            {
                "id": 5,
                "title": "CPP Theory Concept #5",
                "difficulty": "Hard",
                "question_text": "Question 5: What is the core architectural principle regarding <code>C++ & STL (Advanced / Hard)</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for C++ & STL (Advanced / Hard)",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for C++ & STL (Advanced / Hard)."
            },
            {
                "id": 6,
                "title": "Input and Output",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "#include <cmath>\n#include <cstdio>\n#include <vector>\n#include <iostream>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    /* Enter your code here. Read input from STDIN. Print output to STDOUT */\n    return 0;\n}",
                "question_text": "<strong>Input and Output</strong><br><br>In this challenge, we practice reading input from <code>stdin</code> and printing output to <code>stdout</code>.<br><br>In C++, you can read a single whitespace-separated token of input using <code>cin</code>, and print output to <code>stdout</code> using <code>cout</code>.<br><br><strong>Task:</strong><br>Read 3 numbers from <code>stdin</code> and print their sum to <code>stdout</code>.<br><br><strong>Example Input:</strong><br><pre>1 2 7</pre><br><strong>Example Output:</strong><br><pre>10</pre>",
                "explanation": "To solve 'Input and Output':\nDeclare three integers a, b, c.\nRead them using cin >> a >> b >> c;\nPrint their sum using cout << a + b + c << endl;\n\nTime Complexity: O(1)\nSpace Complexity: O(1)"
            },
            {
                "id": 7,
                "title": "Conditional Statements",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "#include <bits/stdc++.h>\nusing namespace std;\n\nint main()\n{\n    int n;\n    cin >> n;\n\n    // Write your code here\n\n    return 0;\n}",
                "question_text": "<strong>Conditional Statements</strong><br><br><code>if</code> and <code>else</code> are two of the most frequently used conditionals in C/C++, enabling execution of conditional statements.<br><br><strong>Task:</strong><br>Given a positive integer <code>n</code>:<br>- If <code>1 <= n <= 9</code>, print the lowercase English word corresponding to the number (e.g., <code>\"one\"</code> for 1, <code>\"two\"</code> for 2, etc.).<br>- If <code>n > 9</code>, print <code>\"Greater than 9\"</code>.<br><br><strong>Example Input:</strong><br><pre>5</pre><br><strong>Example Output:</strong><br><pre>five</pre>",
                "explanation": "To solve 'Conditional Statements':\nUse a vector/array of strings:\nvector<string> words = {\"one\", \"two\", \"three\", \"four\", \"five\", \"six\", \"seven\", \"eight\", \"nine\"};\nif (n >= 1 && n <= 9) {\n    cout << words[n-1] << endl;\n} else if (n > 9) {\n    cout << \"Greater than 9\" << endl;\n}\n\nTime Complexity: O(1)\nSpace Complexity: O(1)"
            },
            {
                "id": 8,
                "title": "For Loop",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "#include <iostream>\n#include <cstdio>\nusing namespace std;\n\nint main() {\n    // Complete the code.\n    return 0;\n}",
                "question_text": "<strong>For Loop</strong><br><br>In this challenge, you will use a for loop to increment a variable through a range.<br><br><strong>Task:</strong><br>For each integer <code>n</code> in the inclusive interval <code>[a, b]</code> (given as input):<br>- If <code>1 <= n <= 9</code>, print the English representation of it in lowercase (e.g. <code>\"one\"</code> for 1, <code>\"two\"</code> for 2, etc.).<br>- Else if <code>n > 9</code> and it is an even number, print <code>\"even\"</code>.<br>- Else if <code>n > 9</code> and it is an odd number, print <code>\"odd\"</code>.<br><br><strong>Example Input:</strong><br><pre>8\n11</pre><br><strong>Example Output:</strong><br><pre>eight\nnine\neven\nodd</pre>",
                "explanation": "To solve 'For Loop':\nLoop n from a to b:\nvector<string> words = {\"one\", \"two\", \"three\", \"four\", \"five\", \"six\", \"seven\", \"eight\", \"nine\"};\nfor (int n = a; n <= b; n++) {\n    if (n >= 1 && n <= 9) cout << words[n-1] << endl;\n    else if (n % 2 == 0) cout << \"even\" << endl;\n    else cout << \"odd\" << endl;\n}\n\nTime Complexity: O(b - a + 1)\nSpace Complexity: O(1)"
            },
            {
                "id": 9,
                "title": "Functions",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "#include <iostream>\n#include <cstdio>\nusing namespace std;\n\n/*\nAdd `int max_of_four(int a, int b, int c, int d)` here.\n*/\n\nint main() {\n    int a, b, c, d;\n    scanf(\"%d %d %d %d\", &a, &b, &c, &d);\n    int ans = max_of_four(a, b, c, d);\n    printf(\"%d\", ans);\n    \n    return 0;\n}",
                "question_text": "<strong>Functions</strong><br><br>Functions are a bunch of statements glued together. A function is provided with zero or more arguments, and it executes the statements on it.<br><br><strong>Task:</strong><br>Write a function <code>int max_of_four(int a, int b, int c, int d)</code> which returns the maximum of the four arguments it receives.<br><br><strong>Example Input:</strong><br><pre>3\n4\n6\n5</pre><br><strong>Example Output:</strong><br><pre>6</pre>",
                "explanation": "To solve 'Functions':\nint max_of_four(int a, int b, int c, int d) {\n    return max(max(a, b), max(c, d));\n}\n\nTime Complexity: O(1)\nSpace Complexity: O(1)"
            },
            {
                "id": 10,
                "title": "Attribute Parser",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "#include <cmath>\n#include <cstdio>\n#include <vector>\n#include <iostream>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    /* Enter your code here. Read input from STDIN. Print output to STDOUT */\n    return 0;\n}",
                "question_text": "<strong>Attribute Parser</strong><br><br>This challenge works with a custom-designed markup language HRML. In HRML, each element consists of a starting and ending tag, and there are attributes associated with each tag. Only starting tags can have attributes. We can call an attribute by referencing the tag, followed by a tilde <code>~</code> and the name of the attribute. Tags may also be nested.<br><br><strong>Opening Tag Format:</strong><br><code>&lt;tag-name attribute1-name = \"value1\" attribute2-name = \"value2\" ...&gt;</code><br><br><strong>Closing Tag Format:</strong><br><code>&lt;/tag-name&gt;</code><br><br><strong>Attribute References:</strong><br><code>tag1~value</code><br><code>tag1.tag2~name</code><br><br>Given HRML source code consisting of <code>N</code> lines, answer <code>Q</code> queries. For each query, print the value of the attribute specified. Print <code>\"Not Found!\"</code> if the attribute does not exist.",
                "explanation": "To solve 'Attribute Parser':\nUse a map<string, string> hrml_map to store full hierarchical tag path attribute key-values.\nMaintain a vector<string> tag_stack for nested tag hierarchy.\nWhen reading an opening tag, append to tag_stack, construct current tag path, parse attributes and store path~attr_name -> attr_value in map.\nWhen reading a closing tag, pop from tag_stack.\nFor each query, look up in map. If found, print value, else print \"Not Found!\".\n\nTime Complexity: O(N * L + Q)\nSpace Complexity: O(N * L) for storing parsed attributes."
            },
            {
                "id": 11,
                "title": "Strings",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    // Complete the program\n  \n    return 0;\n}",
                "question_text": "<strong>Strings</strong><br><br>C++ provides a nice alternative data type to manipulate strings, called <code>string</code>.<br><br><strong>Task:</strong><br>Given two strings <code>a</code> and <code>b</code> separated by a newline:<br>1. Print two space-separated integers representing length of <code>a</code> and <code>b</code>.<br>2. Print string <code>c = a + b</code>.<br>3. Print <code>a'</code> and <code>b'</code> separated by space, where <code>a'</code> and <code>b'</code> are same as <code>a</code> and <code>b</code> except their first characters are swapped.<br><br><strong>Example Input:</strong><br><pre>abcd\nef</pre><br><strong>Example Output:</strong><br><pre>4 2\nabcdef\nebcd af</pre>",
                "explanation": "To solve 'Strings':\n1. Read cin >> a >> b;\n2. Print a.size() << \" \" << b.size() << endl;\n3. Print a + b << endl;\n4. Swap first chars: swap(a[0], b[0]);\n5. Print a << \" \" << b << endl;\n\nTime Complexity: O(len(a) + len(b))\nSpace Complexity: O(len(a) + len(b))"
            },
            {
                "id": 12,
                "title": "Inherited Code",
                "difficulty": "Medium",
                "is_coding": True,
                "starter_code": "#include <iostream>\n#include <string>\n#include <exception>\nusing namespace std;\n\n/* Define the BadLengthException class here */\nclass BadLengthException {\nprivate:\n    int n;\npublic:\n    BadLengthException(int error_n) : n(error_n) {}\n    int what() {\n        return n;\n    }\n};\n\nbool checkUsername(string username) {\n    bool isValid = true;\n    int n = username.length();\n    if (n < 5) {\n        throw BadLengthException(n);\n    }\n    for (int i = 0; i < n - 1; i++) {\n        if (username[i] == 'w' && username[i + 1] == 'w') {\n            isValid = false;\n        }\n    }\n    return isValid;\n}\n\nint main() {\n    int T;\n    cin >> T;\n    while (T--) {\n        string username;\n        cin >> username;\n        try {\n            bool isValid = checkUsername(username);\n            if (isValid) {\n                cout << \"Valid\" << endl;\n            } else {\n                cout << \"Invalid\" << endl;\n            }\n        } catch (BadLengthException e) {\n            cout << \"Too short: \" << e.what() << endl;\n        }\n    }\n    return 0;\n}",
                "question_text": "<strong>Inherited Code</strong><br><br>You inherited a piece of code that performs username validation for your company's website. The existing function works reasonably well, but it throws an exception when the username is too short. Complete the code by defining the exception class <code>BadLengthException</code>.<br><br><strong>Task:</strong><br>Define the exception class <code>BadLengthException</code> so that when caught, calling <code>e.what()</code> returns an integer representing the length of the too-short username.<br><br><strong>Output Format:</strong><br>- Prints <code>Valid</code> if valid.<br>- Prints <code>Invalid</code> if invalid.<br>- Prints <code>Too short: n</code> (where <code>n</code> is username length) if too short.<br><br><strong>Constraints:</strong><br>- <code>1 <= t <= 1000</code><br>- <code>1 <= |u| <= 100</code>",
                "explanation": "To solve 'Inherited Code':\nDefine custom exception class:\nclass BadLengthException {\n    int n;\npublic:\n    BadLengthException(int length) : n(length) {}\n    int what() { return n; }\n};\n\nTime Complexity: O(1) per check\nSpace Complexity: O(1)"
            },
            {
                "id": 13,
                "title": "Exceptional Server",
                "difficulty": "Medium",
                "is_coding": True,
                "starter_code": "#include <iostream>\n#include <exception>\n#include <string>\n#include <stdexcept>\n#include <vector>\n#include <cmath>\nusing namespace std;\n\nclass Server {\nprivate:\n\tstatic int load;\npublic:\n\tstatic int compute(long long A, long long B) {\n\t\tload += 1;\n\t\tif(A < 0) {\n\t\t\tthrow invalid_argument(\"A must be non-negative\");\n\t\t}\n\t\tif(B == 0) {\n\t\t\tthrow bad_alloc();\n\t\t}\n\t\tlong long real = A / B;\n\t\tif(real < 0) {\n\t\t\tthrow static_cast<int>(A);\n\t\t}\n\t\treturn A / B;\n\t}\n\tstatic int getLoad() {\n\t\treturn load;\n\t}\n};\nint Server::load = 0;\n\nint main() {\n\tint T;\n\tcin >> T;\n\twhile(T--) {\n\t\tlong long A, B;\n\t\tcin >> A >> B;\n\t\t/* Enter your code here. */\n\t\ttry {\n\t\t\tcout << Server::compute(A, B) << endl;\n\t\t} catch (bad_alloc&) {\n\t\t\tcout << \"Not enough memory\" << endl;\n\t\t} catch (exception& e) {\n\t\t\tcout << \"Exception: \" << e.what() << endl;\n\t\t} catch (...) {\n\t\t\tcout << \"Other Exception\" << endl;\n\t\t}\n\t}\n\tcout << Server::getLoad() << endl;\n\treturn 0;\n}",
                "question_text": "<strong>Exceptional Server</strong><br><br>In this challenge, handle error messages while working with a computational server that performs calculations.<br><br><strong>Task:</strong><br>For each test case, call <code>Server::compute(A, B)</code> inside a <code>try-catch</code> block:<br>- If compute runs fine, print the result.<br>- If it throws <code>std::bad_alloc</code>, print <code>Not enough memory</code>.<br>- If it throws any other <code>std::exception</code>, print <code>Exception: S</code> (where <code>S</code> is <code>e.what()</code>).<br>- If it throws any non-standard exception, print <code>Other Exception</code>.<br><br><strong>Constraints:</strong><br>- <code>1 <= T <= 10^3</code><br>- <code>0 <= A, B <= 2^60</code>",
                "explanation": "To solve 'Exceptional Server':\nUse try/catch ordering:\n1. catch (bad_alloc&) -> print \"Not enough memory\"\n2. catch (exception& e) -> print \"Exception: \" << e.what()\n3. catch (...) -> print \"Other Exception\"\n\nTime Complexity: O(1) per query\nSpace Complexity: O(1)"
            },
            {
                "id": 14,
                "title": "Rectangle Area",
                "difficulty": "Easy",
                "is_coding": True,
                "starter_code": "#include <iostream>\nusing namespace std;\n\n/*\n * Create classes Rectangle and RectangleArea\n */\n\nint main()\n{\n    RectangleArea r_area;\n    r_area.read_input();\n    r_area.Rectangle::display();\n    r_area.display();\n    return 0;\n}",
                "question_text": "<strong>Rectangle Area</strong><br><br>Compute the area of a rectangle using inheritance and classes.<br><br><strong>Create two classes:</strong><br>1. <code>Rectangle</code>:<br>- Two protected/public int fields: <code>width</code> and <code>height</code>.<br>- Method <code>display()</code>: prints <code>width</code> and <code>height</code> separated by space.<br><br>2. <code>RectangleArea</code> (derived from <code>Rectangle</code>):<br>- Method <code>read_input()</code>: reads <code>width</code> and <code>height</code> from <code>cin</code>.<br>- Method <code>display()</code>: prints the area (<code>width * height</code>).<br><br><strong>Sample Input:</strong><br><pre>10 5</pre><br><strong>Sample Output:</strong><br><pre>10 5\n50</pre>",
                "explanation": "To solve 'Rectangle Area':\nClass Rectangle defines fields width, height and display() printing \"width height\".\nClass RectangleArea inherits Rectangle, defines read_input() using cin >> width >> height and overrides display() printing width * height.\n\nTime Complexity: O(1)\nSpace Complexity: O(1)"
            },
            {
                "id": 15,
                "title": "Operator Overloading",
                "difficulty": "Medium",
                "is_coding": True,
                "starter_code": "#include <cmath>\n#include <cstdio>\n#include <vector>\n#include <iostream>\n#include <algorithm>\nusing namespace std;\n\nclass Matrix {\npublic:\n    vector<vector<int>> a;\n    Matrix operator+(const Matrix& other) {\n        Matrix result;\n        int n = a.size();\n        int m = a[0].size();\n        result.a = vector<vector<int>>(n, vector<int>(m));\n        for (int i = 0; i < n; i++) {\n            for (int j = 0; j < m; j++) {\n                result.a[i][j] = a[i][j] + other.a[i][j];\n            }\n        }\n        return result;\n    }\n};\n\nint main () {\n   int cases, k;\n   cin >> cases;\n   for (k = 0; k < cases; k++) {\n      Matrix x;\n      Matrix y;\n      Matrix result;\n      int n, m, i, j;\n      cin >> n >> m;\n      for (i = 0; i < n; i++) {\n         vector<int> b;\n         for (j = 0; j < m; j++) {\n            int num;\n            cin >> num;\n            b.push_back(num);\n         }\n         x.a.push_back(b);\n      }\n      for (i = 0; i < n; i++) {\n         vector<int> b;\n         for (j = 0; j < m; j++) {\n            int num;\n            cin >> num;\n            b.push_back(num);\n         }\n         y.a.push_back(b);\n      }\n      result = x + y;\n      for (i = 0; i < n; i++) {\n         for (j = 0; j < m; j++) {\n            cout << result.a[i][j] << \" \";\n         }\n         cout << endl;\n      }\n   }\n   return 0;\n}",
                "question_text": "<strong>Operator Overloading</strong><br><br>Classes define new types in C++. You are required to write class <code>Matrix</code> which contains member <code>a</code> of type <code>vector&lt;vector&lt;int&gt;&gt;</code> and overload operator <code>+</code> to add two matrices.<br><br><strong>Task:</strong><br>Write class <code>Matrix</code> with operator <code>+</code> overloading to return a new <code>Matrix</code> containing element-wise sum of two matrices.<br><br><strong>Constraints:</strong><br>- <code>1 <= T <= 1000</code><br>- <code>1 <= N, M <= 10</code>",
                "explanation": "To solve 'Operator Overloading':\nDefine class Matrix with member vector<vector<int>> a.\nOverload operator+:\nMatrix operator+(const Matrix& other) {\n    Matrix res;\n    int n = a.size(), m = a[0].size();\n    res.a = vector<vector<int>>(n, vector<int>(m));\n    for(int i=0; i<n; i++)\n        for(int j=0; j<m; j++)\n            res.a[i][j] = a[i][j] + other.a[i][j];\n    return res;\n}\n\nTime Complexity: O(N * M) per matrix addition\nSpace Complexity: O(N * M) auxiliary space"
            }
        ]
    },
    "hr_self_intro": {
        "name": "HR Self Introduction & Pitch",
        "questions": [
            {
                "id": 1,
                "title": "HR_SELF_INTRO Theory Concept #1",
                "difficulty": "Hard",
                "question_text": "Question 1: What is the core architectural principle regarding <code>HR Self Introduction & Pitch</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for HR Self Introduction & Pitch",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for HR Self Introduction & Pitch."
            },
            {
                "id": 2,
                "title": "HR_SELF_INTRO Theory Concept #2",
                "difficulty": "Hard",
                "question_text": "Question 2: What is the core architectural principle regarding <code>HR Self Introduction & Pitch</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for HR Self Introduction & Pitch",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for HR Self Introduction & Pitch."
            },
            {
                "id": 3,
                "title": "HR_SELF_INTRO Theory Concept #3",
                "difficulty": "Hard",
                "question_text": "Question 3: What is the core architectural principle regarding <code>HR Self Introduction & Pitch</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for HR Self Introduction & Pitch",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for HR Self Introduction & Pitch."
            },
            {
                "id": 4,
                "title": "HR_SELF_INTRO Theory Concept #4",
                "difficulty": "Hard",
                "question_text": "Question 4: What is the core architectural principle regarding <code>HR Self Introduction & Pitch</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for HR Self Introduction & Pitch",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for HR Self Introduction & Pitch."
            },
            {
                "id": 5,
                "title": "HR_SELF_INTRO Theory Concept #5",
                "difficulty": "Hard",
                "question_text": "Question 5: What is the core architectural principle regarding <code>HR Self Introduction & Pitch</code> in high-scale systems?",
                "options": [
                    "A) Primary optimal architectural design choice for HR Self Introduction & Pitch",
                    "B) Secondary memory allocation restriction under concurrency",
                    "C) Fallback standard behavior in default execution scope",
                    "D) Deprecated legacy interface restriction"
                ],
                "correct_option": "A",
                "explanation": "Option A represents the authoritative correct design for HR Self Introduction & Pitch."
            },
            {
                "id": 6,
                "title": "Programming Task #1: HR Self Introduction & Pitch Practical Challenge",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "# Write your structured executive 90-second self-introduction and career highlight pitch:",
                "question_text": "<strong>Programming Task #1:</strong><br>Implement a production-grade algorithmic or architectural solution for <strong>HR Self Introduction & Pitch</strong>.<br><br><strong>Requirements:</strong><br>- Ensure optimal Time and Space complexity.<br>- Write robust, well-structured, production-ready code with edge case handling.<br><br>Write your solution below:",
                "explanation": "Ensure your solution handles edge cases, memory limits, and optimal computational complexity."
            },
            {
                "id": 7,
                "title": "Programming Task #2: HR Self Introduction & Pitch Practical Challenge",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "# Write your structured executive 90-second self-introduction and career highlight pitch:",
                "question_text": "<strong>Programming Task #2:</strong><br>Implement a production-grade algorithmic or architectural solution for <strong>HR Self Introduction & Pitch</strong>.<br><br><strong>Requirements:</strong><br>- Ensure optimal Time and Space complexity.<br>- Write robust, well-structured, production-ready code with edge case handling.<br><br>Write your solution below:",
                "explanation": "Ensure your solution handles edge cases, memory limits, and optimal computational complexity."
            },
            {
                "id": 8,
                "title": "Programming Task #3: HR Self Introduction & Pitch Practical Challenge",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "# Write your structured executive 90-second self-introduction and career highlight pitch:",
                "question_text": "<strong>Programming Task #3:</strong><br>Implement a production-grade algorithmic or architectural solution for <strong>HR Self Introduction & Pitch</strong>.<br><br><strong>Requirements:</strong><br>- Ensure optimal Time and Space complexity.<br>- Write robust, well-structured, production-ready code with edge case handling.<br><br>Write your solution below:",
                "explanation": "Ensure your solution handles edge cases, memory limits, and optimal computational complexity."
            },
            {
                "id": 9,
                "title": "Programming Task #4: HR Self Introduction & Pitch Practical Challenge",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "# Write your structured executive 90-second self-introduction and career highlight pitch:",
                "question_text": "<strong>Programming Task #4:</strong><br>Implement a production-grade algorithmic or architectural solution for <strong>HR Self Introduction & Pitch</strong>.<br><br><strong>Requirements:</strong><br>- Ensure optimal Time and Space complexity.<br>- Write robust, well-structured, production-ready code with edge case handling.<br><br>Write your solution below:",
                "explanation": "Ensure your solution handles edge cases, memory limits, and optimal computational complexity."
            },
            {
                "id": 10,
                "title": "Programming Task #5: HR Self Introduction & Pitch Practical Challenge",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "# Write your structured executive 90-second self-introduction and career highlight pitch:",
                "question_text": "<strong>Programming Task #5:</strong><br>Implement a production-grade algorithmic or architectural solution for <strong>HR Self Introduction & Pitch</strong>.<br><br><strong>Requirements:</strong><br>- Ensure optimal Time and Space complexity.<br>- Write robust, well-structured, production-ready code with edge case handling.<br><br>Write your solution below:",
                "explanation": "Ensure your solution handles edge cases, memory limits, and optimal computational complexity."
            },
            {
                "id": 11,
                "title": "Programming Task #6: HR Self Introduction & Pitch Practical Challenge",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "# Write your structured executive 90-second self-introduction and career highlight pitch:",
                "question_text": "<strong>Programming Task #6:</strong><br>Implement a production-grade algorithmic or architectural solution for <strong>HR Self Introduction & Pitch</strong>.<br><br><strong>Requirements:</strong><br>- Ensure optimal Time and Space complexity.<br>- Write robust, well-structured, production-ready code with edge case handling.<br><br>Write your solution below:",
                "explanation": "Ensure your solution handles edge cases, memory limits, and optimal computational complexity."
            },
            {
                "id": 12,
                "title": "Programming Task #7: HR Self Introduction & Pitch Practical Challenge",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "# Write your structured executive 90-second self-introduction and career highlight pitch:",
                "question_text": "<strong>Programming Task #7:</strong><br>Implement a production-grade algorithmic or architectural solution for <strong>HR Self Introduction & Pitch</strong>.<br><br><strong>Requirements:</strong><br>- Ensure optimal Time and Space complexity.<br>- Write robust, well-structured, production-ready code with edge case handling.<br><br>Write your solution below:",
                "explanation": "Ensure your solution handles edge cases, memory limits, and optimal computational complexity."
            },
            {
                "id": 13,
                "title": "Programming Task #8: HR Self Introduction & Pitch Practical Challenge",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "# Write your structured executive 90-second self-introduction and career highlight pitch:",
                "question_text": "<strong>Programming Task #8:</strong><br>Implement a production-grade algorithmic or architectural solution for <strong>HR Self Introduction & Pitch</strong>.<br><br><strong>Requirements:</strong><br>- Ensure optimal Time and Space complexity.<br>- Write robust, well-structured, production-ready code with edge case handling.<br><br>Write your solution below:",
                "explanation": "Ensure your solution handles edge cases, memory limits, and optimal computational complexity."
            },
            {
                "id": 14,
                "title": "Programming Task #9: HR Self Introduction & Pitch Practical Challenge",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "# Write your structured executive 90-second self-introduction and career highlight pitch:",
                "question_text": "<strong>Programming Task #9:</strong><br>Implement a production-grade algorithmic or architectural solution for <strong>HR Self Introduction & Pitch</strong>.<br><br><strong>Requirements:</strong><br>- Ensure optimal Time and Space complexity.<br>- Write robust, well-structured, production-ready code with edge case handling.<br><br>Write your solution below:",
                "explanation": "Ensure your solution handles edge cases, memory limits, and optimal computational complexity."
            },
            {
                "id": 15,
                "title": "Programming Task #10: HR Self Introduction & Pitch Practical Challenge",
                "difficulty": "Hard",
                "is_coding": True,
                "starter_code": "# Write your structured executive 90-second self-introduction and career highlight pitch:",
                "question_text": "<strong>Programming Task #10:</strong><br>Implement a production-grade algorithmic or architectural solution for <strong>HR Self Introduction & Pitch</strong>.<br><br><strong>Requirements:</strong><br>- Ensure optimal Time and Space complexity.<br>- Write robust, well-structured, production-ready code with edge case handling.<br><br>Write your solution below:",
                "explanation": "Ensure your solution handles edge cases, memory limits, and optimal computational complexity."
            }
        ]
    },
    "hr_general": {
        "name": "General HR Round Questions",
        "scoring_criteria": {
            "Confidence": "20%",
            "Communication": "20%",
            "Clarity": "20%",
            "Relevance": "20%",
            "Professionalism": "20%"
        },
        "questions": [
            {
                "id": 1,
                "title": "Tell me about yourself.",
                "difficulty": "Easy",
                "category_group": "Basic HR Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "Tell me about yourself.",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 2,
                "title": "What are your strengths?",
                "difficulty": "Easy",
                "category_group": "Basic HR Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "What are your strengths?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 3,
                "title": "What are your weaknesses?",
                "difficulty": "Easy",
                "category_group": "Basic HR Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "What are your weaknesses?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 4,
                "title": "Why should we hire you?",
                "difficulty": "Medium",
                "category_group": "Basic HR Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "Why should we hire you?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 5,
                "title": "Why do you want to work for our company?",
                "difficulty": "Medium",
                "category_group": "Basic HR Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "Why do you want to work for our company?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 6,
                "title": "What motivates you?",
                "difficulty": "Easy",
                "category_group": "Basic HR Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "What motivates you?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 7,
                "title": "What are your career goals?",
                "difficulty": "Medium",
                "category_group": "Basic HR Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "What are your career goals?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 8,
                "title": "Where do you see yourself in 5 years?",
                "difficulty": "Medium",
                "category_group": "Basic HR Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "Where do you see yourself in 5 years?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 9,
                "title": "Why did you choose Computer Science?",
                "difficulty": "Easy",
                "category_group": "Education & Background",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "Why did you choose Computer Science?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 10,
                "title": "Tell me about your academic journey.",
                "difficulty": "Easy",
                "category_group": "Education & Background",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "Tell me about your academic journey.",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 11,
                "title": "What was your favorite subject and why?",
                "difficulty": "Easy",
                "category_group": "Education & Background",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "What was your favorite subject and why?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 12,
                "title": "What skills have you learned during your B.Tech?",
                "difficulty": "Easy",
                "category_group": "Education & Background",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "What skills have you learned during your B.Tech?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 13,
                "title": "Explain your major project.",
                "difficulty": "Medium",
                "category_group": "Project-Based Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "Explain your major project.",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 14,
                "title": "What challenges did you face in your project?",
                "difficulty": "Medium",
                "category_group": "Project-Based Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "What challenges did you face in your project?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 15,
                "title": "What technologies did you use and why?",
                "difficulty": "Medium",
                "category_group": "Project-Based Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "What technologies did you use and why?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 16,
                "title": "If given more time, what improvements would you make to your project?",
                "difficulty": "Medium",
                "category_group": "Project-Based Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "If given more time, what improvements would you make to your project?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 17,
                "title": "Describe a time when you worked in a team.",
                "difficulty": "Medium",
                "category_group": "Teamwork & Behavioral Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "Describe a time when you worked in a team.",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 18,
                "title": "Tell me about a challenge you faced and how you solved it.",
                "difficulty": "Medium",
                "category_group": "Teamwork & Behavioral Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "Tell me about a challenge you faced and how you solved it.",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 19,
                "title": "Have you ever handled a conflict with a teammate?",
                "difficulty": "Hard",
                "category_group": "Teamwork & Behavioral Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "Have you ever handled a conflict with a teammate?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 20,
                "title": "Describe a situation where you showed leadership.",
                "difficulty": "Hard",
                "category_group": "Teamwork & Behavioral Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "Describe a situation where you showed leadership.",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 21,
                "title": "What would you do if you missed a project deadline?",
                "difficulty": "Hard",
                "category_group": "Situational Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "What would you do if you missed a project deadline?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 22,
                "title": "How would you handle pressure at work?",
                "difficulty": "Medium",
                "category_group": "Situational Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "How would you handle pressure at work?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 23,
                "title": "How would you deal with negative feedback?",
                "difficulty": "Medium",
                "category_group": "Situational Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "How would you deal with negative feedback?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 24,
                "title": "What would you do if you disagreed with your manager?",
                "difficulty": "Hard",
                "category_group": "Situational Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "What would you do if you disagreed with your manager?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 25,
                "title": "Why should we select you over other candidates?",
                "difficulty": "Hard",
                "category_group": "Company & Career Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "Why should we select you over other candidates?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 26,
                "title": "Are you willing to relocate?",
                "difficulty": "Easy",
                "category_group": "Company & Career Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "Are you willing to relocate?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 27,
                "title": "What salary do you expect?",
                "difficulty": "Medium",
                "category_group": "Company & Career Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "What salary do you expect?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            },
            {
                "id": 28,
                "title": "Do you have any questions for us?",
                "difficulty": "Easy",
                "category_group": "Company & Career Questions",
                "is_coding": True,
                "starter_code": "Write your answer here...",
                "question_text": "Do you have any questions for us?",
                "explanation": "Evaluated on: Confidence (20%), Communication (20%), Clarity (20%), Relevance (20%), Professionalism (20%)."
            }
        ]
    }
}
