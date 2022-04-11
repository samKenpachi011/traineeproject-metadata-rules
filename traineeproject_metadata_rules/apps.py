
from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings

class AppConfig(DjangoAppConfig):
    name = "traineeproject_metadata_rules"
    verbose_name = "TraineeProject Metadata Rules"
    
    
    
if settings.APP_NAME == 'traineeproject_metadata_rules':
    
    from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
    from edc_metadata.apps import AppConfig as MetadataAppConfig
    from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
    from edc_visit_tracking.apps import (
        AppConfig as BaseEdcVisitTrackingAppConfig)

    class EdcMetadataAppConfig(MetadataAppConfig):
        reason_field = {'traineeproject_subject.subjectvisit': 'reason'}

    class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            'traineeproject_subject': ('subject_visit', 'traineeproject_subject.subjectvisit')}

    class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
        country = 'botswana'
        definitions = {
            '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                                 slots=[100, 100, 100, 100, 100, 100, 100]),
            '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                                 slots=[100, 100, 100, 100, 100])}
    
    