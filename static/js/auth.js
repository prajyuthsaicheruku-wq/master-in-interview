document.addEventListener('DOMContentLoaded', () => {
    const loginTabBtn = document.getElementById('loginTabBtn');
    const registerTabBtn = document.getElementById('registerTabBtn');
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const resetForm = document.getElementById('resetForm');
    const forgotPasswordBtn = document.getElementById('forgotPasswordBtn');
    const backToLoginBtn = document.getElementById('backToLoginBtn');

    if (loginTabBtn && registerTabBtn && loginForm && registerForm) {
        loginTabBtn.addEventListener('click', () => {
            loginTabBtn.classList.add('active');
            registerTabBtn.classList.remove('active');
            loginForm.style.display = 'block';
            registerForm.style.display = 'none';
            if (resetForm) resetForm.style.display = 'none';
        });

        registerTabBtn.addEventListener('click', () => {
            registerTabBtn.classList.add('active');
            loginTabBtn.classList.remove('active');
            registerForm.style.display = 'block';
            loginForm.style.display = 'none';
            if (resetForm) resetForm.style.display = 'none';
        });
    }

    if (forgotPasswordBtn && resetForm) {
        forgotPasswordBtn.addEventListener('click', (e) => {
            e.preventDefault();
            loginForm.style.display = 'none';
            registerForm.style.display = 'none';
            resetForm.style.display = 'block';
        });
    }

    if (backToLoginBtn && loginForm) {
        backToLoginBtn.addEventListener('click', (e) => {
            e.preventDefault();
            resetForm.style.display = 'none';
            registerForm.style.display = 'none';
            loginForm.style.display = 'block';
            loginTabBtn.classList.add('active');
            registerTabBtn.classList.remove('active');
        });
    }

    // Toggle password visibility
    const togglePasswordBtns = document.querySelectorAll('.toggle-password');
    togglePasswordBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const inputId = e.currentTarget.getAttribute('data-target');
            const input = document.getElementById(inputId);
            if (input) {
                if (input.type === 'password') {
                    input.type = 'text';
                    e.currentTarget.textContent = '👁️‍🗨️';
                } else {
                    input.type = 'password';
                    e.currentTarget.textContent = '👁️';
                }
            }
        });
    });

    // --- PWA SERVICE WORKER & APP INSTALL PROMPT ---
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/static/sw.js').catch(err => {
            console.log('ServiceWorker registration failed: ', err);
        });
    }

    if (pwaInstallNavBtn) pwaInstallNavBtn.addEventListener('click', () => window.triggerPWAInstall());
    if (pwaInstallCardBtn) pwaInstallCardBtn.addEventListener('click', () => window.triggerPWAInstall());
});

let deferredInstallPrompt = null;

window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredInstallPrompt = e;
});

window.triggerPWAInstall = async function() {
    if (deferredInstallPrompt) {
        deferredInstallPrompt.prompt();
        const choiceResult = await deferredInstallPrompt.userChoice;
        if (choiceResult.outcome === 'accepted') {
            console.log('User accepted the PWA install prompt');
        }
        deferredInstallPrompt = null;
    } else {
        alert('📲 To install InterviewMaster App on your device:\n\n1. Chrome/Edge (Desktop): Click the Install icon (⊕) in the right side of your browser address bar.\n2. Android (Chrome): Tap menu (⋮) -> "Add to Home screen" or "Install app".\n3. iPhone/iPad (Safari): Tap Share button (⎋) -> "Add to Home Screen".');
    }
};

