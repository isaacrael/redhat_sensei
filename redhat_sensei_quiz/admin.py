from django.contrib import admin
from . models import Answer, Question

# Register your models here.

"""
# Note the code below is used as example code for use in changing the display in the admin

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3
"""

"""
# Note the code below is used as example code for use in changing the display in the admin

class ChoiceInLine(admin.TabularInline):
    model = Answer
    extra = 3
"""


"""
# Note the code below is used as example code for use in changing the display in the admin

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]

"""


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']



# Note: the two lines below register the Answer and Question classes
# so that Question & Answers are visible together in the admin site
# making Question & Answer input and deletion very fast

admin.site.register(Answer)


admin.site.register(Question)



