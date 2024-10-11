// وظائف عامة للموقع

// تحميل العبايات المميزة
function loadFeaturedAbayas() {
    const featuredContainer = document.querySelector('.featured-abayas');
    if (featuredContainer) {
        // يمكن هنا إضافة طلب AJAX لجلب العبايات المميزة من الخادم
        // لهذا المثال، سنفترض أن البيانات موجودة في الصفحة
    }
}

// إضافة إلى السلة
function addToCart(abayaId) {
    // يمكن هنا إضافة منطق إضافة العباية إلى سلة التسوق
    console.log(`تمت إضافة العباية رقم ${abayaId} إلى السلة`);
    alert('تمت إضافة العباية إلى السلة');
}

// التحقق من صحة نموذج الدفع
function validatePaymentForm() {
    const form = document.querySelector('#payment-form');
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            // إضافة منطق التحقق من صحة النموذج هنا
            console.log('تم إرسال نموذج الدفع');
            alert('تم استلام طلبك بنجاح!');
        });
    }
}

// تهيئة الصفحة
document.addEventListener('DOMContentLoaded', function() {
    loadFeaturedAbayas();
    validatePaymentForm();
});