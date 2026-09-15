document.addEventListener('DOMContentLoaded', () => {
    const loginTabBtn = document.getElementById('loginTabBtn');
    const registerTabBtn = document.getElementById('registerTabBtn');
    const loginForm = document.getElementById('loginForm');
    const registerContainer = document.getElementById('registerContainer');
    const resetForm = document.getElementById('resetForm');
    const forgotPasswordBtn = document.getElementById('forgotPasswordBtn');
    const backToLoginBtn = document.getElementById('backToLoginBtn');

    if (loginTabBtn && registerTabBtn && loginForm && registerContainer) {
        loginTabBtn.addEventListener('click', () => {
            loginTabBtn.classList.add('active');
            registerTabBtn.classList.remove('active');
            loginForm.style.display = 'block';
            registerContainer.style.display = 'none';
            if (resetForm) resetForm.style.display = 'none';
        });

        registerTabBtn.addEventListener('click', () => {
            registerTabBtn.classList.add('active');
            loginTabBtn.classList.remove('active');
            registerContainer.style.display = 'block';
            loginForm.style.display = 'none';
            if (resetForm) resetForm.style.display = 'none';
        });
    }

    if (forgotPasswordBtn && resetForm) {
        forgotPasswordBtn.addEventListener('click', (e) => {
            e.preventDefault();
            loginForm.style.display = 'none';
            if (registerContainer) registerContainer.style.display = 'none';
            resetForm.style.display = 'block';
        });
    }

    if (backToLoginBtn && loginForm) {
        backToLoginBtn.addEventListener('click', (e) => {
            e.preventDefault();
            resetForm.style.display = 'none';
            if (registerContainer) registerContainer.style.display = 'none';
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

    // PWA Service Worker
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/static/sw.js').catch(err => {
            console.log('ServiceWorker registration failed: ', err);
        });
    }
});

// --- BREVO OTP REGISTRATION LOGIC ---
let resendTimerInterval = null;

function showAlert(elementId, message, type = 'danger') {
    const el = document.getElementById(elementId);
    if (!el) return;
    el.style.display = 'block';
    el.className = 'alert-box';
    if (type === 'danger') {
        el.style.background = 'rgba(239, 68, 68, 0.15)';
        el.style.border = '1px solid rgba(239, 68, 68, 0.4)';
        el.style.color = '#fca5a5';
    } else if (type === 'success') {
        el.style.background = 'rgba(34, 197, 94, 0.15)';
        el.style.border = '1px solid rgba(34, 197, 94, 0.4)';
        el.style.color = '#86efac';
    }
    el.style.padding = '0.65rem 0.9rem';
    el.style.borderRadius = '8px';
    el.style.fontSize = '0.85rem';
    el.innerHTML = message;
}

function hideAlert(elementId) {
    const el = document.getElementById(elementId);
    if (el) el.style.display = 'none';
}

async function handleSendOtp(e) {
    if (e) e.preventDefault();
    hideAlert('step1Alert');

    const username = document.getElementById('regUsername').value.trim();
    const email = document.getElementById('regEmail').value.trim();
    const password = document.getElementById('regPassword').value;

    if (!username || !email || !password) {
        showAlert('step1Alert', 'Please fill in all required fields.');
        return;
    }

    const btn = document.getElementById('sendOtpBtn');
    const spinner = document.getElementById('sendOtpSpinner');
    btn.disabled = true;
    if (spinner) spinner.style.display = 'inline';

    try {
        const res = await fetch('/api/auth/send-register-otp', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, email, password })
        });
        const data = await res.json();

        if (res.ok && data.success) {
            // Transition to Step 2
            document.getElementById('registerFormStep1').style.display = 'none';
            document.getElementById('registerFormStep2').style.display = 'block';
            document.getElementById('displayTargetEmail').textContent = email;
            document.getElementById('regOtpCode').value = '';
            document.getElementById('regOtpCode').focus();

            startResendCountdown(45);
        } else {
            showAlert('step1Alert', data.message || 'Failed to send OTP. Please try again.');
        }
    } catch (err) {
        showAlert('step1Alert', 'Network error. Please try again.');
    } finally {
        btn.disabled = false;
        if (spinner) spinner.style.display = 'none';
    }
}

