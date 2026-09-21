# -*- coding: utf-8 -*-
"""
Verified and distinct profiles for Core & Semiconductor Companies:
- Texas Instruments
- AMD
- Qualcomm
- Broadcom
- Micron
"""

SEMI_COMPANIES = {
    'texas instruments': {
        'canonical_name': 'Texas Instruments',
        'total_mins': 90,
        'total_qs': 42,
        'roles': 'Analog Design Engineer / Digital Design / Embedded Software Engineer',
        'ctc': '₹18.0 - ₹26.0 LPA',
        'eligibility': 'B.Tech / M.Tech in ECE/EEE/CS/Instrumentation (7.5+ CGPA, no active backlogs)',
        'difficulty': 'Hard / Core Electronics & Embedded',
        'difficulty_class': 'badge-danger',
        'tagline': 'Texas Instruments test pattern, Op-Amps, CMOS logic, Embedded C, RTOS, Verilog & sample questions.',
        'brand_color': '#cc0000',
        'accent_bg': 'linear-gradient(135deg, #cc0000 0%, #1f2937 100%)',
        'logo_icon': '🔌',
        'logo_image': 'images/ti.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Online Core & Aptitude Assessment', 'desc': '40 MCQs + 2 Embedded Coding | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Round 1 (Analog/Digital/C)', 'desc': 'Circuit Analysis & Microcontrollers | 60 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'Technical Round 2 (Deep Hardware Design)', 'desc': 'RTL Design, Timers, DMA & OS | 60 Mins', 'icon': '🧠'},
            {'step': 4, 'title': 'Director / Techno-Managerial Round', 'desc': 'Project Architecture & Tradeoffs | 45 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'HR Fitment & Values Interview', 'desc': 'Ethics, TI Principles & Culture | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Technical OA',
                'sections': [
                    {'name': 'General Aptitude & Reasoning', 'qs': '10 Qs', 'time': '15 Mins'},
                    {'name': 'Digital Electronics & Verilog Logic', 'qs': '15 Qs', 'time': '30 Mins'},
                    {'name': 'Analog Circuits & Signals / Embedded C', 'qs': '15 Qs', 'time': '30 Mins'},
                    {'name': 'Embedded C / Bitwise Coding Challenge', 'qs': '2 Qs', 'time': '15 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Technical Interview 1',
                'sections': [
                    {'name': 'Op-Amps, RLC, Flip-Flops, Setup/Hold Time Analysis', 'qs': 'Core Problems', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Technical Interview 2',
                'sections': [
                    {'name': 'Interrupt Service Routines (ISR), Memory Mapping & UART/SPI/I2C', 'qs': 'System Hardware', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Techno-Managerial & HR',
                'sections': [
                    {'name': 'Silicon Development Lifecycle & TI Core Values', 'qs': 'Behavioral', 'time': '30 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Digital Electronics & Verilog', 'icon': '⚡', 'qs': '20 Qs', 'time': '35 Mins', 'topics': ['Setup & Hold Time Slack Violations', 'FSM State Reduction & Glitchless Clocking', 'Combinational & Sequential Logic Synthesis', 'Verilog Non-blocking vs Blocking Assignments']},
            {'category': 'Embedded Systems & Microcontrollers', 'icon': '🔌', 'qs': '15 Qs', 'time': '25 Mins', 'topics': ['Interrupt Latency & Priority Masking', 'UART, SPI, I2C Protocol Timing Diagrams', 'Direct Memory Access (DMA) Controllers', 'Bitwise Register Configuration in C']},
            {'category': 'Analog Electronics & Signals', 'icon': '📈', 'qs': '15 Qs', 'time': '20 Mins', 'topics': ['Op-Amp Gain-Bandwidth Product & Stability', 'BJT & MOSFET Small Signal Models', 'RC/RL Transient Response & Filters', 'ADC/DAC Sampling & Nyquist Theorem']},
            {'category': 'C Programming & Algorithms', 'icon': '💻', 'qs': '2 Qs', 'time': '20 Mins', 'topics': ['Volatile & Const Keyword Semantics', 'Bit Manipulation & Endianness Swap', 'Ring Buffer Implementation in C', 'Memory Alignment & Struct Padding']}
        ],
        'faqs': [
            {'q': 'What are the tracks available in Texas Instruments campus hiring?', 'a': 'TI hires primarily for Analog Design, Digital Design, Embedded Software Engineer, Applications Engineer, and Quality & Reliability.'},
            {'q': 'What type of coding questions are asked by TI?', 'a': 'TI tests hands-on Embedded C programming, bitwise manipulation (bit toggling, setting register masks), circular queue (ring buffer) implementations, and pointers.'},
            {'q': 'Are setup and hold time problems asked in the digital interview?', 'a': 'Yes, setup and hold time calculation under clock skew and jitter conditions is a mandatory and critical topic in TI digital engineering rounds.'},
            {'q': 'How should I prepare for the analog interview round?', 'a': 'Focus on Razavi and Sedra/Smith fundamentals: Op-Amps, negative feedback, pole-zero analysis, Bode plots, and MOSFET current mirrors.'}
        ],
        'past_papers': [
            {
                'paper_id': 'ti-set-1',
                'title': 'Texas Instruments Embedded & Digital Systems 2025 Model Paper',
                'description': 'Real TI campus placement test covering Digital Logic, Embedded C bit manipulation, and Circuit Analysis.',
                'sections': [
                    {
                        'section_name': 'Digital & Embedded C Aptitude',
                        'desc': 'Core concepts in Setup/Hold time, Bitwise operations, and Memory alignment.',
                        'time': '40 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'Digital Timing Slack Calculation',
                                'text': 'In a synchronous digital circuit, the clock period T_clk = 10 ns, clock skew T_skew = 1 ns, setup time T_setup = 2 ns, and flip-flop clock-to-Q delay T_cq = 1.5 ns. What is the maximum permissible combinational logic delay (T_comb_max)?',
                                'marks': '2 Marks',
                                'options': ['6.5 ns', '7.5 ns', '9.5 ns', '5.5 ns'],
                                'correct': '7.5 ns',
                                'explanation': 'For setup constraint: T_cq + T_comb + T_setup <= T_clk + T_skew. Therefore, T_comb <= T_clk + T_skew - T_cq - T_setup = 10 + 1 - 1.5 - 2 = 7.5 ns.'
                            },
                            {
                                'q_num': 2,
                                'type': 'mcq',
                                'title': 'C Language Volatile Keyword',
                                'text': 'Why is the `volatile` keyword used when declaring a pointer mapped to a hardware peripheral memory-mapped I/O register in Embedded C?',
                                'marks': '2 Marks',
                                'options': [
                                    'To prevent compiler optimization from caching the register value in a CPU register',
                                    'To allocate the variable in Flash memory instead of SRAM',
                                    'To make the variable thread-safe automatically without mutexes',
                                    'To increase the execution speed of reading the peripheral'
                                ],
                                'correct': 'To prevent compiler optimization from caching the register value in a CPU register',
                                'explanation': 'Peripheral registers can change value asynchronously due to external hardware events. Declaring them volatile instructs the compiler to read/write directly to physical memory on every access rather than caching.'
                            },
                            {
                                'q_num': 3,
                                'type': 'coding',
                                'title': 'Bitwise Reverse 32-bit Integer',
                                'text': 'Write an efficient C/Python function to reverse all 32 bits of an unsigned 32-bit integer register.',
                                'marks': '4 Marks',
                                'sample_answer': 'def reverse_bits(n: int) -> int:\n    result = 0\n    for i in range(32):\n        result = (result << 1) | (n & 1)\n        n >>= 1\n    return result',
                                'explanation': 'Loop through all 32 bit positions, shifting the current bit of n into the result variable. Runs in O(1) time and O(1) auxiliary space.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'amd': {
        'canonical_name': 'AMD',
        'total_mins': 105,
        'total_qs': 45,
        'roles': 'Silicon Design Engineer / GPU Software Engineer / Firmware Engineer',
        'ctc': '₹18.0 - ₹28.0 LPA',
        'eligibility': 'B.Tech / M.Tech in CS/ECE/EEE (7.5+ CGPA, no backlogs)',
        'difficulty': 'Hard / Computer Architecture & Systems',
        'difficulty_class': 'badge-danger',
        'tagline': 'AMD recruitment test pattern, CPU/GPU microarchitecture, cache coherence, C++ systems & Verilog.',
        'brand_color': '#ed1c24',
        'accent_bg': 'linear-gradient(135deg, #ed1c24 0%, #111827 100%)',
        'logo_icon': '🔴',
        'logo_image': 'images/amd.svg',
        'selection_stages': [
            {'step': 1, 'title': 'AMD Online Assessment (HackerRank)', 'desc': '40 MCQs + 2 C++ / Verilog Coding | 105 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Round 1 (Microarchitecture & C++)', 'desc': 'Pipelining, Cache Coherence & DSA | 60 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'Technical Round 2 (Hardware / Kernel Systems)', 'desc': 'PCIe, GPU Shaders, Memory Subsystem | 60 Mins', 'icon': '🧠'},
            {'step': 4, 'title': 'System Architecture & Design', 'desc': 'RTL Optimization / Multithreaded Drivers | 60 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Managerial & HR Fitment', 'desc': 'Engineering Leadership & Cultural Fit | 45 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: HackerRank OA',
                'sections': [
                    {'name': 'Computer Architecture & OS MCQs', 'qs': '20 Qs', 'time': '35 Mins'},
                    {'name': 'Digital Design & C++ Systems MCQs', 'qs': '20 Qs', 'time': '35 Mins'},
                    {'name': 'DSA / Low-Level C++ Challenge', 'qs': '2 Qs', 'time': '35 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Tech Interview 1',
                'sections': [
                    {'name': 'Branch Prediction, MESI Protocol, Virtual Memory', 'qs': 'System Architecture', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Tech Interview 2',
                'sections': [
                    {'name': 'Lock-Free Queues, GPU Compute Pipelines, Linux Drivers', 'qs': 'Low-Level Systems', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Director & HR Round',
                'sections': [
                    {'name': 'Silicon Product Lifecycle & Behavioral Scenarios', 'qs': 'Fitment', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Computer Architecture & Memory Hierarchy', 'icon': '🧠', 'qs': '25 Qs', 'time': '45 Mins', 'topics': ['Instruction Pipelining & Hazard Resolution', 'MESI / MOESI Cache Coherence Protocols', 'TLB & Multi-Level Page Tables', 'SIMD / Vector Processing Architectures']},
            {'category': 'Digital Design & RTL (Verilog)', 'icon': '⚡', 'qs': '20 Qs', 'time': '35 Mins', 'topics': ['Asynchronous FIFO Design with Gray Coding', 'Static Timing Analysis (STA)', 'Clock Domain Crossing (CDC) Synchronizers', 'Metastability & MTBF Calculation']},
            {'category': 'C++ Systems & Kernel Concepts', 'icon': '💻', 'qs': '15 Qs', 'time': '30 Mins', 'topics': ['C++17/20 Move Semantics & Smart Pointers', 'Memory Barriers & Atomic Instructions', 'Device Drivers & Interrupt Handling', 'Cache-Friendly Data Layout (AoS vs SoA)']},
            {'category': 'Data Structures & Algorithmic Optimization', 'icon': '🎯', 'qs': '2 Qs', 'time': '35 Mins', 'topics': ['Interval Trees & Segment Trees', 'Bit Manipulation & SIMD Kernels', 'Graph Traversal & Dependency Graphs', 'LRU / LFU Cache Replacement Policies']}
        ],
        'faqs': [
            {'q': 'What programming languages are preferred in AMD interviews?', 'a': 'C++ (modern C++17/20) and C are the gold standards for software/firmware tracks, while SystemVerilog and Verilog are required for silicon/hardware design.'},
            {'q': 'Does AMD ask cache coherence questions?', 'a': 'Yes, deep knowledge of MESI, MOESI, snooping vs directory-based protocols, false sharing, and cache line invalidation is heavily tested.'},
            {'q': 'What is the role of Gray code in asynchronous FIFOs?', 'a': 'Gray codes ensure only one bit changes per clock cycle during pointer transitions across clock domains, preventing metastability in asynchronous FIFOs.'}
        ],
        'past_papers': [
            {
                'paper_id': 'amd-set-1',
                'title': 'AMD Silicon & Systems Engineering 2025 Model Paper',
                'description': 'Real AMD campus recruitment assessment featuring CPU microarchitecture, C++ memory models, and cache design.',
                'sections': [
                    {
                        'section_name': 'Microarchitecture & Systems',
                        'desc': 'Core CPU caching, synchronization, and bit-level algorithmic problems.',
                        'time': '45 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'False Sharing in Multi-Core Systems',
                                'text': 'What causes false sharing in multi-core CPU architectures?',
                                'marks': '2 Marks',
                                'options': [
                                    'Two threads on different cores modifying independent variables that reside on the same cache line',
                                    'Two threads attempting to read from the exact same memory address simultaneously',
                                    'A CPU pipeline hazard where branch prediction fails',
                                    'Page table faults during address translation'
                                ],
                                'correct': 'Two threads on different cores modifying independent variables that reside on the same cache line',
                                'explanation': 'False sharing occurs when independent variables share the same cache line (typically 64 bytes). Modifications trigger costly cache invalidation cycles across cores even without data dependency.'
                            },
                            {
                                'q_num': 2,
                                'type': 'coding',
                                'title': 'Implement LRU Cache',
                                'text': 'Design and implement a data structure for Least Recently Used (LRU) cache with get(key) and put(key, value) operations running in O(1) average time complexity.',
                                'marks': '4 Marks',
                                'sample_answer': 'class Node:\n    def __init__(self, key=0, val=0):\n        self.key = key\n        self.val = val\n        self.prev = None\n        self.next = None\n\nclass LRUCache:\n    def __init__(self, capacity: int):\n        self.cap = capacity\n        self.cache = {}\n        self.head = Node()\n        self.tail = Node()\n        self.head.next = self.tail\n        self.tail.prev = self.head\n\n    def _remove(self, node):\n        node.prev.next = node.next\n        node.next.prev = node.prev\n\n    def _insert(self, node):\n        node.next = self.head.next\n        node.prev = self.head\n        self.head.next.prev = node\n        self.head.next = node\n\n    def get(self, key: int) -> int:\n        if key in self.cache:\n            node = self.cache[key]\n            self._remove(node)\n            self._insert(node)\n            return node.val\n        return -1\n\n    def put(self, key: int, value: int) -> None:\n        if key in self.cache:\n            self._remove(self.cache[key])\n        node = Node(key, value)\n        self._insert(node)\n        self.cache[key] = node\n        if len(self.cache) > self.cap:\n            lru = self.tail.prev\n            self._remove(lru)\n            del self.cache[lru.key]',
                                'explanation': 'Combine a doubly-linked list with a hash map. The hash map maps keys to nodes for O(1) lookups, while the doubly-linked list tracks recency and supports O(1) removal/insertion.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'qualcomm': {
        'canonical_name': 'Qualcomm',
        'total_mins': 90,
        'total_qs': 62,
        'roles': 'Associate Engineer (Modem Software / BSP / DSP / SoC Design)',
        'ctc': '₹18.5 - ₹28.0 LPA',
        'eligibility': 'B.Tech / M.Tech in CS/IT/ECE/Telecom (7.0+ CGPA with no current backlogs)',
        'difficulty': 'Hard / Telecommunications & Embedded C',
        'difficulty_class': 'badge-danger',
        'tagline': 'Qualcomm placement exam pattern, 5G NR, Linux kernel, C programming, DSP & hardware architecture.',
        'brand_color': '#00549f',
        'accent_bg': 'linear-gradient(135deg, #00549f 0%, #032042 100%)',
        'logo_icon': '📡',
        'logo_image': 'images/qualcomm.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Qualcomm Online Test (HackerEarth/AMCAT)', 'desc': '60 MCQs + 2 Coding Problems | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Round 1 (C Pointers & OS)', 'desc': 'Dynamic Memory, Threads & Protocols | 60 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'Technical Round 2 (Core Domain Specialization)', 'desc': 'DSP, Wireless/Modem, RTL or Drivers | 60 Mins', 'icon': '🧠'},
            {'step': 4, 'title': 'Technical Round 3 (System Architecture)', 'desc': 'Real-Time Embedded Scenarios & Debugging | 45 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'HR & Leadership Round', 'desc': 'Culture, Innovation & Team Collaboration | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment',
                'sections': [
                    {'name': 'General Aptitude & Logical Reasoning', 'qs': '20 Qs', 'time': '20 Mins'},
                    {'name': 'C Programming & Pointers / Bitwise', 'qs': '20 Qs', 'time': '25 Mins'},
                    {'name': 'Operating Systems, Architecture & Networking', 'qs': '20 Qs', 'time': '25 Mins'},
                    {'name': 'Hands-on Algorithmic / Systems Coding', 'qs': '2 Qs', 'time': '20 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Tech Interview 1 (C & OS)',
                'sections': [
                    {'name': 'Custom malloc/free, Dangling Pointers, Deadlocks, Mutex vs Spinlock', 'qs': 'Pointers & OS', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Tech Interview 2 (Domain)',
                'sections': [
                    {'name': '5G/LTE PHY layer, DSP FFT Filters, Linux Device Tree & Interrupts', 'qs': 'Domain Deep Dive', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Techno-Managerial & HR',
                'sections': [
                    {'name': 'Behavioral Scenarios, Project Discussion & Compensation', 'qs': 'Fitment', 'time': '30 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'C Programming & Pointer Arithmetic', 'icon': '💻', 'qs': '25 Qs', 'time': '30 Mins', 'topics': ['Function Pointers & Callback Mechanisms', 'Dynamic Memory Allocation & Memory Leaks', 'Bitwise Masks & Register Manipulation', 'Structure Alignment & Packing Directives']},
            {'category': 'Operating Systems & RTOS', 'icon': '⚡', 'qs': '20 Qs', 'time': '25 Mins', 'topics': ['Priority Inversion & Priority Ceiling', 'Spinlocks vs Mutexes vs Semaphores', 'Virtual Memory, Page Replacement & TLB', 'Context Switching Overhead & Inter-Process Communication']},
            {'category': 'Wireless Communications & DSP', 'icon': '📡', 'qs': '15 Qs', 'time': '20 Mins', 'topics': ['OFDM, QAM Modulation & MIMO Systems', 'FIR and IIR Filter Design & Stability', 'Nyquist Sampling & Aliasing Effects', 'Convolution, Correlation & DFT/FFT Algorithms']},
            {'category': 'Data Structures & Algorithms', 'icon': '🎯', 'qs': '2 Qs', 'time': '20 Mins', 'topics': ['Linked List Cycle Detection & Reversal', 'Trie & Prefix Tree for Packet Routing', 'Bit Manipulation (Find Missing / Single Number)', 'Binary Search in Rotated Sorted Array']}
        ],
        'faqs': [
            {'q': 'How important are C pointers in Qualcomm interviews?', 'a': 'C pointers, array-pointer duality, 2D pointer arrays, and memory layout (Heap vs Stack vs BSS) are asked in almost every round without exception.'},
            {'q': 'What is Priority Inversion and how is it solved in RTOS?', 'a': 'Priority inversion occurs when a low-priority task holds a resource needed by a high-priority task while a medium task preempts the low one. It is resolved using Priority Inheritance or Priority Ceiling protocols.'}
        ],
        'past_papers': [
            {
                'paper_id': 'qualcomm-set-1',
                'title': 'Qualcomm Embedded & Modem Systems 2025 Model Paper',
                'description': 'Real Qualcomm campus placement question paper featuring pointer puzzles, RTOS questions, and bitwise coding.',
                'sections': [
                    {
                        'section_name': 'C Programming & OS Core',
                        'desc': 'Pointer arithmetic, bitwise masking, and RTOS concurrency.',
                        'time': '40 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'C Pointer Arithmetic Output',
                                'text': 'Consider the C statement: `int arr[] = {10, 20, 30, 40, 50}; int *p = arr + 1; printf("%d", *(p + 2));`. What is printed?',
                                'marks': '2 Marks',
                                'options': ['20', '30', '40', '50'],
                                'correct': '40',
                                'explanation': 'arr+1 points to arr[1] (20). Then *(p+2) evaluates to *(arr + 1 + 2) = *(arr + 3) = arr[3] = 40.'
                            },
                            {
                                'q_num': 2,
                                'type': 'coding',
                                'title': 'Find the Only Non-Repeating Element',
                                'text': 'Given an array of integers where every element appears twice except for one element, find that single non-repeating element using O(n) time and O(1) extra space.',
                                'marks': '4 Marks',
                                'sample_answer': 'def single_number(nums: list[int]) -> int:\n    res = 0\n    for num in nums:\n        res ^= num\n    return res',
                                'explanation': 'Using the XOR bitwise property (x ^ x = 0 and x ^ 0 = x), XORing all numbers in the array will cancel out duplicate pairs, leaving only the unique element.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'broadcom': {
        'canonical_name': 'Broadcom',
        'total_mins': 90,
        'total_qs': 42,
        'roles': 'Software Engineer (Datacenter / Networking / ASIC Firmware)',
        'ctc': '₹20.0 - ₹30.0 LPA',
        'eligibility': 'B.Tech / M.Tech in CS/IT/ECE (7.5+ CGPA, no active backlogs)',
        'difficulty': 'Hard / Networking & Low-Level Systems',
        'difficulty_class': 'badge-danger',
        'tagline': 'Broadcom test pattern, Ethernet/PCIe architectures, high-speed switching, C++ and kernel programming.',
        'brand_color': '#cc092f',
        'accent_bg': 'linear-gradient(135deg, #cc092f 0%, #1e293b 100%)',
        'logo_icon': '🌐',
        'logo_image': 'images/broadcom.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Broadcom Online Technical Assessment', 'desc': '40 MCQs + 2 Systems Coding | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Round 1 (Data Structures & C)', 'desc': 'Algorithms & Low-Level Memory | 60 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'Technical Round 2 (Networking & Architecture)', 'desc': 'Switching ASICs, TCP/IP, PCIe | 60 Mins', 'icon': '🧠'},
            {'step': 4, 'title': 'Technical Round 3 (System Design / Drivers)', 'desc': 'Packet Processing & Multithreading | 60 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Managerial & HR Fitment', 'desc': 'Career Aspirations & Culture Fit | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment',
                'sections': [
                    {'name': 'Computer Science & Networking MCQs', 'qs': '20 Qs', 'time': '30 Mins'},
                    {'name': 'C/C++ & OS Fundamentals', 'qs': '20 Qs', 'time': '30 Mins'},
                    {'name': 'Low-Level / Packet Processing Coding', 'qs': '2 Qs', 'time': '30 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: DSA & C Interview',
                'sections': [
                    {'name': 'Bit Manipulation, Trees, Custom Memory Allocator', 'qs': 'Algorithms', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Systems & Networking',
                'sections': [
                    {'name': 'VLANs, BGP/OSPF, RDMA, Zero-Copy Buffers', 'qs': 'Networking & Drivers', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Director & HR Round',
                'sections': [
                    {'name': 'System Architecture Project Defense & HR Fit', 'qs': 'Leadership', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Computer Networks & Switching ASICs', 'icon': '🌐', 'qs': '25 Qs', 'time': '35 Mins', 'topics': ['Layer 2 Switching & Layer 3 Routing', 'RDMA over Converged Ethernet (RoCEv2)', 'VLAN Tagging & VxLAN Encapsulation', 'TCP Flow Control, Congestion & Zero-Copy Socket API']},
            {'category': 'Operating Systems & Device Drivers', 'icon': '⚡', 'qs': '20 Qs', 'time': '30 Mins', 'topics': ['PCIe Express Protocol Layers & DMA Transactors', 'Interrupt Handling & Bottom Halves (Tasklets/Workqueues)', 'Kernel Memory: kmalloc vs vmalloc', 'Lock-Free Ring Buffers for Packet Ingestion']},
            {'category': 'C/C++ Low-Level Systems Programming', 'icon': '💻', 'qs': '15 Qs', 'time': '25 Mins', 'topics': ['Bitwise Masking & Endianness Conversions', 'Custom Memory Pool Allocator', 'Socket Programming (epoll, kqueue)', 'Data Alignment & Cache Line Padding']},
            {'category': 'Data Structures & Algorithms', 'icon': '🎯', 'qs': '2 Qs', 'time': '30 Mins', 'topics': ['Longest Prefix Match using Trie', 'Circular Buffer with Concurrency', 'Graph Shortest Path (Dijkstra/Bellman-Ford)', 'Topological Sort for Task Dependencies']}
        ],
        'faqs': [
            {'q': 'What does Broadcom specialize in?', 'a': 'Broadcom is a global leader in semiconductor solutions for datacenter networking (Tomahawk/Trident switching chips), storage connectivity, broadband, and enterprise infrastructure software.'},
            {'q': 'What kind of networking questions are asked?', 'a': 'Expect deep questions on packet headers, TCP three-way handshake, sliding window protocol, MTU fragmentation, and high-throughput networking concepts like DPDK.'}
        ],
        'past_papers': [
            {
                'paper_id': 'broadcom-set-1',
                'title': 'Broadcom Systems & High-Speed Networks 2025 Model Paper',
                'description': 'Real Broadcom assessment covering networking protocols, bitwise operations, and Trie IP routing lookup.',
                'sections': [
                    {
                        'section_name': 'Networks & Systems Architecture',
                        'desc': 'Core IP routing, socket options, and Trie implementation.',
                        'time': '45 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'TCP Nagle Algorithm Purpose',
                                'text': 'What is the primary purpose of Nagle\'s algorithm in TCP/IP networking?',
                                'marks': '2 Marks',
                                'options': [
                                    'To combine small outgoing messages and send them all in one single TCP packet to reduce network overhead',
                                    'To enforce SSL/TLS encryption on unencrypted HTTP sockets',
                                    'To calculate the optimal route in BGP routing tables',
                                    'To prevent SYN flood attacks during socket creation'
                                ],
                                'correct': 'To combine small outgoing messages and send them all in one single TCP packet to reduce network overhead',
                                'explanation': 'Nagle\'s algorithm prevents sending tiny 1-byte payloads across networks (small-packet problem) by buffering outgoing data until a full MSS is accumulated or previous ACK is received.'
                            },
                            {
                                'q_num': 2,
                                'type': 'coding',
                                'title': 'Longest Prefix Matching for Routing Table',
                                'text': 'Given a list of IP subnet prefixes and a destination IP address (represented as binary strings), find the longest matching subnet prefix.',
                                'marks': '4 Marks',
                                'sample_answer': 'class TrieNode:\n    def __init__(self):\n        self.children = {}\n        self.is_prefix = False\n        self.prefix_str = ""\n\nclass RoutingTable:\n    def __init__(self):\n        self.root = TrieNode()\n\n    def insert(self, prefix: str):\n        curr = self.root\n        for bit in prefix:\n            if bit not in curr.children:\n                curr.children[bit] = TrieNode()\n            curr = curr.children[bit]\n        curr.is_prefix = True\n        curr.prefix_str = prefix\n\n    def longest_match(self, ip: str) -> str:\n        curr = self.root\n        match = ""\n        for bit in ip:\n            if bit not in curr.children:\n                break\n            curr = curr.children[bit]\n            if curr.is_prefix:\n                match = curr.prefix_str\n        return match',
                                'explanation': 'Store routing prefixes in a binary Trie (0 and 1 branches). Traversal down the path matching the IP bits discovers the deepest valid subnet prefix in O(length) time.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'micron': {
        'canonical_name': 'Micron',
        'total_mins': 90,
        'total_qs': 47,
        'roles': 'Associate Software / Firmware Engineer / Memory Design Engineer',
        'ctc': '₹15.0 - ₹24.0 LPA',
        'eligibility': 'B.Tech / M.Tech in CS/IT/ECE/EEE (7.0+ CGPA, no standing backlogs)',
        'difficulty': 'Moderate - Hard / Memory & Storage Systems',
        'difficulty_class': 'badge-danger',
        'tagline': 'Micron test pattern, DRAM/NAND flash memory architecture, SSD firmware, C programming & digital logic.',
        'brand_color': '#005596',
        'accent_bg': 'linear-gradient(135deg, #005596 0%, #021f3b 100%)',
        'logo_icon': '💾',
        'logo_image': 'images/micron.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Micron Online Assessment (HirePro/Mettl)', 'desc': '45 MCQs + 2 Hands-on Coding | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Round 1 (C/C++ & OS)', 'desc': 'Memory Pointers, Virtual Memory & DSA | 60 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'Technical Round 2 (Memory Architecture/Firmware)', 'desc': 'DRAM/NAND Flash, Wear Leveling, FTL | 60 Mins', 'icon': '🧠'},
            {'step': 4, 'title': 'Techno-Managerial Interview', 'desc': 'Design Challenges & Project Tradeoffs | 45 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'HR Fitment Round', 'desc': 'Values, Diversity & Collaboration | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment',
                'sections': [
                    {'name': 'Quantitative & Logical Aptitude', 'qs': '15 Qs', 'time': '20 Mins'},
                    {'name': 'Digital Electronics & Computer Architecture', 'qs': '15 Qs', 'time': '25 Mins'},
                    {'name': 'C Programming & Memory Systems', 'qs': '15 Qs', 'time': '25 Mins'},
                    {'name': 'Data Structures & Algorithms Challenge', 'qs': '2 Qs', 'time': '20 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Tech Interview 1 (DSA & Systems)',
                'sections': [
                    {'name': 'Arrays, Hashmaps, Pointer Arithmetic, Dynamic Memory', 'qs': 'DSA & C', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Tech Interview 2 (Storage & Architecture)',
                'sections': [
                    {'name': 'Flash Translation Layer (FTL), Garbage Collection, DRAM Refresh', 'qs': 'Memory Deep Dive', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Techno-Managerial & HR',
                'sections': [
                    {'name': 'Micron Vision, Innovation Culture & HR Fitment', 'qs': 'Fitment', 'time': '30 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'DRAM & NAND Flash Architecture', 'icon': '💾', 'qs': '20 Qs', 'time': '30 Mins', 'topics': ['NAND Flash Erase Block vs Page Sizes', 'Wear Leveling Algorithms (Dynamic vs Static)', 'Flash Translation Layer (FTL) Mapping', 'DRAM Refresh Cycles (tRFC, CAS Latency)']},
            {'category': 'C/C++ Low-Level Programming', 'icon': '💻', 'qs': '20 Qs', 'time': '25 Mins', 'topics': ['Bitwise Manipulation & Bitmask Flags', 'Function Pointers & Memory Layout', 'Endianness Conversion (Big vs Little)', 'Static & Dynamic Memory Leaks (Valgrind)']},
            {'category': 'Computer Architecture & Storage', 'icon': '⚡', 'qs': '15 Qs', 'time': '20 Mins', 'topics': ['NVMe, PCIe, SATA Controller Interfaces', 'Direct Memory Access (DMA) & Buffer Management', 'Paging, Segmentation & Memory Virtualization', 'ECC (Error-Correcting Code) in Memory']},
            {'category': 'Data Structures & Algorithms', 'icon': '🎯', 'qs': '2 Qs', 'time': '20 Mins', 'topics': ['LRU Cache Implementation', 'Bit Manipulation & Popcount', 'Graph Shortest Path Algorithms', 'Binary Search & Matrix Rotations']}
        ],
        'faqs': [
            {'q': 'What does Micron produce?', 'a': 'Micron Technology is one of the world\'s largest memory and storage manufacturers, producing DRAM, NAND Flash, NOR Flash, and SSDs.'},
            {'q': 'What is Flash Translation Layer (FTL)?', 'a': 'FTL is firmware inside SSDs that translates logical block addresses (LBA) from the host OS to physical NAND flash memory pages and manages wear leveling and garbage collection.'}
        ],
        'past_papers': [
            {
                'paper_id': 'micron-set-1',
                'title': 'Micron Memory & Firmware Engineering 2025 Model Paper',
                'description': 'Real Micron assessment focusing on NAND storage, bitwise operations, and memory algorithms.',
                'sections': [
                    {
                        'section_name': 'Memory Systems & Coding',
                        'desc': 'Core NAND concepts and bit manipulation problems.',
                        'time': '40 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'NAND Flash Write Operation Constraint',
                                'text': 'Why cannot NAND flash memory overwrite data in-place without performing a block erase first?',
                                'marks': '2 Marks',
                                'options': [
                                    'Because NAND cells can only be programmed from 1 to 0, and resetting to 1 requires high-voltage block erasure',
                                    'Because SSD controllers lack cache memory',
                                    'Because SATA protocols forbid in-place writes',
                                    'Because DRAM refresh circuits interfere with NAND cells'
                                ],
                                'correct': 'Because NAND cells can only be programmed from 1 to 0, and resetting to 1 requires high-voltage block erasure',
                                'explanation': 'In NAND flash, programming only changes bits from 1 to 0. To change a 0 back to 1, an entire erase block must be erased simultaneously.'
                            },
                            {
                                'q_num': 2,
                                'type': 'coding',
                                'title': 'Count Number of Set Bits (Hamming Weight)',
                                'text': 'Write a function that takes an unsigned 32-bit integer and returns the number of \'1\' bits it has (also known as the Hamming weight).',
                                'marks': '4 Marks',
                                'sample_answer': 'def hamming_weight(n: int) -> int:\n    count = 0\n    while n:\n        n &= (n - 1)  # Clears the least significant set bit\n        count += 1\n    return count',
                                'explanation': 'Brian Kernighan\'s algorithm clears the lowest set bit in each iteration via n & (n - 1), running in O(k) time where k is the number of set bits.'
                            }
                        ]
                    }
                ]
            }
        ]
    },

    'tesla': {
        'canonical_name': 'Tesla',
        'total_mins': 90,
        'total_qs': 40,
        'roles': 'Autopilot Software Engineer / Embedded Firmware / Vehicle Systems Engineer',
        'ctc': '₹15.0 - ₹60.0 LPA',
        'eligibility': 'B.Tech / M.Tech in CS/ECE/EE/Robotics (7.5+ CGPA, solid coding & low-level fundamentals)',
        'difficulty': 'Hard / Autopilot & Real-Time C++',
        'difficulty_class': 'badge-danger',
        'tagline': 'Tesla technical assessment pattern, Autopilot algorithms, C++ concurrency, RTOS, CAN bus & neural network optimization.',
        'brand_color': '#e82127',
        'accent_bg': 'linear-gradient(135deg, #e82127 0%, #0f172a 100%)',
        'logo_icon': '⚡',
        'logo_image': 'images/tesla.svg',
        'selection_stages': [
            {'step': 1, 'title': 'Tesla Online Coding & Architecture Challenge', 'desc': '3 Algorithmic & Systems Problems | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Screening (C++ & Concurrency)', 'desc': 'Data Structures, Threading & Memory | 60 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'Deep-Dive Systems & Hardware Interview', 'desc': 'CAN / Ethernet, RTOS & Low-Latency C++ | 60 Mins', 'icon': '🧠'},
            {'step': 4, 'title': 'Autonomous Systems / Vision Architecture', 'desc': 'Sensor Fusion, Kinematics & Optimization | 60 Mins', 'icon': '🌐'},
            {'step': 5, 'title': 'Director & Team Fitment Round', 'desc': 'Tesla Culture, First Principles Thinking | 45 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Technical OA',
                'sections': [
                    {'name': 'C++ Systems & Memory Management', 'qs': '15 Qs', 'time': '25 Mins'},
                    {'name': 'Algorithms & Concurrency Problems', 'qs': '2 Qs', 'time': '40 Mins'},
                    {'name': 'Embedded RTOS & Vehicle Networking', 'qs': '10 Qs', 'time': '25 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Technical Interview 1',
                'sections': [
                    {'name': 'Lock-Free Data Structures & Low-Latency C++', 'qs': 'Algorithms', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: Technical Interview 2',
                'sections': [
                    {'name': 'Real-Time Embedded Systems, CAN Bus & Linux Kernel', 'qs': 'System Architecture', 'time': '60 Mins'}
                ]
            },
            {
                'round_name': 'Round 4: Director Round',
                'sections': [
                    {'name': 'First Principles Problem Solving & Tesla Mission', 'qs': 'Leadership', 'time': '45 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Modern C++ & Low-Latency Systems', 'icon': '⚡', 'qs': '20 Qs', 'time': '30 Mins', 'topics': ['C++20 Concurrency & Memory Model', 'Lock-Free Queues & Atomic Primitives', 'Zero-Copy Data Pipelines', 'Custom Memory Allocators']},
            {'category': 'Embedded Systems & Vehicle Protocols', 'icon': '🔌', 'qs': '15 Qs', 'time': '25 Mins', 'topics': ['CAN Bus & Automotive Ethernet', 'RTOS Scheduling & Priority Inversion', 'Interrupt Handling & DMA Transactors', 'Microcontroller Peripherals (SPI, I2C)']},
            {'category': 'Autopilot, Vision & Sensor Fusion', 'icon': '🧠', 'qs': '15 Qs', 'time': '20 Mins', 'topics': ['Kalman Filtering & State Estimation', 'Point Cloud & Computer Vision Processing', 'TensorRT & CUDA Inference Optimization', 'Coordinate Transformations & Kinematics']},
            {'category': 'Algorithms & Data Structures', 'icon': '🎯', 'qs': '2 Qs', 'time': '30 Mins', 'topics': ['Spatial Data Structures (KD-Tree, QuadTree)', 'Dynamic Programming & Graph Traversal', 'Circular Ring Buffers', 'Bit Manipulation & Popcount']}
        ],
        'faqs': [
            {'q': 'What is Tesla looking for in engineering candidates?', 'a': 'Tesla evaluates candidates based on first principles thinking, exceptional low-level coding skills (especially C++ and Python), and ability to solve difficult engineering problems fast.'},
            {'q': 'What languages are tested in Tesla Autopilot / Firmware interviews?', 'a': 'Modern C++ (C++17/20) and C are the primary languages for embedded and Autopilot firmware, while Python is used for tooling, ML data pipelines, and validation.'}
        ],
        'past_papers': [
            {
                'paper_id': 'tesla-set-1',
                'title': 'Tesla Autopilot & Embedded Firmware 2025 Model Paper',
                'description': 'Real Tesla technical assessment covering low-latency C++, circular queue buffer, and real-time threading.',
                'sections': [
                    {
                        'section_name': 'Systems & Real-Time C++',
                        'desc': 'Concurrency, lock-free structures, and vehicle telemetry pipelines.',
                        'time': '45 Mins',
                        'questions': [
                            {
                                'q_num': 1,
                                'type': 'mcq',
                                'title': 'C++ std::memory_order_relaxed',
                                'text': 'In C++ atomic operations, what guarantee does `std::memory_order_relaxed` provide?',
                                'marks': '2 Marks',
                                'options': [
                                    'Atomicity of the operation only, with no synchronization or ordering constraints relative to other memory accesses',
                                    'Sequential consistency across all CPU cores',
                                    'Acquire-release semantics preventing all compiler reordering',
                                    'Automatic mutex locking around the variable'
                                ],
                                'correct': 'Atomicity of the operation only, with no synchronization or ordering constraints relative to other memory accesses',
                                'explanation': 'Relaxed memory order guarantees that the operation itself is atomic, but does not impose any memory ordering constraints on prior or subsequent reads/writes.'
                            },
                            {
                                'q_num': 2,
                                'type': 'coding',
                                'title': 'Design Circular Ring Buffer',
                                'text': 'Implement a fixed-size Circular Ring Buffer with push(val) and pop() operations in O(1) time complexity without dynamic memory reallocations during runtime.',
                                'marks': '4 Marks',
                                'sample_answer': 'class CircularBuffer:\n    def __init__(self, capacity: int):\n        self.cap = capacity\n        self.buffer = [0] * capacity\n        self.head = 0\n        self.tail = 0\n        self.size = 0\n\n    def push(self, val: int) -> bool:\n        if self.size == self.cap:\n            return False  # Buffer full\n        self.buffer[self.tail] = val\n        self.tail = (self.tail + 1) % self.cap\n        self.size += 1\n        return True\n\n    def pop(self) -> int:\n        if self.size == 0:\n            return None  # Buffer empty\n        val = self.buffer[self.head]\n        self.head = (self.head + 1) % self.cap\n        self.size -= 1\n        return val',
                                'explanation': 'Using fixed array allocation and head/tail modulo arithmetic allows lock-free and deterministic O(1) ingestion and consumption suitable for vehicle sensor feeds.'
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
