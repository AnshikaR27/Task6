import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render
from .models import VisaApplication

def calculate_visa_probability(application_id):
    """Calculate the likelihood of a candidate being granted a visa."""
    try:
        application = VisaApplication.objects.get(id=application_id)
        # Sample criteria for calculation
        score = 0
        max_score = 100

        # Example criteria
        if application.documents:  # Documents uploaded
            score += 40
        if application.visa_type == 'Work':  # Higher chance for work visa
            score += 30
        elif application.visa_type == 'Study':  # Medium chance for study visa
            score += 20
        else:  # Tourist visa
            score += 10
        if application.application_status == 'Pending':  # Status being processed
            score += 20

        percentage = min(100, (score / max_score) * 100)  # Ensure percentage is capped at 100
        return percentage
    except VisaApplication.DoesNotExist:
        return None

def visa_probability_view(request, application_id):
    """View to calculate and show visa probability with a progress bar."""
    percentage = calculate_visa_probability(application_id)
    if percentage is None:
        return render(request, 'visa_probability_error.html', {'error': 'Application not found.'})

    # Generate a progress bar plot
    fig, ax = plt.subplots(figsize=(5, 1))
    ax.barh([''], [percentage], color='skyblue')
    ax.set_xlim(0, 100)
    ax.set_xlabel('Likelihood (%)')
    ax.set_title('Visa Approval Probability')
    ax.text(percentage / 2, 0, f"{percentage:.1f}%", va='center', ha='center', color='black')
    plt.tight_layout()

    # Save the plot to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()

    return render(request, 'visa_probability.html', {
        'application_id': application_id,
        'percentage': percentage,
        'progress_bar': image_base64,
    })
