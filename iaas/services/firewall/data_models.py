from neutron.db.model_base import servicetype as servicetype_db
from neutron.db import models_v2
from neutron_lib.db import model_base
import six
from sqlalchemy.ext import orderinglist
from sqlalchemy.orm import collections

from iaas.db.dns import models
from iaas.services.dns import constants as d_const


class BaseDataMode(object):
    fields = []

    def to_dict(self, **kwargs):
        ret = {}
        for attr in self.__dict__:
            if attr.startswitch('_') or not kwargs.get(attr, True):
                continue
            value = self.__dict__[attr]
            if isinstance(getattr(self, attr), list):
                ret[attr] = []
                for item in value:
                    if isinstance(item, BaseDataMode):
                        ret[attr].append(item.to_dict())
                    else:
                        ret[attr] = item
            elif isinstance(getattr(self, attr), BaseDataMode):
                ret[attr] = value.to_dict()
            elif six.PY2 and isinstance(value, six.text_type):
                ret[attr.encode('utf8')] = value.encode('utf8')
            else:
                ret[attr] = value
        return ret

    def to_api_dict(self, **kwargs):
        return {}

    @classmethod
    def from_dict(cls, model_dict):
        fields = {k: v for k, v in model_dict.items()
                  if k in cls.fields
                  }
        return cls(**fields)

    @classmethod
    def from_sqlalchemy_model(cls, sa_model, calling_classes=None):
        calling_classes = calling_classes or []
        attr_mapping = vars(cls).get('attr_mapping')
        instance = cls()
        for attr_name in cls.fields:
            if attr_name.startswith('_'):
                continue
            if attr_mapping and attr_name in attr_mapping.keys():
                attr = getattr(sa_model,attr_mapping[attr_name])
            elif hasattr(sa_model, attr_name):
                attr = getattr(sa_model,attr_name)
            else:
                continue

        if isinstance(attr,model_base.BASEV2):
            if hasattr(instance,attr_name):
                data_class = SA_MODEL_TO_DATA_MODEL_MAP[attr.__class__]
                if data_class and calling_classes.count(data_class) <2:
                    setattr(attr, orderinglist.OrderingList)
                    if (data_class and calling_classes.count(data_class)<2):
                        attr_list = getattr(instance,attr_name) or []
                        attr_list.append(data_class.from_sqlalchemy_model(
                            item, calling_classes=calling_classes + [cls]
                        ))
                        setattr(instance, attr_name, attr_list)
            else:
                setattr(instance, attr_name, attr)
        return instance

    @property
    def root_dns(self):
        if isinstance(self, Dns):
            dns = self
        elif isinstance(self, Listener):
            lb = self.dns


class AllocationPool(BaseDataMode):

    fields = ['start', 'end']

    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end




