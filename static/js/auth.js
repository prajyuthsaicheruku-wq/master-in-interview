// --- AUTHENTICATION & TAB SWITCHING LOGIC ---
function switchAuthTab(mode) {
    const loginTabBtn = document.getElementById('loginTabBtn');
    const registerTabBtn = document.getElementById('registerTabBtn');
    const loginForm = document.getElementById('loginForm');
    const registerContainer = document.getElementById('registerContainer');
    const resetContainer = document.getElementById('resetContainer');
    const regStep1 = document.getElementById('registerFormStep1');
    const regStep2 = document.getElementById('registerFormStep2');
    const resetStep1 = document.getElementById('resetFormStep1');
    const resetSuccessState = document.getElementById('resetSuccessState');

    // Hide any active alerts
    hideAlert('step1Alert');
    hideAlert('step2Alert');
    hideAlert('resetStep1Alert');

    if (mode === 'register') {
        if (registerTabBtn) registerTabBtn.classList.add('active');
        if (loginTabBtn) loginTabBtn.classList.remove('active');
        if (loginForm) loginForm.style.display = 'none';
        if (resetContainer) resetContainer.style.display = 'none';
        if (registerContainer) {
            registerContainer.style.display = 'block';
            if (regStep1) regStep1.style.display = 'block';
            if (regStep2) regStep2.style.display = 'none';
        }
    } else if (mode === 'reset') {
        if (loginTabBtn) loginTabBtn.classList.remove('active');
        if (registerTabBtn) registerTabBtn.classList.remove('active');
        if (loginForm) loginForm.style.display = 'none';
        if (registerContainer) registerContainer.style.display = 'none';
        if (resetContainer) {
            resetContainer.style.display = 'block';
            if (resetStep1) resetStep1.style.display = 'block';
            if (resetSuccessState) resetSuccessState.style.display = 'none';
        }
    } else {
        // Default: login
        if (loginTabBtn) loginTabBtn.classList.add('active');
        if (registerTabBtn) registerTabBtn.classList.remove('active');
        if (loginForm) loginForm.style.display = 'block';
        if (registerContainer) registerContainer.style.display = 'none';
        if (resetContainer) resetContainer.style.display = 'none';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const loginTabBtn = document.getElementById('loginTabBtn');
    const registerTabBtn = document.getElementById('registerTabBtn');
    const forgotPasswordBtn = document.getElementById('forgotPasswordBtn');

    if (loginTabBtn) loginTabBtn.addEventListener('click', () => switchAuthTab('login'));
    if (registerTabBtn) registerTabBtn.addEventListener('click', () => switchAuthTab('register'));
    if (forgotPasswordBtn) forgotPasswordBtn.addEventListener('click', (e) => {
        e.preventDefault();
        switchAuthTab('reset');
    });

    // Auto-verify register OTP when 6 numeric digits are entered
    const otpInput = document.getElementById('regOtpCode');
    if (otpInput) {
        otpInput.addEventListener('input', (e) => {
            e.target.value = e.target.value.replace(/[^0-9]/g, '');
            if (e.target.value.length === 6) {
                handleVerifyOtp();
            }
        });
    }

    // Auto-format reset OTP
    const resetOtpInput = document.getElementById('resetOtpCode');
    if (resetOtpInput) {
        resetOtpInput.addEventListener('input', (e) => {
            e.target.value = e.target.value.replace(/[^0-9]/g, '');
        });
    }

    // Toggle password visibility function with crisp SVG icons
    const SVG_EYE_OPEN = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>';
    const SVG_EYE_SLASH = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line></svg>';

    window.togglePasswordVisibility = function(inputId, btn) {
        const input = document.getElementById(inputId);
        if (!input) return;
        if (input.type === 'password') {
            input.type = 'text';
            if (btn) {
                btn.innerHTML = SVG_EYE_OPEN;
                btn.title = 'Hide password';
                btn.setAttribute('aria-label', 'Hide password');
                btn.style.color = '#4f46e5';
            }
        } else {
            input.type = 'password';
            if (btn) {
                btn.innerHTML = SVG_EYE_SLASH;
                btn.title = 'Show password';
                btn.setAttribute('aria-label', 'Show password');
                btn.style.color = 'var(--text-muted)';
            }
        }
    };

    // PWA Service Worker
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/static/sw.js').catch(err => {
            console.log('ServiceWorker registration failed: ', err);
        });
    }
});

