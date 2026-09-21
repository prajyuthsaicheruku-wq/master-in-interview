# -*- coding: utf-8 -*-
STARTUP_COMPANIES = {
    'razorpay': {
        'canonical_name': 'Razorpay',
        'total_mins': 90,
        'total_qs': 3,
        'roles': 'Software Development Engineer (SDE-1 / Platform & Payments)',
        'ctc': '₹22.0 - ₹32.0 LPA',
        'eligibility': 'B.Tech / M.Tech in CS/IT or top competitive programming rating',
        'difficulty': 'Hard',
        'difficulty_class': 'badge-danger',
        'tagline': 'Razorpay SDE placement pattern, payment systems, machine coding LLD & solved OA papers.',
        'brand_color': '#0c2340',
        'accent_bg': 'linear-gradient(135deg, #0c2340 0%, #1e3a8a 100%)',
        'logo_icon': '⚡',
        'logo_image': 'images/razorpay.svg',
        'selection_stages': [
            {'step': 1, 'title': 'HackerRank Online Assessment', 'desc': '3 Hard Algorithmic Problems | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Machine Coding Round (LLD)', 'desc': 'Live Executable Class Design (e.g. Splitwise/Wallet) | 90 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'Problem Solving & DSA', 'desc': 'Complex Dynamic Programming & Graphs | 60 Mins', 'icon': '🧠'},
            {'step': 4, 'title': 'Core Systems & Concurrency', 'desc': 'Database Locking, Redis Caching & Golang/Java | 60 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Founders & Culture Round', 'desc': 'First-Principles Thinking & Razorpay Culture | 45 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment',
                'sections': [
                    {'name': 'Array / Bitmask Optimization', 'qs': '1 Q', 'time': '30 Mins'},
                    {'name': 'Graph / Tree Shortest Path', 'qs': '1 Q', 'time': '30 Mins'},
                    {'name': 'Hard Dynamic Programming', 'qs': '1 Q', 'time': '30 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Machine Coding',
                'sections': [
                    {'name': 'Payment Gateway / Splitwise Class Design with Unit Tests', 'qs': '1 System', 'time': '90 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: DSA Round',
                'sections': [
                    {'name': 'Graphs, Sliding Window & Binary Search on Answer', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Culture & Fitment',
                'sections': [
                    {'name': 'Razorpay 6 Cultural Pillars & Past Projects', 'qs': 'Behavioral', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Data Structures & Algorithms', 'icon': '🧠', 'qs': '40 Qs', 'time': '50 Mins', 'topics': ['Graph Shortest Path & Bipartite Graphs', 'Bitmask & State Dynamic Programming', 'Segment Trees with Range Updates', 'Monotonic Stack & Queue']},
            {'category': 'Machine Coding & LLD', 'icon': '💻', 'qs': '30 Qs', 'time': '45 Mins', 'topics': ['Payment Gateway Multi-Bank Routing Design', 'Digital Wallet Ledger with Transaction History', 'Design Patterns (Strategy, State, Observer)', 'Thread-Safe Memory Operations']},
            {'category': 'Databases & Distributed Systems', 'icon': '⚡', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['MySQL Row Locking & Read Committed Isolation', 'Redis Distributed Locks (Redlock)', 'Idempotency in REST APIs', 'Kafka Event Streaming Architecture']},
            {'category': 'Coding Assessment', 'icon': '🎯', 'qs': '3 Qs', 'time': '90 Mins', 'topics': ['Transaction Idempotency Filter', 'Currency Conversion Arbitrage Cycle', 'Optimal Merchant Fee Calculator', 'Stream Top-K Active Merchants']}
        ],
        'faqs': [
            {'q': 'What is the Machine Coding round at Razorpay?', 'a': 'A 90-minute live coding round where candidates must write clean, modular, object-oriented code implementing a complete system (e.g. Expense Sharing, Payment Gateway Routing) with test cases.'},
            {'q': 'Does Razorpay ask about idempotency and concurrency?', 'a': 'Yes, in fintech, understanding idempotency keys, duplicate payment prevention, and database row locks is heavily tested.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Razorpay SDE-1 OA Model 1',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Design an idempotent payment processing queue that discards duplicate webhook transactions arriving within a 5-minute sliding window.',
                'sample_quant': 'Given merchant daily settlement amounts, find the minimum number of currency transfers to settle all merchant bank balances.',
                'sample_tech': 'Explain how idempotency keys guarantee that a network retry does not charge a customer card twice.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Razorpay Machine Coding & LLD Model 2',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Implement a thread-safe digital wallet system with addMoney, transferMoney, and getTransactionHistory with clean OOP classes.',
                'sample_quant': 'Find the longest continuous transaction subsegment with alternating credit and debit values in O(N) time.',
                'sample_tech': 'Describe how distributed locks in Redis (Redlock) ensure single-worker execution during automated batch payouts.'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Razorpay University Hiring Solved Paper Model 3',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Find the shortest path in a payment routing network where certain bank gateways experience dynamic latency penalties.',
                'sample_quant': 'Calculate the minimum number of refund batches needed to disburse customer cashback without exceeding daily bank limits.',
                'sample_tech': 'What is the difference between synchronous HTTP calls and asynchronous Kafka messaging in event-driven financial systems?'
            }
        ]
    },

    'phonepe': {
        'canonical_name': 'PhonePe',
        'total_mins': 90,
        'total_qs': 3,
        'roles': 'Software Engineer (SDE-1 / Backend & Infrastructure)',
        'ctc': '₹24.0 - ₹36.0 LPA',
        'eligibility': 'B.Tech / M.Tech in CS/IT/ECE with strong problem solving skills',
        'difficulty': 'Hard',
        'difficulty_class': 'badge-danger',
        'tagline': 'PhonePe SDE recruitment pattern, UPI architecture, machine coding & solved test papers.',
        'brand_color': '#5f259f',
        'accent_bg': 'linear-gradient(135deg, #5f259f 0%, #3b1464 100%)',
        'logo_icon': '📱',
        'logo_image': 'images/phonepe.svg',
        'selection_stages': [
            {'step': 1, 'title': 'HackerEarth Online Assessment', 'desc': '3 Hard Algorithmic Problems | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Machine Coding Round (LLD)', 'desc': '2.5 Hours Complete Executable Design | 150 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'Data Structures & Algorithms', 'desc': 'Trees, Graphs, DP & Heaps | 60 Mins', 'icon': '🧠'},
            {'step': 4, 'title': 'Systems & DB Concurrency', 'desc': 'MySQL Locking, Redis, Kafka & Threads | 60 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Hiring Manager & Culture', 'desc': 'Engineering Values & High Ownership | 45 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment',
                'sections': [
                    {'name': 'Graph Shortest Path Problem', 'qs': '1 Q', 'time': '30 Mins'},
                    {'name': 'Dynamic Programming on Trees', 'qs': '1 Q', 'time': '30 Mins'},
                    {'name': 'Segment Tree / Range Query Problem', 'qs': '1 Q', 'time': '30 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Machine Coding',
                'sections': [
                    {'name': 'PhonePe UPI QR / Bill Payment Engine (Clean OOP Design)', 'qs': '1 System', 'time': '150 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: DSA Round',
                'sections': [
                    {'name': 'Advanced Problem Solving & Edge Cases', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Managerial',
                'sections': [
                    {'name': 'System Ownership, Scale Scenarios & Culture', 'qs': 'Behavioral', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Data Structures & Algorithms', 'icon': '🧠', 'qs': '45 Qs', 'time': '60 Mins', 'topics': ['Segment Tree & Binary Indexed Tree', 'Graph Shortest Path & Min Cut', 'Dynamic Programming Bitmask', 'Trie & Aho-Corasick']},
            {'category': 'Machine Coding & OOP Architecture', 'icon': '💻', 'qs': '30 Qs', 'time': '45 Mins', 'topics': ['UPI Payment Routing LLD', 'Parking Lot / Flash Sale Queue Design', 'Design Patterns (Factory, Strategy, Chain of Responsibility)', 'Thread Safety & Mutex Locks in Java']},
            {'category': 'Distributed Systems & Databases', 'icon': '⚡', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['HBase & Cassandra Architecture', 'MySQL InnoDB Clustered Indexing', 'Distributed Transaction Sagas', 'Kafka Partition Rebalancing']},
            {'category': 'Live Coding Assessment', 'icon': '🎯', 'qs': '3 Qs', 'time': '90 Mins', 'topics': ['High TPS UPI Switch Routing', 'Transaction Rollback Recovery Engine', 'Merchant Settlement Batch Aggregator', 'Fraudulent Velocity Check Window']}
        ],
        'faqs': [
            {'q': 'How rigorous is the PhonePe Machine Coding round?', 'a': 'Very rigorous. Candidates get 2.5 hours to implement a complete object-oriented system from scratch (e.g. In-memory SQL DB, UPI Router) that compiles, passes all test cases, and follows clean coding principles.'},
            {'q': 'What tech stack does PhonePe emphasize in interviews?', 'a': 'Java, Spring Boot, MySQL, HBase, Aerospike, Kafka, and distributed system architectures.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'PhonePe SDE-1 HackerEarth OA Model 1',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Given an array of UPI transaction timestamps and amounts, find the maximum transaction surge rate over any continuous window of length W.',
                'sample_quant': 'Given a directed graph of server payment rails, find the maximum independent set of non-interfering settlement transactions.',
                'sample_tech': 'Explain how Aerospike / Redis in-memory databases achieve sub-millisecond read/write latency during peak IPL traffic surges.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'PhonePe Machine Coding & LLD Model 2',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Implement an in-memory Key-Value store with transactions (BEGIN, COMMIT, ROLLBACK) and nested transaction support.',
                'sample_quant': 'Find the shortest path in an unweighted grid with teleporters using Breadth First Search.',
                'sample_tech': 'Describe how database isolation levels (Repeatable Read vs Serializable) prevent phantom read anomalies during concurrent bank transfers.'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'PhonePe University Recruitment Solved Paper Model 3',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Given an array of integers, find the number of subarrays whose XOR sum is equal to a given value K in O(N) time.',
                'sample_quant': 'Compute the probability that a distributed payment transaction successfully commits across 3 independent banking microservices.',
                'sample_tech': 'What is the Saga pattern in microservices, and how does compensating transaction logic handle distributed payment rollbacks?'
            }
        ]
    },

    'flipkart': {
        'canonical_name': 'Flipkart',
        'total_mins': 90,
        'total_qs': 3,
        'roles': 'Software Development Engineer (SDE-1)',
        'ctc': '₹22.0 - ₹32.0 LPA',
        'eligibility': 'B.E / B.Tech in CS/IT/ECE (7.0+ CGPA with no backlogs)',
        'difficulty': 'Hard',
        'difficulty_class': 'badge-danger',
        'tagline': 'Flipkart SDE recruitment pattern, machine coding, algorithmic optimization & solved placement papers.',
        'brand_color': '#2874f0',
        'accent_bg': 'linear-gradient(135deg, #2874f0 0%, #1e40af 100%)',
        'logo_icon': '🛍️',
        'logo_image': 'images/flipkart.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Online Coding Assessment (HackerRank)', 'desc': '3 Algorithmic Problems | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Machine Coding Round (LLD)', 'desc': '2.5 Hours Complete Executable OOP Design | 150 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'Problem Solving & DSA', 'desc': 'Complex Dynamic Programming & Trees | 60 Mins', 'icon': '🧠'},
            {'step': 4, 'title': 'Architecture & CS Core', 'desc': 'Databases, Multithreading & High Scale | 60 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Hiring Manager Round', 'desc': 'Problem Solving Approach & Culture Fit | 45 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment',
                'sections': [
                    {'name': 'Array / String Optimization', 'qs': '1 Q', 'time': '25 Mins'},
                    {'name': 'Dynamic Programming / Graph', 'qs': '1 Q', 'time': '35 Mins'},
                    {'name': 'Segment Tree / Advanced DSA', 'qs': '1 Q', 'time': '30 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Machine Coding',
                'sections': [
                    {'name': 'E-Commerce Flash Sale / Cab Booking / Food Delivery LLD', 'qs': '1 System', 'time': '150 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: DSA Round',
                'sections': [
                    {'name': 'Binary Trees, Graphs & Dynamic Programming', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Managerial',
                'sections': [
                    {'name': 'Engineering Standards & Behavioral Scenarios', 'qs': 'Behavioral', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Data Structures & Algorithms', 'icon': '🧠', 'qs': '45 Qs', 'time': '60 Mins', 'topics': ['Graph Shortest Path (Dijkstra, Floyd-Warshall)', 'Dynamic Programming 2D & Tree DP', 'Segment Tree with Lazy Propagation', 'Sliding Window & Hash Maps']},
            {'category': 'Machine Coding & LLD', 'icon': '💻', 'qs': '35 Qs', 'time': '60 Mins', 'topics': ['Clean Architecture & SOLID Principles', 'Design Patterns (Factory, Strategy, Observer)', 'In-Memory Database & Index Design', 'Multi-threaded Concurrency in Java']},
            {'category': 'Database & Scalability Fundamentals', 'icon': '⚡', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['MySQL Indexing & B+ Trees', 'Distributed Caching (Redis/Memcached)', 'Message Brokers (Kafka/RabbitMQ)', 'REST API Design & Microservices']},
            {'category': 'Live Coding Assessment', 'icon': '🎯', 'qs': '3 Qs', 'time': '90 Mins', 'topics': ['Product Catalog Filtering Engine', 'Flash Sale Inventory Lock Manager', 'Warehouse Box Packaging Optimization', 'Optimal Delivery Route Planner']}
        ],
        'faqs': [
            {'q': 'What is the Flipkart Machine Coding round?', 'a': 'Flipkart invented the Machine Coding format: candidates are given 2.5 hours to design, write, compile, and demonstrate a complete, clean, object-oriented software system with clean classes and unit test drivers.'},
            {'q': 'What programming languages are preferred at Flipkart?', 'a': 'Java is the primary language used, though C++ and Python are also supported.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Flipkart SDE-1 OA Benchmark Model 1',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Given warehouse items with dimensions and shipping box volumes, find the minimum number of shipping boxes needed using 3D bin packing approximation.',
                'sample_quant': 'Given customer review strings, find the length of the longest substring that contains at most K distinct vowel characters.',
                'sample_tech': 'Explain how Flipkart handles millions of concurrent order requests during Big Billion Days without database lock contention.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Flipkart Machine Coding & LLD Model 2',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Implement a thread-safe Flash Sale management system with registerUser, addInventory, purchaseItem, and getOrderStatus with clean OOP classes.',
                'sample_quant': 'Find the maximum profit possible from executing up to K parcel delivery route assignments with overlapping time windows.',
                'sample_tech': 'How does Elasticsearch index product catalog data using inverted indexes to deliver instant full-text search results?'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Flipkart Campus Drive Solved Paper Model 3',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Given an undirected graph representing warehouse logistics hubs, find all articulation bridges whose failure isolates a regional warehouse.',
                'sample_quant': 'Calculate the total number of valid permutations for assigning 5 delivery vans to 10 delivery clusters under capacity constraints.',
                'sample_tech': 'What is the difference between synchronous HTTP calls and asynchronous Kafka messaging in e-commerce fulfillment microservices?'
            }
        ]
    },

    'swiggy': {
        'canonical_name': 'Swiggy',
        'total_mins': 90,
        'total_qs': 3,
        'roles': 'Software Development Engineer (SDE-1 / Logistics & Food Delivery)',
        'ctc': '₹18.0 - ₹28.0 LPA',
        'eligibility': 'B.Tech / M.Tech in CS/IT or related engineering branches',
        'difficulty': 'Hard',
        'difficulty_class': 'badge-danger',
        'tagline': 'Swiggy SDE-1 placement pattern, geolocation algorithms, concurrency & past interview papers.',
        'brand_color': '#fc8019',
        'accent_bg': 'linear-gradient(135deg, #fc8019 0%, #ea580c 100%)',
        'logo_icon': '🛵',
        'logo_image': 'images/swiggy.svg',
        'selection_stages': [
            {'step': 1, 'title': 'HackerEarth Online Coding Test', 'desc': '3 Algorithmic Problems | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Machine Coding Round (LLD)', 'desc': 'OOP Class Design & Concurrency | 90 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'Problem Solving & DSA', 'desc': 'Geospatial Graphs & Dynamic Programming | 60 Mins', 'icon': '🧠'},
            {'step': 4, 'title': 'Core CS & System Scalability', 'desc': 'Database Locking, Redis & Message Streams | 45 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Hiring Manager & Culture', 'desc': 'High Ownership & Consumer First Mindset | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment',
                'sections': [
                    {'name': 'Array / String Manipulation', 'qs': '1 Q', 'time': '25 Mins'},
                    {'name': 'Geospatial / Graph Algorithm', 'qs': '1 Q', 'time': '35 Mins'},
                    {'name': 'Dynamic Programming Optimization', 'qs': '1 Q', 'time': '30 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Machine Coding',
                'sections': [
                    {'name': 'Food Delivery Matching / Order Tracking Engine LLD', 'qs': '1 System', 'time': '90 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: DSA Round',
                'sections': [
                    {'name': 'Graph Shortest Paths & Dynamic Programming', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Data Structures & Algorithms', 'icon': '🧠', 'qs': '40 Qs', 'time': '50 Mins', 'topics': ['Geospatial Quadtrees & H3 Indexing', 'Graph BFS/DFS & Dijkstra', 'Dynamic Programming on 2D Grids', 'Sliding Window & Hash Maps']},
            {'category': 'Machine Coding & OOP Architecture', 'icon': '💻', 'qs': '30 Qs', 'time': '40 Mins', 'topics': ['Food Delivery Order Lifecycle LLD', 'Delivery Partner Assignment Engine', 'SOLID Principles & Design Patterns', 'Thread Safety in Java/Go']},
            {'category': 'Database & Infrastructure Core', 'icon': '⚡', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['MySQL Index Optimization & Locking', 'Redis Spatial Commands (GEOSEARCH)', 'Kafka Telemetry Streaming', 'Microservice Resilience & Caching']},
            {'category': 'Live Coding Assessment', 'icon': '🎯', 'qs': '3 Qs', 'time': '90 Mins', 'topics': ['Delivery Partner Batch Assignment', 'Restaurant Surge Pricing Zone Detector', 'Dynamic Kitchen Prep Time Estimator', 'Live Order Tracking State Machine']}
        ],
        'faqs': [
            {'q': 'What does Swiggy emphasize in technical rounds?', 'a': 'Real-world problem solving, geospatial algorithms (distance metrics, clustering), clean OOP machine coding, and high-concurrency database design.'},
            {'q': 'What is the format of the Swiggy Machine Coding round?', 'a': 'A 90-minute round to write an extensible, clean, working Java/Go/Python program modeling an order fulfillment or delivery assignment system.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Swiggy SDE-1 HackerEarth OA Model 1',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Given delivery partner locations and customer orders, implement an algorithm that matches orders to nearest available delivery partners minimizing total delivery latency.',
                'sample_quant': 'In a city road network of N intersections and M roads, find the optimal route that visits K restaurants before reaching customer destination.',
                'sample_tech': 'Explain how Swiggy uses Redis GEO commands and hexagonal geospatial indexing (H3) to compute real-time delivery fee surges.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Swiggy Machine Coding & LLD Model 2',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Design an in-memory restaurant table reservation or food ordering system supporting menu item search, cart checkout, and discount vouchers.',
                'sample_quant': 'Find the maximum number of non-overlapping delivery windows a delivery driver can fulfill within an 8-hour shift.',
                'sample_tech': 'How does distributed locking in Redis prevent double-assignment of an order to two delivery partners simultaneously?'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Swiggy University Drive Solved Paper Model 3',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Given an array of kitchen order prep times and driver arrival times, find the maximum number of orders delivered hot within 30 minutes.',
                'sample_quant': 'Calculate the expected delivery travel time given weather disruption probabilities and traffic density factors.',
                'sample_tech': 'What are the architectural benefits of Go (Golang) goroutines and channels for high-throughput live delivery tracking services?'
            }
        ]
    },

    'zomato': {
        'canonical_name': 'Zomato',
        'total_mins': 90,
        'total_qs': 3,
        'roles': 'Software Development Engineer (SDE-1) / Mobile Engineer (iOS/Android)',
        'ctc': '₹16.0 - ₹26.0 LPA',
        'eligibility': 'B.E / B.Tech in CS/IT or equivalent project portfolio',
        'difficulty': 'Moderate to Hard',
        'difficulty_class': 'badge-warning',
        'tagline': 'Zomato software engineering test pattern, dynamic programming, mobile architecture & solved papers.',
        'brand_color': '#cb202d',
        'accent_bg': 'linear-gradient(135deg, #cb202d 0%, #880e18 100%)',
        'logo_icon': '🍅',
        'logo_image': 'images/zomato.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Online Assessment (HackerRank)', 'desc': '3 Coding Problems | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Problem Solving & DSA', 'desc': 'Arrays, HashMaps & DP | 60 Mins', 'icon': '🧠'},
            {'step': 3, 'title': 'Machine Coding & LLD', 'desc': 'Clean Object Oriented Design | 60 Mins', 'icon': '⚡'},
            {'step': 4, 'title': 'Architecture & Frameworks', 'desc': 'REST APIs, Databases & Mobile/Backend | 45 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Culture & Founders Round', 'desc': 'Ownership, Problem Solving & Fitment | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment',
                'sections': [
                    {'name': 'Array / String Manipulation', 'qs': '1 Q', 'time': '25 Mins'},
                    {'name': 'Sliding Window / Two Pointers', 'qs': '1 Q', 'time': '35 Mins'},
                    {'name': 'Dynamic Programming / Graph', 'qs': '1 Q', 'time': '30 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: DSA Technical',
                'sections': [
                    {'name': 'Trees, Hash Maps & Dynamic Programming', 'qs': '2 Qs', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: LLD & Architecture',
                'sections': [
                    {'name': 'Restaurant Listing & Cart Management LLD', 'qs': '1 Design', 'time': '60 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Data Structures & Algorithms', 'icon': '🧠', 'qs': '40 Qs', 'time': '50 Mins', 'topics': ['Sliding Window & Hash Maps', 'Binary Trees & BST Traversals', 'Graph Shortest Paths (BFS/Dijkstra)', 'Dynamic Programming Subsequences']},
            {'category': 'OOP & Low-Level Design', 'icon': '💻', 'qs': '30 Qs', 'time': '40 Mins', 'topics': ['Restaurant Menu & Cart Class Design', 'Discount Coupon Application Engine', 'Design Patterns (Factory, Builder, Strategy)', 'Concurrency & Thread Safety']},
            {'category': 'Databases & Web/Mobile Core', 'icon': '⚡', 'qs': '30 Qs', 'time': '30 Mins', 'topics': ['SQL Normalization & Indexing', 'Redis Caching for Search Listings', 'RESTful API Design & HTTP Statuses', 'Async I/O & Event Loops']},
            {'category': 'Live Coding Assessment', 'icon': '🎯', 'qs': '3 Qs', 'time': '90 Mins', 'topics': ['Restaurant Rating Weighted Aggregator', 'Promo Code Discount Optimization', 'Delivery Route Cluster Grouping', 'Sliding Window Restaurant Search']}
        ],
        'faqs': [
            {'q': 'What does Zomato look for in fresher SDEs?', 'a': 'Practical problem solving, fast coding speed, strong grasp of data structures, ability to build real-world web/mobile applications, and high product sense.'},
            {'q': 'Is knowledge of mobile development (React Native / Android / iOS) helpful for Zomato?', 'a': 'Yes, for mobile engineering tracks, proficiency in Kotlin, Swift, or React Native is highly valued.'}
        ],
        'past_papers': [
            {
                'year': '2025 Official Assessment Paper',
                'title': 'Zomato SDE-1 HackerRank OA Model 1',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Given an array of restaurant ratings and review counts, compute the top-K highest Bayesian weighted rating restaurants in O(N log K) time.',
                'sample_quant': 'Find the maximum consecutive days a customer ordered food from distinct restaurants using a sliding window hash map.',
                'sample_tech': 'Explain how caching restaurant menus in Redis reduces database load during peak lunch and dinner hours.'
            },
            {
                'year': '2024 Memory Based Paper',
                'title': 'Zomato Technical Onsite & LLD Model 2',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Design an in-memory food delivery cart system with addItem, applyCoupon, calculateTax, and checkout functions with clean OOP classes.',
                'sample_quant': 'Given a 2D grid representing city zones, find the minimum delivery fee path from restaurant to customer using Dijkstra.',
                'sample_tech': 'Differentiate between optimistic locking and pessimistic locking when reserving dining tables in restaurants.'
            },
            {
                'year': '2023 Campus Placement Paper',
                'title': 'Zomato University Hiring Solved Paper Model 3',
                'total_qs': 3,
                'duration': '90 Mins',
                'sample_coding': 'Find the longest palindromic substring in a customer search query string using Dynamic Programming in O(N^2) time.',
                'sample_quant': 'Calculate the total number of distinct meal combinations a customer can choose from a multi-course menu under price constraints.',
                'sample_tech': 'What is the difference between client-side rendering and server-side rendering in modern web frontends?'
            }
        ]
    }
}
