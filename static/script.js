// Sample data matching your dataset format
const sampleData = {
    'State': 'CA',
    'Account length': 100,
    'Area code': 415,
    'International plan': 'No',
    'Voice mail plan': 'Yes',
    'Number vmail messages': 25,
    'Total day minutes': 200,
    'Total day calls': 100,
    'Total day charge': 34.0,
    'Total eve minutes': 200,
    'Total eve calls': 100,
    'Total eve charge': 17.0,
    'Total night minutes': 200,
    'Total night calls': 100,
    'Total night charge': 9.0,
    'Total intl minutes': 10,
    'Total intl calls': 4,
    'Total intl charge': 2.7,
    'Customer service calls': 1
};

function fillSampleData() {
    Object.keys(sampleData).forEach(key => {
        const element = document.getElementById(key);
        if (element) {
            element.value = sampleData[key];
        }
    });
}

// Form submission
document.getElementById('predictForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const submitBtn = e.target.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerHTML;
    
    // Show loading
    submitBtn.innerHTML = '<span class="loading"></span> Predicting...';
    submitBtn.disabled = true;
    
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        
        if (response.ok) {
            displayResult(result);
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        submitBtn.innerHTML = originalText;
        submitBtn.disabled = false;
    }
});

function displayResult(result) {
    // Hide placeholder, show results
    document.getElementById('placeholder').style.display = 'none';
    document.getElementById('resultContent').style.display = 'block';
    
    // Update prediction card
    const card = document.getElementById('predictionCard');
    const icon = document.getElementById('predictionIcon');
    const text = document.getElementById('predictionText');
    const risk = document.getElementById('riskText');
    const prob = document.getElementById('probabilityValue');
    
    // Reset classes
    card.className = 'prediction-card';
    
    if (result.prediction === 'Churn') {
        if (result.churn_probability > 70) {
            card.classList.add('danger');
            icon.className = 'fas fa-exclamation-circle';
        } else {
            card.classList.add('warning');
            icon.className = 'fas fa-exclamation-triangle';
        }
        text.textContent = 'Likely to Churn';
        text.style.color = '#ef4444';
    } else {
        card.classList.add('success');
        icon.className = 'fas fa-check-circle';
        text.textContent = 'Likely to Stay';
        text.style.color = '#10b981';
    }
    
    risk.textContent = result.risk_level + ' Risk';
    prob.textContent = result.confidence + '%';
    
    // Update progress bars
    document.getElementById('churnBar').style.width = result.churn_probability + '%';
    document.getElementById('churnPercent').textContent = result.churn_probability + '%';
    document.getElementById('noChurnBar').style.width = result.no_churn_probability + '%';
    document.getElementById('noChurnPercent').textContent = result.no_churn_probability + '%';
    
    // Generate insights
    const insights = generateInsights(result);
    const insightsList = document.getElementById('insightsList');
    insightsList.innerHTML = insights.map(i => `<li><i class="fas fa-info-circle"></i> ${i}</li>`).join('');
}

function generateInsights(result) {
    const insights = [];
    
    if (result.churn_probability > 70) {
        insights.push('High churn risk - immediate retention action recommended');
    } else if (result.churn_probability > 30) {
        insights.push('Moderate churn risk - monitor closely');
    } else {
        insights.push('Low churn risk - maintain current service');
    }
    
    // Get form values for insights
    const serviceCalls = parseInt(document.getElementById('Customer service calls').value) || 0;
    const intlPlan = document.getElementById('International plan').value;
    const accountLength = parseInt(document.getElementById('Account length').value) || 0;
    
    if (serviceCalls > 3) {
        insights.push('Multiple service calls detected - satisfaction issue');
    }
    
    if (intlPlan === 'Yes' && result.churn_probability > 50) {
        insights.push('International plan user at risk - review international rates');
    }
    
    if (accountLength < 12) {
        insights.push('New customer (< 1 year) - early retention phase');
    }
    
    if (result.churn_probability > 50) {
        insights.push('Consider offering loyalty discount or plan upgrade');
    }
    
    return insights;
}

// In script.js
document.getElementById('State').addEventListener('change', function() {
    if (this.value === 'CA') {
        document.getElementById('Area code').value = '415';
    }
});