from django.apps import apps as django_apps
from edc_constants.constants import FEMALE, YES, NEG
from edc_metadata_rules import PredicateCollection


# PredicateCollection groups predicates for use in rules
class SubjectPredicates(PredicateCollection):
    
    app_label = 'traineeproject_subject'
    visit_model = f'{app_label}.subjectvisit'

# make pregnancy status available for females

    def func_participant_is_female(self,visit=None, **kwargs):
        # returns true if the participant is female
        
        subjectconsent_cls = django_apps.get_model('traineeproject_subjectconsent')
        
        try:
            subjectconsent_obj = subjectconsent_cls.objects.filter(
                subject_identifier = visit.appointment.subject_identifier).latest('created')
        except subjectconsent_cls.DoesNotExist:
            return False             
        else:  
            if visit.visit_code_sequence > 0:
                return False
            return subjectconsent_obj.gender == FEMALE
                
                      