// --- BREVO OTP REGISTRATION LOGIC ---
let resendTimerInterval = null;
let resetResendTimerInterval = null;

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
    if (e && e.preventDefault) e.preventDefault();
    hideAlert('step1Alert');

    const username = document.getElementById('regUsername').value.trim();
    const email = document.getElementById('regEmail').value.trim();
    const password = document.getElementById('regPassword').value;

    if (!username || !email || !password) {
        showAlert('step1Alert', '⚠️ Please fill in all required fields.');
        return false;
    }

    if (username.length < 3) {
        showAlert('step1Alert', '⚠️ Username must be at least 3 characters long.');
        return false;
    }

    if (password.length < 6) {
        showAlert('step1Alert', '⚠️ Password must be at least 6 characters long.');
        return false;
    }

    const btn = document.getElementById('sendOtpBtn');
    btn.disabled = true;
    const origHtml = btn.innerHTML;
    btn.innerHTML = '<span>📨 Sending verification OTP...</span>';

    try {
        const res = await fetch('/api/auth/send-register-otp', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, email, password })
        });
        const data = await res.json();

        if (res.ok && data.success) {
            document.getElementById('registerFormStep1').style.display = 'none';
            document.getElementById('registerFormStep2').style.display = 'block';
            document.getElementById('displayTargetEmail').textContent = email;
            const otpInput = document.getElementById('regOtpCode');
            otpInput.value = '';
            setTimeout(() => otpInput.focus(), 150);
            startResendCountdown(45);
        } else {
            showAlert('step1Alert', data.message || '⚠️ Failed to send verification code. Please try again.');
        }
    } catch (err) {
        showAlert('step1Alert', '⚠️ Network error communicating with server. Please try again.');
    } finally {
        btn.disabled = false;
        btn.innerHTML = origHtml;
    }
    return false;
}

async function handleVerifyOtp(e) {
    if (e && e.preventDefault) e.preventDefault();
    hideAlert('step2Alert');

    const username = document.getElementById('regUsername').value.trim();
    const email = document.getElementById('regEmail').value.trim();
    const password = document.getElementById('regPassword').value;
    const targetRoleEl = document.getElementById('targetRole');
    const target_role = targetRoleEl ? targetRoleEl.value : 'Software Engineer';
    const otp_code = document.getElementById('regOtpCode').value.trim();

    if (!otp_code || otp_code.length !== 6) {
        showAlert('step2Alert', '⚠️ Please enter the full 6-digit OTP code.');
        return false;
    }

    const btn = document.getElementById('verifyOtpBtn');
    btn.disabled = true;
    const origHtml = btn.innerHTML;
    btn.innerHTML = '<span>⏳ Verifying OTP & Creating Account...</span>';

    try {
        const res = await fetch('/api/auth/verify-register-otp', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, email, password, target_role, otp_code })
        });
        const data = await res.json();

        if (res.ok && data.success) {
            showAlert('step2Alert', '✅ OTP Verified! Welcome to Interview Master. Redirecting...', 'success');
            setTimeout(() => {
                window.location.href = data.redirect_url || '/dashboard';
            }, 700);
        } else {
            showAlert('step2Alert', data.message || '⚠️ Invalid or expired OTP code.');
            btn.disabled = false;
            btn.innerHTML = origHtml;
        }
    } catch (err) {
        showAlert('step2Alert', '⚠️ Network error during verification. Please try again.');
        btn.disabled = false;
        btn.innerHTML = origHtml;
    }
    return false;
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
            showAlert('step2Alert', data.message || '⚠️ Failed to resend code.');
            resendBtn.disabled = false;
            resendBtn.textContent = 'Resend OTP';
        }
    } catch (err) {
        showAlert('step2Alert', '⚠️ Network error. Please try again.');
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

// --- PASSWORD RESET LINK FLOW ---
async function handleSendResetLink(e) {
    if (e && e.preventDefault) e.preventDefault();
    hideAlert('resetStep1Alert');

    const email = document.getElementById('resetEmail').value.trim();
    if (!email) {
        showAlert('resetStep1Alert', '⚠️ Please enter your registered email address.');
        return false;
    }

    const btn = document.getElementById('sendResetOtpBtn');
    btn.disabled = true;
    const origHtml = btn.innerHTML;
    btn.innerHTML = '<span>📨 Sending reset link...</span>';

    try {
        const res = await fetch('/api/auth/send-reset-link', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email })
        });
        const data = await res.json();

        if (res.ok && data.success) {
            document.getElementById('resetFormStep1').style.display = 'none';
            document.getElementById('resetSuccessState').style.display = 'block';
            document.getElementById('displayResetTargetEmail').textContent = email;
        } else {
            showAlert('resetStep1Alert', data.message || '⚠️ Failed to send reset link. Please check your email.');
        }
    } catch (err) {
        showAlert('resetStep1Alert', '⚠️ Network error communicating with server. Please try again.');
    } finally {
        btn.disabled = false;
        btn.innerHTML = origHtml;
    }
    return false;
}

function goBackToResetStep1() {
    hideAlert('resetStep1Alert');
    const successState = document.getElementById('resetSuccessState');
    if (successState) successState.style.display = 'none';
    const form1 = document.getElementById('resetFormStep1');
    if (form1) form1.style.display = 'block';
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

