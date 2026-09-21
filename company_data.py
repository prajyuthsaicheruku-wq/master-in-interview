# -*- coding: utf-8 -*-
"""
Central repository of verified, distinct company profiles for the Interview & Placement preparation platform.
Aggregates profiles across:
1. Product & FAANG
2. Banking & Finance
3. Startups & Fintech
4. Core & Semiconductor
5. Consulting & Strategy
6. Service & IT
"""

import os
import sys

# Import company groups
from company_profiles.def_faang import FAANG_COMPANIES
from company_profiles.def_finance import FINANCE_COMPANIES
from company_profiles.def_startups import STARTUP_COMPANIES
from company_profiles.def_semi import SEMI_COMPANIES
from company_profiles.def_consulting import CONSULTING_COMPANIES
from company_profiles.def_service import SERVICE_COMPANIES

# Master combined dictionary
ALL_COMPANY_PROFILES = {}

# Merge all in priority order
for source in [
    FAANG_COMPANIES,
    FINANCE_COMPANIES,
    STARTUP_COMPANIES,
    SEMI_COMPANIES,
    CONSULTING_COMPANIES,
    SERVICE_COMPANIES
]:
    for key, val in source.items():
        ALL_COMPANY_PROFILES[key.strip().lower()] = val

# Mapping of common aliases / variations to canonical profile keys
COMPANY_ALIASES = {
    'tcs': 'tcs digital',
    'tata consultancy services': 'tcs digital',
    'tcs ninja': 'tcs digital',
    'tcs prime': 'tcs digital',
    'infosys sp': 'infosys',
    'infosys dse': 'infosys',
    'infy': 'infosys',
    'cognizant': 'cognizant genc',
    'cognizant next': 'cognizant genc',
    'cognizant genc next': 'cognizant genc',
    'deloitte': 'deloitte nla',
    'deloitte consulting': 'deloitte nla',
    'bcg': 'boston consulting group (bcg)',
    'boston consulting group': 'boston consulting group (bcg)',
    'mckinsey': 'mckinsey & company',
    'mckinsey and company': 'mckinsey & company',
    'ti': 'texas instruments',
    'texas instruments ti': 'texas instruments',
    'jpmorgan': 'jpmorgan chase',
    'jpmc': 'jpmorgan chase',
    'j.p. morgan': 'jpmorgan chase',
    'jp morgan': 'jpmorgan chase',
    'amex': 'american express',
    'american express amex': 'american express',
    'walmart': 'walmart global tech',
    'walmart labs': 'walmart global tech',
    'lti': 'ltimindtree',
    'mindtree': 'ltimindtree',
    'techm': 'tech mahindra',
    'hcl': 'hcltech',
    'hcl technologies': 'hcltech',
    'persistent': 'persistent systems',
    'gs': 'goldman sachs',
    'ms': 'morgan stanley',
}