async function handleVerifyOtp(e) {
    if (e) e.preventDefault();
    hideAlert('step2Alert');

    const username = document.getElementById('regUsername').value.trim();
    const email = document.getElementById('regEmail').value.trim();
    const password = document.getElementById('regPassword').value;
    const target_role = document.getElementById('targetRole').value;
    const otp_code = document.getElementById('regOtpCode').value.trim();

    if (!otp_code || otp_code.length !== 6) {
        showAlert('step2Alert', 'Please enter the 6-digit OTP code.');
        return;
    }

    const btn = document.getElementById('verifyOtpBtn');
    const spinner = document.getElementById('verifySpinner');
    btn.disabled = true;
    if (spinner) spinner.style.display = 'inline';

    try {
        const res = await fetch('/api/auth/verify-register-otp', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, email, password, target_role, otp_code })
        });
        const data = await res.json();

        if (res.ok && data.success) {
            showAlert('step2Alert', '✅ OTP Verified! Redirecting to Dashboard...', 'success');
            setTimeout(() => {
                window.location.href = data.redirect_url || '/';
            }, 800);
        } else {
            showAlert('step2Alert', data.message || 'Invalid or expired OTP.');
            btn.disabled = false;
            if (spinner) spinner.style.display = 'none';
        }
    } catch (err) {
        showAlert('step2Alert', 'Network error during verification.');
        btn.disabled = false;
        if (spinner) spinner.style.display = 'none';
    }
}

function startResendCountdown(seconds) {
    const resendBtn = document.getElementById('resendOtpBtn');
    const countdownSpan = document.getElementById('resendCountdown');
    if (!resendBtn || !countdownSpan) return;

    if (resendTimerInterval) clearInterval(resendTimerInterval);
    resendBtn.disabled = true;
    let remaining = seconds;
    countdownSpan.textContent = remaining;

    resendTimerInterval = setInterval(() => {
        remaining -= 1;
        countdownSpan.textContent = remaining;
        if (remaining <= 0) {
            clearInterval(resendTimerInterval);
            resendBtn.disabled = false;
            resendBtn.innerHTML = 'Resend OTP';
        }
    }, 1000);
}

async function resendOtpCode() {
    hideAlert('step2Alert');
    const username = document.getElementById('regUsername').value.trim();
    const email = document.getElementById('regEmail').value.trim();
    const password = document.getElementById('regPassword').value;

    const resendBtn = document.getElementById('resendOtpBtn');
    resendBtn.disabled = true;
    resendBtn.textContent = 'Sending...';

    try {
        const res = await fetch('/api/auth/send-register-otp', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, email, password })
        });
        const data = await res.json();
        if (res.ok && data.success) {
            showAlert('step2Alert', '✅ New verification code sent to your email!', 'success');
            startResendCountdown(45);
        } else {
            showAlert('step2Alert', data.message || 'Failed to resend code.');
            resendBtn.disabled = false;
            resendBtn.textContent = 'Resend OTP';
        }
    } catch (err) {
        showAlert('step2Alert', 'Network error. Please try again.');
        resendBtn.disabled = false;
        resendBtn.textContent = 'Resend OTP';
    }
}

function goBackToStep1() {
    hideAlert('step1Alert');
    hideAlert('step2Alert');
    document.getElementById('registerFormStep2').style.display = 'none';
    document.getElementById('registerFormStep1').style.display = 'block';
}

// --- PWA APP INSTALL PROMPT ---
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
            console.log('User accepted PWA install');
        }
        deferredInstallPrompt = null;
    } else {
        alert('📲 To install InterviewMaster App on your device:\n\n1. Chrome/Edge (Desktop): Click Install icon (⊕) in address bar.\n2. Android: Tap (⋮) -> Add to Home screen.\n3. iOS Safari: Tap Share (⎋) -> Add to Home Screen.');
    }
};
