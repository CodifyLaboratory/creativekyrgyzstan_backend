from modeltranslation.translator import register, TranslationOptions
# from submit.models import Submit
# from association_member.models import RulesAndPolitics, Members
# from contacts.models import Contact
# from event.models import Event
from mainpage.models import MainPage

@register(MainPage)
class MainPageTranslationOptions(TranslationOptions):
    fields = ('short_description', 'advantages')

# @register(Event)
# class EventTranslationOptions(TranslationOptions):
#     fields = ('name', 'text')

# @register(Contact)
# class ContactTranslationOptions(TranslationOptions):
#     fields = ('address')

# @register(RulesAndPolitics)
# class RulesAndPoliticsTranslationOptions(TranslationOptions):
#     fields = ('how_to')

# @register(Members)
# class MembersTranslationOptions(TranslationOptions):
#     fields = ('bio')

# @register(Submit)
# class SubmitTranslationOptions(TranslationOptions):
#     fields = ('company_name', 'full_name', 'position', 'company_field', 'company_activity')