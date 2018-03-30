from dataloader.models import SamplingFeature, Result
from django import template
from django.core.exceptions import ObjectDoesNotExist
import re

from dataloaderinterface.models import SiteRegistration, SiteSensor

register = template.Library()
#
#
# @register.filter(name='get_registration')
# def get_registration(sampling_feature):
#     if not isinstance(sampling_feature, SamplingFeature):
#         return
#
#     return DeviceRegistration.objects.filter(deployment_sampling_feature_uuid__exact=sampling_feature.sampling_feature_uuid).first()

#
# @register.filter(name='get_sensor_csv_path')
# def get_sensor_csv_path(sensor):
#     if not isinstance(sensor, SiteSensor):
#         return
#     try:
#         return SiteResultSerializer(sensor.result).get_file_path()
#     except ObjectDoesNotExist:
#         return None

@register.filter(name='get_site_sensor')
def get_site_sensor(site, variable_code):
    if not isinstance(site, SiteRegistration) or not site.status_sensors:
        return

    return next((sensor for sensor in site.status_sensors if sensor.variable_code==variable_code), None)


@register.filter(name='can_administer_site')
def can_administer_site():
    pass
    # return DeviceRegistration.objects.filter(deployment_sampling_feature_uuid__exact=sampling_feature.sampling_feature_uuid).first()


@register.filter(name='add_input_class', is_safe=True)
def add_input_class(value, arg):
    if re.search(r'class', value, re.IGNORECASE):
        return re.sub(r'(class=")', r'\1{0} '.format(arg), value)
    else:
        return re.sub(r'(<input)', r'\1 class="{0}"'.format(arg), value)


@register.filter("roundfloat")
def round_float(value, argv):
    if isinstance(value, float):
        round_to = 1
        if argv is not None and isinstance(argv, int):
            round_to = argv
        return round(value, round_to)
    else:
        return value
