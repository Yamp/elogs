if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/service-worker.js').then(function(registration) {
            // Регистрация успешна
            console.log('ServiceWorker registration successful with scope: ', registration.scope);
        }).catch(function(err) {
            // Регистрация не успешна
            console.log('ServiceWorker registration failed: ', err);
        });
    });
}