def get_company_full_profile(company_name: str):
    """
    Lookup full verified company metadata, exam patterns, sectional syllabus, 
    recruitment stages, FAQs, and realistic model question papers.
    """
    if not company_name:
        return None
    
    clean_key = company_name.strip().lower()
    
    # 1. Direct match
    if clean_key in ALL_COMPANY_PROFILES:
        return ALL_COMPANY_PROFILES[clean_key]
    
    # 2. Alias match
    if clean_key in COMPANY_ALIASES:
        target = COMPANY_ALIASES[clean_key]
        if target in ALL_COMPANY_PROFILES:
            return ALL_COMPANY_PROFILES[target]
    
    # 3. Substring match
    for k, profile in ALL_COMPANY_PROFILES.items():
        if k in clean_key or clean_key in k:
            return profile
    
    # 4. Fallback profile
    display_title = company_name.title()
    return {
        'canonical_name': display_title,
        'total_mins': 90,
        'total_qs': 45,
        'roles': f'Software Engineer / Associate Consultant at {display_title}',
        'ctc': '₹6.0 - ₹12.0 LPA',
        'eligibility': 'B.Tech / M.Tech / MCA (60%+ in 10th, 12th & Graduation, no active backlogs)',
        'difficulty': 'Moderate',
        'difficulty_class': 'badge-info',
        'tagline': f'{display_title} recruitment test pattern, quantitative aptitude, technical MCQs & coding challenges.',
        'brand_color': '#2563eb',
        'accent_bg': 'linear-gradient(135deg, #2563eb 0%, #1e293b 100%)',
        'logo_icon': '🏢',
        'logo_image': f'images/{clean_key.replace(" ", "")}.svg',
        'selection_stages': [
            {'step': 1, 'title': f'{display_title} Online Technical Assessment', 'desc': 'Aptitude, Core CS & Coding | 90 Mins', 'icon': '💻'},
            {'step': 2, 'title': 'Technical Interview 1 (DSA & Projects)', 'desc': 'Data Structures & Problem Solving | 45 Mins', 'icon': '⚡'},
            {'step': 3, 'title': 'Technical Interview 2 (System Architecture)', 'desc': 'Databases, OOP & System Concepts | 45 Mins', 'icon': '🧠'},
            {'step': 4, 'title': 'HR & Leadership Fitment', 'desc': 'Culture Fit & Behavioral Scenarios | 30 Mins', 'icon': '🤝'}
        ],
        'table_headers': ['Round', 'Section Details', 'No. of Questions', 'Time Allotted'],
        'table_rounds': [
            {
                'round_name': 'Round 1: Online Assessment',
                'sections': [
                    {'name': 'Quantitative & Logical Aptitude', 'qs': '20 Qs', 'time': '25 Mins'},
                    {'name': 'Core CS & Programming Fundamentals', 'qs': '20 Qs', 'time': '25 Mins'},
                    {'name': 'Hands-on Coding Challenge', 'qs': '2 Qs', 'time': '40 Mins'}
                ]
            },
            {
                'round_name': 'Round 2: Technical Interview',
                'sections': [
                    {'name': 'Problem Solving & System Architecture', 'qs': 'Interview', 'time': '45 Mins'}
                ]
            },
            {
                'round_name': 'Round 3: HR Round',
                'sections': [
                    {'name': 'Behavioral & Leadership Discussion', 'qs': 'Fitment', 'time': '30 Mins'}
                ]
            }
        ],
        'syllabus': [
            {'category': 'Quantitative & Logical Aptitude', 'icon': '🧮', 'qs': '20 Qs', 'time': '25 Mins', 'topics': ['Percentages, Profit & Loss, Ratios', 'Time, Speed & Work Calculations', 'Logical Deductions & Syllogisms', 'Data Interpretation']},
            {'category': 'Computer Science Fundamentals', 'icon': '💻', 'qs': '20 Qs', 'time': '25 Mins', 'topics': ['Object-Oriented Programming (OOP)', 'Database Management Systems & SQL', 'Operating Systems Core Concepts', 'Data Structures (Arrays, Trees, Graphs)']},
            {'category': 'Hands-on Algorithmic Coding', 'icon': '🎯', 'qs': '2 Qs', 'time': '40 Mins', 'topics': ['Two Pointer & Sliding Window', 'Hash Maps & Subarray Sums', 'Dynamic Programming Basics', 'String Pattern Matching']},
            {'category': 'Communication & Behavioral', 'icon': '🗣️', 'qs': 'Interview', 'time': '30 Mins', 'topics': ['STAR Method Responses', 'Conflict Resolution in Teams', 'Project Walkthrough & Key Decisions', 'Cultural & Leadership Alignment']}
        ],
        'faqs': [
            {'q': f'What is the hiring process at {display_title}?', 'a': f'The standard recruitment flow consists of an Online Technical Assessment (Aptitude + Coding), followed by 1-2 Technical Interviews and an HR fitment discussion.'},
            {'q': f'What coding languages are supported at {display_title}?', 'a': 'Most online assessment platforms support Python, Java, C++, and C.'}
        ],
        'past_papers': []
    }


