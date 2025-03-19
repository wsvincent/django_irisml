from django.contrib import admin
from .models import IrisPrediction


@admin.register(IrisPrediction)
class IrisPredictionAdmin(admin.ModelAdmin):
    list_display = (
        "prediction",
        "created_at_display",
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
    )
    list_filter = (
        "created_at",
        "prediction",
    )  # Enables filtering by date and prediction type
    search_fields = ("prediction",)  # Adds search functionality
    ordering = ("-created_at",)  # Orders by most recent predictions

    def created_at_display(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M")

    created_at_display.admin_order_field = "created_at"
    created_at_display.short_description = "Created At"
