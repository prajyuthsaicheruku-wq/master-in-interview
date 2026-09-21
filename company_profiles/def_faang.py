# -*- coding: utf-8 -*-
FAANG_COMPANIES = {
    'uber': {
        'canonical_name': 'Uber',
        'total_mins': 90,
        'total_qs': 4,
        'roles': 'Software Engineer I / II (L3/L4 - Backend & Distributed Systems)',
        'ctc': '₹38.0 - ₹52.0 LPA',
        'eligibility': 'B.E / B.Tech / M.Tech in CS/IT/ECE (7.0+ CGPA with no backlogs)',
        'difficulty': 'Hard / Elite',
        'difficulty_class': 'badge-danger',
        'tagline': 'Uber software engineering placement pattern, algorithms, high-scale system design & solved past papers.',
        'brand_color': '#000000',
        'accent_bg': 'linear-gradient(135deg, #1f2937 0%, #000000 100%)',
        'logo_icon': '🚗',
        'logo_image': 'images/uber.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Online Coding Assessment', 'desc': 'CodeSignal Framework | 4 Questions | 70–90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical DSA Round', 'desc': 'Graphs, DP & Trees | 2 Problems | 60 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'Machine Coding & LLD', 'desc': 'Low-Level Design & Concurrency | 1 Problem | 60 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'System Architecture (HLD)', 'desc': 'Microservices & Geospatial Scale | 60 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Bar Raiser & Values', 'desc': 'Uber Norms & Cultural Fitment | 45 Mins', 'icon': '🎯'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: CodeSignal OA',
                'sections': [
                    {'name': 'Array & String Manipulation', 'qs': '1 Q', 'time': '15 Mins'},
                    {'name': 'Matrix & Simulation Logic', 'qs': '1 Q', 'time': '15 Mins'},
                    {'name': 'Sliding Window & Hash Logic', 'qs': '1 Q', 'time': '20 Mins'},
                    {'name': 'Hard Graph / DP Optimization', 'qs': '1 Q', 'time': '20 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: DSA CoderPad',
                'sections': [
                    {'name': 'Graph Shortest Path & Dijkstra', 'qs': '1 Q', 'time': '30 Mins'},
                    {'name': 'Dynamic Programming on Trees', 'qs': '1 Q', 'time': '30 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Machine Coding',
                'sections': [
                    {'name': 'Cab Dispatch / Surge Pricing LLD', 'qs': '1 System', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: System Architecture',
                'sections': [
                    {'name': 'Real-Time Telemetry & Kafka Pipelines', 'qs': '1 Design', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 5: Bar Raiser',
                'sections': [
                    {'name': 'Behavioral, Leadership & Uber Culture', 'qs': '5–8 Qs', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'DSA & Advanced Algorithms', 'icon': '🧠', 'qs': '45 Qs', 'time': '60 Mins', 'topics': ['Graph Shortest Path (Dijkstra, A*)', 'Dynamic Programming on Trees & Bitmasks', 'Trie & Segment Trees', 'Sliding Window & Two Pointers']},
            {'category': 'System Architecture & LLD', 'icon': '💻', 'qs': '30 Qs', 'time': '45 Mins', 'topics': ['Microservices & Rate Limiting Token Bucket', 'Low-Level Class Design (Cab Dispatching)', 'Concurrency & Mutex Locks in Go/Java', 'Cache Invalidation Strategies (Redis)']},
            {'category': 'CS Fundamentals & Databases', 'icon': '⚡', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['OS Virtual Memory & Paging', 'PostgreSQL vs Cassandra Indexing', 'Kafka & Event Streams Pub/Sub', 'gRPC & TCP Socket Protocols']},
            {'category': 'Live Coding Assessment', 'icon': '🎯', 'qs': '2 Qs', 'time': '60 Mins', 'topics': ['Geospatial Quadtree / H3 Indexing', 'Optimal Fleet Matching Algorithms', 'Real-Time Telemetry Stream Processing', 'Dynamic Surge Pricing Logic']}
        ],
        'faqs': [
            {'q': 'What coding platform does Uber use for campus & off-campus hiring?', 'a': 'Uber uses CodeSignal (General Coding Assessment) and HackerRank. The test strictly checks correctness, time complexity, and hidden edge cases.'},
            {'q': 'Is there negative marking in Uber Online Assessment?', 'a': 'No, there is no negative marking, but CodeSignal scores speed and test case pass rates dynamically.'},
            {'q': 'What is Uber\'s Bar Raiser round?', 'a': 'A comprehensive interview conducted by an independent senior engineer from another team to evaluate cultural values, architectural rigor, and candidate potential.'},
            {'q': 'What programming languages are preferred in Uber technical interviews?', 'a': 'Java, Go, C++, and Python are widely supported and accepted.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Uber SDE-1 CodeSignal Benchmark Test Model 1',
                'total_qs': 4,
                'duration': '90 Mins',
                'sample_coding': 'Given driver locations on a 2D coordinate plane and rider requests, implement a geospatial nearest-K matching algorithm within distance D in O(N log K).',
                'sample_quant': 'In a fleet routing graph of V vertices and E weighted edges, compute the minimum time to route N vehicles to destinations without bottleneck link overlap.',
                'sample_tech': 'Explain how Uber uses Uber H3 hexagonal geospatial indexing system to compute local surge pricing in real-time.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Uber Onsite Technical & System Design Model 2',
                'total_qs': 4,
                'duration': '90 Mins',
                'sample_coding': 'Design a thread-safe distributed rate limiter using the Token Bucket algorithm supporting 100k requests/second.',
                'sample_quant': 'Given a stream of real-time GPS telemetry packets, detect taxi speeding anomalies using a sliding window median filter.',
                'sample_tech': 'Differentiate between optimistic and pessimistic locking in relational databases when handling ride payment transactions.'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Uber University Graduate SDE Placement Paper Model 3',
                'total_qs': 4,
                'duration': '90 Mins',
                'sample_coding': 'Find the shortest path in a directed weighted graph that visits a mandatory subset of K transit hub nodes.',
                'sample_quant': 'Calculate the expected waiting time for a rider given Poisson arrival rates of cabs and exponential trip durations.',
                'sample_tech': 'How does Kafka guarantee message ordering across partitions when streaming ride event logs?'
            }
        ]
    },

    'salesforce': {
        'canonical_name': 'Salesforce',
        'total_mins': 90,
        'total_qs': 23,
        'roles': 'Associate Member of Technical Staff (AMTS) / Software Engineer',
        'ctc': '₹32.0 - ₹44.0 LPA',
        'eligibility': 'B.E / B.Tech / M.Tech in CS/IT (7.0+ CGPA with no active backlogs)',
        'difficulty': 'Hard / Product Tier',
        'difficulty_class': 'badge-danger',
        'tagline': 'Salesforce AMTS placement pattern, cloud architectures, OOP design patterns & solved model papers.',
        'brand_color': '#00a1e0',
        'accent_bg': 'linear-gradient(135deg, #00a1e0 0%, #0369a1 100%)',
        'logo_icon': '☁️',
        'logo_image': 'images/salesforce.svg',
        'selection_stages': [
            {'step': 1, 'title': 'HackerRank Online Test', 'desc': '20 MCQs + 3 Coding Qs | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical DSA Round 1', 'desc': 'Binary Trees, Graphs & DP | 60 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'Technical Round 2 (OOP/LLD)', 'desc': 'SOLID Design & Multi-Tenancy | 60 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Cloud & Architecture', 'desc': 'REST APIs, Microservices & SQL | 45 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Managerial & HR Round', 'desc': 'Salesforce Core Values & Fitment | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: HackerRank OA',
                'sections': [
                    {'name': 'CS Core & OOP MCQs', 'qs': '20 Qs', 'time': '30 Mins'},
                    {'name': 'Data Structures Coding', 'qs': '2 Qs', 'time': '40 Mins'},
                    {'name': 'Advanced Algorithm Challenge', 'qs': '1 Q', 'time': '20 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: DSA Interview',
                'sections': [
                    {'name': 'Binary Trees, BSTs & Heap', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: OOP & LLD',
                'sections': [
                    {'name': 'SOLID Principles & Multi-Tenant DB Modeling', 'qs': '1 Design', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Managerial',
                'sections': [
                    {'name': 'Salesforce Ohana Culture & Scenarios', 'qs': '5–8 Qs', 'time': '30 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Data Structures & Algorithms', 'icon': '🧠', 'qs': '40 Qs', 'time': '50 Mins', 'topics': ['Binary Search & Sorting', 'Graph BFS/DFS & Topo Sort', 'Hash Maps & LRU Cache', 'Recursion & Backtracking']},
            {'category': 'OOP & Cloud Concepts', 'icon': '💻', 'qs': '35 Qs', 'time': '40 Mins', 'topics': ['SOLID Design Principles', 'Multi-Tenant Cloud Architectures', 'RESTful API Design', 'Distributed Data Modeling']},
            {'category': 'SQL, DB & Web Fundamentals', 'icon': '⚡', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['Relational Schema Normalization', 'Transactions & ACID Semantics', 'Async JavaScript & Event Loop', 'HTTP Security & OAuth 2.0']},
            {'category': 'Coding Assessment', 'icon': '🎯', 'qs': '2 Qs', 'time': '60 Mins', 'topics': ['Custom Data Structure Implementation', 'Tree Traversal & Modification', 'Matrix Path Optimization', 'String Parsing & Validation']}
        ],
        'faqs': [
            {'q': 'What is the AMTS hiring process at Salesforce?', 'a': 'A 90-minute HackerRank OA followed by 3 technical rounds (DSA, OOP/LLD, Cloud/DB) and 1 managerial round.'},
            {'q': 'What topics are most asked in Salesforce DSA rounds?', 'a': 'Binary Trees, BSTs, Graphs (Dijkstra, Cycle Detection), and LRU Cache design.'},
            {'q': 'Does Salesforce test multi-tenancy and cloud fundamentals?', 'a': 'Yes, freshers are asked about multi-tenant databases, API design, caching, and ACID transactions.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Salesforce AMTS Placement Paper Model 1',
                'total_qs': 23,
                'duration': '90 Mins',
                'sample_coding': 'Design an LRU Cache with O(1) time complexity for get and put operations using doubly linked list and hash map.',
                'sample_quant': 'Given N cloud servers with specific RAM limits, allocate M incoming tasks to maximize utilization without exceeding capacity.',
                'sample_tech': 'Explain multi-tenant architecture and how data isolation is enforced across different enterprise tenants in database systems.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Salesforce AMTS Coding & CS MCQ Model 2',
                'total_qs': 23,
                'duration': '90 Mins',
                'sample_coding': 'Given a binary tree, serialize it to a string and deserialize the string back to the original binary tree structure.',
                'sample_quant': 'Find the maximum sum path between any two leaf nodes in a weighted binary tree.',
                'sample_tech': 'Explain ACID properties in relational databases and how dirty reads are prevented in Read Committed isolation level.'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Salesforce University Hiring Solved Paper Model 3',
                'total_qs': 23,
                'duration': '90 Mins',
                'sample_coding': 'Find the smallest missing positive integer in an unsorted array in O(N) time and O(1) auxiliary space.',
                'sample_quant': 'Calculate the minimum number of network hops between two client nodes in an enterprise server topology.',
                'sample_tech': 'What is the difference between synchronous and asynchronous web API execution models?'
            }
        ]
    },

    'atlassian': {
        'canonical_name': 'Atlassian',
        'total_mins': 90,
        'total_qs': 4,
        'roles': 'Graduate Software Engineer / Full Stack Engineer',
        'ctc': '₹30.0 - ₹45.0 LPA',
        'eligibility': 'B.Tech / Dual Degree in CS/IT/ECE (Skill-first evaluation)',
        'difficulty': 'Hard / Elite',
        'difficulty_class': 'badge-danger',
        'tagline': 'Atlassian Graduate Engineer test pattern, data structures, behavioral values interview & solved papers.',
        'brand_color': '#0052cc',
        'accent_bg': 'linear-gradient(135deg, #0052cc 0%, #172b4d 100%)',
        'logo_icon': '🔷',
        'logo_image': 'images/atlassian.svg',
        'selection_stages': [
            {'step': 1, 'title': 'HackerRank Online Assessment', 'desc': '3 Coding Problems | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'CoderPad Live Pair Coding', 'desc': 'DSA & Clean Code | 60 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'System Modeling & LLD', 'desc': 'Object Modeling & Refactoring | 60 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Craft & Architecture', 'desc': 'Web, Concurrency & APIs | 60 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Atlassian Values Interview', 'desc': '5 Core Values & Behavioral Fit | 45 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: HackerRank OA',
                'sections': [
                    {'name': 'Standard DSA Problem', 'qs': '1 Q', 'time': '25 Mins'},
                    {'name': 'Optimization / DP Problem', 'qs': '1 Q', 'time': '35 Mins'},
                    {'name': 'String / Parser Logic', 'qs': '1 Q', 'time': '30 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Pair Programming',
                'sections': [
                    {'name': 'Live CoderPad Coding with Unit Tests', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: System Modeling',
                'sections': [
                    {'name': 'Class Hierarchy & Extensibility Design', 'qs': '1 Design', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Values Round',
                'sections': [
                    {'name': 'Atlassian 5 Core Values Assessment', 'qs': 'Behavioral', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Problem Solving & DSA', 'icon': '🧠', 'qs': '45 Qs', 'time': '60 Mins', 'topics': ['Hash Table Lookups', 'Priority Queues & Heaps', 'Dynamic Programming memoization', 'Tree & Graph Traversals']},
            {'category': 'System Modeling & Clean Code', 'icon': '💻', 'qs': '30 Qs', 'time': '45 Mins', 'topics': ['Clean Architecture & Refactoring', 'Design Patterns (Factory, Observer)', 'Concurrency in Java/Python', 'Unit Testing & Mocking']},
            {'category': 'Atlassian Values & Behavioral', 'icon': '🗣️', 'qs': '15 Qs', 'time': '30 Mins', 'topics': ['Open Company No Bullshit', 'Build with Heart & Balance', 'Don’t #@!% the Customer', 'Play as a Team']},
            {'category': 'Live Coding Assessment', 'icon': '⚡', 'qs': '2 Qs', 'time': '60 Mins', 'topics': ['File System Hierarchy Search', 'Rate Limiter & Token Bucket', 'Markdown Document Parser', 'Distributed Task Scheduler']}
        ],
        'faqs': [
            {'q': 'What does Atlassian evaluate during live pair programming?', 'a': 'Code cleanliness, modular structure, meaningful variable naming, test-driven approach (writing unit tests), and edge case handling.'},
            {'q': 'How important is the Atlassian Values interview?', 'a': 'Crucial. Atlassian weighs culture fit equally with technical ability; candidates must demonstrate alignment with their 5 core values.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Atlassian Graduate Engineer OA Paper Model 1',
                'total_qs': 4,
                'duration': '90 Mins',
                'sample_coding': 'Design a rate limiter that tracks request timestamps per API key and allows at most K requests in any rolling W-second window.',
                'sample_quant': 'Given an array of Jira ticket dependencies (directed edges), return a valid topological build order or detect circular dependency.',
                'sample_tech': 'Explain the Factory and Observer design patterns and how they are applied in event-driven collaborative editing software.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Atlassian Live CoderPad Pair Programming Model 2',
                'total_qs': 4,
                'duration': '90 Mins',
                'sample_coding': 'Implement an in-memory file system with mkdir, ls, addContentToFile, and readContentFromFile with clean OOP classes.',
                'sample_quant': 'Find the maximum collection of non-overlapping sprint tasks given their start and finish timestamps.',
                'sample_tech': 'How do you handle thread safety and race conditions when multiple users edit the same Confluence document concurrently?'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Atlassian University Hiring Solved Paper Model 3',
                'total_qs': 4,
                'duration': '90 Mins',
                'sample_coding': 'Write a Markdown parser that converts nested bullet points and bold/italic tags into standard semantic HTML tags.',
                'sample_quant': 'Calculate the minimum number of server nodes required to host M collaborative workspace channels.',
                'sample_tech': 'Explain the difference between optimistic concurrency control and pessimistic locking in distributed document stores.'
            }
        ]
    },

    'nvidia': {
        'canonical_name': 'NVIDIA',
        'total_mins': 90,
        'total_qs': 37,
        'roles': 'System Software Engineer / GPU Architecture & Deep Learning Engineer',
        'ctc': '₹24.0 - ₹38.0 LPA',
        'eligibility': 'B.Tech / M.Tech in CS/ECE/EE (Strong C/C++ & Computer Architecture)',
        'difficulty': 'Very Hard / Systems Tier',
        'difficulty_class': 'badge-danger',
        'tagline': 'NVIDIA placement exam pattern, C/C++ systems programming, GPU computing & solved hardware/software papers.',
        'brand_color': '#76b900',
        'accent_bg': 'linear-gradient(135deg, #76b900 0%, #4d7c0f 100%)',
        'logo_icon': '👁️',
        'logo_image': 'images/nvidia.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Online Assessment', 'desc': '35 Core MCQs + 2 C/C++ Coding Qs | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'C/C++ & Memory Deep Dive', 'desc': 'Pointers, Allocators & Assembly | 60 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'OS & Concurrency Round', 'desc': 'Virtual Memory, POSIX & Locks | 60 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'DSA & Problem Solving', 'desc': 'Bit Manipulation & Graph Optimizations | 60 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Hiring Manager & Culture', 'desc': 'GPU Systems & Innovation Fitment | 45 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment',
                'sections': [
                    {'name': 'C/C++ Pointers & Bitwise MCQs', 'qs': '15 Qs', 'time': '25 Mins'},
                    {'name': 'OS, Caches & Architecture MCQs', 'qs': '20 Qs', 'time': '25 Mins'},
                    {'name': 'Systems Programming Coding', 'qs': '2 Qs', 'time': '40 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Systems Interview',
                'sections': [
                    {'name': 'Pointers, Struct Padding, Volatile, Virtual Tables', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: OS & Concurrency',
                'sections': [
                    {'name': 'Page Tables, Cache Lines, Mutexes & Semaphores', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Managerial',
                'sections': [
                    {'name': 'GPU Architecture Awareness & Project Deep-Dive', 'qs': 'Behavioral', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'C/C++ & Systems Programming', 'icon': '💻', 'qs': '40 Qs', 'time': '50 Mins', 'topics': ['Pointers, Memory Allocation & Bitwise Ops', 'Volatile, Const, Static Keywords', 'Multithreading & Synchronization', 'POSIX Threads & Mutexes']},
            {'category': 'OS & Computer Architecture', 'icon': '⚡', 'qs': '35 Qs', 'time': '40 Mins', 'topics': ['Virtual Memory, Paging & TLB', 'Cache Coherence (MESI Protocol)', 'Interrupts, DMA & Device Drivers', 'Instruction Pipeline Hazards']},
            {'category': 'Data Structures & Optimization', 'icon': '🧠', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['Bit Manipulation & Masks', 'Graph Traversals & Trees', 'Priority Queues & Heaps', 'Cache-Friendly Algorithms']},
            {'category': 'CUDA & Parallel Systems Basics', 'icon': '🎯', 'qs': '2 Qs', 'time': '60 Mins', 'topics': ['SIMD vs SIMT Execution', 'GPU Thread Blocks & Warps', 'Shared Memory vs Global Memory', 'Matrix Multiplication Parallelization']}
        ],
        'faqs': [
            {'q': 'Is strong C/C++ mandatory for NVIDIA software roles?', 'a': 'Yes, NVIDIA places heavy emphasis on low-level C/C++, pointer arithmetic, struct memory alignment, and cache-friendly data structures.'},
            {'q': 'What hardware concepts are tested for software engineers at NVIDIA?', 'a': 'CPU cache hierarchies (L1/L2/L3), TLBs, page faults, virtual memory translation, and SIMD vectorization.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'NVIDIA System Software Engineer OA Model 1',
                'total_qs': 37,
                'duration': '90 Mins',
                'sample_coding': 'Write a C function to reverse the bits of a 32-bit unsigned integer without using standard library functions.',
                'sample_quant': 'Given an aligned memory buffer, implement a custom memory allocator (malloc and free) supporting 64-byte alignment.',
                'sample_tech': 'Explain the difference between process page table lookups and TLB cache hits, and describe how TLB shootdown works in multi-core CPUs.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'NVIDIA Systems & C++ Programming Model 2',
                'total_qs': 37,
                'duration': '90 Mins',
                'sample_coding': 'Implement a thread-safe lock-free ring buffer for producer-consumer communication using atomic memory compare-and-swap.',
                'sample_quant': 'Calculate the cache line footprint of a 2D matrix traversal when iterating row-major vs column-major order.',
                'sample_tech': 'What is the purpose of the volatile keyword in C, and why is it essential when accessing memory-mapped I/O registers?'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'NVIDIA University Recruitment Solved Paper Model 3',
                'total_qs': 37,
                'duration': '90 Mins',
                'sample_coding': 'Given an array of integer GPU core utilization rates, find the maximum contiguous subarray with sum divisible by K.',
                'sample_quant': 'Analyze the pipeline hazard stalls in a 5-stage RISC processor executing conditional branch instructions.',
                'sample_tech': 'Explain the SIMT (Single Instruction, Multiple Threads) execution model in GPU architectures and how warp divergence impacts performance.'
            }
        ]
    },

    'walmart': {
        'canonical_name': 'Walmart Global Tech',
        'total_mins': 90,
        'total_qs': 22,
        'roles': 'Software Development Engineer (SDE-1)',
        'ctc': '₹18.0 - ₹26.0 LPA',
        'eligibility': 'B.E / B.Tech / M.Tech in CS/IT/ECE (7.0+ CGPA with no backlogs)',
        'difficulty': 'Hard / Product Tier',
        'difficulty_class': 'badge-danger',
        'tagline': 'Walmart Global Tech SDE placement pattern, scalable e-commerce systems, DSA & solved model papers.',
        'brand_color': '#0071dc',
        'accent_bg': 'linear-gradient(135deg, #0071dc 0%, #0284c7 100%)',
        'logo_icon': '🛒',
        'logo_image': 'images/walmart.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Online Assessment', 'desc': '20 CS Core MCQs + 2 Coding Qs | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'DSA Technical Round 1', 'desc': 'Trees, Graphs & Dynamic Programming | 60 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'Low-Level Design (LLD)', 'desc': 'OOP Design & Database Modeling | 60 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'High Scale Architecture', 'desc': 'Caching, Inventory & Microservices | 45 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'HR & Values Interview', 'desc': 'Customer Centricity & Behavioral | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment',
                'sections': [
                    {'name': 'CS Core MCQs (DBMS, OS, OOP, DSA)', 'qs': '20 Qs', 'time': '30 Mins'},
                    {'name': 'Medium/Hard Algorithmic Coding', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: DSA Interview',
                'sections': [
                    {'name': 'Sliding Window, Graphs & DP', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: LLD & Database',
                'sections': [
                    {'name': 'E-Commerce Cart / Inventory LLD', 'qs': '1 Design', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: HR & Managerial',
                'sections': [
                    {'name': 'Past Projects & Walmart Values', 'qs': 'Behavioral', 'time': '30 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Data Structures & Algorithms', 'icon': '🧠', 'qs': '40 Qs', 'time': '50 Mins', 'topics': ['Sliding Window & Two Pointers', 'Graph BFS/DFS & Dijkstra', 'Dynamic Programming Subsequences', 'Binary Search on Answer']},
            {'category': 'System Design & LLD', 'icon': '💻', 'qs': '30 Qs', 'time': '45 Mins', 'topics': ['E-Commerce Inventory Locking', 'Shopping Cart Class Design', 'Redis Cache Invalidation', 'Microservices Communication (REST/gRPC)']},
            {'category': 'Database & Core CS', 'icon': '⚡', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['SQL Joins & Index Optimization', 'ACID Transactions & Row Locks', 'OS Multi-threading & Synchronization', 'Computer Networks (HTTP/2, CDN)']},
            {'category': 'Live Coding Challenge', 'icon': '🎯', 'qs': '2 Qs', 'time': '60 Mins', 'topics': ['Optimal Warehouse Package Packing', 'Product Recommendation Graph', 'Flash Sale Distributed Queue', 'Cart Discount Coupon Engine']}
        ],
        'faqs': [
            {'q': 'What is the difficulty of Walmart Global Tech coding round?', 'a': 'Medium to Hard LeetCode style problems focusing on Arrays, Dynamic Programming, and Graph Traversals.'},
            {'q': 'Does Walmart test system design for freshers?', 'a': 'Freshers are primarily tested on Low-Level Design (class modeling, design patterns) and basic caching/database concepts.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Walmart Global Tech SDE-1 OA Model 1',
                'total_qs': 22,
                'duration': '90 Mins',
                'sample_coding': 'Given product dimensions and delivery box capacities, determine the minimum number of shipping boxes needed using 0/1 knapsack variation.',
                'sample_quant': 'Calculate the maximum profit from buying and selling warehouse inventory items with at most K transactions.',
                'sample_tech': 'Explain how database indexing using B+ Trees speeds up multi-column product search queries.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Walmart Global Tech Onsite Technical Model 2',
                'total_qs': 22,
                'duration': '90 Mins',
                'sample_coding': 'Design an in-memory shopping cart discount coupon application engine applying percentage and flat discounts with precedence rules.',
                'sample_quant': 'Given a supply chain fulfillment graph, find the maximum flow of goods from suppliers to retail centers using Ford-Fulkerson.',
                'sample_tech': 'How do you prevent inventory overselling during high-traffic flash sales using distributed Redis locking?'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Walmart Campus Placement Solved Paper Model 3',
                'total_qs': 22,
                'duration': '90 Mins',
                'sample_coding': 'Find the longest continuous subarray of items whose total price does not exceed a maximum spending budget.',
                'sample_quant': 'Compute the probability that at least one of N customer orders experiences delivery delay given independent distribution routes.',
                'sample_tech': 'What is the difference between synchronous HTTP calls and asynchronous Kafka messaging in e-commerce microservices?'
            }
        ]
    },

    'amazon': {
        'canonical_name': 'Amazon',
        'total_mins': 105,
        'total_qs': 2,
        'roles': 'Software Development Engineer (SDE-1)',
        'ctc': '₹28.0 - ₹44.0 LPA',
        'eligibility': 'B.E / B.Tech / M.Tech in CS/IT/EC (6.5+ CGPA with no backlogs)',
        'difficulty': 'Hard / Elite',
        'difficulty_class': 'badge-danger',
        'tagline': 'Amazon SDE placement pattern, Leadership Principles, algorithms, LLD & solved OA papers.',
        'brand_color': '#ff9900',
        'accent_bg': 'linear-gradient(135deg, #ff9900 0%, #d97706 100%)',
        'logo_icon': '📦',
        'logo_image': 'images/amazon.svg',
        'selection_stages': [
            {'step': 1, 'title': 'HackerRank OA & Work Style', 'desc': '2 Coding Qs + 20 LP Scenarios | 105 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Interview 1 (DSA)', 'desc': 'Trees, Graphs & Amazon LP | 60 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'Technical Interview 2 (LLD)', 'desc': 'Object Oriented Design & Concurrency | 60 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Technical Interview 3 (DSA/System)', 'desc': 'Optimization & Scalability | 60 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Bar Raiser Round', 'desc': 'Hard Problem Solving & 16 Leadership Principles | 60 Mins', 'icon': '🎯'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: HackerRank OA',
                'sections': [
                    {'name': 'Algorithmic Coding Challenge', 'qs': '2 Qs', 'time': '70 Mins'},
                    {'name': 'Work Style & Amazon Leadership Simulation', 'qs': '20 Scenarios', 'time': '35 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Technical Interview 1',
                'sections': [
                    {'name': 'Binary Trees, Graphs, Heaps & Customer Obsession', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Technical Interview 2',
                'sections': [
                    {'name': 'Object Oriented Class Design (LLD) & Ownership', 'qs': '1 Design', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Bar Raiser',
                'sections': [
                    {'name': 'Deep Algorithmic Optimization & 16 Leadership Principles', 'qs': '1 Q + LP', 'time': '60 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Data Structures & Algorithms', 'icon': '🧠', 'qs': '45 Qs', 'time': '60 Mins', 'topics': ['Trees & Binary Search Trees (LCA, Views)', 'Graph BFS/DFS & Shortest Paths', 'Top-K Elements & Heaps', 'Dynamic Programming Grids & Knapsack']},
            {'category': 'Object Oriented & Low-Level Design', 'icon': '💻', 'qs': '30 Qs', 'time': '45 Mins', 'topics': ['Locker Management System Design', 'Parking Lot / Elevator System LLD', 'SOLID Principles & Design Patterns', 'Thread Safety in Java/C++']},
            {'category': 'Amazon Leadership Principles (LP)', 'icon': '🗣️', 'qs': '20 Scenarios', 'time': '35 Mins', 'topics': ['Customer Obsession & Ownership', 'Bias for Action & Invent and Simplify', 'Earn Trust & Deliver Results', 'Have Backbone; Disagree and Commit']},
            {'category': 'Live Coding Assessment', 'icon': '⚡', 'qs': '2 Qs', 'time': '70 Mins', 'topics': ['Package Fulfillment Optimization', 'Minimum Cost to Connect Warehouse Servers', 'LRU Cache with Time-to-Live', 'Critical Connections in a Network (Bridges)']}
        ],
        'faqs': [
            {'q': 'How important are Amazon Leadership Principles during interviews?', 'a': 'Extremely important. Every interview round allocates 20–25 minutes specifically to evaluate past experiences using the STAR method against Amazon\'s 16 Leadership Principles.'},
            {'q': 'What is the Bar Raiser round at Amazon?', 'a': 'An interview conducted by an Amazonian outside the hiring team to ensure the candidate raises the bar of talent across the company.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Amazon SDE-1 Official Online Assessment Model 1',
                'total_qs': 2,
                'duration': '105 Mins',
                'sample_coding': 'Given packages with weights and warehouse vehicle capacities, find the minimum number of delivery trips required such that total package weight per trip does not exceed max capacity.',
                'sample_quant': 'Given critical server communication links in AWS data centers, find all bridge edges whose removal disconnects the server cluster using Tarjan\'s Bridge Finding algorithm.',
                'sample_tech': 'Explain how Amazon DynamoDB provides single-digit millisecond latency at any scale using consistent hashing and partition keys.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Amazon SDE Onsite Technical & System LLD Model 2',
                'total_qs': 2,
                'duration': '105 Mins',
                'sample_coding': 'Design an in-memory file system or locker delivery matching system adhering to clean OOP design principles with unit tests.',
                'sample_quant': 'Find the maximum profit possible from executing up to 2 parcel delivery route assignments with overlapping time windows.',
                'sample_tech': 'Describe how distributed locks with TTL in Redis / DynamoDB prevent double-booking of package lockers.'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Amazon University Hiring Solved Placement Paper Model 3',
                'total_qs': 2,
                'duration': '105 Mins',
                'sample_coding': 'Find the shortest path in a 2D warehouse maze with obstacles and multiple key-and-door dependencies using BFS with bitmask state.',
                'sample_quant': 'Calculate the expected package delivery delay when routing across M independent fulfillment centers.',
                'sample_tech': 'What is the difference between latency and throughput, and how does horizontal autoscaling address traffic surges in AWS ECS?'
            }
        ]
    },

    'google': {
        'canonical_name': 'Google',
        'total_mins': 90,
        'total_qs': 2,
        'roles': 'Software Engineer (L3 / Early Career)',
        'ctc': '₹32.0 - ₹55.0 LPA',
        'eligibility': 'B.S / M.S / Ph.D in CS/IT or STEM fields',
        'difficulty': 'Very Hard / Elite',
        'difficulty_class': 'badge-danger',
        'tagline': 'Google Software Engineer recruitment pattern, graph theory, dynamic programming & solved GOC papers.',
        'brand_color': '#4285f4',
        'accent_bg': 'linear-gradient(135deg, #4285f4 0%, #34a853 100%)',
        'logo_icon': '🌐',
        'logo_image': 'images/google.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Google Online Challenge (GOC)', 'desc': '2 Hard Algorithmic Problems | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Screen (Virtual)', 'desc': 'Live Coding & Complexity | 45 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'Onsite Technical 1 (DSA)', 'desc': 'Advanced Graph Algorithms | 45 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Onsite Technical 2 (DP/Trees)', 'desc': 'Optimization & Data Structures | 45 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Googleyness & Leadership', 'desc': 'Navigating Ambiguity & Culture | 45 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Google Online Challenge',
                'sections': [
                    {'name': 'Advanced Graph / Tree Problem', 'qs': '1 Q', 'time': '45 Mins'},
                    {'name': 'Hard Dynamic Programming / Math Problem', 'qs': '1 Q', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Technical Screen',
                'sections': [
                    {'name': 'Live CoderPad Problem Solving & Edge Cases', 'qs': '1–2 Qs', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Onsite Coding 1',
                'sections': [
                    {'name': 'Complex Graph Theory & Disjoint Sets', 'qs': '1 Q', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Onsite Coding 2',
                'sections': [
                    {'name': 'Dynamic Programming on Trees / Segment Trees', 'qs': '1 Q', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 5: Googleyness',
                'sections': [
                    {'name': 'Ethics, Collaboration & Open-Ended Scenarios', 'qs': 'Behavioral', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Advanced Graph Theory', 'icon': '🧠', 'qs': '45 Qs', 'time': '60 Mins', 'topics': ['Shortest Path (Dijkstra, Bellman-Ford, Floyd-Warshall)', 'Bipartite Graphs & Maximum Flow', 'Topological Sorting & SCC (Kosaraju, Tarjan)', 'Disjoint Set Union (DSU) with Path Compression']},
            {'category': 'Dynamic Programming & Math', 'icon': '💻', 'qs': '40 Qs', 'time': '60 Mins', 'topics': ['DP on Trees & Directed Acyclic Graphs', 'Bitmask DP & Digit DP', 'Matrix Exponentiation & Combinatorics', 'Game Theory (Minimax, Nim Sum)']},
            {'category': 'Complex Data Structures', 'icon': '⚡', 'qs': '35 Qs', 'time': '45 Mins', 'topics': ['Segment Trees with Lazy Propagation', 'Fenwick Tree (Binary Indexed Tree)', 'Trie with Suffix Structures', 'Monotonic Stacks and Deques']},
            {'category': 'Googleyness & Engineering Values', 'icon': '🎯', 'qs': '15 Qs', 'time': '45 Mins', 'topics': ['Thriving in Ambiguity', 'Constructive Feedback & Psychological Safety', 'Intellectual Humility & Bias for Good', 'Data-Driven Decision Making']}
        ],
        'faqs': [
            {'q': 'What does Google expect in live technical interviews?', 'a': 'Google assesses thought process, asking clarifying questions, analyzing time/space complexities upfront, writing bug-free modular code on Google Docs / CoderPad, and dry running with edge cases.'},
            {'q': 'What is Googleyness?', 'a': 'Googleyness assesses how you work collaboratively, respond to ambiguity, do the right thing ethically, and demonstrate intellectual humility.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Google Online Challenge (GOC) Model 1',
                'total_qs': 2,
                'duration': '90 Mins',
                'sample_coding': 'Given a tree of N nodes where each node has a value, find the maximum path sum between any two nodes such that the path contains at most K prime numbers.',
                'sample_quant': 'Given N points on a 2D plane, find the minimum perimeter triangle whose vertices are chosen from the given set of points.',
                'sample_tech': 'Explain how MapReduce processes massive datasets in parallel across clusters and handles node failures during execution.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Google SWE Onsite Coding & Complexity Model 2',
                'total_qs': 2,
                'duration': '90 Mins',
                'sample_coding': 'Implement a dynamic range maximum query data structure with point updates using a Segment Tree in O(log N) per operation.',
                'sample_quant': 'Find the number of ways to color an N-node undirected cycle graph using K distinct colors such that no two adjacent nodes have the same color.',
                'sample_tech': 'How does Google Spanner provide globally distributed ACID transactions with external consistency using TrueTime API?'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Google University Hiring Solved Paper Model 3',
                'total_qs': 2,
                'duration': '90 Mins',
                'sample_coding': 'Given a grid of characters, find the shortest path from start to finish that collects all keys to unlock corresponding doors using BFS with bitmask state.',
                'sample_quant': 'Determine the probability that a random walk on an infinite 2D grid returns to the origin within N steps.',
                'sample_tech': 'What are the trade-offs between gRPC protocol buffers and REST JSON for high-throughput microservice communication?'
            }
        ]
    },

    'microsoft': {
        'canonical_name': 'Microsoft',
        'total_mins': 90,
        'total_qs': 3,
        'roles': 'Software Engineer (L59 / L60)',
        'ctc': '₹26.0 - ₹44.0 LPA',
        'eligibility': 'B.Tech / M.Tech in CS/IT/ECE (7.0+ CGPA with no backlogs)',
        'difficulty': 'Hard',
        'difficulty_class': 'badge-danger',
        'tagline': 'Microsoft software engineering test pattern, binary trees, dynamic programming & solved past papers.',
        'brand_color': '#00a4ef',
        'accent_bg': 'linear-gradient(135deg, #00a4ef 0%, #0078d4 100%)',
        'logo_icon': '🪟',
        'logo_image': 'images/microsoft.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Codility Online Assessment', 'desc': '3 Coding Tasks | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Round 1 (DSA)', 'desc': 'Binary Trees, Linked Lists & Pointers | 60 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'Technical Round 2 (Algorithms)', 'desc': 'Graphs, DP & String Optimization | 60 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Technical Round 3 (LLD)', 'desc': 'Low-Level Design & Azure Basics | 60 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'As-Appropriate (AA) / Partner', 'desc': 'System Vision & Cultural Fitment | 45 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Codility OA',
                'sections': [
                    {'name': 'Array & String Manipulation Task', 'qs': '1 Q', 'time': '25 Mins'},
                    {'name': 'Binary Tree / Graph Task', 'qs': '1 Q', 'time': '35 Mins'},
                    {'name': 'Algorithm Optimization Task', 'qs': '1 Q', 'time': '30 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: DSA Technical 1',
                'sections': [
                    {'name': 'Binary Search Trees & Linked Lists', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: DSA Technical 2',
                'sections': [
                    {'name': 'Dynamic Programming & Graph Traversals', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: AA / Partner Round',
                'sections': [
                    {'name': 'Software Architecture & Microsoft Growth Mindset', 'qs': 'Behavioral', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Data Structures & Algorithms', 'icon': '🧠', 'qs': '45 Qs', 'time': '60 Mins', 'topics': ['Binary Trees (LCA, Serialization, Diameter)', 'Linked Lists (Reversal, Fast & Slow Pointers)', 'Graph BFS/DFS & Shortest Paths', 'Dynamic Programming Subsequences']},
            {'category': 'Object Oriented Design & LLD', 'icon': '💻', 'qs': '30 Qs', 'time': '45 Mins', 'topics': ['Design Patterns (Singleton, Factory, Observer)', 'Thread-Safe Class Implementation', 'SOLID Principles in C#/C++/Java', 'Exception Handling & Memory Management']},
            {'category': 'Operating Systems & Cloud Fundamentals', 'icon': '⚡', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['Threads, Processes & Critical Sections', 'Virtual Memory & Paging Algorithms', 'Azure Cloud Fundamentals (Blob, SQL, Functions)', 'Distributed Caching Principles']},
            {'category': 'Live Coding Assessment', 'icon': '🎯', 'qs': '3 Qs', 'time': '90 Mins', 'topics': ['Reverse Words in a String In-Place', 'Serialize and Deserialize a Binary Tree', 'Merge K Sorted Linked Lists', 'Word Ladder Graph BFS']}
        ],
        'faqs': [
            {'q': 'What platform does Microsoft use for campus and off-campus OA?', 'a': 'Microsoft primarily uses Codility. The tests place heavy emphasis on 100% test case pass rates and edge case handling.'},
            {'q': 'What is the AA (As-Appropriate) round at Microsoft?', 'a': 'The AA round is conducted by a senior leader/partner who has final veto authority and assesses cultural fit, growth mindset, and long-term potential.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Microsoft SWE Codility Benchmark Paper Model 1',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Given an array of strings representing version numbers, sort them in ascending semantic version order without using standard library sort.',
                'sample_quant': 'Find the lowest common ancestor of two nodes in a binary tree with parent pointers in O(H) time and O(1) extra space.',
                'sample_tech': 'Explain how the CLR (Common Language Runtime) in .NET manages memory and garbage collection across Generations 0, 1, and 2.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Microsoft SDE Onsite Technical Model 2',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Implement an algorithm to clone a complex linked list where each node contains an arbitrary random pointer.',
                'sample_quant': 'Given a directed graph of software build dependencies, find if a circular dependency exists and output a valid build order.',
                'sample_tech': 'Differentiate between process isolation and thread execution contexts in Windows NT kernel architecture.'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Microsoft University Recruitment Solved Paper Model 3',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Given an array of meeting time intervals with start and end times, find the minimum number of conference rooms required.',
                'sample_quant': 'Calculate the total number of unique BSTs that can be formed with values from 1 to N using Catalan numbers.',
                'sample_tech': 'What is Azure Cosmos DB and how does it provide tunable multi-model consistency levels (Strong, Bounded Staleness, Session, Eventual)?'
            }
        ]
    },

    'meta': {
        'canonical_name': 'Meta',
        'total_mins': 70,
        'total_qs': 4,
        'roles': 'Software Engineer (E3 / Rotational Software Engineer)',
        'ctc': '₹35.0 - ₹60.0 LPA',
        'eligibility': 'B.E / B.Tech / M.Tech in CS/IT/ECE',
        'difficulty': 'Hard / Speed Tier',
        'difficulty_class': 'badge-danger',
        'tagline': 'Meta software engineer assessment pattern, rapid coding, graph algorithms & solved past papers.',
        'brand_color': '#0668e1',
        'accent_bg': 'linear-gradient(135deg, #0668e1 0%, #004ac1 100%)',
        'logo_icon': '♾️',
        'logo_image': 'images/meta.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Automated Coding Screen', 'desc': 'CodeSignal Framework | 4 Questions | 70 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Live Technical Screen', 'desc': '2 DSA Problems on CoderPad | 45 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'Onsite Coding Round 1', 'desc': '2 Graph/Tree Problems | 45 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Onsite Coding Round 2', 'desc': '2 DP/Optimization Problems | 45 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Behavioral & Core Values', 'desc': 'Move Fast & Build Social Value | 45 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: CodeSignal Screen',
                'sections': [
                    {'name': 'Array & String Manipulation', 'qs': '1 Q', 'time': '15 Mins'},
                    {'name': 'Matrix & Simulation Logic', 'qs': '1 Q', 'time': '15 Mins'},
                    {'name': 'Sliding Window & Hash Logic', 'qs': '1 Q', 'time': '20 Mins'},
                    {'name': 'Hard Graph / Tree Optimization', 'qs': '1 Q', 'time': '20 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Technical Screen',
                'sections': [
                    {'name': 'Live CoderPad Coding with Clean Syntax', 'qs': '2 Qs', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Onsite Coding 1',
                'sections': [
                    {'name': 'Graphs, Connected Components & BSTs', 'qs': '2 Qs', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Behavioral',
                'sections': [
                    {'name': 'Meta Values (Move Fast, Focus on Long-Term Impact)', 'qs': 'Behavioral', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Data Structures & Speed Coding', 'icon': '🧠', 'qs': '45 Qs', 'time': '60 Mins', 'topics': ['Arrays & Two Pointers Speed Execution', 'Graph BFS/DFS & Shortest Path', 'Binary Tree Vertical & Level Order Views', 'Sliding Window Maximum & Minimum']},
            {'category': 'Dynamic Programming & Strings', 'icon': '💻', 'qs': '35 Qs', 'time': '45 Mins', 'topics': ['Regular Expression Matching Logic', 'Word Break & Edit Distance DP', 'Palindrome Partitioning', 'Trie Autocomplete']},
            {'category': 'CS Fundamentals & Architecture', 'icon': '⚡', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['Graph Database Concepts (TAO Architecture)', 'Distributed Feed Generation & Fanout', 'Memcached & Redis Caching', 'OS Concurrency & Threads']},
            {'category': 'Live Coding Assessment', 'icon': '🎯', 'qs': '2 Qs', 'time': '45 Mins', 'topics': ['Binary Tree Right Side View', 'Accounts Merge (Disjoint Sets)', 'Subarray Sum Equals K', 'Alien Dictionary Topological Sort']}
        ],
        'faqs': [
            {'q': 'Why is Meta coding interview famous for speed?', 'a': 'Meta expects candidates to solve 2 distinct LeetCode Medium/Hard algorithmic problems within a single 45-minute interview round, requiring fast coding and flawless syntax.'},
            {'q': 'Does Meta allow syntax lookup during interviews?', 'a': 'No, candidates code live on a plain text editor / CoderPad without autocomplete.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Meta Software Engineer OA Model 1',
                'total_qs': 4,
                'duration': '70 Mins',
                'sample_coding': 'Given an array of user accounts with email lists, merge accounts belonging to the same user using Disjoint Set Union (DSU) in O(N log N).',
                'sample_quant': 'Given a binary tree, return the vertical order traversal of its nodes values from top to bottom and left to right.',
                'sample_tech': 'Explain Meta TAO (The Associations and Objects) distributed graph datastore used to serve the social graph with low latency.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Meta SWE Technical Onsite Model 2',
                'total_qs': 4,
                'duration': '70 Mins',
                'sample_coding': 'Given a dictionary of words from an alien language, derive the alphabetical ordering of characters using Topological Sort.',
                'sample_quant': 'Find the maximum sum of a non-empty contiguous subarray containing at most one deleted element.',
                'sample_tech': 'How does news feed generation handle read-heavy fanout vs write-heavy celebrity account updates?'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Meta University Hiring Solved Paper Model 3',
                'total_qs': 4,
                'duration': '70 Mins',
                'sample_coding': 'Find the shortest path in a binary matrix from top-left to bottom-right avoiding obstacles using 8-directional BFS.',
                'sample_quant': 'Compute the total number of continuous subarrays whose sum equals an integer K using a hash map in O(N) time.',
                'sample_tech': 'Describe how distributed caching with Memcached mitigates database thundering herd problems at social media scale.'
            }
        ]
    },

    'netflix': {
        'canonical_name': 'Netflix',
        'total_mins': 120,
        'total_qs': 3,
        'roles': 'Software Engineer (L4/L5) & Platform Infrastructure Engineer',
        'ctc': '₹35.0 - ₹65.0 LPA',
        'eligibility': 'B.E / B.Tech / M.Tech with strong high-scale systems portfolio',
        'difficulty': 'Very Hard / Elite',
        'difficulty_class': 'badge-danger',
        'tagline': 'Netflix software engineering placement pattern, distributed streaming, concurrency & solved past papers.',
        'brand_color': '#e50914',
        'accent_bg': 'linear-gradient(135deg, #e50914 0%, #b81d24 100%)',
        'logo_icon': '🎬',
        'logo_image': 'images/netflix.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Online Technical Assessment', 'desc': '3 Advanced Systems/DSA Problems | 120 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Concurrency & Sockets Deep Dive', 'desc': 'Asynchronous I/O & Microservices | 60 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'High Scale Microservices (LLD)', 'desc': 'Fault Tolerance & Resilience (Hystrix) | 60 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Distributed Streaming Architecture', 'desc': 'CDN, Video Encoding & Open Connect | 60 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Netflix Culture Memo Fitment', 'desc': 'Freedom & Responsibility / Context Over Control | 45 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment',
                'sections': [
                    {'name': 'Algorithmic Problem Solving', 'qs': '2 Qs', 'time': '60 Mins'},
                    {'name': 'Distributed Systems Coding', 'qs': '1 Q', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Concurrency & Sockets',
                'sections': [
                    {'name': 'Async Event Loop & Thread Pools', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Distributed Architecture',
                'sections': [
                    {'name': 'Global Video Streaming & Caching Hierarchy', 'qs': '1 Design', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Culture Memo',
                'sections': [
                    {'name': 'Freedom & Responsibility / High Performance Fit', 'qs': 'Behavioral', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Concurrency & Systems Programming', 'icon': '🧠', 'qs': '40 Qs', 'time': '60 Mins', 'topics': ['Non-Blocking I/O (Netty, Epoll)', 'Thread-Safe Memory Models & Mutexes', 'gRPC & HTTP/2 Multiplexing', 'Actor Models & Reactive Streams']},
            {'category': 'Distributed Streaming Architecture', 'icon': '💻', 'qs': '35 Qs', 'time': '45 Mins', 'topics': ['Open Connect Custom CDN Architecture', 'Dynamic Video Bitrate Adaptation (ABR)', 'Chaos Engineering (Chaos Monkey)', 'Cassandra & EVCache Sharding']},
            {'category': 'Data Structures & Algorithms', 'icon': '⚡', 'qs': '35 Qs', 'time': '45 Mins', 'topics': ['Graph Shortest Path & Flow Networks', 'LRU/LFU Tiered Caching Implementation', 'Dynamic Programming Subsets', 'Segment Trees & Fenwick Trees']},
            {'category': 'Netflix Culture & Leadership', 'icon': '🎯', 'qs': '15 Qs', 'time': '45 Mins', 'topics': ['Context Over Control', 'Highly Aligned, Loosely Coupled', 'Stunning Colleagues & High Performance', 'Freedom and Responsibility']}
        ],
        'faqs': [
            {'q': 'What is unique about the Netflix engineering hiring process?', 'a': 'Netflix places extraordinary weight on culture alignment with its famous Culture Memo (Freedom & Responsibility) and tests high-scale distributed systems knowledge.'},
            {'q': 'Does Netflix offer equity or all-cash compensation?', 'a': 'Netflix offers top-of-market compensation where candidates can choose their own customized split between all-cash salary and stock options.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Netflix Platform Software Engineer OA Model 1',
                'total_qs': 3,
                'duration': '120 Mins',
                'sample_coding': 'Design a tiered multi-level caching system (L1 memory, L2 SSD, L3 remote cluster) with adaptive write-through and eviction policies.',
                'sample_quant': 'Given user playback bitrate logs over time, compute the maximum continuous smooth playback buffer duration using sliding window dynamic programming.',
                'sample_tech': 'Explain how Netflix Open Connect CDN appliances cache video chunks at ISP networks to eliminate international backbone traffic.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Netflix Systems & Concurrency Technical Model 2',
                'total_qs': 3,
                'duration': '120 Mins',
                'sample_coding': 'Implement a thread-safe distributed rate limiter and circuit breaker that trips when error rates exceed 5% over 10 seconds.',
                'sample_quant': 'Find the minimum bandwidth required to stream N video segments across M network links without packet loss.',
                'sample_tech': 'Describe how Chaos Engineering (Chaos Monkey) tests resilience by randomly terminating production microservice instances.'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Netflix University Graduate Solved Paper Model 3',
                'total_qs': 3,
                'duration': '120 Mins',
                'sample_coding': 'Given a directed graph of video microservice dependencies, find all critical single-points-of-failure using Tarjan\'s articulation points.',
                'sample_quant': 'Calculate the expected server failover time in a distributed quorum consensus system using Raft algorithm.',
                'sample_tech': 'What are the architectural benefits of Cassandra for high-write viewing history telemetry compared to traditional MySQL?'
            }
        ]
    },

    'apple': {
        'canonical_name': 'Apple',
        'total_mins': 90,
        'total_qs': 25,
        'roles': 'Software Engineer / Core OS & iOS Frameworks Engineer',
        'ctc': '₹28.0 - ₹48.0 LPA',
        'eligibility': 'B.Tech / M.Tech in CS/IT/ECE (7.0+ CGPA with no backlogs)',
        'difficulty': 'Hard / Systems Tier',
        'difficulty_class': 'badge-danger',
        'tagline': 'Apple software engineering placement pattern, Swift/C++ internals, memory optimization & solved past papers.',
        'brand_color': '#a3aaae',
        'accent_bg': 'linear-gradient(135deg, #2d3748 0%, #1a202c 100%)',
        'logo_icon': '🍎',
        'logo_image': 'images/apple.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Online Technical Assessment', 'desc': '22 CS Core MCQs + 3 Coding Qs | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Interview 1 (DSA)', 'desc': 'Data Structures & Algorithms | 60 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'Technical Interview 2 (OS/Memory)', 'desc': 'Memory Optimization & Concurrency | 60 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Technical Interview 3 (Craftsmanship)', 'desc': 'Clean Code & Framework Design | 60 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Hiring Manager & Culture', 'desc': 'Passion for Products & Apple Culture | 45 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment',
                'sections': [
                    {'name': 'CS Core MCQs (Memory, OS, OOP, C/C++)', 'qs': '22 Qs', 'time': '30 Mins'},
                    {'name': 'Algorithmic Coding Challenge', 'qs': '3 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Technical Interview 1',
                'sections': [
                    {'name': 'Binary Trees, Graphs & Recursion', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: OS & Memory',
                'sections': [
                    {'name': 'Pointers, ARC Memory Management & Threads', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Managerial',
                'sections': [
                    {'name': 'Apple Design Philosophy & Innovation Mindset', 'qs': 'Behavioral', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Data Structures & Algorithms', 'icon': '🧠', 'qs': '40 Qs', 'time': '50 Mins', 'topics': ['Trees & BST Traversals', 'Graph BFS/DFS & Topo Sort', 'Linked List Cycle Detection & Reversals', 'Dynamic Programming on Strings']},
            {'category': 'Systems & Memory Optimization', 'icon': '💻', 'qs': '35 Qs', 'time': '40 Mins', 'topics': ['Automatic Reference Counting (ARC)', 'Memory Leaks & Retain Cycles', 'Grand Central Dispatch (GCD) & Concurrency', 'Virtual Memory & Cache Coherence']},
            {'category': 'C/C++ & Swift Fundamentals', 'icon': '⚡', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['Pointer Arithmetic & Struct Layout', 'Virtual Tables & Protocol Witnesses', 'Bitwise Manipulation', 'Exception Safety & RAII']},
            {'category': 'Live Coding Assessment', 'icon': '🎯', 'qs': '3 Qs', 'time': '60 Mins', 'topics': ['Top-K Frequent App Events', 'Thread-Safe LFU Cache', 'Autocomplete Trie with Wildcards', 'In-Memory Key-Value Store']}
        ],
        'faqs': [
            {'q': 'What does Apple look for in software engineering candidates?', 'a': 'Deep understanding of memory management, meticulous attention to detail, robust unit testing, clean API design, and a strong passion for user experience.'},
            {'q': 'Is knowledge of Swift or Objective-C mandatory for freshers?', 'a': 'No, strong proficiency in C++, Java, or Python is completely acceptable for general software roles.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Apple Software Engineer OA Model 1',
                'total_qs': 25,
                'duration': '90 Mins',
                'sample_coding': 'Given a stream of app event logs with timestamps, find the top-K most frequent events in O(N log K) time using a min-heap.',
                'sample_quant': 'Analyze the time and space complexity of a recursive algorithm for generating all subsets of a set.',
                'sample_tech': 'Explain how Swift\'s Automatic Reference Counting (ARC) handles weak and unowned references to prevent retain cycles.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Apple Onsite Technical & Systems Model 2',
                'total_qs': 25,
                'duration': '90 Mins',
                'sample_coding': 'Implement an LFU (Least Frequently Used) Cache with O(1) average time complexity for both get and put operations.',
                'sample_quant': 'Given a continuous stream of integer metrics, calculate the running median after each insertion using two heaps.',
                'sample_tech': 'Describe Grand Central Dispatch (GCD) in Apple platforms and compare concurrent queues with serial dispatch queues.'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Apple University Graduate Solved Paper Model 3',
                'total_qs': 25,
                'duration': '90 Mins',
                'sample_coding': 'Design a thread-safe, memory-efficient trie data structure supporting autocomplete search with wildcard queries.',
                'sample_quant': 'Find the minimum number of operations to convert one binary string to another using dynamic programming.',
                'sample_tech': 'What is Metal graphics API and how does it provide low-overhead GPU acceleration on Apple silicon?'
            }
        ]
    },

    'oracle': {
        'canonical_name': 'Oracle',
        'total_mins': 105,
        'total_qs': 47,
        'roles': 'Associate Software Engineer (Server Technology / Oracle Cloud Infrastructure - OCI)',
        'ctc': '₹16.0 - ₹28.0 LPA',
        'eligibility': '60% or 6.5 CGPA in B.E/B.Tech/MCA with no backlogs',
        'difficulty': 'Hard',
        'difficulty_class': 'badge-danger',
        'tagline': 'Oracle recruitment exam pattern, database internals, SQL optimization & solved placement papers.',
        'brand_color': '#f80000',
        'accent_bg': 'linear-gradient(135deg, #f80000 0%, #c00000 100%)',
        'logo_icon': '🔴',
        'logo_image': 'images/oracle.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Oracle Online Assessment', 'desc': '45 CS MCQs + 2 Coding Qs | 105 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Interview 1 (DSA)', 'desc': 'Trees, Graphs & Dynamic Programming | 60 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'Technical Interview 2 (DB/SQL)', 'desc': 'B+ Trees, Transactions & Indexing | 60 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Technical Interview 3 (OOP/Cloud)', 'desc': 'Java Concurrency & OCI Architecture | 45 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'HR Interview', 'desc': 'Communication & General Behavioral | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment',
                'sections': [
                    {'name': 'CS Core MCQs (DBMS, OS, Networks, Java)', 'qs': '45 Qs', 'time': '45 Mins'},
                    {'name': 'Data Structures Coding Challenge', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: DSA Interview',
                'sections': [
                    {'name': 'Binary Search Trees & Graph Algorithms', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Database & OS',
                'sections': [
                    {'name': 'SQL Query Optimization, B+ Tree Indexes & Locks', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: HR Round',
                'sections': [
                    {'name': 'Behavioral Fitment & Relocation Flexibility', 'qs': 'Behavioral', 'time': '30 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Database Management & SQL', 'icon': '🧠', 'qs': '40 Qs', 'time': '45 Mins', 'topics': ['B+ Tree Indexing Mechanisms', 'ACID Transactions & Two-Phase Locking', 'Database Normalization (1NF to BCNF)', 'Query Execution Plans & Hash Joins']},
            {'category': 'Data Structures & Algorithms', 'icon': '💻', 'qs': '35 Qs', 'time': '45 Mins', 'topics': ['Trees & BST (LCA, Views, Balancing)', 'Graph BFS/DFS & Dijkstra', 'Dynamic Programming on Arrays', 'Hash Tables & Collision Resolution']},
            {'category': 'Operating Systems & Java/C++', 'icon': '⚡', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['Virtual Memory, Paging & Segment Tables', 'Threads, Mutexes & Reader-Writer Locks', 'Java Memory Model & Garbage Collection', 'OOP Principles & Design Patterns']},
            {'category': 'Coding Assessment', 'icon': '🎯', 'qs': '2 Qs', 'time': '60 Mins', 'topics': ['Subarray Product Less Than K', 'Binary Tree Maximum Path Sum', 'Database Log Transaction Replayer', 'Optimal Resource Allocation Grid']}
        ],
        'faqs': [
            {'q': 'How heavily is DBMS tested in Oracle technical interviews?', 'a': 'Very heavily. Candidates are expected to know database storage engines, transaction isolation levels, indexing (B+ Trees, Bitmap), and write optimized SQL queries.'},
            {'q': 'What is the structure of the Oracle Online Assessment?', 'a': 'A 105-minute test with 45 technical MCQs covering OS, DBMS, Networks, and Java/C++, plus 2 Coding questions.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Oracle Server Technology OA Model 1',
                'total_qs': 47,
                'duration': '105 Mins',
                'sample_coding': 'Given an array of integer database transaction IDs and a target lock timeout, find all contiguous subsegments where total transaction cost is less than K.',
                'sample_quant': 'Calculate the maximum number of simultaneous transactions supported without exceeding buffer cache threshold.',
                'sample_tech': 'Explain how Oracle database handles Write-Ahead Logging (WAL) using Redo Logs to ensure durability across system crashes.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Oracle OCI Technical Interview Model 2',
                'total_qs': 47,
                'duration': '105 Mins',
                'sample_coding': 'Given a binary tree, write an algorithm to return the maximum path sum between any two nodes in O(N) time.',
                'sample_quant': 'Determine the minimum number of table partition shards required to distribute N user records uniformly using hash partitioning.',
                'sample_tech': 'Differentiate between clustered and secondary B+ Tree indexes, explaining why leaf nodes are doubly linked.'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Oracle University Recruitment Solved Paper Model 3',
                'total_qs': 47,
                'duration': '105 Mins',
                'sample_coding': 'Implement an algorithm that reorders database query tasks based on precedence constraints using Kahn\'s topological sort algorithm.',
                'sample_quant': 'Find the total number of distinct BSTs that can be formed from N distinct keys.',
                'sample_tech': 'Explain Multi-Version Concurrency Control (MVCC) and how undo tablespaces support consistent read views.'
            }
        ]
    },

    'adobe': {
        'canonical_name': 'Adobe',
        'total_mins': 120,
        'total_qs': 18,
        'roles': 'Member of Technical Staff (MTS-1) / Software Engineer',
        'ctc': '₹24.0 - ₹40.0 LPA',
        'eligibility': 'B.E / B.Tech / M.Tech in CS/IT/ECE (7.0+ CGPA with no active backlogs)',
        'difficulty': 'Hard / Product Tier',
        'difficulty_class': 'badge-danger',
        'tagline': 'Adobe MTS placement pattern, computer graphics, advanced algorithms & solved past papers.',
        'brand_color': '#ff0000',
        'accent_bg': 'linear-gradient(135deg, #ff0000 0%, #cc0000 100%)',
        'logo_icon': '🎨',
        'logo_image': 'images/adobe.svg',
        'selection_stages': [
            {'step': 1, 'title': 'HackerRank Online Assessment', 'desc': '15 Quant/Cognitive MCQs + 3 Coding Qs | 120 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Interview 1 (DSA)', 'desc': 'Complex Trees, Graphs & DP | 60 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'Technical Interview 2 (Math & OOP)', 'desc': 'Mathematical Algorithms & Design | 60 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Technical Interview 3 (Graphics/System)', 'desc': 'Media Processing & C++ Internals | 60 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Director / HR Interview', 'desc': 'Creativity, Culture & Behavioral Fit | 45 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: HackerRank OA',
                'sections': [
                    {'name': 'Quantitative & Cognitive MCQs', 'qs': '15 Qs', 'time': '30 Mins'},
                    {'name': 'Algorithmic Coding Challenge', 'qs': '3 Qs', 'time': '90 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: DSA Technical 1',
                'sections': [
                    {'name': 'Binary Trees, Graphs & Dynamic Programming', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Math & Systems',
                'sections': [
                    {'name': 'Geometry / Math Algorithms, C++ Internals & OOP', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Director Round',
                'sections': [
                    {'name': 'Adobe Core Values, Innovation & Projects', 'qs': 'Behavioral', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Data Structures & Algorithms', 'icon': '🧠', 'qs': '45 Qs', 'time': '60 Mins', 'topics': ['Binary Trees & Lowest Common Ancestor', 'Graph Shortest Paths & Minimum Spanning Trees', 'Dynamic Programming on 2D Grids', 'Trie & String Pattern Matching (KMP)']},
            {'category': 'Mathematical & Geometry Algorithms', 'icon': '💻', 'qs': '30 Qs', 'time': '40 Mins', 'topics': ['Convex Hull & Line Intersection', 'Matrix Transformations & 2D Rotation', 'Combinatorics & Number Theory', 'Bit Manipulation & Bitmasks']},
            {'category': 'Object Oriented & Systems C++', 'icon': '⚡', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['C++ Virtual Tables & Memory Management', 'Smart Pointers & RAII Idioms', 'Design Patterns (Strategy, Composite)', 'Multithreading & Thread Pools']},
            {'category': 'Live Coding Assessment', 'icon': '🎯', 'qs': '3 Qs', 'time': '90 Mins', 'topics': ['2D Image Layer Rasterization', 'PDF Document Text Flow Parser', 'Word Search in 2D Character Board', 'Longest Arithmetic Subsequence']}
        ],
        'faqs': [
            {'q': 'What distinguishes Adobe technical interviews from others?', 'a': 'Adobe emphasizes mathematical problem solving, computational geometry (2D points, lines, polygons), dynamic programming, and clean C++/Java OOP design.'},
            {'q': 'What is the format of the Adobe HackerRank OA?', 'a': 'A 120-minute test consisting of 15 high-level quantitative & aptitude MCQs followed by 3 medium/hard coding problems.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Adobe Member of Technical Staff OA Model 1',
                'total_qs': 18,
                'duration': '120 Mins',
                'sample_coding': 'Given a 2D matrix representing digital canvas pixels, implement the flood fill algorithm supporting diagonal pixel connectivity and color thresholding.',
                'sample_quant': 'Find the minimum area rectangle formed by a set of N points on a 2D Cartesian plane with sides parallel to coordinate axes.',
                'sample_tech': 'Explain how C++ smart pointers (std::unique_ptr, std::shared_ptr) prevent memory leaks in large media editing applications.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Adobe MTS Technical Onsite Model 2',
                'total_qs': 18,
                'duration': '120 Mins',
                'sample_coding': 'Given a 2D board of characters and a list of dictionary words, find all words present on the board using a Trie and Backtracking.',
                'sample_quant': 'Calculate the maximum number of collinear points among a given set of N 2D points in O(N^2) time using slope hash maps.',
                'sample_tech': 'What is the Composite design pattern and how is it used to model nested document shapes and grouping in Adobe Illustrator?'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Adobe University Campus Solved Paper Model 3',
                'total_qs': 18,
                'duration': '120 Mins',
                'sample_coding': 'Find the length of the longest arithmetic subsequence in a given integer array using dynamic programming in O(N^2) time.',
                'sample_quant': 'Determine the probability that three randomly chosen points on a circle form an acute-angled triangle.',
                'sample_tech': 'Explain how image compression algorithms (like JPEG DCT or PNG DEFLATE) achieve high compression ratios while preserving visual fidelity.'
            }
        ]
    }
}