def get_all_companies_hub_data():
    """
    Returns curated metadata for all 46+ companies for rendering the Dream Companies Hub Grid,
    filtering by sector categories, searching, and sorting by CTC/popularity.
    """
    # Curated ordered company definitions matching the visual grid layout
    hub_companies_spec = [
        # Top Prominent Row (Matching exact layout in user mock)
        {'key': 'google', 'category': 'product', 'category_label': 'Product & FAANG', 'locations': 'Bangalore, Hyderabad, Gurugram', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 100, 'min_sal': 20.0, 'max_sal': 55.0},
        {'key': 'amazon', 'category': 'product', 'category_label': 'Product & FAANG', 'locations': 'Bangalore, Hyderabad, Chennai', 'hiring': 'Limited', 'hiring_class': 'status-limited', 'popularity': 99, 'min_sal': 18.0, 'max_sal': 45.0},
        {'key': 'microsoft', 'category': 'product', 'category_label': 'Product & FAANG', 'locations': 'Hyderabad, Bangalore', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 98, 'min_sal': 18.0, 'max_sal': 44.0},
        {'key': 'tcs digital', 'category': 'service', 'category_label': 'Service & IT', 'locations': 'Hyderabad, Mumbai, Pune', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 97, 'min_sal': 3.36, 'max_sal': 11.5},
        {'key': 'accenture', 'category': 'consulting', 'category_label': 'Consulting', 'locations': 'Bangalore, Chennai, Hyderabad', 'hiring': 'Limited', 'hiring_class': 'status-limited', 'popularity': 96, 'min_sal': 4.5, 'max_sal': 12.0},
        {'key': 'deloitte nla', 'category': 'consulting', 'category_label': 'Consulting', 'locations': 'Hyderabad, Bangalore, Chennai', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 95, 'min_sal': 7.6, 'max_sal': 13.5},
        {'key': 'hcltech', 'category': 'service', 'category_label': 'Service & IT', 'locations': 'Noida, Bangalore, Chennai', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 92, 'min_sal': 4.25, 'max_sal': 6.5},
        {'key': 'jpmorgan chase', 'category': 'finance', 'category_label': 'Banking & Finance', 'locations': 'Mumbai, Bengaluru, Delhi', 'hiring': 'Upcoming', 'hiring_class': 'status-upcoming', 'popularity': 94, 'min_sal': 17.0, 'max_sal': 24.0},
        {'key': 'flipkart', 'category': 'startups', 'category_label': 'Startups', 'locations': 'Bangalore, Hyderabad', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 93, 'min_sal': 22.0, 'max_sal': 32.0},
        {'key': 'tesla', 'category': 'semiconductor', 'category_label': 'Core & Semiconductor', 'locations': 'Bangalore, Hyderabad', 'hiring': 'Not Hiring', 'hiring_class': 'status-nothiring', 'popularity': 91, 'min_sal': 15.0, 'max_sal': 60.0},

        # Product & FAANG
        {'key': 'uber', 'category': 'product', 'category_label': 'Product & FAANG', 'locations': 'Bangalore, Hyderabad', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 96, 'min_sal': 38.0, 'max_sal': 52.0},
        {'key': 'salesforce', 'category': 'product', 'category_label': 'Product & FAANG', 'locations': 'Hyderabad, Bangalore', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 93, 'min_sal': 32.0, 'max_sal': 44.0},
        {'key': 'atlassian', 'category': 'product', 'category_label': 'Product & FAANG', 'locations': 'Bengaluru (Remote-First)', 'hiring': 'Limited', 'hiring_class': 'status-limited', 'popularity': 92, 'min_sal': 30.0, 'max_sal': 45.0},
        {'key': 'nvidia', 'category': 'product', 'category_label': 'Product & FAANG', 'locations': 'Bengaluru, Pune, Hyderabad', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 97, 'min_sal': 24.0, 'max_sal': 38.0},
        {'key': 'walmart', 'category': 'product', 'category_label': 'Product & FAANG', 'locations': 'Bengaluru, Chennai, Gurgaon', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 91, 'min_sal': 18.0, 'max_sal': 26.0},
        {'key': 'meta', 'category': 'product', 'category_label': 'Product & FAANG', 'locations': 'Gurugram, Bengaluru', 'hiring': 'Limited', 'hiring_class': 'status-limited', 'popularity': 95, 'min_sal': 35.0, 'max_sal': 60.0},
        {'key': 'netflix', 'category': 'product', 'category_label': 'Product & FAANG', 'locations': 'Mumbai, Bengaluru', 'hiring': 'Upcoming', 'hiring_class': 'status-upcoming', 'popularity': 90, 'min_sal': 35.0, 'max_sal': 65.0},
        {'key': 'apple', 'category': 'product', 'category_label': 'Product & FAANG', 'locations': 'Hyderabad, Bengaluru', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 95, 'min_sal': 28.0, 'max_sal': 48.0},
        {'key': 'oracle', 'category': 'product', 'category_label': 'Product & FAANG', 'locations': 'Bengaluru, Hyderabad, Noida', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 89, 'min_sal': 16.0, 'max_sal': 28.0},
        {'key': 'adobe', 'category': 'product', 'category_label': 'Product & FAANG', 'locations': 'Noida, Bengaluru', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 92, 'min_sal': 24.0, 'max_sal': 40.0},

        # Banking & Finance
        {'key': 'goldman sachs', 'category': 'finance', 'category_label': 'Banking & Finance', 'locations': 'Bengaluru, Hyderabad', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 95, 'min_sal': 24.0, 'max_sal': 34.0},
        {'key': 'morgan stanley', 'category': 'finance', 'category_label': 'Banking & Finance', 'locations': 'Mumbai, Bengaluru', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 92, 'min_sal': 20.0, 'max_sal': 28.0},
        {'key': 'american express', 'category': 'finance', 'category_label': 'Banking & Finance', 'locations': 'Gurugram, Bengaluru', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 89, 'min_sal': 16.0, 'max_sal': 24.0},
        {'key': 'barclays', 'category': 'finance', 'category_label': 'Banking & Finance', 'locations': 'Pune, Chennai', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 88, 'min_sal': 14.0, 'max_sal': 20.0},

        # Startups
        {'key': 'razorpay', 'category': 'startups', 'category_label': 'Startups', 'locations': 'Bengaluru', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 91, 'min_sal': 22.0, 'max_sal': 32.0},
        {'key': 'phonepe', 'category': 'startups', 'category_label': 'Startups', 'locations': 'Bengaluru, Pune', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 93, 'min_sal': 24.0, 'max_sal': 36.0},
        {'key': 'swiggy', 'category': 'startups', 'category_label': 'Startups', 'locations': 'Bengaluru', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 90, 'min_sal': 18.0, 'max_sal': 28.0},
        {'key': 'zomato', 'category': 'startups', 'category_label': 'Startups', 'locations': 'Gurugram, Bengaluru', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 89, 'min_sal': 16.0, 'max_sal': 26.0},

        # Core & Semiconductor
        {'key': 'texas instruments', 'category': 'semiconductor', 'category_label': 'Core & Semiconductor', 'locations': 'Bangalore, Hyderabad', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 91, 'min_sal': 18.0, 'max_sal': 26.0},
        {'key': 'amd', 'category': 'semiconductor', 'category_label': 'Core & Semiconductor', 'locations': 'Hyderabad, Bengaluru', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 90, 'min_sal': 18.0, 'max_sal': 28.0},
        {'key': 'qualcomm', 'category': 'semiconductor', 'category_label': 'Core & Semiconductor', 'locations': 'Hyderabad, Bengaluru, Chennai', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 92, 'min_sal': 18.5, 'max_sal': 28.0},
        {'key': 'broadcom', 'category': 'semiconductor', 'category_label': 'Core & Semiconductor', 'locations': 'Bengaluru, Hyderabad', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 89, 'min_sal': 20.0, 'max_sal': 30.0},
        {'key': 'micron', 'category': 'semiconductor', 'category_label': 'Core & Semiconductor', 'locations': 'Hyderabad, Sanand', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 88, 'min_sal': 15.0, 'max_sal': 24.0},

        # Consulting
        {'key': 'mckinsey & company', 'category': 'consulting', 'category_label': 'Consulting', 'locations': 'Gurugram, Mumbai, Bengaluru', 'hiring': 'Limited', 'hiring_class': 'status-limited', 'popularity': 94, 'min_sal': 22.0, 'max_sal': 32.0},
        {'key': 'boston consulting group (bcg)', 'category': 'consulting', 'category_label': 'Consulting', 'locations': 'Mumbai, New Delhi, Bengaluru', 'hiring': 'Limited', 'hiring_class': 'status-limited', 'popularity': 93, 'min_sal': 22.0, 'max_sal': 32.0},
        {'key': 'ey', 'category': 'consulting', 'category_label': 'Consulting', 'locations': 'Bengaluru, Gurugram, Hyderabad', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 90, 'min_sal': 8.0, 'max_sal': 12.5},
        {'key': 'pwc', 'category': 'consulting', 'category_label': 'Consulting', 'locations': 'Kolkata, Mumbai, Bengaluru', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 90, 'min_sal': 8.5, 'max_sal': 13.5},
        {'key': 'kpmg', 'category': 'consulting', 'category_label': 'Consulting', 'locations': 'Mumbai, Gurugram, Bengaluru', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 89, 'min_sal': 8.0, 'max_sal': 12.5},

        # Service & IT
        {'key': 'infosys', 'category': 'service', 'category_label': 'Service & IT', 'locations': 'Bengaluru, Pune, Hyderabad, Chennai', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 94, 'min_sal': 3.6, 'max_sal': 9.5},
        {'key': 'wipro', 'category': 'service', 'category_label': 'Service & IT', 'locations': 'Bengaluru, Hyderabad, Chennai', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 91, 'min_sal': 3.5, 'max_sal': 6.5},
        {'key': 'capgemini', 'category': 'service', 'category_label': 'Service & IT', 'locations': 'Mumbai, Bengaluru, Pune, Hyderabad', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 91, 'min_sal': 4.25, 'max_sal': 7.5},
        {'key': 'cognizant genc', 'category': 'service', 'category_label': 'Service & IT', 'locations': 'Chennai, Coimbatore, Bengaluru', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 92, 'min_sal': 4.0, 'max_sal': 9.0},
        {'key': 'tech mahindra', 'category': 'service', 'category_label': 'Service & IT', 'locations': 'Pune, Hyderabad, Noida, Bengaluru', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 88, 'min_sal': 3.25, 'max_sal': 5.5},
        {'key': 'ltimindtree', 'category': 'service', 'category_label': 'Service & IT', 'locations': 'Mumbai, Bengaluru, Chennai, Pune', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 89, 'min_sal': 4.0, 'max_sal': 6.5},
        {'key': 'mphasis', 'category': 'service', 'category_label': 'Service & IT', 'locations': 'Bengaluru, Chennai, Pune', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 86, 'min_sal': 3.5, 'max_sal': 5.0},
        {'key': 'hexaware', 'category': 'service', 'category_label': 'Service & IT', 'locations': 'Navi Mumbai, Chennai, Pune', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 87, 'min_sal': 4.0, 'max_sal': 6.0},
        {'key': 'persistent systems', 'category': 'service', 'category_label': 'Service & IT', 'locations': 'Pune, Hyderabad, Bengaluru, Goa', 'hiring': 'Hiring', 'hiring_class': 'status-hiring', 'popularity': 88, 'min_sal': 5.0, 'max_sal': 9.0},
    ]

    result = []
    for item in hub_companies_spec:
        prof = get_company_full_profile(item['key']) or {}
        c_name = prof.get('canonical_name', item['key'].title())
        logo_img = prof.get('logo_image', f"images/{item['key'].replace(' ', '')}.svg")
        ctc_str = prof.get('ctc', f"₹{item['min_sal']} - ₹{item['max_sal']} LPA")

        result.append({
            'name': c_name,
            'canonical_name': c_name,
            'category': item['category'],
            'category_label': item['category_label'],
            'cat_slug': f"cat-{item['category']}",
            'locations': item['locations'],
            'hiring_status': item['hiring'],
            'hiring_class': item['hiring_class'],
            'logo_image': logo_img,
            'ctc': ctc_str,
            'min_sal': item['min_sal'],
            'max_sal': item['max_sal'],
            'popularity': item['popularity'],
            'roles': prof.get('roles', f'Software Engineer at {c_name}'),
            'tagline': prof.get('tagline', '')
        })

    return result

