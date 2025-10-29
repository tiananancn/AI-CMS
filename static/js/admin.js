// 管理后台通用JavaScript代码

document.addEventListener('DOMContentLoaded', function() {
    // 自动隐藏alert消息
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => {
                alert.remove();
            }, 300);
        }, 5000);
    });

    // 确认删除操作
    window.confirmAction = function(message, callback) {
        if (confirm(message)) {
            callback();
        }
    };

    // 搜索功能
    const searchInput = document.querySelector('#globalSearch');
    if (searchInput) {
        searchInput.addEventListener('keyup', function(e) {
            if (e.key === 'Enter') {
                performSearch(this.value);
            }
        });
    }

    // 自动保存草稿
    let autoSaveTimer;
    const autoSaveInputs = document.querySelectorAll('[data-autosave]');
    autoSaveInputs.forEach(input => {
        input.addEventListener('input', function() {
            clearTimeout(autoSaveTimer);
            autoSaveTimer = setTimeout(() => {
                autoSave(this);
            }, 3000);
        });
    });
});

function performSearch(query) {
    if (query.trim() === '') return;
    console.log('Searching for:', query);
    // 这里可以实现搜索逻辑
}

function autoSave(element) {
    const form = element.closest('form');
    if (!form) return;

    const formData = new FormData(form);
    fetch('/admin/autosave', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Auto-saved:', data);
    })
    .catch(error => {
        console.error('Auto-save failed:', error);
    });
}

// 文件上传预览
function previewImage(input, previewElement) {
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
            previewElement.src = e.target.result;
            previewElement.style.display = 'block';
        };
        reader.readAsDataURL(input.files[0]);
    }
}

// 拖拽上传
function initDragAndDrop(dropZoneId, inputId) {
    const dropZone = document.getElementById(dropZoneId);
    const fileInput = document.getElementById(inputId);

    if (!dropZone || !fileInput) return;

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, preventDefaults, false);
    });

    ['dragenter', 'dragover'].forEach(eventName => {
        dropZone.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, unhighlight, false);
    });

    dropZone.addEventListener('drop', handleDrop, false);

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    function highlight(e) {
        dropZone.classList.add('highlight');
    }

    function unhighlight(e) {
        dropZone.classList.remove('highlight');
    }

    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        handleFiles(files);
    }

    function handleFiles(files) {
        fileInput.files = files;
        // 触发change事件
        fileInput.dispatchEvent(new Event('change'));
    }
}
