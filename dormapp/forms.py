from django.forms import ModelForm
from dormapp.models import ResHallReview

class ResHallReviewForm(ModelForm):
	class Meta:
		model=ResHallReview
		fields=['starRating','reviewTitle','reviewBody']