# -*- coding: utf-8 -*-
import os, tempfile
from appconf import AppConf
from django.apps import apps
from django.utils.functional import lazy
from commerceml import conf as default


class CmlConf(AppConf):
    USE_ZIP = default.USE_ZIP # FIXME: True not working
    FILE_LIMIT = default.FILE_LIMIT
    MAX_EXEC_TIME = default.MAX_EXEC_TIME
    EXPORT_FOLDER = tempfile.gettempdir()
    IMPORT_FOLDER = tempfile.gettempdir()
    MODELS_APP = 'cml'
    
    PRODUCT = lazy(apps.get_model(app_label=MODELS_APP, model_name='Product'))
    PRODUCT_PROPERTY = apps.get_model(app_label=MODELS_APP, model_name='PRODUCTPROPERTY')
    CATEGORY = apps.get_model(app_label=MODELS_APP, model_name='CATEGORY')
    MANUFACTURER = apps.get_model(app_label=MODELS_APP, model_name='MANUFACTURER')
    IMAGE = apps.get_model(app_label=MODELS_APP, model_name='IMAGE')
    ORDER = apps.get_model(app_label=MODELS_APP, model_name='ORDER')
    ORDER_ITEM = apps.get_model(app_label=MODELS_APP, model_name='ORDERITEM')    
    
    class Meta:
        prefix = 'CML'

