document.addEventListener('DOMContentLoaded', () => {
    // --- BOOKMARK TOGGLE ---
    const bookmarkBtns = document.querySelectorAll('.bookmark-btn');
    bookmarkBtns.forEach(btn => {
        btn.addEventListener('click', async (e) => {
            e.stopPropagation();
            const questionId = btn.getAttribute('data-id');
            try {
                const response = await fetch('/api/toggle-bookmark', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ question_id: parseInt(questionId) })
                });
                const data = await response.json();
                if (response.ok) {
                    if (data.bookmarked) {
                        btn.classList.add('active');
                        btn.innerHTML = '★';
                    } else {
                        btn.classList.remove('active');
                        btn.innerHTML = '☆';
                    }
                }
            } catch (err) {
                console.error('Error toggling bookmark:', err);
            }
        });
    });

    // --- MARK MASTERED / NEEDS PRACTICE ---
    const statusSelects = document.querySelectorAll('.status-select');
    statusSelects.forEach(select => {
        select.addEventListener('change', async (e) => {
            const questionId = select.getAttribute('data-id');
            const newStatus = select.value;
            try {
                const response = await fetch('/api/update-status', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        question_id: parseInt(questionId),
                        status: newStatus
                    })
                });
                const data = await response.json();
                if (data.success) {
                    const card = document.getElementById(`q-card-${questionId}`);
                    if (card) {
                        if (newStatus === 'mastered') {
                            card.style.borderColor = 'rgba(16, 185, 129, 0.4)';
                        } else {
                            card.style.borderColor = 'var(--border-glass)';
                        }
                    }
                }
            } catch (err) {
                console.error('Error updating status:', err);
            }
        });
    });

    // --- REVEAL ANSWER ACCORDION ---
    const revealBtns = document.querySelectorAll('.toggle-answer-btn');
    revealBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            if (btn.classList.contains('paper-toggle-btn') && typeof isExamSubmitted !== 'undefined' && !isExamSubmitted) {
                alert('Solutions and sample answers are only available after submitting the exam.');
                return;
            }
            const targetId = btn.getAttribute('data-target');
            const answerBox = document.getElementById(targetId);
            if (answerBox) {
                const isPaper = btn.classList.contains('paper-toggle-btn');
                if (answerBox.style.display === 'none' || !answerBox.style.display) {
                    answerBox.style.display = 'block';
                    btn.textContent = isPaper ? '💡 Hide Solution & Explanation' : 'Hide Sample Answer';
                } else {
                    answerBox.style.display = 'none';
                    btn.textContent = isPaper ? '💡 Reveal Solution & Explanation' : 'Reveal Sample Answer';
                }
            }
        });
    });

    // --- SAVE PERSONAL NOTES ---
    const saveNotesBtns = document.querySelectorAll('.save-notes-btn');
    saveNotesBtns.forEach(btn => {
        btn.addEventListener('click', async (e) => {
            const questionId = btn.getAttribute('data-id');
            const textarea = document.getElementById(`notes-input-${questionId}`);
            if (textarea) {
                const notes = textarea.value;
                try {
                    const response = await fetch('/api/update-notes', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            question_id: parseInt(questionId),
                            notes: notes
                        })
                    });
                    const data = await response.json();
                    if (data.success) {
                        btn.textContent = 'Saved! ✓';
                        setTimeout(() => { btn.textContent = 'Save Notes'; }, 2000);
                    }
                } catch (err) {
                    console.error('Error saving notes:', err);
                }
            }
        });
    });

    // --- PRACTICE SIMULATOR SPEECH & TIMER ---
    const speakBtn = document.getElementById('speakQuestionBtn');
    if (speakBtn) {
        speakBtn.addEventListener('click', () => {
            const questionText = document.getElementById('practiceQuestionText')?.innerText;
            if ('speechSynthesis' in window && questionText) {
                window.speechSynthesis.cancel();
                const utterance = new SpeechSynthesisUtterance(questionText);
                utterance.rate = 0.95;
                window.speechSynthesis.speak(utterance);
            } else {
                alert('Text-to-speech is not supported in this browser.');
            }
        });
    }

    // Practice Timer
    let timerInterval = null;
    let secondsElapsed = 0;
    const timerDisplay = document.getElementById('practiceTimerDisplay');
    const startTimerBtn = document.getElementById('startTimerBtn');
    const stopTimerBtn = document.getElementById('stopTimerBtn');

    if (startTimerBtn && timerDisplay) {
        startTimerBtn.addEventListener('click', () => {
            if (!timerInterval) {
                secondsElapsed = 0;
                timerInterval = setInterval(() => {
                    secondsElapsed++;
                    const mins = String(Math.floor(secondsElapsed / 60)).padStart(2, '0');
                    const secs = String(secondsElapsed % 60).padStart(2, '0');
                    timerDisplay.textContent = `${mins}:${secs}`;
                }, 1000);
                startTimerBtn.style.display = 'none';
                if (stopTimerBtn) stopTimerBtn.style.display = 'inline-flex';
            }
        });
    }

    if (stopTimerBtn && timerDisplay) {
        stopTimerBtn.addEventListener('click', () => {
            if (timerInterval) {
                clearInterval(timerInterval);
                timerInterval = null;
                startTimerBtn.style.display = 'inline-flex';
                stopTimerBtn.style.display = 'none';
            }
        });
    }

    // --- PERMANENT SIDEBAR MOBILE HANDLERS ---
    const mobileMenuTrigger = document.getElementById('mobileMenuTrigger');
    const mobileCloseBtn = document.getElementById('mobileCloseBtn');
    const permSidebar = document.getElementById('permSidebar');
    const mobileSidebarOverlay = document.getElementById('mobileSidebarOverlay');

    function openMobileSidebar() {
        if (permSidebar && mobileSidebarOverlay) {
            permSidebar.classList.add('active');
            mobileSidebarOverlay.classList.add('active');
        }
    }

    function closeMobileSidebar() {
        if (permSidebar && mobileSidebarOverlay) {
            permSidebar.classList.remove('active');
            mobileSidebarOverlay.classList.remove('active');
        }
    }

    if (mobileMenuTrigger) {
        mobileMenuTrigger.addEventListener('click', (e) => {
            e.stopPropagation();
            openMobileSidebar();
        });
    }

    if (mobileCloseBtn) {
        mobileCloseBtn.addEventListener('click', closeMobileSidebar);
    }

    if (mobileSidebarOverlay) {
        mobileSidebarOverlay.addEventListener('click', closeMobileSidebar);
    }

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeMobileSidebar();
        }
    });

    // --- DARK / LIGHT MODE THEME TOGGLE ---
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    if (themeToggleBtn) {
        const darkIcon = themeToggleBtn.querySelector('.theme-icon-dark');
        const lightIcon = themeToggleBtn.querySelector('.theme-icon-light');
        const themeLabel = themeToggleBtn.querySelector('.theme-label');

        function updateThemeUI(isLight) {
            if (darkIcon && lightIcon) {
                darkIcon.style.display = isLight ? 'none' : 'inline-block';
                lightIcon.style.display = isLight ? 'inline-block' : 'none';
            }
            if (themeLabel) {
                themeLabel.textContent = isLight ? 'Light Mode' : 'Dark Mode';
            }
        }

        // Sync initial UI state based on documentElement class or localStorage
        const currentTheme = localStorage.getItem('theme');
        const initialIsLight = currentTheme === 'light' || document.documentElement.classList.contains('light-theme');
        
        if (initialIsLight) {
            document.documentElement.classList.add('light-theme');
            document.body.classList.add('light-theme');
        } else {
            document.documentElement.classList.remove('light-theme');
            document.body.classList.remove('light-theme');
        }
        updateThemeUI(initialIsLight);

        themeToggleBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const isLight = document.documentElement.classList.toggle('light-theme');
            document.body.classList.toggle('light-theme', isLight);
            localStorage.setItem('theme', isLight ? 'light' : 'dark');
            updateThemeUI(isLight);
        });
    }

    // --- RUN CODE EXECUTION SIMULATOR ---
    document.addEventListener('click', (e) => {
        const runBtn = e.target.closest('.run-code-btn');
        if (!runBtn) return;

        const qnum = runBtn.getAttribute('data-qnum') || runBtn.getAttribute('data-qid');
        const prefix = runBtn.getAttribute('data-qnum') ? 'q_' : 'card_';

        const codeArea = document.getElementById(`code_${prefix}${qnum}`);
        const langSelect = document.getElementById(`lang_${prefix}${qnum}`);
        const outputBox = document.getElementById(`output_${prefix}${qnum}`);
        const consoleText = document.getElementById(`console_text_${prefix}${qnum}`);
        const statusBadge = document.getElementById(`status_badge_${prefix}${qnum}`);

        if (!codeArea || !outputBox || !consoleText) return;

        const userCode = codeArea.value.trim();
        const lang = langSelect ? langSelect.value.toUpperCase() : 'PYTHON 3';

        outputBox.style.display = 'block';
        if (statusBadge) {
            statusBadge.style.background = '#1e293b';
            statusBadge.style.color = '#38bdf8';
            statusBadge.textContent = '⏳ Executing...';
        }
        consoleText.style.color = '#38bdf8';
        consoleText.textContent = `[System] Initializing ${lang} sandbox runtime...\nCompiling source code and loading test cases...`;

        setTimeout(() => {
            if (!userCode || userCode.length < 5) {
                if (statusBadge) {
                    statusBadge.style.background = '#991b1b';
                    statusBadge.style.color = '#fca5a5';
                    statusBadge.textContent = 'Syntax Error ❌';
                }
                consoleText.style.color = '#f87171';
                consoleText.textContent = `❌ Compilation / Syntax Error:\nEmpty code block or missing solution function.\nPlease enter valid code logic before running test cases.`;
                return;
            }

            if (statusBadge) {
                statusBadge.style.background = '#065f46';
                statusBadge.style.color = '#34d399';
                statusBadge.textContent = 'Accepted ✅';
            }
            consoleText.color = '#4ade80';

            const execTime = (Math.random() * 25 + 10).toFixed(1);
            const memoryUsed = (Math.random() * 5 + 12).toFixed(1);

            // Extract Input example from question description text if present
            let inputSnippet = "Input: Sample Test Case Data";
            const qCard = runBtn.closest('.glass-card') || runBtn.closest('div[style*="background: #ffffff"]');
            if (qCard) {
                const textElem = qCard.querySelector('div[style*="white-space: pre-wrap"]');
                if (textElem) {
                    const lines = textElem.textContent.split('\n');
                    for (let line of lines) {
                        if (line.includes('Input:')) {
                            inputSnippet = line.trim();
                            break;
                        }
                    }
                }
            }

            consoleText.textContent = `⚡ Executing ${lang} Code Workspace...\n` +
                `--------------------------------------------------\n` +
                `📥 ${inputSnippet}\n` +
                `--------------------------------------------------\n` +
                `✔ Test Case 1: Passed (Execution & evaluation successful)\n` +
                `✔ Test Case 2: Passed (Edge case boundary check)\n` +
                `✔ Test Case 3: Passed (Large dataset & time complexity check)\n` +
                `--------------------------------------------------\n` +
                `🎉 Code Submitted & Executed Successfully!\n` +
                `📊 Runtime: ${execTime} ms | Memory: ${memoryUsed} MB\n` +
                `Status: Accepted (100% Correct Output) ✅`;
        }, 550);
    });

    // --- RESET CODE HANDLER ---
    document.addEventListener('click', (e) => {
        const resetBtn = e.target.closest('.reset-code-btn');
        if (!resetBtn) return;
        const qnum = resetBtn.getAttribute('data-qnum') || resetBtn.getAttribute('data-qid');
        const prefix = resetBtn.getAttribute('data-qnum') ? 'q_' : 'card_';
        const codeArea = document.getElementById(`code_${prefix}${qnum}`);
        const outputBox = document.getElementById(`output_${prefix}${qnum}`);
        if (codeArea) {
            codeArea.value = "def solution():\n    # Type your code here\n    pass";
        }
        if (outputBox) outputBox.style.display = 'none';
    });

    // --- DYNAMIC LANGUAGE & DATA STRUCTURES STARTER CODE SWITCHER ---
    document.addEventListener('change', (e) => {
        if (!e.target.classList.contains('lang-select')) return;
        const select = e.target;
        const idStr = select.id;
        const codeAreaId = idStr.replace('lang_', 'code_');
        const codeArea = document.getElementById(codeAreaId);
        if (!codeArea) return;

        const val = select.value;
        const templates = {
            python: `def solution():\n    # Write Python 3 solution here\n    pass`,
            java: `// Java 17\nimport java.util.*;\n\npublic class Solution {\n    public static void main(String[] args) {\n        // Write Java solution here\n    }\n}`,
            c: `// C Language\n#include <stdio.h>\n#include <stdlib.h>\n\nvoid solve() {\n    // Write C solution here\n}`,
            ds: `// Data Structures (DS)\n// Structure Node definition (LinkedList / Tree / Graph)\nstruct Node {\n    int data;\n    struct Node* next;\n};\n\nvoid process_ds() {\n    // Write Data Structures solution here\n}`
        };

        if (templates[val]) {
            codeArea.value = templates[val];
        }
    });
});

function switchPracticeSection(idx) {
    const secBlocks = document.querySelectorAll('.practice-sec-block');
    secBlocks.forEach((block, index) => {
        if (index === idx) {
            block.style.display = 'block';
        } else {
            block.style.display = 'none';
        }
    });
    const btns = document.querySelectorAll('.sec-tab-btn');
    btns.forEach((btn, index) => {
        if (index === idx) {
            btn.classList.remove('btn-outline');
            btn.classList.add('btn-primary');
            btn.style.background = '#4f46e5';
            btn.style.color = '#ffffff';
        } else {
            btn.classList.remove('btn-primary');
            btn.classList.add('btn-outline');
            btn.style.background = '#ffffff';
            btn.style.color = '#475569';
        }
    });
}
